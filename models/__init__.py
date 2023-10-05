#!/usr/bin/python3
"""Magic method to create models package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
