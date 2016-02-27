#
# anycall.py
#
# A generic driver for calling any function from a python module. A useful tool
# for plugging in and invoking any plot, data analysis etc. custom function. The
# back-end function must assume string arguments.
#
# Copyright (C) 2014-2015, Vasileios Karakasis
# All rights reserved.
# 

import anycall.impl
import inspect
import sys

AVAILABLE_OPS = { }

def list_ops(show_help='none'):
    """
    List available operations.
    """
    sys.stdout.write('Available operations:\n')
    for k, v in AVAILABLE_OPS.items():
        sys.stdout.write('=> %s%s\n' % (k, inspect.formatargspec(
                    inspect.getargspec(v)[0])))
        doc = inspect.getdoc(v)
        if doc and show_help in ['short', 'full']:
            if show_help == 'short':
                print('    %s' % doc.split('.')[0])
            else:
                print('    %s' % doc)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        anycall.impl.print_error("too few arguments")
        anycall.impl.print_usage(sys.stderr)
        sys.exit(1)

    user_modules = []
    if sys.argv[1].startswith("modules"):
        if len(sys.argv) < 3:
            anycall.impl.print_error("too few arguments")
            anycall.impl.print_usage(sys.stderr)
            sys.exit(1)
        for m in sys.argv[1].split("=")[1].split(","):
            user_modules.append(m)
        op = sys.argv[2]
        op_args = sys.argv[3:]
    else:
        op = sys.argv[1]
        op_args = sys.argv[2:]
    
    # Build op's kwargs
    op_kwargs = {}
    for a in op_args:
        k, v = a.split("=", 1)
        op_kwargs[k] = v

    # Try to import user supplied modules
    available_ops = inspect.getmembers(sys.modules[__name__],
                                       inspect.isfunction)
    for m_name in user_modules:
        try:
            loaded_modules = anycall.impl.load_module_recursive(m_name)
            for m in loaded_modules:
                available_ops = available_ops + \
                    inspect.getmembers(sys.modules[m], inspect.isfunction)
        except ImportError as e:
            anycall.impl.print_error("could not load module: %s" % e.args)
            sys.exit(1)
    
    AVAILABLE_OPS = anycall.impl.convert_to_dict(available_ops)
    try:
        AVAILABLE_OPS[op](**op_kwargs)
    except KeyError:
        anycall.impl.print_error("requested operation `%s' not found" % op)
        sys.exit(1)
