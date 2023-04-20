def cont_diam(sand):
    cont_menor = 0
    cont_maior = 0
    for i in sand:
      if i == "<":
        cont_menor += 1
      elif i == ">" and cont_menor > cont_maior:
        if cont_menor > 0:
          cont_maior += 1

    if cont_menor > cont_maior:
      awn = cont_maior
    else: 
      awn = cont_menor
    return awn

for i in range (int(input())):
  print(cont_diam(list(input())))