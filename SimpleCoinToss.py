import matplotlib.pyplot as plt
from random import *


numToss = 1000  # number of times you toss the coin
endedHeads = 0  # record how many resulted in 'heads'
endedTails = 0  # record how many resulted in 'tails'
endedEven = 0  # record how many tests ended on an even i value
endedOdd = 0  # record how many test ended on an odd i value
x = 0

for i in range(numToss):
    # print("Test Case: ", i)
    x = 1
    while randint(0, 1) != 0:
        endedTails += 1
        # print("Tails Count: ", endedTails)
        x += 1
    # else:
    endedHeads += 1
    # print("Heads Count: ", endedHeads)
    if x % 2 == 0:
        endedEven += 1
        # print("X is Even")
    else:
        endedOdd += 1
        # print("X is Odd")


# Gather results and print them to console
# results = [endedHeads, endedTails]
results2 = [endedEven, endedOdd]
print('Out of %i tosses, %i heads appeared on an even toss and %i heads appeared on an odd toss' % (numToss, endedEven, endedOdd))


plt.title("First heads on even/number of tosses(1000 simulations)")
plt.bar([0, 1], results2, width=.9, align='center')
plt.ylabel("Number of Simulations")
plt.xticks([0, 1], ["Even", "Odd"])
plt.show()
