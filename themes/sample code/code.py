import asyncio

def showcase():
    """Some code to showcase the syntax.

    Docstrings are recognized and have an additional scope.
    Color schemas can render them differently from other strings.

    HACK doctests are highlighted too.
    
        >>> print('''hello
        ... world''')
    """

    @decorator(param='spam')
    async def coroutine(db:aio_db.DatabaseConnection) -> List[str]:
        r"""A coroutine."""

        await logger.log('working\x12with %r', aio_db)

        async with db.transaction():
            result = await db.query(...)
            print(f'Result: {result!r}')

    mapping = None     # type: Dict[int, Any] # PEP 484

    # a regular expression
    get_regex = lambda: re.compile(     # type: ignore
        r"""\A
            word
            (?:                         # a comment
               (?P<fill>.)?
               (?P<align>[<>=^])        (?# another comment)
            )?
            another word\.\.\.
            (?:\.(?P<precision>0|(?!0)\d+))?
        \Z""",
        re.VERBOSE | re.DOTALL)

    # NOTE Numbers with leading zeros are invalid in Python 3,
    # use 0o...
    answer = func(0xdeadbeef + 0b00100001 + 0123 + 0o123 +
                  1_005_123 + # PEP 515
                  # complex numbers
                  .10e12 + 2j) @ mat

    return R'''No escapes '\' in this \one'''



    

from time import localtime

activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting' }
raw_input("Enter an integer from 1 to 99: ")
# This is the first attempt 
# type: int
time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
        break
else:
    print 'Unknown, AFK or sleeping!'

Celsius = int(raw_input("Enter a temperature in Celsius: "))

Fahrenheit = 9.0/5.0 * Celsius + 32

print "Temperature:", Celsius, "Celsius = ", Fahrenheit, " F"    

class TestMedian(unittest.TestCase):
    def testMedian(self):
        self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)

print queens
print "\n".join(". "*q + "Q " + ". "*(BOARD_SIZE-q-1) for q in queens)

import random
n = random.randint(1, 99)
guess = int(raw_input("Enter an integer from 1 to 99: "))
while n != "guess":
    print
    if guess < n:
        print "guess is low"
        guess = int(raw_input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print "guess is high"
        guess = int(raw_input("Enter an integer from 1 to 99: "))
    else:
        print "you guessed it!"
        break
    print


