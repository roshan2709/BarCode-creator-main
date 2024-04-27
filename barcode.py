#You should have python installed in your desktop/laptop
# module to be install
# 1)pyqrcode :- pip install pyqrcode 2)png :- pip install pypng
import pyqrcode
import png
from pyqrcode import QRCode
rittik = "https://www.linkedin.com/in/rittik-roshan-kumar/"
url=pyqrcode.create(rittik)
url.png("anyname.png",scale=6)
