#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os.path
import io

from googleapiclient.http import MediaIoBaseDownload
from zdrive import DriveAPI
from multiprocessing import Process


class Downloader(DriveAPI):
    def __init__(self):
        super(Downloader, self).__init__()
        self.DEFAULT_STORAGE_PATH = 'drive_content'

    def __create_Directory(self, path=None):
        if path is None:
            path = self.DEFAULT_STORAGE_PATH
        if not os.path.isdir(path):
            os.mkdir(path=path)

        return path

    def downloadFolder(self, folderId, destinationFolder=None):

        path = self.__create_Directory(destinationFolder)
        page_token = None

        while True:
            results = self.service.files().list(
                spaces='drive',
                pageToken=page_token,
                q="parents in '{0}'".format(folderId),
                fields="nextPageToken, files(id, name, mimeType)"
            ).execute()

            items = results.get('files', [])
            download_processes = []
            for item in items:
                itemName = item['name']
                itemId = item['id']
                itemType = item['mimeType']
                filePath = os.path.join(path, itemName)

                if itemType == 'application/vnd.google-apps.folder':
                    print("Stepping into folder: {0}".format(filePath))
                    self.downloadFolder(itemId, filePath)  # Recursive call
                else:
                    p = Process(target=self.downloadFile, args=[itemId, filePath])
                    p.start()
                    download_processes.append(p)

            for process in download_processes:
                process.join()

            page_token = results.get('nextPageToken', None)
            if page_token is None:
                break

    def downloadFile(self, fileId, filePath=None):
        # Note: The parent folders in filePath must exist
        print("\t -> Downloading file with id: {0} name: {1}".format(fileId, filePath))
        request = self.service.files().get_media(fileId=fileId)
        fh = io.FileIO(filePath, mode='wb')

        try:
            downloader = MediaIoBaseDownload(fh, request, chunksize=1024 * 1024)

            current_progress = -1
            done = False
            while done is False:
                status, done = downloader.next_chunk(num_retries=2)
                if status:
                    progress = int(status.progress() * 100)
                    if progress % 10 == 0 and progress != current_progress:
                        print(
                            " \t Downloading fileId: {0}, {1}% complete!".format(fileId, int(status.progress() * 100)))
                        current_progress = progress
            print("Download Complete!")
        except Exception as e:
            print(str(e))
            return
        finally:
            fh.close()
