import numpy as np
import matplotlib.pyplot as plt

from random import randint
niveles = int(12)
if niveles >= 1:
  lineas = [0]*(niveles)

for h in range((niveles)**1*250):
  almacen = -1
  for j in range(niveles):
    almacen += randint(0, 1)
  lineas[almacen] += 1
print((niveles)**1*250, "canicas fueron utilizadas")
print(lineas)
X = np.arange(-((len(lineas)/2)-.5), (len(lineas)/2)+.5)
plt.suptitle('GRAFICA DE GALTON')
plt.bar(X + 0.00, lineas, width=0.25)
plt.show()