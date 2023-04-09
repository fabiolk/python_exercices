# Every end of year there is a party in Fantastic Education Institution (FEI). Early in July, the registration is open to take part in it. At registration, the user can choose whether to be "O Amigo do Habay" (The Friend of Habay) in the party or not. The most logical choice would be Yes, because it is a privilege to be The Friend of Habay, since he is the coolest person in FEI. However, there are some people who definitely don't want to be The Friend of Habay, and for unknown reasons.

# Only one will be chosen. As a result, many students who chose the option Yes registered several times to increase their chance of being The Friend of Habay. The party organizer hired you to organize the website's registration, since there is a registration spam going on. The criteria to be the chosen one is the number of letters of the first name, and if there is more than one name with the same number of letters, wins the one who first registered. The final organization of the registered users should follow the order of choice (Yes or No), while respecting the alphabetical order.

# Note: No one who chose the option No registered more than once.

# Input
# The input consists of a single test case. Each line consists of the user's first name (no spaces), followed by the option YES (if the user wants to be O Amigo do Habay, i.e., The Friend of Habay) or NO (if the user doesn't). Read input until the user enters "FIM" (without quotes).

# Output
# Print the registered users in order of choice, respecting the alphabetical order, then print the winner's name. Print a blank line between the list of registered users and the winner's name.

# name = ['Joao', 'Carlos', 'Abner', 'Samuel', 'Ricardo', 'Abhay', 'Samuel', 'Andres', 'Roberto', 'Carlos', 'Samuel', 'Samuel', 'Abhay', 'Aline', 'Andres']
# opt = ['NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'YES', 'YES', 'NO', 'YES', 'YES', 'YES', 'YES', 'YES', 'YES']

name = list()
opt = list()
len_ = list()
name_s = list()
name_n = list()

i = -1

while(i != 0):
  aux = input()

  if str(aux) == 'FIM':
    break
  else:
    aux = aux.split(' ')
    name.append(aux[0])
    opt.append(aux[1])

for i in range(len(name)):

  if opt[i] == 'YES':

    name_s.append(name[i])
    len_.append(len(name[i]))

  else:
    name_n.append(name[i])

res = [i for n, i in enumerate(name_s) if i not in name_s[:n]]

res_sorted = sorted(res, reverse = False)

for i in range(len(res_sorted)):
  print(res_sorted[i])
  
name_n_sorted = sorted(name_n, reverse = False)

for i in range(len(name_n_sorted)):
  print(name_n_sorted[i])

print()

print('Amigo do Habay:')

for i in range(len(name_s)):
  if len_[i] == max(len_):
    print(name_s[i])
    break