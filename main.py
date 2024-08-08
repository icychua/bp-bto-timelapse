#!/usr/bin/python3

import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials
from picamera2 import Picamera2, Preview
from PIL import Image

GDRIVE_FOLDER_ID = '1T5fAvCXxWbFAt9arTqdvK7hxquNam8w1'

def upload_to_gdrive(folder, filename, gdrive_id):
    gauth = GoogleAuth()
    scope = ["https://www.googleapis.com/auth/drive"]
    gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name('svc_creds.json',scope)
    
    drive = GoogleDrive(gauth)
    
    gfile = drive.CreateFile({'parents': [{'id':gdrive_id}], 'title': filename})
    gfile.SetContentFile(folder+ '/' + filename)
    gfile.Upload()

def get_formatted_now():
    dt_now = datetime.datetime.now()
    return str(dt_now)[:13] + "hrs"

def capture_photo(save_as_filename=None):
    picam = Picamera2()

    config = picam.create_preview_configuration(main={"size":(1600,1200)})
    picam.configure(config)

    #picam.start_preview(Preview.QTGL)

    picam.start()
    if save_as_filename is None:
        save_as_filename = get_formatted_now() + '.jpg'
    picam.capture_file("photos/" + save_as_filename)
    picam.close()
    
#     img = Image.open("photos/" + save_as_filename)
#     img = img.rotate(90)
#     img.save("photos/" + save_as_filename)
    
    return save_as_filename
    
filename = capture_photo()
print("Photo captured: " + str(filename))

upload_to_gdrive('photos', filename, GDRIVE_FOLDER_ID)
print("Uploaded at " + str(datetime.datetime.now()))

      
