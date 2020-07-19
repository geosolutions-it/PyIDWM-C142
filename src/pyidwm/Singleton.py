# -*- coding: utf-8 -*-


class Singleton:
    """
    Singleton class to decorate classes for the Singleton pattern
    """
    @staticmethod
    def decorator(clazz):
        """
        Decorator function to make a class as singleton
        :param clazz: class to make singleton
        :return:
        """
        class ClassWrapper(clazz):
            """
            Class wrapper implementing the singleton pattern
            """
            _instance = None

            def __new__(cls, *args, **kwargs):
                """
                new method
                :param args:
                :param kwargs:
                """
                if ClassWrapper._instance is None:
                    ClassWrapper._instance = super(ClassWrapper, cls).__new__(cls, *args, **kwargs)
                    ClassWrapper._instance._sealed = False
                return ClassWrapper._instance

            def __init__(self, *args, **kwargs):
                """
                Constructor
                :param args:
                :param kwargs:
                """
                if self._sealed:
                    return
                super(ClassWrapper, self).__init__(*args, **kwargs)
                self._sealed = True

        ClassWrapper.__name__ = clazz.__name__
        return ClassWrapper
