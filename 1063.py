def trem(entrada, saida):
  estacao = list()
  mov = list()
  for vagao in entrada:
    estacao.append(vagao)
    mov.append('I')
    while len(estacao) > 0 and estacao[-1] == saida[0]:
      estacao.pop()
      saida.pop(0)
      mov.append('R')
  if len(estacao) != 0:
    mov.append(' Impossible')
  return "".join(mov)

while True:
  num_vagaos = int(input())
  if num_vagaos == 0:
    break
  entrada = input().split()
  saida = input().split()
  print(trem(entrada, saida))