import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
a = 6
rho = a * (1 - np.sin(x))  # 笛卡尔心形公式
plt.subplot(polar=True) # 设置为极坐标
plt.plot(x, rho, c='r')
plt.text(0, 0, 'LOVE YOU!', color='m')
plt.show()
