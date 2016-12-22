Pashto Cardinals
=================
A package that can convert a number to Pashto language


Install
=========
Via Pip:

$ pip install pashtocardinals

OR

$ sudo pip install pashtocardinals


Usage
======
from pashtocardinals import *

pashtocardinals.convert(234) 

The above code will return "دوه سوه او څلور دیرش"


Simple Example
==============
from pashtocardinals import *

user_input = raw_input("Enter an integer:\n>> ")

pashtocardinals.convert(user_input)


License
=======
The MIT License (MIT). Please see License File for more information.
