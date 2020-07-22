import usb
import usb.backend.libusb1 as libusb1

backend = libusb1.get_backend(find_library=lambda _: "LibUSB/MS64/dll/libusb-1-0.dll")
dev = usb.core.find(backend=backend)

print(dev)
parameter_list
