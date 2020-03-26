import matplotlib.pyplot as plt

from lab3.data.MESI.mb1.MESI_microbench1_1024 import CPU_1 as CPU_1_mesi_1024, CPU_2 as CPU_2_mesi_1024, \
    CPU_3 as CPU_3_mesi_1024
from lab3.data.MESI.mb1.MESI_microbench1_2048 import CPU_1 as CPU_1_mesi_2048, CPU_2 as CPU_2_mesi_2048, \
    CPU_3 as CPU_3_mesi_2048
from lab3.data.MESI.mb1.MESI_microbench1_32768 import CPU_1 as CPU_1_mesi_32768, CPU_2 as CPU_2_mesi_32768, \
    CPU_3 as CPU_3_mesi_32768
from lab3.data.MESI.mb1.MESI_microbench1_65536 import CPU_1 as CPU_1_mesi_65536, CPU_2 as CPU_2_mesi_65536, \
    CPU_3 as CPU_3_mesi_65536
from lab3.data.MSI.mb1.MSI_microbench1_1024 import CPU_1 as CPU_1_msi_1024, CPU_2 as CPU_2_msi_1024, \
    CPU_3 as CPU_3_msi_1024
from lab3.data.MSI.mb1.MSI_microbench1_2048 import CPU_1 as CPU_1_msi_2048, CPU_2 as CPU_2_msi_2048, \
    CPU_3 as CPU_3_msi_2048
from lab3.data.MSI.mb1.MSI_microbench1_32768 import CPU_1 as CPU_1_msi_32768, CPU_2 as CPU_2_msi_32768, \
    CPU_3 as CPU_3_msi_32768
from lab3.data.MSI.mb1.MSI_microbench1_65536 import CPU_1 as CPU_1_msi_65536, CPU_2 as CPU_2_msi_65536, \
    CPU_3 as CPU_3_msi_65536
from lab3.functions import mean_cpu_cores, filter_array

# BENCHMARK 1

x = [1024, 2048, 32768, 65536]

MSI_1024 = mean_cpu_cores([CPU_1_msi_1024, CPU_2_msi_1024, CPU_3_msi_1024])
MSI_2048 = mean_cpu_cores([CPU_1_msi_2048, CPU_2_msi_2048, CPU_3_msi_2048])
MSI_32768 = mean_cpu_cores([CPU_1_msi_32768, CPU_2_msi_32768, CPU_3_msi_32768])
MSI_65536 = mean_cpu_cores([CPU_1_msi_65536, CPU_2_msi_65536, CPU_3_msi_65536])

MESI_1024 = mean_cpu_cores([CPU_1_mesi_1024, CPU_2_mesi_1024, CPU_3_mesi_1024])
MESI_2048 = mean_cpu_cores([CPU_1_mesi_2048, CPU_2_mesi_2048, CPU_3_mesi_2048])
MESI_32768 = mean_cpu_cores([CPU_1_mesi_32768, CPU_2_mesi_32768, CPU_3_mesi_32768])
MESI_65536 = mean_cpu_cores([CPU_1_mesi_65536, CPU_2_mesi_65536, CPU_3_mesi_65536])

MSI = [MSI_1024, MSI_2048, MSI_32768, MSI_65536]
MESI = [MESI_1024, MESI_2048, MESI_32768, MESI_65536]

plt.figure()
plt.xlabel("Array Size")
plt.ylabel("Read Hits")
plt.plot(x, filter_array(MSI, 1), label="MSI")
plt.plot(x, filter_array(MESI, 1), label="MESI")
plt.show()

plt.figure()
plt.xlabel("Array Size")
plt.ylabel("Read Misses")
plt.plot(x, filter_array(MSI, 2), label="MSI")
plt.plot(x, filter_array(MESI, 2), label="MESI")
plt.show()


plt.figure()
plt.xlabel("Array Size")
plt.ylabel("Read Requests Sent")
plt.plot(x, filter_array(MSI, 4), label="MSI")
plt.plot(x, filter_array(MESI, 4), label="MESI")
plt.show()

# BENCHMARK 2
