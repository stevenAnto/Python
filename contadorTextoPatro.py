def count_hi(str):
  contador = 0 
  for i in range(len(str)-1):
    x = str [i:i+2]
    if x=="hi" :  contador +=1
  return contador
