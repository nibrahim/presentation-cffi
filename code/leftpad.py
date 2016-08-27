from ctypes import *
leftpad = CDLL("./libleftpad.so")

leftpad.left_pad_string.argtypes = [c_char_p, c_size_t, c_size_t]
leftpad.left_pad_string.restype = c_char_p

ip = "python".encode('ascii')
ret = leftpad.left_pad_string(ip, len(ip), 15)

print "'%s'"%(ret,)


