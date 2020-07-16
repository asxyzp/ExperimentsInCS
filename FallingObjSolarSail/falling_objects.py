#Program for mathematical model of a falling object using divided difference method or euler's method
#Created by Aashish Loknath Panigrahi
import matplotlib.pyplot as plt
time_arr=[0]                                 #Will store values of time with initial time =0 s
velocity_arr=[0]                             #Will store values of velocity with initial time =0 m/s
def velocity_time(mass,tdiff,drag_coeff,n):  #mass= mass of object , tdiff= diff in time & drag_coeff=drag coefficient
    i=0                                      #n=number of data points to calculate
    while i<=n-1:
        v_next=velocity_arr[i]+(9.8-(drag_coeff*1.0*velocity_arr[i])/(mass*1.0))*tdiff
        velocity_arr.append(v_next)
        time_arr.append(time_arr[i]+tdiff)
        i=i+1

velocity_time(50,2,12.5,50)
#print velocity_arr
#print time_arr
plt.plot(time_arr,velocity_arr)
plt.suptitle("Mathematical model for falling object by euler's method")
plt.xlabel("Time (In Sec)")
plt.ylabel("Velocity (In m/s)")
plt.show()
