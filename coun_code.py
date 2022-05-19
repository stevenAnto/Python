#
#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
def count_code(str):
  contador = 0
  for i in range(len(str)-1) :
    x = str[i:i+4]
    x1 = x [0:2]
    x2 = x [3:]
    if x1 == "co" and x2 == "e" :  contador +=1
  return contador
