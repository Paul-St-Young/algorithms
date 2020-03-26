import numpy as np
import random


def calc_distance(city_list, number_cities):
    sum_distance = 0
    for  city in range(number_cities):
        pair1 = city_list[city]
        pair2 = city_list[(city+1)%number_cities]
        #print('pair2 ', pair2)
        distance = np.sqrt((pair1[0] - pair2[0])**2 + (pair1[1] - pair2[1])**2)
        sum_distance += distance

    return sum_distance

def switch(city_list, index1, index2):

    list_copy = list(city_list)
    list_copy[index1] = city_list[index2]
    list_copy[index2] = city_list[index1]

    return list_copy

#------------------------------------------------------------------------------
#                                  main
#-------------------------------------------------------------------------------
tau_init = 100
time_const = 10
tau_iters = 1000
number_cities = 100
city_list = []

for city in range(number_cities):
    x = random.uniform(0,20)
    y = random.uniform(0,20)
    city_list.append((x,y))

tau_schedule = [tau_init * np.exp(-t/time_const) for t \
                        in range(0,tau_iters)]

print('previous city distance' , calc_distance(city_list, number_cities))

for tau in tau_schedule:
    while(True):
        city_i = int(random.randint(0,number_cities-1))
        city_j = int(random.randint(0,number_cities-1))
        if(city_i != city_j ):
            break

    D_old = calc_distance(city_list, number_cities)
    proposed_city_list  = switch(city_list, city_i, city_j)
    #print('proposesd', proposed_city_list)
    D_new = calc_distance(proposed_city_list, number_cities)
    delta_distance = D_new - D_old
    #print('delta_distance', delta_distance)


    if delta_distance <= 0:
        city_list = proposed_city_list
    else :
        acceptance_prob = min(1,np.exp(-delta_distance/tau))
        if acceptance_prob > random.uniform(0,1):
            city_list = proposed_city_list


print('final city distance: ', calc_distance(city_list, number_cities))
