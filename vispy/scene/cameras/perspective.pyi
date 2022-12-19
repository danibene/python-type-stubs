from vispy.util.event import Event
from vispy._typing import Scalar

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import division

import math
import numpy as np

from .base_camera import BaseCamera
from ...util import keys, transforms
from ...visuals.transforms import MatrixTransform

class PerspectiveCamera(BaseCamera):

    _state_props = ...

    def __init__(
        self,
        fov: float = 60.0,
        scale_factor: Scalar | None = None,
        center=None,
        **kwargs
    ): ...
    def viewbox_mouse_event(self, event: Event): ...
    @property
    def scale_factor(self): ...
    @scale_factor.setter
    def scale_factor(self, value): ...
    @property
    def near_clip_distance(self): ...
    def _set_range(self, init): ...
    def viewbox_resize_event(self, event: Event): ...
    def _update_transform(self, event=None): ...
    def _update_projection_transform(self, fx, fy): ...

class Base3DRotationCamera(PerspectiveCamera):
    def __init__(self, fov=0.0, **kwargs): ...
    @property
    def distance(self): ...
    @distance.setter
    def distance(self, distance): ...
    def viewbox_mouse_event(self, event: Event): ...
    def _update_camera_pos(self): ...
    def _get_dim_vectors(self): ...
    def _update_projection_transform(self, fx, fy): ...
    def _update_rotation(self, event): ...
    def _rotate_tr(self): ...
    def _dist_to_trans(self, dist): ...
