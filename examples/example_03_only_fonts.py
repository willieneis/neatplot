import numpy as np
import matplotlib.pyplot as plt

import neatplot
neatplot.set_style('fonts')


# Data
x = np.linspace(0, 10, 100)
y = np.cos(x)
z = np.sin(x) + 0.1 * x
zz = -0.5 * np.cos(x)

# Plot
fig, ax = plt.subplots()
ax.plot(x, y, label='Cos($x$)')
ax.plot(x, z, '--', label='Sin($x$) + $0.1x$')
ax.plot(x, zz, ':', label='$-\\frac{1}{2}$Cos($x$)')

# Text
ax.legend(loc=1)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_title('Sine($x$) and Cosine($x$)')

# Lims
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-1.5, 2.5)

# Show figure
plt.show()
