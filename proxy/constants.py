# !/usr/bin/env python
# -*- encoding: utf-8 -*-


class Constants(object):
    class ConstantError(TypeError):
        pass

    class UpperCaseError(ConstantError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstantError(f"Const can't change. {name}.")
        if not name.isupper():
            raise self.UpperCaseError(f"Const name must be uppercase. {name}.")
        self.__dict__[name] = value
