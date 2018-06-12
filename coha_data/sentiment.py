import nltk
import collections
import re
import pandas as pd
import numpy as np


master_data = []
all_adjectives = []
master_count = 0

filenames = ["albatross.csv","ambrosia.csv","antelope.csv","badger.csv","basswood.csv","beaver.csv","bee.csv","beetle.csv","bellflower.csv","birch.csv","bison.csv","bittern.csv","black.csv","blackbird.csv","blue.csv","boxwood.csv","brier.csv","buckeye.csv","buckwheat.csv","bulrush.csv","buttercup.csv","butterfly.csv","cactus.csv","cardinal.csv","caribou.csv","catalpa.csv","chestnut.csv","clematis.csv","clover.csv","condor.csv","coot.csv","cottonwood.csv","cougar.csv","crayfish.csv","crocodile.csv","crow.csv","cuckoo.csv","cypress.csv","deer.csv","dogwood.csv","dolphin.csv","duck.csv","elk.csv","elm.csv","fern.csv","ferret.csv","finch.csv","fir.csv","flycatcher.csv","fox.csv","foxglove.csv","frog.csv","geranium.csv","goldfinch.csv","goose.csv","grasshopper.csv","grizzly.csv","grouse.csv","hackberry.csv","hare.csv","harlequin.csv","hawk.csv","hellebore.csv","hemlock.csv","herbaceous.csv","heron.csv","honeysuckle.csv","huckleberry.csv","hummingbird.csv","hyssop.csv","iguana.csv","jackdaw.csv","juniper.csv","kingfisher.csv","lichen.csv","lilac.csv","lizard.csv","lobelia.csv","lynx.csv","magnolia.csv","magpie.csv","mallard.csv","maple.csv","marigold.csv","mink.csv","moose.csv","mountain.csv","mulberry.csv","muskrat.csv","oak.csv","ocelot.csv","opossum.csv","oriole.csv","otter.csv","owl.csv","panther.csv","parrot.csv","pelican.csv","pimpernel.csv","pine.csv","poplar.csv","porcupine.csv","porpoise.csv","quail.csv","raven.csv","salamander.csv","sassafras.csv","skunk.csv","snail.csv","snake.csv","spruce.csv","squirrel.csv","stork.csv","sturgeon.csv","swan.csv","sycamore.csv","tapir.csv","terrapin.csv","thistle.csv","thrush.csv","toad.csv","tortoise.csv","trillium.csv","trout.csv","tulip.csv","vulture.csv","warbler.csv","wasp.csv","whale.csv","wild.csv","willow.csv","wolf.csv","woodchuck.csv","woodpecker.csv"]

positive = []

for name in filenames:
	
	colnames = ['entry','year','genre','source','a','b','c','text']
	keyword = name[0:-4]
	print(keyword)
	data = pd.read_csv(name, names=colnames)

	texts = data.text.tolist()
	years = data.year.tolist()
	
	line_count = len(texts)
	master_count=master_count+line_count
	
	texts = [s for s in texts if isinstance(s, str)]
	texts = [s.replace('\xc2\xa0', ' ') for s in texts]
	texts = [s.lstrip() for s in texts]

	texts.pop(0)
	years.pop(0)

	join = zip(years, texts)

	from nltk.corpus import sentiwordnet as swn # importing sentiwordnet
	from nltk.tag.perceptron import PerceptronTagger # importing a tagger
	from nltk.tokenize import word_tokenize # tokenizing the input
	tagger=PerceptronTagger() # init the tagger in default mode

	for i in join:
		text_orig = i[1]
		year = i[0]
		text = text_orig
		text = nltk.word_tokenize(text)
		if keyword in text:
			ind = text.index(keyword)
			w1=ind-1
			w2=ind+1
			text = " ".join(text[w1:w2])
		
			for word, tag in tagger.tag(word_tokenize(text)): 
				
				if tag=="JJ": # check if the word is an adjective
					# SentiWordNet 
					if len(list(swn.senti_synsets(word, "a"))) > 0:
						synset=list(swn.senti_synsets(word, "a"))[0] # get the most likely synset
						if synset.pos_score() > synset.neg_score():
							positive.append([year,word,keyword,text_orig])

# counting positive by decade

decade_counts = [0]*16
decade_words = [[]]*16

