# import the required libraries
from __future__ import print_function

import pathlib
import pickle
import os.path
import io
import shutil
import requests

from mimetypes import MimeTypes
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from zdrive import DriveAPI


class Downloader(DriveAPI):
    def __init__(self):
        super().__init__()
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

            for item in items:
                itemName = item['name']
                itemId = item['id']
                itemType = item['mimeType']
                filePath = os.path.join(path, itemName)

                if itemType == 'application/vnd.google-apps.folder':
                    print("Stepping into folder: {0}".format(filePath))
                    self.downloadFolder(itemId, filePath)  # Recursive call
                else:
                    self.downloadFile(itemId, filePath)

            page_token = results.get('nextPageToken', None)
            if page_token is None:
                break

    def downloadFile(self, fileId, filePath=None):
        # Note: The parent folders in filePath must exist
        print("-> Downloading file with id: {0} name: {1}".format(fileId, filePath))
        request = self.service.files().get_media(fileId=fileId)
        fh = io.FileIO(filePath, mode='wb')

        try:
            downloader = MediaIoBaseDownload(fh, request, chunksize=1024 * 1024)

            done = False
            while done is False:
                status, done = downloader.next_chunk(num_retries=2)
                if status:
                    if int(status.progress()*100) % 10 == 0:
                        print(" \t Download %d%%." % int(status.progress() * 100))
            print("Download Complete!")
        except Exception as e:
            raise Exception(e)
        finally:
            fh.close()
