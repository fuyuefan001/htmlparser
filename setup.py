#!/usr/bin/env python
# coding=utf-8

from setuptools import setup


setup(
    name="commentparser",
    version="1.0",
    author="Yuefan Fu",
    author_email="fuyuefan001@gmail.com",
    url='https://github.com/fuyuefan001/htmlparser',
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.21.0',
        'setuptools>=16.0',
        'bs4>=0.0.1',
        'praw'
    ],
    zip_safe=False
)