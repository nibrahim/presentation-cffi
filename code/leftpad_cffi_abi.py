import cffi

ffi = cffi.FFI()
ffi.cdef("""
char *left_pad_string(char *ip, size_t ip_count, size_t pad_count);
""")

c_leftpad = ffi.dlopen("./libleftpad.so")

def leftpad(ip):
    ip = ip.encode('ascii')
    op = c_leftpad.left_pad_string(ip, len(ip), 20)
    return ffi.string(op).decode('ascii')




