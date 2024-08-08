# Photo Capture and Google Drive Uploader

This Python script captures a photo using a Raspberry Pi camera, saves it locally, and uploads it to a specified Google Drive folder. 

## Features

- **Photo Capture**: Utilizes the `Picamera2` library to capture high-resolution photos with the Raspberry Pi camera.
- **Automatic File Naming**: The photo is saved with a timestamp in the format `YYYY-MM-DD HHhrs.jpg`.
- **Google Drive Upload**: Automatically uploads the captured photo to a designated Google Drive folder using the `PyDrive` library and service account credentials.

## Requirements

- Raspberry Pi with a connected camera.
- Python 3.x.
- The following Python packages:
  - `pydrive`
  - `oauth2client`
  - `picamera2`
  - `Pillow`
