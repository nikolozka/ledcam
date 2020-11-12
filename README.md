# ledcam
fadecandy + opencv2

* Open-CV Dependencies *

sudo apt-get install libtiff5-dev libjasper-dev libpng12-dev

sudo apt-get install libjpeg-dev

sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

sudo apt-get install libgtk2.0-dev

sudo apt-get install libgtk-3-dev

sudo apt-get install libatlas-base-dev gfortran

sudo apt-get install libatlas-base-dev git

sudo apt-get install python3-pip

pip3 install numpy 

pip3 install opencv-python

* Install Fadecandy - you can skip this step if working with DotStar LEDs *

git clone https://github.com/scanlime/fadecandy

cp fadecandy/examples/python/opc.py copy to same folder as the python sketch

start fadecandy server

* Dependencies for Dotstar variant - you can skip this step if working with NeopPixels *

pip3 install RPI.GPIO

sudo pip3 install adafruit-blinka

* enable SPI + I2c for Dotstar - you can skip this step if working with NeopPixels *

sudo rasp-config -> interfacing options -> SPI enable + I2C enable

* clone into this project & run it *

git clone https://github.com/nikolozka/ledcam

cd ledcam

python3 usbcam.py - for Neopixel/Fadecandy variant
python3 usbcam_dotstar.py - for Neopixel/Fadecandy variant
