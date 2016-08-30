import leftpad as c_leftpad


def leftpad(ip):
    ip = ip.encode('ascii')
    op = c_leftpad.lib.left_pad_string(ip, len(ip), 20)
    return c_leftpad.ffi.string(op).decode('ascii')

