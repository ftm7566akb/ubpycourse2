import csv
import time
f=[]
t = time.time()
for i in range(0 , 49690):
    f[i] == [0]
with open('C:\\Users\\LavaN-32428068\\Desktop\\._order_products__prior.csv') as order:
    readCSV = csv.reader(order, delimiter=',')
    for row in readCSV:
        f[row(2)] = f[row(2)]+1   #row[2]=products_id
t1 = time.time()

max = max(f)
min = min(f)

with open('C:\\Users\\LavaN-32428068\\Desktop\\products.csv') as pro:
    readCSV1 = csv.reader(pro , delimiter=',')
    for row in readCSV1:
      if row(1) == max:  #row[1]=products_id
          print('max :' , row(2))  #row[2]=products_name
      elif row(1) == min:
          print('min :' , row(2))

print('time :',t1-t)



