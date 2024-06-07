import matplotlib
matplotlib.__version__
import matplotlib.pyplot as plt
x = [2016, 2017, 2018, 2019, 2020]
y = [350, 410, 520, 695, 543]
plt.plot(x, y)
plt.show()
plt.title('Annual sales')
plt.xlabel('years')
plt.ylabel('sales')
plt.show()

# plot 스타일 예시
plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c="b", lw=5, ls="--", marker="o",
          ms=15, mec="g", mew=5, mfc="r")
plt.title("스타일 적용 예")
plt.show()


# bar plot
y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
x = range(len(y1))
x         # [0, 1, 2, 3]
plt.bar(x, y1, width = 0.7, color = "blue")
plt.bar(x, y2, width = 0.7, color = "red", bottom = y1)
plt.title('Querterly sales')
plt.xlabel('Quarters')
plt.ylabel('sales')
xLable = ['first', 'second', 'third', 'fourth']
plt.legend(['chairs', 'desks'])
plt.xticks(x, xLable, fontsize = 10)
plt.show()

# Axes3D PLOT
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
XX, YY = np.meshgrid(X, Y)
RR = np.sqrt(XX ** 2 + YY ** 2)
ZZ = np.sin(RR)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_title("3D Surface plot")
ax.plot_surface(XX, YY, ZZ, rstride=1, cstride=1, cmap='hot')
plt.show()

