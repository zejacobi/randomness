"""
It is possible to calculate pi by placing points randomly on a grid.

Imagine if you will, a circle inside a square. The square has side length 2r and the circle has
radius r. For mathematical simplicity, we will place the origin in the centre of the circle.

The circle is described by the equation :math:`x^2 + y^2 \leq r^2`. The area of the square is
described by :math:`-r \leq x \leq r ; -r \leq y \leq r`.

The area of the circle is :math:`\pi r^2` and the area of the square is :math:`4r^2`.

If you rearrange both equations, you see: :math:`r^2 = \frac{A_square}{4} = \frac{A_circle}{\pi}`.

Therefore, :math:`\pi = \frac{4A_circle}{A_square}`.

If you distribute points randomly on a grid and use enough points, then you can replace the
area of the square and the area of the circle with the number of points inside of each,
respectively.
"""

from math import pi, fabs


class Pi(object):
    def __init__(self, generator):
        """
        Gives us tools to test how well or how quickly a random number generator can be used to
            determine pi, using the method explained above.

        :param callable generator: A PRNG or RNG that gives numbers in [0, 1)
        """
        self.test_generator = generator
        self.in_circle = 0
        self.iterations = 0

    def _plot_point(self):
        """
        Adds one point to the estimate of pi and increments internal states (iterations, points
            within circle) accordingly.

        :return: None
        """
        x = self.test_generator()
        y = self.test_generator()
        self.in_circle += ((x ** 2 + y ** 2) <= 1)
        self.iterations += 1

    def _calculate_eps(self):
        """
        Calculates the difference between the estimate of pi and the actual value of pi.

        :return: The absolute error between the current estimate of pi and the actual value of pi
        :rtype: float
        :note:
            This is lacking any guidance as to how close you _should_ be to pi after a given number
            of iterations.
        """
        pi_est = 4 * self.in_circle / self.iterations
        return fabs(pi_est - pi)

    def bounded_test(self, iterations):
        """
        Calculates the error (epsilon) between pi as calculated by the provided generator and 
            actual pi after a given number of iterations.

        :param int iterations: The number of iterations to try. Please use a positive integer.
        :return: The error between the calculated value of pi and the real value of pi
        :rtype: float
        """
        self.in_circle = 0
        self.iterations = 0
        for _ in range(iterations):
            self._plot_point()

        return self._calculate_eps()

    def unbounded_test(self, tolerance, max_iterations=None):
        """
        Calculate the number of iterations (up to an optional max) that the generator requires to
            get to a certain precision of pi (tolerance).

        :param float tolerance: The precision/closeness with which you want the generator to get
            to pi
        :param int max_iterations: An optional number provided as a courtesy to prevent melted CPUs.
            Use this to terminate iteration after a certain number of tests.
        :return: The number of iterations required to get to pi within the provided tolerance.
        :rtype: int
        """
        self.in_circle = 0
        self.iterations = 0
        self._plot_point()
        while self._calculate_eps() > tolerance and \
                (not max_iterations or self.iterations < max_iterations):
            self._plot_point()

        return self.iterations

