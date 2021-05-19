from ctypes import *
from os import path

dll = PyDLL(path.join(path.dirname(__file__), './lib/grayscale.dll'))

# math
dll.gs_sum.restype = py_object
dll.gs_sum.argtypes = py_object,

dll.gs_mean.restype = py_object
dll.gs_mean.argtypes = py_object,

dll.gs_pow.restype = py_object
dll.gs_pow.argtypes = py_object, py_object

dll.gs_sqrt.restype = py_object
dll.gs_sqrt.argtypes = py_object,

dll.gs_var.restype = py_object
dll.gs_var.argtypes = py_object,

dll.gs_std.restype = py_object
dll.gs_std.argtypes = py_object,

dll.gs_min.restype = py_object
dll.gs_min.argtypes = py_object,

dll.gs_max.restype = py_object
dll.gs_max.argtypes = py_object,
