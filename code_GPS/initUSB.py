import usb.core

for dev in usb.core.find(find_all=True):
    print("Device:", dev.filename())
    print("idVendor: %d (%s)" % (dev.idVendor, hex(dev.idVendor)))
    print("idProdut: %d (%s)" % (dev.idProduct, hex(dev.idProduct)))
