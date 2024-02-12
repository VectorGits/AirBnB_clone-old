#!/usr/bin/python3
"""
Initialization for the Models Package
"""

# import the FileStorage class from the file_storage module
from models.engine.file_storage import FileStorage

# create an instance of FileStorage and assign it to the variable 'storage'
storage = FileStorage()

# call the 'reload' method on the 'storage' instance
storage.reload()
