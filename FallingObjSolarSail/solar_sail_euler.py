#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mathematical model of solar sail
@author: aalpanigrahi
"""

#Import statements :-
import matplotlib.pyplot as plt
import math

time_arr=[0]
velo_arr=[0]
dist=[]
def ssail_vt(area,degree,distance,mass_sail,time_diff,number_of_points):
    """
    To find and plot the mathematical model of a solar sail
    :param area: Area of the solar sail
    :param degree: Degree wrt sun/star
    :param distance: Distance from sun/star
    :param mass_sail: mass of body/sail
    :return: NILL
    """
    sun_luminosity =  3.828 * (10 ** 26)
    speed_of_light = 299792458
    dist.append(distance)
    i = 0
    while i < number_of_points:
        v_next = ((sun_luminosity*area*math.cos(degree)*time_diff)/( 4*math.pi*((velo_arr[i]*time_diff+dist[i])**2)*speed_of_light*mass_sail ))+velo_arr[i]
        velo_arr.append(v_next)
        time_arr.append(time_arr[i]+time_diff)
        dist.append(velo_arr[i]*time_diff+dist[i])
        i += 1
    '''
    j=0
    while j<number_of_points:
        print(velo_arr[i]," ",time_arr[i])
    '''
dist_earth_sun = 149.6*(10**9)
degree = 0
area = 800*800
mass_sail = 10 * area
time_diff = 3600       # 60 min * 60 sec = 3600 sec or 1 hour
number_of_hours = 300
number_of_points = number_of_hours * time_diff


ssail_vt(area,degree,dist_earth_sun,mass_sail,time_diff,number_of_points)

plt.plot(time_arr,velo_arr)
plt.suptitle("Solar sail Velocity-Time plot")
plt.xlabel("Time (In Sec)")
plt.ylabel("Velocity (In m/s)")
plt.show()

plt.plot(time_arr,dist)
plt.suptitle("Solar sail Distance-Time plot")
plt.xlabel("Time (In Sec)")
plt.ylabel("Distance (In meters)")
plt.show()


