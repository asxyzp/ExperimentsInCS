#Plotting blood pressure using matplotlib
#Created by asxyzp (Aashish Panigrahi)

import matplotlib.pyplot as plt

SYSTOLIC  = [136,136,135,127,124,135,120,143,126,114,110]   #Stores values of systolic blood pressure
DIASTOLIC = [88,92,90,87,88,98,88,96,89,97,84]              #Stores values of Diastolic blood pressure
HEARTB    = [69,80,77,101,93,97,86,87,82,98,111]            #Stores values of Heart beat
TIME = []
XTICKS = ["6FEB\n6:46PM","6FEB\n10:35PM","7FEB\n8:30AM","7FEB\n7:45PM","7FEB\n10:10PM","8FEB\n9:27AM","8FEB\n9:21PM","9FEB\n8:40AM","9FEB\n9:30PM","10FEB\n10:15AM","10FEB\n8:30PM"]
#(^) Stores time at which observation was taken for xticks

for i in range(1,len(SYSTOLIC)+1):
    TIME.append(i)

print("\nNumber of data points:")
print("SYS=",len(SYSTOLIC),"\nDIA=",len(DIASTOLIC),"\nHEB=",len(HEARTB),"\nTIM=",len(TIME))

#PLotting blood pressure values
plt.plot(TIME,SYSTOLIC,'r',label='Systolic Pressure')               #Plots TIME vs SYSTOLIC
plt.legend()
plt.plot(TIME,DIASTOLIC,'g',label="Diastolic Pressure")             #Plots TIME vs DIASTOLIC
plt.legend()
plt.plot(TIME,HEARTB,'b',label="Heartbeat")                         #Plots TIME vs HEARTB
plt.legend()
plt.ylabel("SYSTOLIC / DIASTOLIC / HEART BEAT")                     #Labels Y-axis
plt.xlabel("TIME")                                                  #Labels X-axis
plt.grid()                                                          #Shows grid in the graph
plt.xticks(TIME,XTICKS,rotation='vertical')                       

#Plotting normal range for DIA/HB
SYSUP = []                                                          #Will store upper bound of normal Systolic pressure range
SYSDOWN = []                                                        #Will store lower bound of normal Systolic pressure range
DIAUP = []                                                          #Will store upper bound of normal Diastolic pressure range
DIADOWN = []                                                        #Will store lower bound of normal Diastolic pressure range
for i in range(len(SYSTOLIC)):
    SYSUP.append(120)
    SYSDOWN.append(80)
    DIAUP.append(80)
    DIADOWN.append(60)
plt.plot(TIME,SYSUP,'y-',label='Systolic Pressure Upper & Lower Bound')       #Plots TIME vs SYSTOLIC MAX UP Range
plt.legend()
plt.plot(TIME,SYSDOWN,'y-',)                                                  #Plots TIME vs SYSTOLIC MAX DOWN Range
plt.plot(TIME,DIAUP,'k-',label='Diastolic Pressure Upper & Lower Bound')      #Plots TIME vs DIASTOLIC MAX UP Range
plt.legend()
plt.plot(TIME,DIADOWN,'k-')                                                   #Plots TIME vs DIASTOLIC MAX DOWN Range

plt.show()
