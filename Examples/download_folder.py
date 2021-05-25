#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zdrive import Downloader

d = Downloader()

# STEP 1

# get a list of "folder_id" in the DRIVE
ids_list = d.listFolders()
print(ids_list)

# STEP 2

# pick the folder_id  of the folder to download from the ids_list above
folder_id = 'XXXX-YYYY-ZZZZ'

# STEP 3

# download the folder with default output path. A folder named "drive_content" should appear containing
# the data from the specified DRIVE folder
d.downloadFolder(folder_id)

# OR specify the output path for the downloaded data. In case, the output_path
# specified doesn't already exist, zdrive will create a folder there
output_path = "/Users/abhinavanand/Downloads/data"
res = d.downloadFolder(folder_id, destinationFolder=output_path)
print(res)
