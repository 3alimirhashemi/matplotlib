from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

plt.style.use('dark_background')
data = pd.read_csv('data.csv')
Responder_id = data['Responder_id']
LanguagesWorkedWith = data['LanguagesWorkedWith']
Languages_Counter = Counter()
for res in LanguagesWorkedWith:
    Languages_Counter.update(res.split(';'))

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
plt.ylabel('Pandas Programing')
plt.tight_layout()
plt.show()
