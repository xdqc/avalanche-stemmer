import math
import json
from avalanche import i_stem

stems = set()
word_stems = {}
# ss = SnowballStemmer('english')

stopwords_stem = set()
with open('./stopwords_stem.txt', 'r') as f:
  [stopwords_stem.add(w.strip()) for w in f]

trans = json.load(
    open('./word_list_tran.json', 'r', encoding='utf8'))

word_order = {}
stem_order = {}

with open('./corpus.txt') as f:
  for (i, w) in enumerate(f, start=1):
    w = w.strip()
    if w == 'wasnt':
      break

    word_order[w] = 1 / math.log1p(i)

    if w in stopwords_stem:
      continue

    s = i_stem(w, True)
    if w in trans:
      if 'zh' in trans[w]:
        tr = {w: trans[w]['zh']}
        if s in word_stems:
          word_stems[s].append(tr)
        else:
          word_stems[s] = [tr]

###########################################

# Order stems ranking

for s in word_stems:
  score = 0
  for i, w in enumerate(word_stems[s]):
    score += word_order[[*w][0]] / (2**i)
  stem_order[s] = score

sorted_stem = sorted(stem_order, key=stem_order.get, reverse=True)


###########################################

# Print the result

index = 0
stems_result = {'': [{'': ''}]}
for i, s in enumerate(sorted_stem, start=1):
  if 0 < len(word_stems[s]) :
    stems_result[s] = word_stems[s]
    index += 1
    print(index, s)
    for w in word_stems[s]:
      print(f'\t{[*w][0]}\t{w[[*w][0]]}')

###########################################

# Output Translate JSON asset

with open('./word_stems_zh.json', 'w', encoding='utf8') as f:
  json.dump(stems_result, f)
