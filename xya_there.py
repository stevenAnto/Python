#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
  for i in range(len(str)-1) :
    x= str[i:i+3]
    if x== "xyz" and str[i-1]!="." : return True
  return False

