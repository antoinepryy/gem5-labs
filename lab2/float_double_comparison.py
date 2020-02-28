import matplotlib.pyplot as plt
from

x = [128, 256, 512, 1024, 2048]
final_tick = [126381000, 74603000, 48788000, 35430000, 28962000]

plt.figure()
plt.xlabel('Vector size')
plt.ylabel('Final tick')
plt.plot(x, final_tick)

plt.show()
