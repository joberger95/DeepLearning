import usb.core
import usb.util

dev = usb.core.find(idVendor=0xFFFE, idProduct=0x0001)

if dev is None:
    raise ValueError("Device Not Found")

print(dev)
