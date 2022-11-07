# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
number = 15
pprint([{
    "bin": bin(i),
    "dec": i,
    "oct": oct(i),
    "hex": hex(i),
 } for i in range(number+1)])
