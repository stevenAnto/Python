def cat_dog(str):
  contCat=0
  contDog=0
  for i in range(len(str)-1) :
    x = str [i : i+3]
    if x == "cat" : contCat+=1
    if x == "dog" : contDog+=1
  if contCat == contDog : return True
  else : return False

