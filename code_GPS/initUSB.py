import usb.core
import usb.util

dev = usb.core.find(idVendor=0x001, idProduct=0x002)

if dev is None:
    raise ValueError("Device Not Found")

print(dev)
