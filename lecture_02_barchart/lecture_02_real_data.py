from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter

plt.style.use('seaborn-v0_8-dark')
with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    row = next(csv_reader)

    Languages_Counter = Counter()
    for row in csv_reader:
        Languages_Counter.update(row['LanguagesWorkedWith'].split(';'))


lang = []
lang_use = []

for i in Languages_Counter.most_common(15):
    lang.append(i[0])
    lang_use.append(i[1])


lang.reverse()
lang_use.reverse()
plt.barh(lang, lang_use)

plt.title('Best Languages Programing')
plt.xlabel('ali mirhashemi')
plt.tight_layout()
plt.show()







