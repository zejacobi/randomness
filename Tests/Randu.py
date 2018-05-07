"""Very bad PRNG. Used here because we want a bad PRNG to compare with Python's good built
   in PRNG. See: http://physics.ucsc.edu/~peter/115/randu.pdf"""

from random import random


class Randu(object):
    def __init__(self, seed=None):
        """Very bad PRNG that is set up here to emulate the python random interface. It has
            methods *seed* and *random* that work the exact same as their Python counterparts.
            You can call this with seed. If you don't, we just get one from Python's PRNG, which
            is pretty decent.

            :param int seed: Random seed to use, affects which numbers you will receive from the
                generator.
        """
        self.modulo = 2 ** 31
        self.coefficient = 65539

        if not seed:
            seed = int(random() * self.modulo)

        self.current_value = seed % self.modulo

    def seed(self, seed):
        """Set the seed of this truly awful PRNG.

            :param int seed: A seed value
            :return: None
        """
        self.current_value = seed
        self.random()

    def random(self):
        """Gives a pseudo-random number in [0, 1), but only if you don't want your number to be
            that (pseudo-)random

            :return: A floating point number
            :rtype: float
        """
        self.current_value = (self.coefficient * self.current_value) % self.modulo
        return self.current_value / self.modulo
