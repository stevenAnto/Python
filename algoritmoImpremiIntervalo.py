
def sum67(nums):
  suma=0
  i=0;
  while i<len(nums) :
    if nums[i]==6:
      i+=1
      print ("entro")
      print ("i "+str(i))
      while nums[i]!= 7 and i != len(nums)-1:
        print("ciclos"+str(i))
        i+=1
      i+=1
    else : 
      suma+= nums[i]
      i+=1
      print ("suma2  "+str(suma))
  return suma

print(sum67([1, 2, 2,6,99,99,7]))
