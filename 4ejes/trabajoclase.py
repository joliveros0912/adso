import random
vec=[]
suma=0
acml=0
for i in range(random.randint(10,25)):
    vec.insert(i,round(random.random()*100))
    suma+=vec[i]
    acml+=1
print(vec)
print(suma)
print(acml)
