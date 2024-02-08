#!/usr/bin/python3
"""
Module that contains model and file storage initialization code
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
