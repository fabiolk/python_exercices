p = {
      "W" : 1, 
      "H" : 1/2, 
      "Q" : 1/4, 
      "E" : 1/8, 
      "S" : 1/16, 
      "T" : 1/32, 
      "X" : 1/64
    }

while True:
  r = input()
  if r == '*':
    break
  r =  r.split('/')
  sum_ = 0
  for c in r:
    tmp = 0
    for i in c:
      tmp += p[i]
      if tmp > 1:
        break
    if tmp == 1:
      sum_ += 1

  print(sum_)