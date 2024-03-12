#!/usr/bin/env python3
"""This module is used to create a unique FileStorage
instance for our application"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
