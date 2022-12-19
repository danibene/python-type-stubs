from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-
# vispy: testskip
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import print_function

import sys
import os
import warnings
from os import path as op
from copy import deepcopy
from functools import partial

from ..util import use_log_level, run_subprocess
from ..util.ptime import time
from ._testing import has_application, nottest, IS_CI, IS_TRAVIS_CI

_line_sep = ...

class VispySkipSuite(Exception):
    def __init__(self, msg=""): ...

def _get_import_dir(): ...
def _unit(mode, extra_arg_string="", coverage=False): ...
def _docs(): ...
def _flake(): ...
def _check_line_endings(): ...

_script: str = ...

bad_examples: list = ...

def _skip_example(fname): ...
def _examples(fnames_str): ...
@nottest
def test(
    label: str = "full", extra_arg_string: str | ArrayLike = "", coverage: bool = False
): ...
