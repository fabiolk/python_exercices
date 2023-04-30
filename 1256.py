var = 0
n = int(input())
while n:
    n -= 1
    m_c = input().split()
    m = int(m_c[0])
    c = int(m_c[1])
    val_hash = {str(t) : [] for t in range(m)}
    tmp = input().split()
    if var:
      print()
    for x in tmp:
      num = int(x) % m
      val_hash[str(num)].append(int(x))
    for x in val_hash:
      print('%d -> ' % int(x), end = '')
      for y in val_hash[x]:
          print('%d -> ' % y, end = '')
      print('\\')
    var = 1