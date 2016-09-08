# leftpad_cffi_build.py

from cffi import FFI

ffi = FFI()
ffi.set_source('pyleftpad', '',
               libraries=["leftpad"],
               library_dirs=['.'])

ffi.cdef("char *left_pad_string(char *ip, size_t ip_count, size_t pad_count);")

if __name__ == '__main__':
    ffi.compile()
