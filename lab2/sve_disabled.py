import matplotlib.pyplot as plt

x = [1024, 2048]
sve_tick = [35430000, 28962000]
sve_disabled_tick = [127915000, 51190000]

plt.figure()
plt.xlabel('Vector size')
plt.ylabel('Final tick')
plt.plot(x, sve_tick, label="active")
plt.plot(x, sve_disabled_tick, label="disabled")
plt.legend(loc="upper right")
plt.show()
