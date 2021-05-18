from ctypes import *
from os import path

dll = PyDLL(path.join(path.dirname(__file__), './lib/grayscale.dll'))

dll.sum.restype = py_object
dll.sum.argtypes = py_object,

dll.mean.restype = py_object
dll.mean.argtypes = py_object,

dll.var.restype = py_object
dll.var.argtypes = py_object,

dll.std.restype = py_object
dll.std.argtypes = py_object,
