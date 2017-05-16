#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib_mate import Path

p = Path(Path(__file__).parent, "pyclopedia")
p = Path(r"C:\Users\shu\PycharmProjects\py34\pyclopedia-project\pyclopedia\p03_stdlib")
p.autopep8()
p.execute_pyfile()