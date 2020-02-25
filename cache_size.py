import matplotlib.pyplot as plt

exp = ["L1 = 4096B, L2 = 4096B",
       "L1 = 2048B, L2 = 4096B",
       "L1 = 1024B, L2 = 4096B",
       "L1 = 1024B, L2 = 2048B",
       "L1 = 1024B, L2 = 1024B"
       ]

x = ["4096/4096",
     "2048/4096",
     "1024/4096",
     "1024/2048",
     "1024/1024"
     ]
final_tick = [
    132119850000,
    175517156000,
    198279143000,
    201011407000,
    201052413000
]

# T1 T2 T3 T4 T5 average hit

L1_miss_rate = [0.062362, 0.224800, 0.288673, 0.288673, 0.288673]
L2_miss_rate = [0.309918, 0.099225, 0.088960, 0.103981, 0.104597]

L1_overall_hits = [9323264, 7708102, 7072985, 7072985, 7072985]
L2_overall_hits = [428657, 2014439, 2616013, 2572882, 2571111]

plt.figure()
plt.xlabel('L1/L2 (Bytes)')
plt.ylabel('Final Tick (nb)')
plt.plot(x, final_tick)

plt.figure()
plt.xlabel('L1/L2 (Bytes)')
plt.ylabel('Miss Rate')
plt.plot(x, L1_miss_rate, 'r', label='L1')
plt.plot(x, L2_miss_rate, 'b', label='L2')
plt.legend(loc="upper right")

plt.figure()
plt.xlabel('L1/L2 (Bytes)')
plt.ylabel('Total Hits')
plt.plot(x, L1_overall_hits, 'r', label='L1')
plt.plot(x, L2_overall_hits, 'b', label='L2')
plt.legend(loc="upper right")
plt.show()
