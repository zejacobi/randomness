from random import random

from Battery import Pi
from Tests.Randu import Randu

randu = Randu()

randu_pi = Pi.Pi(randu.random)
system_pi = Pi.Pi(random)

print('System Pi does it in: ', sum([system_pi.unbounded_test(0.01) for i in range(1000)]))
print('Randu Pi does it in: ', sum([randu_pi.unbounded_test(0.01) for i in range(1000)]))