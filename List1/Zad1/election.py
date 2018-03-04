import matplotlib.pyplot as plt
from random import random
from math import log2, ceil

# population_ages = [23, 54, 12, 53, 65, 76, 43, 65, 12, 54, 89, 76, 34, 45, 65, 44, 33, 21, 32, 54, 87, 65, 78, 54, 74, 23, 25, 26, 1]
# bins = [x*10 for x in range(0,9)]

def has_broadcasted(probability_of_broadcasting):
    return random() < probability_of_broadcasting

# def election(number_of_stations, probability_of_broadcasting):
#     number_of_attempts_in_slot = 0
#     i = 0
#     while number_of_attempts_in_slot != 1:
#         number_of_attempts_in_slot = 0
#         i += 1
#         for station in range(number_of_stations):
#             if has_broadcasted(probability_of_broadcasting):
#                 number_of_attempts_in_slot += 1
#     return i

def election(number_of_stations, probability_of_broadcasting = [], *args):
    number_of_attempts_in_slot = 0
    i = 0
    while number_of_attempts_in_slot != 1:
        number_of_attempts_in_slot = 0
        i += 1
        position_in_probability_list = (i - 1) % len(probability_of_broadcasting)
        for station in range(number_of_stations):
            if has_broadcasted(probability_of_broadcasting[position_in_probability_list]):
                number_of_attempts_in_slot += 1
    return i

def plot_histogram(number_of_slots_till_success, bins):
    plt.hist(number_of_slots_till_success, bins=bins, rwidth=0.8)
    
    plt.xlabel("Number of slots required for success")
    plt.ylabel("Number of trials")
    plt.title("ELECTION(p)")

    plt.show()

# scenario 1 - number of stations known
def test1(number_of_stations, number_of_trials):
    bins = []
    bins.extend([i+0.5 for i in range(20)])
    probability_of_broadcasting = [1/number_of_stations]
    number_of_slots_till_success = []
    for i in range (number_of_trials):
        number_of_slots_till_success.extend([election(number_of_stations, probability_of_broadcasting)])
    
    plot_histogram(number_of_slots_till_success, bins)

# scenario 2 - upper limit on number of stations
def test2(number_of_stations, upper_limit, number_of_trials):
    number_of_trials_per_round = ceil(log2(upper_limit))
    bins = []
    bins.extend([i+0.5 for i in range(40)])
    probability_of_broadcasting = []
    for i in range(1, number_of_trials_per_round + 1):
        probability_of_broadcasting.extend([1/(2**i)])
    number_of_slots_till_success = []
    for i in range (number_of_trials):
        number_of_slots_till_success.extend([election(number_of_stations, probability_of_broadcasting)])

    plot_histogram(number_of_slots_till_success, bins)


test1(10, 10000)
#test2(2, 100, 10000)
#test2(50,100, 10000)
#test2(100, 100, 10000)