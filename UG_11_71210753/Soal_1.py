def add(x,y):
    hasil=x+y
    return hasil
def subtract(x,y):
    hasil=x-y
    return hasil
def multiply(x,y):
    hasil=x*y
    return hasil
def divide(x,y):
    hasil=x/y
    return hasil

inputan=(int(input('select operation :\n1.add\n2.subtract\n3.multiply\n4.divide\n==> ')))
inputan1=(float(input('first number: ')))
inputan2=(float(input('second number: ')))

if inputan == 1:
    print(inputan1,'+',inputan2)
    print(add(inputan1,inputan2))   

elif inputan == 2:
    print(inputan1,'-',inputan2)
    print(subtract(inputan1,inputan2))

elif inputan == 3:
    print(inputan1,'x',inputan2)
    print(multiply(inputan1,inputan2))

elif inputan == 4:
    print(inputan1,':',inputan2)
    print(divide(inputan1,inputan2))

else:
    print('masukin inputnya yang bener bosque, pake angka aja !!')
