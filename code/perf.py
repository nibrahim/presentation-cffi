# perf.py
import timeit

from leftpad_ctypes import leftpad as ctypes_leftpad
from leftpad_cffi_abi import leftpad as cffi_abi_leftpad
from leftpad_cffi_api import leftpad as cffi_api_leftpad

print ("CFFI API", timeit.timeit(lambda : cffi_api_leftpad("python")))
print ("CFFI ABI", timeit.timeit(lambda : cffi_abi_leftpad("python")))
print ("Ctypes ", timeit.timeit(lambda : ctypes_leftpad("python")))
