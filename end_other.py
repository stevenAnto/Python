#Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
#In Python s1.endswith(s2) tests if string s1 ends with string s2 -- makes this much easier!

def end_other(a, b):
  if len(a) > len (b) :
    sub = a[len(a)-len(b):]
    if  sub.lower() == b.lower() : return True
    else : return False
  else :
    sub = b[len(b)-len(a):]
    if  sub.lower() == a.lower() : return True
    else : return False

