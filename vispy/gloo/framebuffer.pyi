from vispy.gloo.framebuffer import RenderBuffer
from typing import Literal
from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

from .globject import GLObject
from .texture import Texture2D
from .wrappers import _check_valid, read_pixels
from .context import get_current_canvas

# ------------------------------------------------------ RenderBuffer class ---

class RenderBuffer(GLObject):

    _GLIR_TYPE: str = ...

    def __init__(
        self,
        shape: tuple | None = None,
        format: None | Literal["color", "depth", "stencil"] = None,
        resizeable: bool = True,
    ): ...
    @property
    def shape(self): ...
    @property
    def format(self): ...
    def resize(
        self,
        shape: tuple[int, ...],
        format: None | Literal["color", "depth", "stencil"] = None,
    ): ...

# ------------------------------------------------------- FrameBuffer class ---
class FrameBuffer(GLObject):

    _GLIR_TYPE: str = ...

    def __init__(
        self,
        color: RenderBuffer | None = None,
        depth: RenderBuffer | None = None,
        stencil: RenderBuffer | None = None,
    ): ...
    def activate(self): ...
    def deactivate(self): ...
    def __enter__(self): ...
    def __exit__(self, t, val, trace): ...
    def _set_buffer(self, buffer, format): ...
    @property
    def color_buffer(self): ...
    @color_buffer.setter
    def color_buffer(self, buffer): ...
    @property
    def depth_buffer(self): ...
    @depth_buffer.setter
    def depth_buffer(self, buffer): ...
    @property
    def stencil_buffer(self): ...
    @stencil_buffer.setter
    def stencil_buffer(self, buffer): ...
    @property
    def shape(self): ...
    def resize(self, shape: tuple[int, int]): ...
    def read(
        self, mode: str = "color", alpha: bool = True, crop: ArrayLike | None = None
    ) -> ArrayLike: ...
