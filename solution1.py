#function for  question 1.

def threesquares(m):
  if(m<0):
    return(False)
  else :
      for i in range(0,m):
        for j in range(0,m):
          if(m==(4**i *(8*j+7))):
            return(False)
      return(True)


#function for question 2.

def repfree(s):
  for i in range(0,len(s)):
    for j in range(i+1,len(s)):
      if(s[i]==s[j]):
        return(False)
  return(True)
  
  
#function for question 3.


def hillvalley(l):
    is_dec, is_inc = False, False
    inflections = 0
    for i in range(len(l)-1):
        if inflections > 1:
            # Early stop if more than 1 inflection
            return False
        right = l[i+1]
        middle = l[i]
        diff = right - middle
        if diff > 0:
            if is_dec:
                inflections += 1
            is_inc = True
            is_dec = False
        elif diff < 0:
            if is_inc:
                inflections += 1
            is_dec = True
            is_inc = False
    if inflections == 1:
        return True
    return False

assert hillvalley([1, 1, 1, 1, 1]) is False
assert hillvalley([1, 1]) is False
assert hillvalley([1]) is False
assert hillvalley([1, 2, 3, 5, 4]) is True
assert hillvalley([5, 4, 1, 2, 3]) is True
assert hillvalley([1, 2, 3, 5, 5]) is False
assert hillvalley([9, 5, 4, -1, -2, 3, 7]) is True
assert hillvalley([1, 2, 3, 5, 4, 3, 2, 1]) is True
assert hillvalley([9, -1, 4, -1, -2, 3]) is False
import ast

def tolist(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "threesquares":
   arg = parse(farg)
   print(threesquares(arg))
elif fname == "repfree":
   arg = parse(farg)
   print(repfree(arg))
elif fname == "hillvalley":
   arg = parse(farg)
   print(hillvalley(arg))
else:
   print("Function", fname, "unknown")
