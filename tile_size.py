import matplotlib.pyplot as plt

x = [8, 16, 32, 64, 128]
final_tick = [233794035000, 104902746000, 69872753000, 57170921000, 51750534000]

bw_read = [3261674, 7302154, 11065601, 13690876, 15598525]
bw_inst_read = [255404, 569213, 854582, 1044447, 1153843]
bw_write = [1558705, 3506791, 5367471, 6726776, 7905001]
bw_total = [4820380, 10808945, 16433072, 20417653, 23503526]

plt.figure()
plt.xlabel('Tile size')
plt.ylabel('Final tick')
plt.plot(x, final_tick)

plt.figure()
plt.xlabel('Tile size')
plt.ylabel('Bandwidth (Bytes / s)')
plt.plot(x, bw_read, label="read")
plt.plot(x, bw_inst_read, label="instructions read")
plt.plot(x, bw_write, label="write")
plt.plot(x, bw_total, label="total")
plt.legend(loc="upper right")
plt.show()

plt.show()
