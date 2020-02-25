import matplotlib.pyplot as plt

# FLOPS = 4 CPUs * 2 cores * 2GHz = 16GFLOPS
Cortex_A15_peak = 16000000 #FLOPS
x64_DDR3_1600_bw = 12800000  # RAM bandwidth in B/s

computer_bound = Cortex_A15_peak / x64_DDR3_1600_bw

AI = [0, computer_bound, 4]
FLOPs = [0, Cortex_A15_peak, Cortex_A15_peak]

#threaded_insts = 6216906 + 4271814 + 4483288 + 7747797
threaded_insts = 589824 + 524288 + 524288 + 524288
threaded_bytes = 122776
threaded_duration = 55.053555

threaded_AI = threaded_insts / threaded_bytes
threaded_FLOPs = threaded_insts / threaded_duration
print(threaded_FLOPs)
#threaded_tiled_insts = 11121753 + 9515952 + 10221995 + 12815746
threaded_tiled_insts = 589824 + 524288 + 524288 + 524288
threaded_tiled_bytes = 138585
threaded_tiled_duration = 55.053555

threaded_tiled_AI = threaded_tiled_insts / threaded_tiled_bytes
threaded_tiled_FLOPs = threaded_tiled_insts / threaded_tiled_duration

plt.figure()
plt.xlabel('Arithmetic Intensity (FLOPs / Byte)')
plt.ylabel('Perf. (FLOPS)')
plt.plot(AI, FLOPs, label='Roofline')
#plt.plot(threaded_AI, threaded_FLOPs, 'ro', label='Version 3')
#plt.plot(threaded_tiled_AI, threaded_tiled_FLOPs, 'go', label='Version 4')
#plt.legend(loc="upper right")
plt.show()

