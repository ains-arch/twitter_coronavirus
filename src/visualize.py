#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True)
parser.add_argument('--key', required=True)
parser.add_argument('--percent', action='store_true')
args = parser.parse_args()

# imports
import json
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

# visualize the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1], item[0]), reverse=True)
keys = []
values = []
count = 0
for k, v in items:
    if count <= 9:
        keys += [k]
        values += [int(v)]
    count += 1
n = len(keys)
ind = np.arange(n)
fig = plt.bar(ind, values)
plt.ylabel('Number of Tweets')
plt.xticks(ind, keys)
title = 'Tweets With'
if "#코로나바이러스" in args.key:
    title += " the Korean Coronavirus Hashtag by"
elif "#コロナウイルス" in args.key:
    title += " the Japanese Coronavirus Hashtag by"
elif "#冠状病毒" in args.key:
    title += " the Chinese Coronavirus Hashtag by"
else:
    title += f" '{args.key}' by"
if "country" in args.input_path:
    title += ' Country'
    axis = 'Country Code'
else:
    title += ' Language'
    axis = 'Language Code'
plt.title(title)
plt.xlabel(axis)
plt.tight_layout()
plt.savefig(f"./{args.input_path}_{args.key}_figure.png")
