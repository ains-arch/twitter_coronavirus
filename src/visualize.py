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
import numpy as np

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
#print(items)
keys = []
values = []
count = 0
for k,v in items:
    if count <=9:
        keys += [k]
        values += [int(v)]
    count += 1
n = len(keys)
ind = np.arange(n)
fig = plt.bar(ind, values)
plt.ylabel('Number of Tweets')
plt.xticks(ind, keys)
#title = 'Tweets Including'
#if "coronavirus" in args.key:
    #title += f' {args.key} by'
#else:
    #title += " the Korean Coronavirus Hashtag by"
if "country" in args.input_path:
    #title += ' Country'
    axis = 'Country Code'
else:
    #title += 'language'
    axis = 'Language Code'
#plt.title(title)
plt.xlabel(axis)
# fig, ax = plt.subplots(nrows=1, ncols=1)
# ax.plot(keys[0:11], values[0:11])
plt.savefig(f"./{args.input_path}_{args.key}_figure.png")
#plt.close(fig)
# print(k,':',v)
