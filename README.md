# Coronavirus on Twitter in 2020

In this project, I scanned all geotagged tweets posted in 2020 to analyze the spread of coronavirus information on social media.
This project allowed me to:

1. work with large scale datasets
1. work with multilingual text
1. use the MapReduce divide-and-conquer paradigm to create parallel code

## Background

**About the Data:**

Approximately 500 million tweets are sent everyday.
Of those tweets, about 2% are *geotagged*.
That is, the user's device includes location information about where the tweets were sent from.
I obtained a dataset that contains all geotagged tweets that were sent in 2020.
In total, there are about 1.1 billion tweets in this dataset.

The tweets for each day are stored in a zip file `geoTwitterYY-MM-DD.zip`,
and inside this zip file are 24 text files, one for each hour of the day.
Each text file contains a single tweet per line in JSON format.

**About MapReduce:**

I followed the [MapReduce](https://en.wikipedia.org/wiki/MapReduce) procedure to analyze these tweets.
The partition step was already done in the creation of the dataset as the tweets are already split into one file per day.
I implemented the map and reduce steps.


## Method

### Mapping and visualizing a single day

I was provided a `map.py` file that would process the zip file for an individual day.
I started by using this command to process all of the tweets sent on Febuary 16th.

I was also provided a `visualize.py` file that would print the output from running the `map.py` file.
I then used this command to display the total number of times the hashtag `#coronavirus` was used on 16 February in each of the languages supported by Twitter.

### Reducing and visualizing multiple days

I was provided a `reduce.py` file that would merge the outputs generated by the `map.py` file so that the combined files could be visualized.
I generated a new output file for February 17th and visualized it by merging it into a single file with `reduce.py`.

### Modifying the mapper

I modified the `map.py` file so that it tracks the usage of the hashtags on both a language and country level.
I then created a shell script called `run_maps.sh` that loops over each file in the dataset and runs the `map.py` command on that file.
Because of the size of the dataset, I ran all these `map.py` commands in parallel.

### Reducing the outputs

I used `reduce.py` file to combine all of the language files into a single file, and all of the country files into a different file.

### Visualizing the full dataset

I modified the `visualize.py` file so that, rather than simply printing the results, it generates a bar graph of the results and stores the bar graph as a png file using the matplotlib library.
I used this command to create the following bar graphs of the top 10 languages and countries by volume of tweets with the given hashtag:

<img src=reduced.lang_#coronavirus_figure.png width=100% />

<img src=reduced.country_#coronavirus_figure.png width=100% />

<img src=reduced.lang_#코로나바이러스_figure.png width=100% />

<img src=reduced.country_#코로나바이러스_figure.png width=100% />

By "Korean Coronavirus Hashtag", I am referring specifically to `#코로나바이러스`.
`und`, or "undefined" tweets are tweets that don't have language metadata.

I created a new visualization command from scratch, called `alternative_reduce.py`, that takes as input on the command line a list of hashtags,
and outputs a line plot.
I used this command to created the following plot:

<img src=alternative.png width=100% />
