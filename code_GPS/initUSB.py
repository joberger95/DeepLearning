import sys
import usb.core
import usb.util

print(usb.__version__)
busses = usb.busses()
for bus in busses:
    devices = bus.devices
    for dev in devices:
        if dev != None:
            try:
                usd_dev = usb.core.find(idVendor=dev.idVendor, idProduct=dev.idProduct)
                print(usb_dev)
            except:
                pass
# 1a40:0101
dev = usb.core.find(idVendor=0x0403, idProduct=0x6001)
print("The 8087:0024 is : ", dev)
if dev is None:
    raise ValueError("Device not found!")
else:

    if dev.is_kernel_driver_active(0):
        try:
            dev.detach_kernel_driver(0)
            print("kernel driver detached")
        except usb.core.USBError as e:
            sys.exit("Could not detach kernel driver: %s" % str(e))
    else:
        print("no kernel driver attached")
    try:
        usb.util.claim_interface(dev, 0)
        print("claimed device")
    except:
        sys.exit("Could not claim the device: %s" % str(e))
    try:
        dev.set_configuration()
        dev.reset()
    except usb.core.USBError as e:
        sys.exit("Could not set configuration: %s" % str(e))

usb.util.release_interface(dev, interface)
dev.attach_kernel(interface)
