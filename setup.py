#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages
from zdrive.version import VERSION

__version__ = VERSION


if sys.version_info[:2] <= (2, 7):
    with open("README.rst") as f:
        long_description = f.read()
else:
    with open("README.rst", encoding="utf8") as f:
        long_description = f.read()


setup(
    name='ZDrive',
    author='Abhinav Anand',
    version=VERSION,
    author_email='abhinavanand1905@gmail.com',
    description="A lightweight module to download and upload data to Google Drive contents",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='https://github.com/ab-anand/Zdrive',
    license='MIT',
    install_requires=[
        "pathlib >= 1.0.1",
        "setuptools >= 44.1.1",
        "google-auth-oauthlib >= 0.4.4"
    ],
    # dependency_links=dependency_links,
    # adding package data to it
    packages=find_packages(exclude=['contrib', 'docs']),
    download_url='https://github.com/ab-anand/zdrive/tarball/' + __version__,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Topic :: System",
        "Topic :: System :: Operating System",
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
    ],
    keywords=['Google Drive', 'Utility', 'Automation', 'File management', 'File Organizer']
)