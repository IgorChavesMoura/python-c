from ctypes import *

so_file = "./functions.so"

#libc = CDLL(util.find_library('c'))

c_functions = CDLL(so_file)

c_functions.print_string.argtypes = (c_char_p,)
c_functions.print_string.restype = c_char_p

c_functions.hash.argtypes = (c_char_p,)

arg = 'Original Data'

c_arg = c_char_p(arg)

result = c_functions.hash(c_arg)

print(result)

#libc.free(result)