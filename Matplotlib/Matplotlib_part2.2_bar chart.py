import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import Counter

plt.style.use('fivethirtyeight')

# #Import data method 1-------------------------------------------------------
# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     language_counter = Counter()
#
#     for row in csv_reader:
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))

# #Import data method 2-------------------------------------------------------

data = pd.read_csv('data_4.csv')
ids = data['Responder_id']
lang_responders = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responders:
    language_counter.update(response.split(';'))
#-------------------------------------------------------------------------------

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

#Label
plt.title("Most popular languages")
plt.xlabel("Number of people who use")

plt.tight_layout()

plt.savefig('bar_part2.2.png')

plt.show()
