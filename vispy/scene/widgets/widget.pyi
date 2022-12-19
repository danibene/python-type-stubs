from vispy.scene.widgets.widget import Widget

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import division

import numpy as np

from ..visuals import Compound
from ...visuals.mesh import MeshVisual
from ...visuals.transforms import STTransform
from ...visuals.filters import Clipper
from ...util.event import Event
from ...geometry import Rect
from ...color import Color

class Widget(Compound):
    def __init__(
        self,
        pos: tuple[float, float] = ...,
        size: tuple[float, float] = ...,
        border_color=None,
        border_width: float = 1,
        bgcolor=None,
        padding: int = 0,
        margin: int = 0,
        **kwargs
    ): ...
    @property
    def pos(self): ...
    @pos.setter
    def pos(self, p): ...
    @property
    def size(self): ...
    @size.setter
    def size(self, s): ...
    @property
    def width(self): ...
    @property
    def width_min(self): ...
    @width_min.setter
    def width_min(self, width_min): ...
    @property
    def width_max(self): ...
    @width_max.setter
    def width_max(self, width_max): ...
    @property
    def height(self): ...
    @property
    def height_min(self): ...
    @height_min.setter
    def height_min(self, height_min): ...
    @property
    def height_max(self): ...
    @height_max.setter
    def height_max(self, height_max): ...
    @property
    def rect(self): ...
    @rect.setter
    def rect(self, r): ...
    @property
    def inner_rect(self): ...
    @property
    def stretch(self): ...
    @stretch.setter
    def stretch(self, s): ...
    def _update_layout(self): ...
    def _update_clipper(self): ...
    @property
    def border_color(self): ...
    @border_color.setter
    def border_color(self, b): ...
    @property
    def bgcolor(self): ...
    @bgcolor.setter
    def bgcolor(self, value): ...
    @property
    def margin(self): ...
    @margin.setter
    def margin(self, m): ...
    @property
    def padding(self): ...
    @padding.setter
    def padding(self, p): ...
    def _update_line(self): ...
    def _update_colors(self): ...
    @property
    def picking(self): ...
    @picking.setter
    def picking(self, p): ...
    def _update_visibility(self): ...
    def _update_child_widgets(self): ...
    def add_widget(self, widget: Widget) -> Widget: ...
    def add_grid(self, *args, **kwargs): ...
    def add_view(self, *args, **kwargs): ...
    def remove_widget(self, widget: Widget): ...
