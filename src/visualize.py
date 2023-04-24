#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)

keys = []
values = []
for k,v in items:
    keys += [k]
    values += [int(v)]
fig = plt.bar(keys[0:11], values[0:11])
# fig, ax = plt.subplots(nrows=1, ncols=1)
# ax.plot(keys[0:11], values[0:11])
plt.savefig(f"./{args.input_path}_{args.key}_figure.png")
#plt.close(fig)
# print(k,':',v)
