from picamera2 import Picamera2, Preview
import time
from PIL import Image
picam = Picamera2()
config = picam.create_preview_configuration(main={"size":(1600,1200)})
picam.configure(config)

picam.start_preview(Preview.QTGL)


picam.start()
picam.capture_file("test.jpg")
time.sleep(1)
#picam.close()

img = Image.open("test.jpg")
#img = img.rotate()
img.save("test.jpg")


