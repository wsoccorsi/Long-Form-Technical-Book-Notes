"""
Chapter 6 - Descriptors
"""
class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return self


        formated_print = "Call {}.__get__({}, {})".format(
            self.__class__.__name__, instance, owner
        )
        print(formated_print)

        return instance


class ClientClass:
    descriptor = DescriptorClass()


client = ClientClass()

# This makes a call instead of returning an object
client.descriptor