"""
Falling object family of curves for varying mass
Created on Fri Dec 14 23:24:12 2018
@author: aalpanigrahi
"""

import matplotlib.pyplot as plt

time_arr1 = [0]  # Will store time for all the velocity arrays
velo_arr1 = [0]  # Will store velocity for condition 1
velo_arr2 = [0]  # Will store velocity for condition 2
velo_arr3 = [0]  # Will store velocity for condition 3
velo_arr4 = [0]  # Will store velocity for condition 4
velo_arr5 = [0]  # Will store velocity for condition 5
velo_arr6 = [0]  # Will store velocity for condition 6
velo_arr7 = [0]  # Will store velocity for condition 7
velo_arr8 = [0]  # Will store velocity for condition 8
velo_arr9 = [0]  # Will store velocity for condition 9
velo_arr10 = [0]  # Will store velocity for condition 10

time_arr_ss = [0]
velo_arr_ss = [0]  # Will store velocity for space shuttle

def velocity_time1(mass,tdiff,drag_coeff,n):  # mass= mass of object , tdiff= diff in time & drag_coeff=drag coefficient
    i = 0                                       # n=number of data points to calculate
    while i <= n-1:
        v_next = velo_arr1[i] + (9.8 - (drag_coeff * 1.0 * velo_arr1[i])/(mass * 1.0)) * tdiff
        velo_arr1.append(v_next)
        time_arr1.append(time_arr1[i] + tdiff)
        i=i+1

def velocity_time2(mass,tdiff,drag_coeff,n):  # mass= mass of object , tdiff= diff in time & drag_coeff=drag coefficient
    i = 0                                       # n=number of data points to calculate
    while i <= n-1:
        v_next = velo_arr2[i] + (9.8 - (drag_coeff * 1.0 * velo_arr2[i])/(mass * 1.0)) * tdiff
        velo_arr2.append(v_next)
        i=i+1

def velocity_time3(mass,tdiff,drag_coeff,n):  # mass= mass of object , tdiff= diff in time & drag_coeff=drag coefficient
    i = 0                                       # n=number of data points to calculate
    while i <= n-1:
        v_next = velo_arr3[i] + (9.8 - (drag_coeff * 1.0 * velo_arr3[i])/(mass * 1.0)) * tdiff
        velo_arr3.append(v_next)
        i=i+1


def velocity_time4(mass,tdiff,drag_coeff,n):  # mass= mass of object , tdiff= diff in time & drag_coeff=drag coefficient
    i = 0                                       # n=number of data points to calculate
    while i <= n-1:
        v_next = velo_arr4[i] + (9.8 - (drag_coeff * 1.0 * velo_arr4[i])/(mass * 1.0)) * tdiff
        velo_arr4.append(v_next)
        i=i+1

def velocity_time5(mass,tdiff,drag_coeff,n):  # mass= mass of object , tdiff= diff in time & drag_coeff=drag coefficient
    i = 0                                       # n=number of data points to calculate
    while i <= n-1:
        v_next = velo_arr5[i] + (9.8 - (drag_coeff * 1.0 * velo_arr5[i])/(mass * 1.0)) * tdiff
        velo_arr5.append(v_next)
        i=i+1


def velocity_time7(mass, tdiff, drag_coeff,
                   n):  # mass= mass of object , tdiff= diff in time & drag_coeff=drag coefficient
    i = 0  # n=number of data points to calculate
    while i <= n - 1:
        v_next = velo_arr7[i] + (9.8 - (drag_coeff * 1.0 * velo_arr7[i]) / (mass * 1.0)) * tdiff
        velo_arr7.append(v_next)
        i = i + 1


def velocity_time8(mass, tdiff, drag_coeff,
                   n):  # mass= mass of object , tdiff= diff in time & drag_coeff=drag coefficient
    i = 0  # n=number of data points to calculate
    while i <= n - 1:
        v_next = velo_arr8[i] + (9.8 - (drag_coeff * 1.0 * velo_arr8[i]) / (mass * 1.0)) * tdiff
        velo_arr8.append(v_next)
        i = i + 1


def velocity_time9(mass, tdiff, drag_coeff,
                   n):  # mass= mass of object , tdiff= diff in time & drag_coeff=drag coefficient
    i = 0  # n=number of data points to calculate
    while i <= n - 1:
        v_next = velo_arr9[i] + (9.8 - (drag_coeff * 1.0 * velo_arr9[i]) / (mass * 1.0)) * tdiff
        velo_arr9.append(v_next)
        i = i + 1


def velocity_time10(mass, tdiff, drag_coeff,
                   n):  # mass= mass of object , tdiff= diff in time & drag_coeff=drag coefficient
    i = 0  # n=number of data points to calculate
    while i <= n - 1:
        v_next = velo_arr10[i] + (9.8 - (drag_coeff * 1.0 * velo_arr10[i]) / (mass * 1.0)) * tdiff
        velo_arr10.append(v_next)
        i = i + 1

#Orion multipurpose crew vehicle
def velocity_time_orion(mass, tdiff, drag_coeff,
                   n):  # mass= mass of object , tdiff= diff in time & drag_coeff=drag coefficient
    i = 0  # n=number of data points to calculate
    while i <= n - 1:
        v_next = velo_arr_ss[i] + (9.8 - (drag_coeff * 1.0 * velo_arr_ss[i]) / (mass * 1.0)) * tdiff
        velo_arr_ss.append(v_next)
        time_arr_ss.append(time_arr_ss[i] + tdiff)
        i = i + 1


velocity_time1(30, 2, 12.5, 50)
velocity_time2(40, 2, 12.5, 50)
velocity_time3(50, 2, 12.5, 50)
velocity_time4(60, 2, 12.5, 50)
velocity_time5(70, 2, 12.5, 50)
velocity_time7(90, 2, 12.5, 50)
velocity_time8(100, 2, 12.5, 50)
velocity_time9(110, 2, 12.5, 50)
velocity_time10(120, 2, 12.5, 50)
# Orion multipurpose crew vehicle weighs 25,848 kg
velocity_time_orion(25848, 2, 12.5, 10000)

# print velocity_arr
# print time_arr
plt.plot(time_arr1, velo_arr1 , time_arr1 , velo_arr2 , time_arr1 , velo_arr3, time_arr1 , velo_arr4, time_arr1 , velo_arr5, time_arr1 , velo_arr7, time_arr1 , velo_arr8, time_arr1 , velo_arr9, time_arr1 , velo_arr10)
plt.suptitle("Mathematical model for falling object by euler's method")
plt.xlabel("Time (In Sec)")
plt.ylabel("Velocity (In m/s)")
plt.show()

plt.plot(time_arr_ss,velo_arr_ss)
plt.suptitle("Mathematical model for orion shuttle by euler's method")
plt.xlabel("Time (In Sec)")
plt.ylabel("Velocity (In m/s)")
plt.show()
