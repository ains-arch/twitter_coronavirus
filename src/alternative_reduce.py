#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--keys',nargs='+',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

for key in args.keys:
    # load each of the input paths
    sorted(args.input_paths)
    yaxis = []
    total = defaultdict(lambda: Counter())
    for path in args.input_paths:
        with open(path) as f:
            tmp = json.load(f)
            num = 0
            try:
                for k in tmp[key]:
                    num += tmp[key][k]
            except:
                print('man')
            yaxis.append(num)
    plt.plot(np.arange(366), yaxis, label = key)
n = len(args.keys)
ind = np.arange(n)
plt.ylabel('# of Tweets')
plt.xticks(ind, args.keys)
plt.xlabel('Day')
# fig, ax = plt.subplots(nrows=1, ncols=1)
# ax.plot(keys[0:11], values[0:11])
plt.legend()
plt.savefig('alternative')
#plt.close(fig)
# print(k,':',v)