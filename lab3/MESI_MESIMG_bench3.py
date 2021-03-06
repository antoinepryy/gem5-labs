import matplotlib.pyplot as plt

from lab3.data.MESI.mb3.MESI_microbench3_1024 import CPU_1 as CPU_1_mesi_1024, CPU_2 as CPU_2_mesi_1024
from lab3.data.MESI.mb3.MESI_microbench3_2048 import CPU_1 as CPU_1_mesi_2048, CPU_2 as CPU_2_mesi_2048
from lab3.data.MESI.mb3.MESI_microbench3_32768 import CPU_1 as CPU_1_mesi_32768, CPU_2 as CPU_2_mesi_32768
from lab3.data.MESI.mb3.MESI_microbench3_65536 import CPU_1 as CPU_1_mesi_65536, CPU_2 as CPU_2_mesi_65536
from lab3.data.MESIMG.mb3.MESIMG_microbench3_1024 import CPU_1 as CPU_1_mesimg_1024, CPU_2 as CPU_2_mesimg_1024
from lab3.data.MESIMG.mb3.MESIMG_microbench3_2048 import CPU_1 as CPU_1_mesimg_2048, CPU_2 as CPU_2_mesimg_2048
from lab3.data.MESIMG.mb3.MESIMG_microbench3_32768 import CPU_1 as CPU_1_mesimg_32768, CPU_2 as CPU_2_mesimg_32768
from lab3.data.MESIMG.mb3.MESIMG_microbench3_65536 import CPU_1 as CPU_1_mesimg_65536, CPU_2 as CPU_2_mesimg_65536
from lab3.functions import mean_cpu_cores, filter_array

# BENCHMARK 3

x = [1024, 2048, 32768, 65536]

MESIMG_1024 = mean_cpu_cores([CPU_1_mesimg_1024, CPU_2_mesimg_1024])
MESIMG_2048 = mean_cpu_cores([CPU_1_mesimg_2048, CPU_2_mesimg_2048])
MESIMG_32768 = mean_cpu_cores([CPU_1_mesimg_32768, CPU_2_mesimg_32768])
MESIMG_65536 = mean_cpu_cores([CPU_1_mesimg_65536, CPU_2_mesimg_65536])

MESI_1024 = mean_cpu_cores([CPU_1_mesi_1024, CPU_2_mesi_1024])
MESI_2048 = mean_cpu_cores([CPU_1_mesi_2048, CPU_2_mesi_2048])
MESI_32768 = mean_cpu_cores([CPU_1_mesi_32768, CPU_2_mesi_32768])
MESI_65536 = mean_cpu_cores([CPU_1_mesi_65536, CPU_2_mesi_65536])

MESIMG = [MESIMG_1024, MESIMG_2048, MESIMG_32768, MESIMG_65536]
MESI = [MESI_1024, MESI_2048, MESI_32768, MESI_65536]

data_array = {0: "CPUId",
              1: "numReadHits",
              2: "numReadMisses",
              3: "numReadOnInvalidMisses",
              4: "numReadRequestsSent",
              5: "numReadMissesServicedByOthers",
              6: "numReadMissesServicedByShared",
              7: "numReadMissesServicedByModified",
              8: "numWriteHits",
              9: "numWriteMisses",
              10: "numWriteOnSharedMisses",
              11: "numWriteOnInvalidMisses",
              12: "numInvalidatesSent",
              13: "numInclusionMisses",
              14: "numInclusionHits",
              15: "numLLCMisses",
              16: "numLLCHits"
              }

plt.figure()
plt.xlabel("Array Size")
plt.ylabel("Read Requests")
plt.plot(x, filter_array(MESIMG, 1), label="MESIMG Hits")
plt.plot(x, filter_array(MESI, 1), label="MESI Hits")
plt.plot(x, filter_array(MESIMG, 2), label="MESIMG Misses")
plt.plot(x, filter_array(MESI, 2), label="MESI Misses")
plt.legend(loc="upper right")
plt.show()

plt.figure()
plt.xlabel("Array Size")
plt.ylabel("Miss Serviced by")
plt.plot(x, filter_array(MESIMG, 6), label="Shared in MESIMG")
plt.plot(x, filter_array(MESIMG, 7), label="Modified in MESIMG")
plt.plot(x, filter_array(MESI, 6), label="Shared in MESI")
plt.plot(x, filter_array(MESI, 7), label="Modified in MESI")
plt.legend(loc="upper right")
plt.show()

plt.figure()
plt.xlabel("Array Size")
plt.ylabel("Write Requests")
plt.plot(x, filter_array(MESIMG, 8), label="MESIMG Hits")
plt.plot(x, filter_array(MESIMG, 9), label="MESIMG Misses")
plt.plot(x, filter_array(MESI, 8), label="MESI Hits")
plt.plot(x, filter_array(MESI, 9), label="MESI Misses")
plt.legend(loc="upper right")
plt.show()

plt.figure()
plt.xlabel("Array Size")
plt.ylabel("Invalidates Sent")
plt.plot(x, filter_array(MESIMG, 12), label="MESIMG")
plt.plot(x, filter_array(MESI, 12), label="MESI")
plt.legend(loc="upper right")
plt.show()
