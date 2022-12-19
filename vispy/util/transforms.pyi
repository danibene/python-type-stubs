from np import dtype
from numpy.typing import ArrayLike, NDArray

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

# Note: we use functions (e.g. sin) from math module because they're faster

import math
import numpy as np

def translate(offset: ArrayLike, dtype: np.dtype | None = None) -> NDArray: ...
def scale(s: ArrayLike, dtype: np.dtype | None = None) -> NDArray: ...
def rotate(angle: float, axis: NDArray, dtype=None) -> NDArray: ...
def ortho(
    left: float, right: float, bottom: float, top: float, znear: float, zfar: float
) -> NDArray: ...
def frustum(
    left: float, right: float, bottom: float, top: float, znear: float, zfar: float
) -> NDArray: ...
def perspective(fovy: float, aspect: float, znear: float, zfar: float) -> NDArray: ...
def affine_map(points1, points2): ...
