from __future__ import annotations
from typing import TYPE_CHECKING
from itertools import tee

"""
Chapter 6 - Descriptors
"""
# class DescriptorClass:
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#
#
#         formated_print = "Call {}.__get__({}, {})".format(
#             self.__class__.__name__, instance, owner
#         )
#         print(formated_print)
#
#         return instance
#
#
# class ClientClass:
#     descriptor = DescriptorClass()
#
#
# client = ClientClass()
#
# # This makes a call instead of returning an object
# client.descriptor
# print(ClientClass.descriptor)

### End Example ###

# if TYPE_CHECKING:
#     from collections.abc import Callable
#     from typing import Any
#
# class Validation:
#     def __init__(self, validation_function: Callable[[Any], bool], error_msg: str) -> None:
#         self.validation_function = validation_function
#         self.error_msg = error_msg
#
#     def __call__(self, value):
#         if not self.validation_function(value):
#             raise ValueError(f"{value!r} {self.error_msg}")
#
# class Field:
#     def __init__(self, *validations):
#         self.name = None
#         self.validations = validations
#
#     def __set_name__(self, owner, name):
#         self._name = name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return instance.__dict__[self._name]
#
#     def validate(self, value):
#         for validation in self.validations:
#             validation(value)
#
#     def __set__(self, instance, value):
#         self.validate(value)
#         instance.__dict__[self._name] = value
#
# class ClientClass:
#     descriptor = Field(
#         Validation(lambda x: isinstance(x, (int, float)), "is not a number"),
#         Validation(lambda x: x >= 0, "is not >= 0"),
#     )
#
# client = ClientClass()
# client.descriptor = 'bro'
# client.descriptor

"""
Chapter 7 - Generators, Iterators, and Asynchronous Programming
"""

# purchases = [1,2,3,4,5,6,7]
# def load_purchases(pur):
#     for purchase in pur:
#         yield(purchase)


purchases = (i for i in range(0, 10))
for i in purchases:
    print(i)

for i in purchases:
    print(i, 'hi')