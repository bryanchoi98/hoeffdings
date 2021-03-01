import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv("rs_1.csv")

# df.plot(kind='line', x='x', y='y', logx=True)
# plt.show()

import csv
with open('lw_1.csv', 'r') as file:
    reader = csv.reader(file)
    pactual = 0.31767256956993134
    epsilon = 0.010133060973840369
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
        # if counter > 0:
        #     if int(row[0]) == 1:
        #         rain += (float(row[0]) * float(row[1]))
        # counter += 1
        # finalhash.append([counter, rain])
        # print(rain/counter)
        # if int(row[0]) == 1:
        rain += (float(row[0]) * float(row[1]))
        counter += (float(row[0]) * float(row[1]))
        accepted.append(accept)
        rejected.append(reject)
        rejectionsampling.append(accept)
        index.append(counter)
        if accept == 0:
            finalhash.append(0)
            epsilons.append(0)
            accept+=1
        else:
            # print(rain/counter)
            finalhash.append(rain/counter)
            epsilons.append(abs((rain/accept) - pactual))
    print(counter)
    plt.figure()
    # plt.errorbar(x=index, y=finalhash, yerr=epsilon)
    print(rain, counter)
    print(counter)
    plt.plot(finalhash)
    plt.xscale('log')
    # plt.show()
    
