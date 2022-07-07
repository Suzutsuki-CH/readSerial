import pandas
import matplotlib.pyplot as plt
from scipy.fft import *
import numpy as np
import time


cNames = ["Mag1","Mag2","Mag3",
          "Acc1_1","Acc1_2","Acc1_3",
          "Gyro1","Gyro2","Gyro3",
          "Acc2_1","Acc2_12","Acc2_3","Time"]
raw = pandas.read_csv("AGM_data.csv",names=cNames)

Time = raw.Time.to_list()
Acc1_1 = raw.Acc1_1.to_list()
Acc1_2 = raw.Acc1_2.to_list()
Acc1_3 = raw.Acc1_3.to_list()

Avg1_1 = np.average(Acc1_1)
Acc1_1 = [x-Avg1_1 for x in Acc1_1]
Avg1_2 = np.average(Acc1_2)
Acc1_2 = [x-Avg1_2 for x in Acc1_2]
Avg1_3 = np.average(Acc1_3)
Acc1_3 = [x-Avg1_3 for x in Acc1_3]


# Initial starting point
t0 = Time[0]
# Set the first element to 0 and convert unit to second
Time = [(x-t0) for x in Time]


f = np.fft.fftfreq(2000,6)  # Frequency steps
# f = [x/2000 for x in Time]

# FFT for Acc1_1
# 1657207723942751300
init = time.time_ns()

while True:
    if time.time_ns()!=init:
        diff = time.time_ns()
        break



print(diff-init)

Acc1_1_F=fft(Acc1_1)
end = time.time_ns()



while True:
    if time.time_ns()!=init:
        # print(time.time_ns())
        break

Acc1_1_mag=np.abs(Acc1_1_F)/len(Acc1_1)
# FFT for Acc1_2
Acc1_2_F=fft(Acc1_2)
Acc1_2_mag=np.abs(Acc1_2_F)/len(Acc1_2)
# FFT for Acc1_3
Acc1_3_F=fft(Acc1_3)
Acc1_3_mag=np.abs(Acc1_3_F)/len(Acc1_3)


# Test code
# SinWave = [np.sin(2*np.pi*x) for x in Time]
# SinF = fft(SinWave)
# SinF_mag = np.abs(SinF)/len(SinWave)

# Test plot
# fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
# ax1.plot(Time,SinWave,'.-',alpha=0.4,markersize=2)
# ax2.plot(f,SinF,'.-',alpha=0.4,markersize=2)
# ax2.set_xlim([-0.00005,0.0001])
#   plt.show()

# plot
fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
ax1.plot(Time,Acc1_1,'.-',alpha=0.4,markersize=2)
ax2.plot(f,Acc1_1_mag,'.-',alpha=0.4,markersize=2)
plt.show()
# plot
fig, [[ax1_1, ax1_2, ax1_3],[ax1_1_f, ax1_2_f, ax1_3_f]] = plt.subplots(nrows=2, ncols=3)

ax1_1.plot(Time,Acc1_1,'.-',alpha=0.4,markersize=2)
ax1_1_f.plot(f,Acc1_1_mag,'.-',alpha=0.4,markersize=2)
ax1_2.plot(Time,Acc1_2,'.-',alpha=0.4,markersize=2)
ax1_2_f.plot(f,Acc1_2_mag,'.-',alpha=0.4,markersize=2)
ax1_3.plot(Time,Acc1_3,'.-',alpha=0.4,markersize=2)
ax1_3_f.plot(f,Acc1_3_mag,'.-',alpha=0.4,markersize=2)
plt.show()
