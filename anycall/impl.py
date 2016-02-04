#
# anycall.impl
#
# Anycall utility functions. Put any function you want to hide from the simple
# ops listing
#
# Copyright (C) 2014-2015, Vasileios Karakasis
# All rights reserved.
#

import imp
import inspect
import os.path
import sys

def load_module_recursive(name):
    """
    Load module name recursively, descending to submodules if name contains dots.
    """
    module_names = name.split(".")
    module_path = [ "." ] + sys.path
    m_path = []
    for m_name in module_names:
        mod = imp.find_module(m_name, module_path)
        imp.load_module(m_name, *mod)
        m_path.append(mod[1])
        module_path = m_path

    return module_names


def convert_to_dict(list):
    """
    Convert list of 2-element (key, value) tuples to a dict.
    """
    ret = {}
    for e in list:
        k, v = e[:2]
        ret[k] = v

    return ret

def print_error(msg):
    """
    Print error message msg to standard error. The msg message is printed as-is
    on standard error prefixed with `argv[0]:'. A newline is also appended.
    """
    sys.stderr.write("%s: %s\n" % (sys.argv[0], msg))

def print_usage(out):
    """
    Print to usage message to output stream out.
    """
    out.write("Usage: %s [modules=<modules>] <op> [op_kwargs]\n" % sys.argv[0])

