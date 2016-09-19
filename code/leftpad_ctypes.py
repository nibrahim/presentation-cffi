from ctypes import *
c_leftpad = CDLL("./libleftpad.so")

c_leftpad.left_pad_string.argtypes = [c_char_p, c_size_t, c_size_t]
c_leftpad.left_pad_string.restype = c_char_p

def leftpad(ip):
    ip = ip.encode('ascii')
    ret = c_leftpad.left_pad_string(ip, len(ip), 20)
    return ret.decode('ascii')

print ("'%s'"%(leftpad("python")))


