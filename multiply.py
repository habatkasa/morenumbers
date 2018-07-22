def pult(a,b):
    if b==1:

        return a
    else:

        return a+pult(a,b-1)

print(pult(52,7))