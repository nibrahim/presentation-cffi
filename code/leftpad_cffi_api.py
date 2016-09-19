import pyleftpad

def leftpad(ip):
    ip = ip.encode('ascii')
    op = pyleftpad.lib.left_pad_string(ip, len(ip), 20)
    return pyleftpad.ffi.string(op).decode('ascii')

if __name__ == '__main__':
    print ("'{}'".format(leftpad("python")))

