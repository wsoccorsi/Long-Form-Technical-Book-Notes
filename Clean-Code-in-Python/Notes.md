# Clean Code in Python - Develop Maintainable and efficient code by Mariano Anaya

Missing Chapters 1 - 5, notes to be ported 

## Chapter 6 - Getting More Out of Our Objects with Descriptors

* Descriptors are another distinctive feature of Python that take object-oriented programming to another level, 
and their potential allows users to build more powerful and reusable abtractions. Most of the time, the full potential
of descriptors is observed in libraries or frameworks
* A descriptor is an object that is an instance of a class that implements the descriptor protocol
* A descriptor has the magic methods (__get__, __set__, __delete__, __set_name__)
* A domain model - A diagram of class definitions and their interaction.
* A descriptor must be defined by the class atribute and not an instance attribute of a class
* The most common idiom is to just return the descriptor itself when instance is None.
* If a descriptor doesn't implement `__set__` then any value on the right-hand side of the statement will override the descriptor entirely.


	__set__(self, instance, value)
	client.descriptor = "value"

* !s = __str__, !r = __repr__ in `.format()`
* Essentially the @property decorater, though unsure which is more appropriate, ie when to use one or the other??
* Data descriptor - Implements `__set__` or `__delete__` magic methods
* Non-Data Descriptor - Just implements `__get__`
* So you would use a descriptor in place of the @property decorator if the @property decorator is duplicating logic throughout
the appllication. A descriptor can make this inot a class and be implemented through object instantiation
* Since descriptors are a class attribute they are shared in every instance of the object, which is not good (coupling)
* Also access attributes with `__dict__` for descriptors
* Descriptors can be incorporated to make "better" decorators
* Avoid putting business logic into a descriptor, instead focus on implementational code (thats a weird word to use).
Meaning defining a new data structure or object that another part of our business logic will use as a tool.
* You can replace the following decorator implementation with a descriptor

``` 
@Serialization(username=show_original,
        password=hide_field,
        ip=show_originial,
        timestamp=format_time)
# replaced with the descriptors
class LoginEvent(BaseEvent): 
    username = ShowOriginal()
    password = HideField()
    ip = ShowOriginal()
    timestamp = FormatTime()
```

* Methods are actaully just functions that are able to be set as methods because they are descriptors 
* Some decorators, such as `@property`, `@classmethod`, and `@staticmethod` are descriptors
* `__slots__`is a magic method to define a fixed set of fields an object of that can can have

## Chapter 7 - Generators, Iterators, and Asynchronous Programming

* Generators are idomatic iteration in Python that improves performance of a program by using less memory
* Anytime we add a yield statement it will make the function a generator


```
	def load_purchages(filename):
		with open(filename) as f:
			for line in f:
				*_, price_raw = line.partition(",")
				yield float(price_raw)
```

* Generator Expressions - Generators defined by comprehension `(x**2 for x in range(10))`
* Always pass a generator expression, instead of a list comprehension, to functions that expect iterables, such as
`mix(), max(), sum()`. This is more efficient and Pythonic
* itertools is a generator module, that can perform memory efficient computation on iterables
* Flatten the iteration into a single loop if possible. Don't write code that uses for loop iteration with breaks etc..
* A Iterable implements the `__iter__` magic method and a Sequence implements `__getitem__ and __len__`
* Usually choose an iterable over a sequence
* Coroutines - A function whos execution can be suspended at a given point in time, to later be resumed
* Coroutine methods are - `close(), throw(), send()`
* Are coroutines generators? Yes
* However this book mentions.. oddly that the `send()` method is the method that distinguishes a coroutine 
from a generator
* We can create asynchronous programs in Python using coroutines. Meaning we can create programs that have many coroutines, 
schedule them to work in a particular order, and switch between them when they're suspended after a yield from has been called
on each of them.
* We create generators when we want to achieve efficeint iteration. We typically create coroutines with the goal of running
non-blocking I/O operations
* A coroutine is defined with `async def`
* Asynchronous magic methods `__aenter__, __aexit__, __aiter__, __anext__`

_might want to review the end asynchronous bit_

## Chapter 8 - Unit Testing and Refactoring
   
* Unit tests are corse, and critical component of the software and they should be treated with the same considerations as the business logic.
* Unit testss are a piece of code that imports parts of the code with the business logic and tests it with assertions:
	- Isoliation: Unit tests should be completely independent from any other external agent, and they have to focus only on the 
	business logic. For this reasion, they do not connect to a database, they don't perform HTTP requests, and so on. Isolation means
	that the tests are independent among themselves: they must be able to run in any order, without depending on any pervious state.
	- Performance: Unit tests must run quickly. They are indended to be run multiple times, repeatedly.
	- Repeatability: Unit tests should be able to objectively assess the status of the software in a deterministic way. This means the 
	results yielded by the tests should be repeatable. Unit tests assess the status of the code: if a test fails, it 
	must keep on failing until the code is fixed. Tests shouldn't be flakey or randomized * iteresting
        - Self-validating: The execution of a unit test determines its result. There should be no extra step required to interpret the
	unit test 
* Integration tests - To test multiple componenets at once. We want to use HTTP requests, connect to databases etc here. But we should avoid
testing external dependency via the Internet (that might be Kafka)
* Acceptance test - An automaticed form of testing that tries to validate the system from the perspective of a user
* The better the tests, the more likely it is that we can deliever value quicly without being stopped by bugs every now and then.
* When the entire code is driven by the way it's going to be tested via test-driven-design
* It is not our job to test dependencies
* Parametize tests to make them faster (just some test with multiple fixture conditions)
* Use @pytest.mark.parametrize to eliminate repetition, keep the body of the test as cohesive as possible
* Code coverage should never be a target, that being said an acceptable range is above 80%
* Abuse in monkey patching is a red flag and generally means there is a mistake in our code
* Test Doubles - *ruby loves this stuff*, is a type of object that will take the place of a real one in our test suite for different reasons 
(maybe we don't need the actual production code, but just a dummy object would work, or maybe we can't use it because it requires access to 
services or it has side effect that we don't want in our unit ests etc..)
* Mock is a test double
* A MagicMock supports magic methods ie, the dunders
* Make methods for repetable asserstions
* Mutation Testing - The code will be modified to new versions called mutatants that are variations of the original code, but with some 
of its lgoic latered (for example, operators are swapped, conditions are inverted). A good test suite will catch these mutatnts can kill them, 
in whuch case we c an rely on the tests. In short these break this breaks our tests and well if they don't break we wrote bad tests.
* Test Driven Desing (TDD), making the tests before the code

## Chapter 9 - Common Design Patterns  
* We should not force the application of a design pattern to the solution we are building, but rather evolve, refactore, and impove our
solusion until a pattern emerges.
*  
