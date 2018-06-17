# Historical Analysis of Species References in American English 

Data and analysis for a study that uses the two largest available American English language corpora, Google Books and COHA, to investigate relations between ecology and language. 

There are two parts: an examination of frequency of common names of species followed by aspect-level sentiment analysis of concordance lines.

## Files

#### google_books_data:
* **getngrams.py** - python script to retrieve data behind the trajectories plotted on the Google Ngram Viewer. (For usage see [google-ngrams](https://github.com/econpy/google-ngrams) 
* **species_ngram_NA_normalized.csv** & **species_ngram_BR_normalized.csv** - data collected by running getngrams.py on each species name. Normalized with respect to the average. (NA: American, BR: British)  
* **NA_google_data_normalized.csv** & **BR_google_data_normalized.csv** - summary of species_ngram_NA_normalized. (Used for plotting) 
* **rural_pop_US.csv** & **rural_pop_BR.csv** - percent of populaton rural
* **COHA_normalized.csv** - frequency data from the Corpus of Historical American English
* **figure1.py** - plotting/statistical analysis for North American frequency and population data (1800-2000)
* **figure2.py** - plotting/statistical analysis for North American frequency and population data (1900-2000)
* **figure3.py** plotting/statistical analysis for British frequency and population data (1800-2000) 
* **figure4.py** plotting/statistical analysis for British frequency and population data (1850-1920)

#### coha_data:
* **speciesname.csv (*caribou.csv*, *elm.csv*, etc.) - key word in context (kwic) lines from the [Corpus of Historical American English](https://corpus.byu.edu/coha/)
* **COHA_normalized.csv** - frequency data from the Corpus of Historical American English
* **coha_content.csv** - data for the composition of the COHA corpus
* **sentiment.py** - sentiment analysis script: uses Natural Language Toolkit (NLTK) and [SentiWordNet](http://www.nltk.org/_modules/nltk/corpus/reader/sentiwordnet.html) for aspect-level sentiment of adjective/target-noun pairs  
* **annotated.csv** - output of *sentiment.py*, manually annotated
* **final.csv** - retained kwic lines from *annotated.csv*
* **figure5.py** - plotting/statistical analysis of sentiment analysis results  


### Prerequisites

#### Python Packages and Modules
*pandas*
*numpy*
*scipy*
*matplotlib*
*nltk*

## Authors

* **Craig Frayne** (https://github.com/craigmateo)

## Acknowledgments

* [google-ngrams](https://github.com/econpy/google-ngrams) 
* [Corpus of Historical American English](https://corpus.byu.edu/coha/)
* [NLTK SentiWordNet](http://www.nltk.org/_modules/nltk/corpus/reader/sentiwordnet.html)