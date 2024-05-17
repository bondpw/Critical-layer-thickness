import numpy as np
import matplotlib.pyplot as plt

'''The range of Indium and Antimony contents you want to scan over, the third number is the amount of steps'''
In_x_list = np.linspace(0.1,0.5,10000)
Sb_y_list = np.linspace(0.65,0.95,10)
'''If only doing one calculation, these should be set for the Indium and Antimony contents respectively'''
In_x = 0.3
Sb_y = 0.1
'''Physical constants, from Matthews Blakeslee and Vurgaftman'''
b = 4
a_InSb = 6.4794
c12_InSb = 373.5
c11_InSb = 684.7
a_InAs = 6.0512
c12_InAs = 452.6
c11_InAs = 832.9
a_GaSb = 6.0959
c12_GaSb = 402.6
c11_GaSb = 884.2
a_GaAs = 5.65325
c12_GaAs = 566
c11_GaAs = 1221

'''Mathhews Blakeslee equation'''
def hc(b,e,v,x):
    return (b/(4*np.pi*e))*((1-(v*0.25))/((1+v)*0.5))*(np.log(x/b)+1)

'''List for data storage if doing a scan over multiple Indium and Antimony contents'''
hc_list = [[] for i in Sb_y_list]

'''Loop to calculate over a range'''
for i in range(len(Sb_y_list)):
    '''This set she antimony content of the alloy'''
    Sb_y = Sb_y_list[i]
    for j in range(len(In_x_list)):
        '''Setting the indium content of the alloy'''
        In_x = In_x_list[j]
        '''Calculation of alloy dependant variables'''
        a_alloy = ((In_x*Sb_y)*a_InSb) + ((In_x*(1-Sb_y))*a_InAs) + (((1-In_x)*Sb_y)*a_GaSb)+ (((1-In_x)*(1-Sb_y))*a_GaAs)
        c11_alloy =  ((In_x*Sb_y)*c11_InSb) + ((In_x*(1-Sb_y))*c11_InAs) + (((1-In_x)*Sb_y)*c11_GaSb)+ (((1-In_x)*(1-Sb_y))*c11_GaAs)
        c12_alloy = ((In_x*Sb_y)*c12_InSb) + ((In_x*(1-Sb_y))*c12_InAs) + (((1-In_x)*Sb_y)*c12_GaSb)+ (((1-In_x)*(1-Sb_y))*c12_GaAs)
        e = abs((a_GaSb / a_alloy) - 1)
        v = c12_alloy/(c12_alloy + c11_alloy)
        '''Caculation of the critical layer thickness'''
        x=2
        crit = hc(b,e,v,x)
        while abs(crit-x)>0:
            x=crit
            dumcrit = hc(b,e,v,x)
        '''This puts the critical layer thickness of a given alloy in its corresponding list'''
        hc_list[i].append(dumcrit)

'''This plots the data'''
for i in range(len(hc_list)):
    plt.plot(In_x_list,hc_list[i],label = "Sb: "+str(float('%.3g' % Sb_y_list[i])))   
plt.legend()
plt.show()     