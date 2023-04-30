#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', nargs='+', required=True)
parser.add_argument('--keys', nargs='+', required=True)
args = parser.parse_args()

# imports
import json
from collections import Counter, defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

for key in args.keys:
    sorted(args.input_paths)
    yaxis = []
    total = defaultdict(lambda: Counter())
    errors = 0
    for path in args.input_paths:
        with open(path) as f:
            tmp = json.load(f)
            num = 0
            try:
                for k in tmp[key]:
                    num += tmp[key][k]
            except KeyError:  # no tweets with that hashtag that day
                pass
            yaxis.append(num)
    plt.plot(np.arange(366), yaxis, label=key)
plt.ylabel('Number of Tweets')
dates = [0, 58, 119, 180, 242, 303]
months = ['Jan.', "March", "May", "July", "Sept.", "Nov."]
plt.xticks(dates, months)
plt.xlabel('Date')
plt.title("Tweets with Coronavirus Hashtags per Day in 2020")
plt.legend()
plt.tight_layout()
plt.savefig('alternative')
