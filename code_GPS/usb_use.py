import usb.core
import usb.util

dev = usb.core.find(idVendor=0x0403, idProduct=0x6001)

if dev is None:
    raise ValueError("Device not found")
else:
    print(dev)
    dev.set_configuration()


# def send(cmd):
#     # address taken from results of print(dev):   ENDPOINT 0x3: Bulk OUT
#     dev.write(3, cmd)
#     # address taken from results of print(dev):   ENDPOINT 0x81: Bulk IN
#     result = dev.read(0x81, 100000, 1000)
#     return result


def get_data(ch):
    # first 4 bytes indicate the number of data bytes following
    rawdata = send(":DATA:WAVE:SCREen:CH{}?".format(ch))
    data = []
    for idx in range(4, len(rawdata), 2):
        # take 2 bytes and convert them to signed integer using "little-endian"
        point = int().from_bytes(
            [rawdata[idx], rawdata[idx + 1]], "little", signed=True
        )
        data.append(point / 4096)  # data as 12 bit
    return data


def get_header():
    # first 4 bytes indicate the number of data bytes following
    header = send(":DATA:WAVE:SCREen:HEAD?")
    header = header[4:].tobytes().decode("utf-8")
    return header


# header = get_header()
data = get_data(1)
### end of code
