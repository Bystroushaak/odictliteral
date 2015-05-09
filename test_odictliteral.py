#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import pytest

from odictliteral import odict
from odictliteral import OrderedDict


# Tests =======================================================================
def test_odictType():
    complex_dict = odict[
        "another": odict[
            "here": "more keys",
            1: "hello"
        ],
        "key": "val",
        2: "numeric",
        "aaa": "bbb"
    ]

    complex_ordered_dict = OrderedDict([
        ["another", OrderedDict([
            ["here", "more keys"],
            [1, "hello"]
        ])],
        ["key", "val"],
        [2, "numeric"],
        ["aaa", "bbb"]
    ])

    assert complex_dict == complex_ordered_dict

    assert list(complex_dict.keys()) == ["another", "key", 2, "aaa"]


def test_constructor():
    assert odict(fist=1) == odict["fist": 1]
    assert odict([("fist", 1), ("second", 2)]) == odict["fist": 1, "second": 2]


def test_errors():
    with pytest.raises(SyntaxError):
        odict[1]

    with pytest.raises(SyntaxError):
        odict["hello"]

    with pytest.raises(SyntaxError):
        assert odict[["key", "val"]]

    with pytest.raises(SyntaxError):
        assert odict[("key", "val")]


def test_repr():
    assert repr(odict()) == "odict()"
    assert repr(odict["key": "val"]) == 'odict[key: val]'
    assert repr(odict["k": "v", "x": "y"]) == 'odict[k: v, x: y]'
