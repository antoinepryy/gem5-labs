import matplotlib.pyplot as plt

# FLOPS = 4 CPUs * 2 cores * 2GHz = 16GFLOPS
Cortex_A15_peak = 16000000  # FLOPS
x64_DDR3_1600_bw = 12800000  # RAM bandwidth in B/s

computer_bound = Cortex_A15_peak / x64_DDR3_1600_bw

AI = [0, computer_bound, 20]
FLOPs = [0, Cortex_A15_peak, Cortex_A15_peak]

threaded_insts = 218267
threaded_bytes = 6759232
threaded_duration = 55.053555
threaded_AI = threaded_insts / threaded_bytes
threaded_FLOPs = threaded_insts / threaded_duration

threaded_tiled_insts = 218268
threaded_tiled_bytes = 7115904
threaded_tiled_duration = 51.346730
threaded_tiled_AI = threaded_tiled_insts / threaded_tiled_bytes
threaded_tiled_FLOPs = threaded_tiled_insts / threaded_tiled_duration

plt.figure()
plt.xlabel('Arithmetic Intensity (FLOPs / Byte)')
plt.ylabel('Perf. (FLOPS)')
plt.plot(AI, FLOPs, label='Roofline')
plt.plot(threaded_AI, threaded_FLOPs, 'ro', label='Version 3')
plt.plot(threaded_tiled_AI, threaded_tiled_FLOPs, 'go', label='Version 4')
plt.legend(loc="upper right")
plt.xscale("log")
plt.yscale("log")
plt.show()
