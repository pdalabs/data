import csv
num_attribute=6
a=[]
with open('a6.csv','r') as file:
 reader=csv.reader(file)
 a=list(reader)
hypothesis=a[1][:-1]
for i in a:
 if i[-1]=='yes':
  for j in range(num_attribute):
    if i[j]!=hypothesis[j]:
     hypothesis[j]='?'
print(hypothesis)
print("\n the maximally specific hyothesis for a given training examples\n")
print(hypothesis)