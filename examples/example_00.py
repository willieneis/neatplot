import numpy as np
import matplotlib.pyplot as plt

import neatplot
neatplot.set_style()


x = np.linspace(0, 10, 100)
y = np.cos(x)
z = np.sin(x) + 0.1 * x
zz = -0.5 * np.cos(x)


h1, = plt.plot(x, y, label='Cos($x$)')
h2, = plt.plot(x, z, '--', label='Sin($x$) + $0.1x$')
h3, = plt.plot(x, zz, ':', label='$-\\frac{1}{2}$Cos($x$)')


plt.legend(handles=[h1, h2, h3], loc=1)

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.xlim([-0.5, 10.5])
plt.ylim([-1.5, 2.5])

plt.title('Sine($x$) and Cosine($x$)')

neatplot.save_figure('example_00')

plt.show()
