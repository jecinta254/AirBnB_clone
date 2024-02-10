#!/usr/bin/python3
"""__init__ magic method to our model directory"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
