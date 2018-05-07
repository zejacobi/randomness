"""
It is possible to calculate Pi by placing points randomly on a grid.

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