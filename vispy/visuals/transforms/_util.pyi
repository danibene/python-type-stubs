from typing import Callable
from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import division

import functools

import numpy as np
from ...util import logger
from functools import wraps

def arg_to_array(func: Callable) -> Callable: ...
def as_vec4(obj: ArrayLike, default: ArrayLike = ...) -> ArrayLike: ...
def arg_to_vec4(func): ...

class TransformCache(object):
    def __init__(self, max_age=1): ...
    def get(self, path): ...
    def _create(self, path): ...
    def roll(self): ...
