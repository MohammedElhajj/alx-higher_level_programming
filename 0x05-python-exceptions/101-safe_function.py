#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        func_result = fct(*args)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return
    return (func_result)
