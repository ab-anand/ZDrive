ZDrive
=======

|license| |pypi| |python|

*A lightweight and easy to use Python library to upload and download contents from Google Drive.*

:Author: Abhinav Anand

.. contents::
    :backlinks: none

.. sectnum::

What is it
---------------
`[back to top] <https://github.com/ab-anand/ZDrive#zdrive>`__

*Google Drive is the most used cloud storage platform. A need for some minimal yet effective tool to transfer
contents to and from Drive is important!*


There is a number of such libraries already present with `Pydrive <https://github.com/googleworkspace/PyDrive>`__ being
the most amazing. Pydrive has a lot of functionalities but there are certain major things that it lacks. The goal of this library is
to address the bulk uploading/downloading functionality in a way that is easy-to-use and yet covers the users' requirements.


Features
--------
`[back to top] <https://github.com/ab-anand/ZDrive#zdrive>`__

- Upload folders anywhere in the Drive maintaining the **same directory** structure as present locally.
- Download folders from anywhere in the Drive to anywhere in the PC maintaining the **same directory structure** as present in the Drive.
- Download or Upload whole directory in less than 5 lines of code.
- Can sustain minor network interruptions.
- Bulk upload/download made easy.
- Minimal dependencies.
- Easy to use.
- Fast!
- Returns ``JSON`` objects
- Support
    - **OS Support**: Linux, Windows, Mac
    - **Language Support**: Python 2.x, 3.x

Installation
------------
`[back to top] <https://github.com/ab-anand/ZDrive#zdrive>`__

Option 1: installing through `pip <https://pypi.org/project/ZDrive/>`__ (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`pypi package link <https://pypi.org/project/ZDrive/>`__

``$ pip install ZDrive``

If you are behind a proxy

``$ pip --proxy [username:password@]domain_name:port install ZDrive``

**Note:** If you get ``command not found`` then
``$ sudo apt-get install python-pip`` should fix that

Option 2: Installing from source (Only if you must)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ git clone https://github.com/ab-anand/ZDrive.git
    $ cd ZDrive/
    $ pip install -r requirements.txt
    $ python setup.py install

**Note:** If you get ``permission denied`` then
``$ sudo python setup.py install`` should fix that


Usage
-----
`[back to top] <https://github.com/ab-anand/ZDrive#zdrive>`__

Initial Setup
~~~~~~~~~~~~~~
- Follow the `article <https://medium.com/swlh/google-drive-api-with-python-part-i-set-up-credentials-1f729cb0372b>`__ to get your drive-api credentials.
- Once you have the ``clients-secret.json``, rename it to ``credentials.json`` and place it in the same folder where you'll be running the script.

Downloader
~~~~~~~~~~~~~~

- ``Downloader()`` allows you to download folder/files from the Drive.
- The output location where the files will get downloaded can be specified too.
- ``Downloader()`` maintains the same directory tree structure while downloading from the Drive thus making it convenient to read.
- Google Drive is a semantic (also called tag-based) file system meaning it stores files not based on their location, but based on an ID.
- Semantic file systems allow you to have multiple files with the same name and to have one file appearing in multiple places.
- Thus for performing any action related to a file/folder in Drive, we would need the IDs of the file/folder.
- ``ZDrive`` allows you to retrieve a list of files/folders present inside the Drive along with their IDs.
- ``Downloader()`` also uses multiprocessing for speeding up the download process.
- Using the ``Downloader()``

.. code:: python

    >>> from zdrive import Downloader
    >>> output_directory = "/home/abhinav/Documents"
    >>> d = Downloader()
    >>> folder_id = 'XXXX-YYYY-ZZZZ'
    >>> d.downloadFolder(folder_id, destinationFolder=output_directory)


- If no ``destinationFolder`` is specified, then ``Downloader()`` would create a default folder named ``drive_content`` and it would download the contents there.
- Also, if the specified ``destinationFolder`` doesn't already exist, ``Downloader()`` would create the folder first and the perform the downloading.

Uploader
~~~~~~~~~~~~~~~~


- ``Uploader()`` allows you to upload folder/files from the local PC to drive.
- Uploading can be done from any specified location inside the local PC.
- Data can be uploaded at the ROOT level of the Drive or inside any specific folder in the Drive.
- In case of a minor internet interruption(~10-15 secs) the upload would be paused and once the internet connection is stable. The uploading will get resumed.
- ``Uploader()`` also maintains the exact same directory tree structure while uploading from the local PC to Drive.
- The level of child directories to be uploaded is decided by ``max_depth`` parameter as shown in the example below.
- By default, ``max_depth = 5``
- Using ``Uploader()``

.. code:: python

    >>> from zdrive import Uploader
    >>> input_directory = "/home/abhinav/Downloads"
    >>> u = Uploader()
    >>> parent_folder_id = u.createFolder(name="Data")
    >>> result = u.uploadFolder(input_directory, max_depth=3, parentId=parent_folder_id)
    >>> print(result)

    '{
        "files":
            {
                "/Users/abhinavanand/Downloads/test/def.pdf": "1pJNIu-0oyzaUgjLvnf6-3mk81iwLBXyS"
            },
        "folders":
            {
            "/Users/abhinavanand/Downloads/test/test-level-1":
                {
                    "files":
                    {
                        "/Users/abhinavanand/Downloads/test/test-level-1/abc.pdf": "1YwZs__92yzWdM2e7Nc2atF5lzLnyYV9i"
                    },
                    "folders": {},
                    "id": "1zzh_hGImg94SnzrMC8LdH1vgbO3LMksD"
                }
            }
    }'

- If no ``parentId`` is specified, then ``Uploader()`` would upload the contents from local PC to the ROOT level in Drive.


Contributing
------------
`[back to top] <https://github.com/ab-anand/ZDrive#zdrive>`__

Please refer `Contributing page for details <https://github.com/ab-anand/Zdrive/blob/master/CONTRIBUTING.rst>`__


Bugs
----
`[back to top] <https://github.com/ab-anand/ZDrive#zdrive>`__

Please report the bugs at the `issue
tracker <https://github.com/ab-anand/ZDrive/issues>`__



License
-------
`[back to top] <https://github.com/ab-anand/ZDrive#zdrive>`__


Built with ♥ by `Abhinav Anand <https://github.com/ab-anand/>`__ under the `MIT License <https://github.com/ab-anand/ZDrive/blob/master/LICENSE/>`__ ©

You can find a copy of the License at `http://abhinav.mit-license.org/ <http://abhinav.mit-license.org/>`__


.. |upload| image:: https://github.com/ab-anand/ZDrive/actions/workflows/python-publish.yml/badge.svg
    :target: https://github.com/ab-anand/ZDrive/actions/workflows/python-publish.yml
.. |license| image:: https://img.shields.io/github/license/ab-anand/ZDrive?color=orange
    :alt: GitHub license
    :target: https://github.com/ab-anand/ZDrive/blob/master/LICENSE
.. |pypi| image:: https://img.shields.io/pypi/v/zdrive?color=green
    :alt: PyPI
.. |python| image:: https://img.shields.io/pypi/pyversions/zdrive?color=red
    :alt: PyPI - Python Version