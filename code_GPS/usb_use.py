import usb.core
import usb.util

dev = usb.core.find(idVendor=0x0403, idProduct=0x6001)

if dev is None:
    raise ValueError("Device not found")
else:
    print(dev)
    dev.set_configuration()

print(usb.core.Device.get_active_configuration(dev))

