#!/usr/bin/env python
# -*- coding: utf-8 -*-

from p01_startwith_single_underscore import *

if __name__ == "__main__":
    # regular name can be imported
    assert public_var == "public_var"
    assert public_func() == "public_func"
    assert PublicClass.__name__ == "PublicClass"
    assert PublicClass._non_public_method() == "_non_public_method"
    assert PublicClass.public_method() == "public_method"

    # name start with single underscore cannot be imported
    try:
        _non_public_var
    except NameError:
        pass
    except:
        raise

    try:
        _non_public_func()
    except NameError:
        pass
    except:
        raise

    try:
        _NonPublicClass
    except NameError:
        pass
    except:
        raise

    try:
        assert _NonPublicClass._non_public_method() == "_non_public_method"
    except NameError:
        pass
    except:
        raise

    try:
        assert _NonPublicClass.public_method() == "public_method"
    except NameError:
        pass
    except:
        raise

    # name start with single underscore can be accessed by parent_object.name
    # for example: module_name.variable_name, module_name.function_name
    # module_name.class_name
    import p01_startwith_single_underscore

    assert p01_startwith_single_underscore._non_public_var == "_non_public_var"
    assert p01_startwith_single_underscore._non_public_func() == "_non_public_func"
    assert p01_startwith_single_underscore._NonPublicClass.__name__ == "_NonPublicClass"
    assert p01_startwith_single_underscore._NonPublicClass._non_public_method(
    ) == "_non_public_method"
