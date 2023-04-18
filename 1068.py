def validate(text):
  
  S = []
  c1 = "("
  c2 = ")"
  
  for caract in text:
    if caract == ' ':
      continue
    if caract in c1:
      S.append(caract)
    elif caract in c2:
      if len(S) == 0: 
        return False
      if c2.index(caract) != c1.index(S.pop()): 
        return False
  return len(S) == 0 

while True:
  try:
    for t in test:
      if (validate(input())):
        print("correct")
      else:
        print("incorrect")
  except EOFError:
    break