for i in positive:
	year = i[0]
	word = i[1]
	if year.startswith('185'):
		decade_counts[0] += 1
		decade_words[0].append(word)
	if year.startswith('186'):
		decade_counts[1] += 1
		decade_words[1].append(word)
	if year.startswith('187'):
		decade_counts[2] += 1 
		decade_words[2].append(word)
	if year.startswith('188'):
		decade_counts[3] += 1 
		decade_words[3].append(word)
	if year.startswith('189'):
		decade_counts[4] += 1 
		decade_words[4].append(word)
	if year.startswith('190'):
		decade_counts[5] += 1 
		decade_words[5].append(word)
	if year.startswith('191'):
		decade_counts[6] += 1 
		decade_words[6].append(word)
	if year.startswith('192'):
		decade_counts[7] += 1 
		decade_words[7].append(word)
	if year.startswith('193'):
		decade_counts[8] += 1 
		decade_words[8].append(word)
	if year.startswith('194'):
		decade_counts[9] += 1 
		decade_words[9].append(word)
	if year.startswith('195'):
		decade_counts[10] += 1 
		decade_words[10].append(word)
	if year.startswith('196'):
		decade_counts[11] += 1 
		decade_words[11].append(word)
	if year.startswith('197'):
		decade_counts[12] += 1 	
		decade_words[12].append(word)
	if year.startswith('198'):
		decade_counts[13] += 1 
		decade_words[13].append(word)
	if year.startswith('199'):
		decade_counts[14] += 1 
		decade_words[14].append(word)
	if year.startswith('200'):
		decade_counts[15] += 1 
		decade_words[15].append(word)


# normalize with respect to frequency

colnamesSpecies = ["decade","AVG","Tree","Root","Sycamore","Bird","Birch","Butterfly","Buckeye","Brier","Chestnut","Flower","Clover","Plant","Animal","Oak","Dogwood","Frog","Lilac","Maple","River","Mulberry","Poplar","Thistle","Tulip","Willow","Spruce","Soil","Owl","Woodpecker","Heron","Bee","Forest","Trout","Cardinal","Hawk","Blackbird","Duck","Hummingbird","Goose","Grouse","Quail","Warbler","Thrush","Vulture","Cuckoo","Crow","Raven","Swan","Condor","Oriole","Finch","Kingfisher","Blue","Albatross","Pelican","Magpie","Chickadee","Parrot","Meadowlark","Stork","Beaver","Bison","Squirrel","Chipmunk","Fox","Hare","Ferret","Lynx","Caribou","Elk","Skunk","Wolf","Coyote","Deer","Muskrat","Otter","Dolphin","Opossum","Woodchuck","Ambrosia","Boxwood","Clover","Fern","Harlequin","Hellebore","Huckleberry","Juniper","Mesquite","Milkweed","Nightshade","Thistle","Orchid","Willow","Snake","Deciduous","Coniferous","Woodland","Mangrove","Reef","Ocean","Lizard","Iguana","Terrapin","Tortoise","Crocodile","Wasp","Fir","Cypress","Catalpa","Elm","Hemlock","Pine","Salamander","Badger","Beetle","Lichen","Toad","Pickrel","Sturgeon","Snail","Panther","Grasshopper","Crayfish","Cactus","Buckwheat","Geranium","Geranium","Prarie","Grizzly","Black","Mink","Wild","Tapir","Antelope","Mountain","Moose","Elk","Bassilisk","Flycatcher","Phoebe","Vireo","Nuthatch","Wren","Wren","Bluebird","Sparrow","Junco","Tanager","Balsam","Hyssop","Jack-in-the-Pulpit","Pawpaw","Foxglove","Marigold","Bellflower","Sedge","Hackberry","Clematis","Honeysuckle","Goldenrod","Lobelia","Magnolia","Herbaceous","Cottonwood","Buttercup","Elderberry","Elderberry","Bloodroot","Sassafras","Bulrush","Pimpernel","Basswood","Trillium","Cattail","Pecarry","Cougar","Skunk","Porpoise","Whale","Porcupine","Ocelot","Wild Boar","Coot","Goldfinch","Bittern","Jackdaw","Mallard"]
dataSpecies = pd.read_csv('species_COHA_normalized.csv', names=colnamesSpecies)
column = keyword.capitalize()
decadeStats = dataSpecies[column].tolist()
decadeStats.pop(0)			
decadeStats = [x for x in decadeStats if str(x) != 'nan']
decadeStats = [float(x) for x in decadeStats]
decadeStats = [1 if x==0 else x for x in decadeStats]		

normalized = [x/y for x, y in zip(decade_counts, decadeStats)]

# append to the master list 

master_data.append(normalized)
	
avg = [sum(i)/len(i) for i in zip(*master_data)]

decades = [1850,1860,1870,1880,1890,1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000]

# save file with years, adjectives, and kwic lines	

with open("adjectives.txt", "w") as f: 
	for i in positive:
		f.write(i[0] + "\t" + i[1] + "\t" + i[2] + "\t" + i[3] + "\n") 	
	
# # plot
	
# import matplotlib.pyplot as plt

# x = decades
# y = avg

# plt.scatter(x,y)
# plt.ylabel("Frequency of Adjective-Entity Pairs (Normalized)")

# z = np.polyfit(x, y, 1)
# p = np.poly1d(z)
# plt.plot(x,p(x),"r--")

# plt.show()