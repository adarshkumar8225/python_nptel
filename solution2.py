#remove duplicate element from list.
def remdup(l):
  res=[]
  for i in l:
    if i not in res:
      res.append(i)
      
  return(res)

#sum of square of even and odd number.

def sumsquare(l):
  even=0
  odd=0
  s=[]
  for i in range(0,len(l)):
    if(l[i]%2==0):
      even=even+(l[i]**2)
    else:
      odd=odd+(l[i]**2)
  s.append(odd)
  s.append(even)
  return(s)

#transpose of matrix


def transpose(m):
  k=[]
  
  x=[]
  for j in range(0,len(m[0])):
    for i in range(0,len(m)):
      k.append(m[i][j])
    x.append(k)
    k=[]
  return(x)
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "remdup":
  arg = parse(farg)
  print(remdup(arg))

if fname == "sumsquare":
  arg = parse(farg)
  print(sumsquare(arg))

if fname == "transpose":
  arg = parse(farg)
  savearg = arg
  ans = transpose(arg)
  if savearg == arg:
    print(ans)
  else:
    print("Side effect")
