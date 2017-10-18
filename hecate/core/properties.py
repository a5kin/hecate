import math

import numpy as np


class Property:
    """
    Base class for all properties.

    """
    def __init__(self):
        self._dtype = None
        self._ctype = None
        self._bit_width = None
        self._width = None
        self._best_type = None
        self._types = (
            # (bit_width, numpy_dtype, gpu_c_type)
            (8, np.uint8, 'char'),
            (16, np.uint16, 'short'),
            (32, np.uint32, 'int'),
        )

    @property
    def best_type(self):
        if self._best_type is None:
            self._best_type = self._types[-1]
            for t in self._types:
                type_width = t[0]
                if self.bit_width <= type_width:
                    self._best_type = t
                    break
        return self._best_type

    @property
    def dtype(self):
        if self._dtype is not None:
            return self._dtype
        self._dtype = self.best_type[1]
        return self._dtype

    @property
    def ctype(self):
        if self._ctype is not None:
            return self._ctype
        self._ctype = 'unsigned ' + self.best_type[2]
        return self._ctype

    @property
    def bit_width(self):
        if self._bit_width is None:
            self._bit_width = self.calc_bit_width()
        return self._bit_width

    @property
    def width(self):
        if self._width is None:
            type_width = self.best_type[0]
            self._width = int(math.ceil(self.bit_width / type_width))
        return self._width

    def calc_bit_width(self):
        return 1  # default, just for consistency


class IntegerProperty(Property):

    def __init__(self, max_val):
        self.max_val = max_val
        super(IntegerProperty, self).__init__()

    def calc_bit_width(self):
        return int(math.log2(self.max_val)) + 1


class ContainerProperty(Property):

    @property
    def dtype(self):
        # hardcoded
        return np.uint8

    @property
    def ctype(self):
        # hardcoded
        return "unsigned char"
