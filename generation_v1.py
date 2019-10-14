import random, re, json

def generate(elems):
  l = []
  for e in re.split(" ", elems):#on découpe en symboles
    if e in dic:#on a un symbole non-terminal
      choix = re.split("\|", dic[e])#cf JSON grammar symbols separated by "|"
      j = random.randrange(len(choix))
      l += generate(choix[j])# on appelle récursivement la fonction
    else:#on a un symbole terminal
      l.append(e)
  return l

global dic
dic = json.load(open("JCVD.json"))#les règles de génération

StructPhrases = re.split("\|", dic["P"])#On fait une liste des phrases possibles
nbPhrases = 10

for i in range(nbPhrases):
  j = random.randrange(0, len(StructPhrases))
  chunks = StructPhrases[j]#on chosiit une structure de phrase au hasard
  res = generate(chunks)
  print(" ".join(res))
