import matplotlib.pyplot as plt

x = [128, 256, 512, 1024, 2048]
final_tick = [126381000, 74603000, 48788000, 35430000, 28962000]
committed_vect_instructions = [179282, 89682, 44882, 22482, 11282]
mem_read = [36288, 36288, 36288, 36288, 36288]
cache_hit_miss = [[116041, 1309], [65099, 1051], [52436, 914], [39802, 748], [33479, 671]]

plt.figure()
plt.xlabel('Vector size')
plt.ylabel('Final tick')
plt.plot(x, final_tick)

plt.figure()
plt.xlabel('Vector size')
plt.ylabel('Vector instructions committed')
plt.plot(x, committed_vect_instructions)

plt.figure()
plt.xlabel('Vector size')
plt.ylabel('Vector instructions committed')
plt.plot(x, mem_read)

plt.figure()
plt.xlabel('Vector size')
plt.ylabel('Cache request')
plt.plot(x, [k[0] for k in cache_hit_miss], label="hits")
plt.plot(x, [k[1] for k in cache_hit_miss], label="miss")

plt.show()


plt.show()
