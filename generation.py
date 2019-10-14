import random, re, json

def filter_out(e, dic_prov):
  for cle, val in dic_prov.items():#Filters out symbols used (to improve)
    symbols = val.split("|")
    elems = [x for x in val.split("|") if x!=e]
    if symbols!=elems:
      dic_prov[cle] = dic[cle] if len(elems)==0 else "|".join(elems)
  return dic_prov

def generate(elems, dic):
  l = []
  for e in re.split(" ", elems):
    if e in dic:#on a un symbole non-terminal
      choix = re.split("\|", dic[e])#cf JSON
      l += generate(choix[random.randrange(0, len(choix))], dic)
    else:#on a un symbole terminal
      l.append(e)
      dic = filter_out(e, dic)
  return l

dic = json.load(open("JCVD.json"))#les règles de génération
#dic = json.load(open("LaFontaine.json"))#d'autres règles de génération

Struct = re.split("\|", dic["P"])#On fait une liste des phrases possibles
nbPhrases = 10

for i in range(0, nbPhrases):
  chunks = StructPhrases[random.randrange(len(Struct))]#random structure
  print(" ".join(generate(chunks, dic)))
