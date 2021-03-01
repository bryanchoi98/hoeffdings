import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv("rs_1.csv")

# df.plot(kind='line', x='x', y='y', logx=True)
# plt.show()

import csv
with open('rs_1.csv', 'r') as file:
    reader = csv.reader(file)
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
        # epsilons.append(abs((rain/counter) - pactual))
        accepted.append(accept)
        rejected.append(reject)
        rejectionsampling.append(accept)
        index.append(counter)
        finalhash.append(rain/counter)
    # print(counter)
    # print(rain)
    # print(finalhash)
    print(counter)
    plt.figure()
    plt.plot(finalhash)
    # plt.errorbar(x=index, y=finalhash, yerr=epsilon)
    plt.xscale('log')
    plt.show()
    # print(accept)
    print(epsilons)
    
