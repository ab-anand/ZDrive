#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zdrive import Uploader

u = Uploader()


# STEP 1 (optional)

# get a list of "folder_id" in the DRIVE
ids_list = u.listFolders()
print(ids_list)

# pick the folder_id  of the folder inside which the content should be uploaded
parent_folder_id = 'XXXX-YYYY-ZZZZ'

# STEP 2 (optional BUT recommended if you don't need STEP 1)

# create a folder inside which the content from input folder should be uploaded.
# The "parentId" field in the line below is an optional parameter. It specifies the
# folder inside which the required folder will be created. When left empty, ROOT will
# be considered as the parent.
parent_folder_id = u.createFolder(name="Data", parentId="xysdw1212@#&")


# STEP 3

# upload the folder with default "max_depth" and at the root level.
# Again the "parentId" is an optional parameter. When left empty, folders will be uploaded
# at the root level.

input_folder_path = "/Users/abhinavanand/Downloads/data"
u.uploadFolder(input_folder_path, parentId=parent_folder_id)
