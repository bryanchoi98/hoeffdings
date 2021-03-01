import pandas as pd
import matplotlib.pyplot as plt
import math

# df = pd.read_csv("rs_1.csv")

# df.plot(kind='line', x='x', y='y', logx=True)
# plt.show()

import csv
with open('rs_1.csv', 'r') as file:
    reader = csv.reader(file)
    pactual = 0.31767256956993134
    epsilon = 0.0081292841
    # for row in reader:
    #     print(row)
    counter = 0
    rain = 0
    accept = 0
    reject = 0
    index = []
    accepted = []
    rejected = []
    rejectionsampling = []
    epsilons = []
    finalhash = []
    addepsilon = []
    subepsilon = []
    for row in reader:
        # print(row[1])
        if int(row[1]) >= 0:
            accept += 1
        else:
            reject += 1
        if counter > 0:
            if int(row[1]) == 1:
                rain += 1
        counter += 1
        # finalhash.append([counter, rain])
        # print(rain/counter)
        accepted.append(accept)
        rejected.append(reject)
        rejectionsampling.append(accept)
        index.append(counter)
        if accept == 0:
            finalhash.append(0)
            epsilons.append(0)
        else:
            epsilon = math.sqrt(3.688879/(2 * counter))
            finalhash.append(rain/accept)
            epsilons.append(epsilon)
            addepsilon.append(rain/accept + epsilon)
            subepsilon.append(rain/accept - epsilon)
    # print(counter)
    # print(rain)
    # print(finalhash)
    # plt.plot(finalhash)
    print(counter)
    plt.figure()
    # plt.errorbar(x=index, y=finalhash, yerr=epsilon)
    plt.plot(finalhash)
    plt.plot(addepsilon)
    plt.plot(subepsilon)
    plt.xscale('log')
    plt.show()
    print(epsilons)
    # print(epsilons)
    
