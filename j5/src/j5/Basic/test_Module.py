#!/usr/bin/env python

import os
from j5.Basic import Module

class TestModule:
    def test_find_module(self):
        target_file = Module.__file__
        if target_file.endswith(".pyc") or target_file.endswith(".pyo"):
            target_file = target_file[:target_file.rfind(".")] + ".py"
        assert Module.find_module("j5") == os.path.dirname(os.path.dirname(target_file))
        assert Module.find_module("j5.Basic") == os.path.dirname(target_file)
        assert Module.find_module("j5.Basic.Module") == target_file

    def test_resolve(self):
        assert Module.resolvemodule("j5.Basic.Module") == Module
        from j5.Config import ConfigTree
        assert Module.resolvemodule("j5.Config.ConfigTree.Node") == ConfigTree.Node

