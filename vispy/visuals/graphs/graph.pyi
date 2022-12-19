from numpy.typing import ArrayLike, NDArray

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from ..visual import CompoundVisual
from ..line import ArrowVisual
from ..markers import MarkersVisual
from . import layouts

class GraphVisual(CompoundVisual):

    _arrow_attributes = ...
    _arrow_kwargs = ...
    _node_kwargs = ...

    _arrow_kw_trans = ...
    _node_kw_trans = ...
    _node_properties_args = ...

    def __init__(
        self,
        adjacency_mat: ArrayLike | NDArray | None = None,
        directed: bool = False,
        layout: str | None = None,
        animate: bool = False,
        line_color: str | ColorMap | None = None,
        line_width: float | None = None,
        arrow_type: str | None = None,
        arrow_size: float | None = None,
        node_symbol: str | None = None,
        node_size: float | None = None,
        border_color: str | ColorMap | None = None,
        face_color: str | ColorMap | None = None,
        border_width: float | None = None,
    ): ...
    @property
    def adjacency_matrix(self): ...
    @property
    def layout(self): ...
    @layout.setter
    def layout(self, value): ...
    @property
    def directed(self): ...
    @directed.setter
    def directed(self, value): ...
    @property
    def animate(self): ...
    @animate.setter
    def animate(self, value): ...
    def animate_layout(self): ...
    def set_final_layout(self): ...
    def reset_layout(self): ...
    def set_data(self, adjacency_mat: NDArray | None = None, **kwargs): ...
