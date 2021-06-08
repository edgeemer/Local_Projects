from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np
from cmath import sqrt

# Создание файла.
pdf = PdfPages("../Figures.pdf")

# Создание сюжетов и их сохранение.
FUNCTIONS = [np.sin, np.cos, lambda x: x**2]
X = np.linspace(-5, 5, 100)
X1 = (X-2)**3
for function in FUNCTIONS:
    plt.plot(X1, function(X1))
    pdf.savefig()
    plt.close()
X2 = []
for x in X1:
    X2.append(sqrt((x-2)**3))
X2 = np.array(X2)
plt.plot(X1, X2)
pdf.savefig()
plt.close()

# Сохранение файла
pdf.close()
