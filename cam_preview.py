#!/usr/bin/python3

import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials
from picamera2 import Picamera2, Preview
from PIL import Image

picam = Picamera2()

camera_config = picam.create_preview_configuration()
picam.configure(camera_config)


picam.start_preview(Preview.QTGL)
picam.start()

