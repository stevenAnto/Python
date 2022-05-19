def has22(nums):
  contador = 0
  for x in nums :
    if x == 2 : 
      contador+=x
      print (contador)
      if contador == 4 : return False
    else : contador = 0
  return True

print (has22([1, 2, 2]))

