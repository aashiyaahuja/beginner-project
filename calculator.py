#BASIC INTERACTIVE CALCULATOR
history=[]
a= float(input("Enter starting no.:"))
opr=int(input("Choose operation number:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n"))
b=float(input("Enter second no.:"))
result=0
if(opr==1):
    sum=a+b
    print(f"{a}+{b}={sum}")
    history.append(f"{a}+{b}={sum}")
    result+=sum
elif(opr==2):
    diff=a-b
    print(f"{a}-{b}={diff}")
    history.append(f"{a}-{b}={diff}")
    result+=diff
elif(opr==3):
    mul=a*b
    print(f"{a}*{b}={mul}")
    history.append(f"{a}*{b}={mul}")
    result+=mul
elif(opr==4):
    if(b==0):
       print("Cannot divide by zero")
    else:
      div=a/b
      print(f"{a}/{b}={div}")
      history.append(f"{a}/{b}={div}")
      result+=div
elif(opr==5):
    power=a**b
    print(f"{a}**{b}={power}")
    history.append(f"{a}**{b}={power}") 
    result+=power
else:
  print("not valid")

while True:
  opr=int(input("Choose operation number:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. History\n7. Exit\n"))
  if(opr==1):
    x=float(input("next number:"))
    sum=result+x
    print(f"{result}+{x}={sum}")
    history.append(f"{result}+{x}={sum}")
    result=sum
  elif(opr==2):
    x=float(input("next number:"))
    diff=result-x
    print(f"{result}-{x}={diff}")
    history.append(f"{result}-{x}={diff}")
    result=diff
  elif(opr==3):
    x=float(input("next number:"))
    mul=result*x
    print(f"{result}*{x}={mul}")
    history.append(f"{result}*{x}={mul}")
    result=mul
  elif(opr==4):
    x=float(input("next number:"))
    if(x==0):
       print("cannot divide by zero")
    else:
      div=result/x
      print(f"{result}/{x}={div}")
      history.append(f"{result}/{x}={div}")
      result=div
  elif(opr==5):
    x=float(input("next number:"))
    power=result**x
    print(f"{result}**{x}={power}")
    history.append(f"{result}**{x}={power}") 
    result=power
  elif(opr==6):
     print(history)
  elif(opr==7):
     print(result)
     break
  else:
    print("not valid")