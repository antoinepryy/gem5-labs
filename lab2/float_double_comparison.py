import matplotlib.pyplot as plt


x = [128, 256, 512, 1024, 2048]
float_tick = [126381000, 74603000, 48788000, 35430000, 28962000]
double_tick = [438905000, 232156000, 128030000, 76721000, 51190000]
float_vector = [179282, 89682, 44882, 22482, 11282]
double = []

plt.figure()
plt.xlabel('Vector size')
plt.ylabel('Final tick')
plt.plot(x, float_tick)
plt.plot(x, double_tick)
plt.show()
