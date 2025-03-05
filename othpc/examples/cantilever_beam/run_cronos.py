#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (C) EDF 2025

@authors: Elias Fekhari, Joseph Muré
"""
import openturns as ot
from cantilever_beam import CantileverBeam
import othpc

cb = CantileverBeam("template/beam_input_template.xml", "template/beam")
dw = othpc.DaskFunction(cb)
dwfun = ot.Function(dw)
X = ot.Sample.ImportFromCSVFile("input_doe/doe100.csv", ",")
Y = dwfun(X)
print(Y)