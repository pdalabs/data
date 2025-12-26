import csv

num_attribute = 6
a = []

with open('enjoysport.csv', 'r') as file:
    reader = csv.reader(file)
    a = list(reader)

hypothesis = a[1][:-1]

for i in a[1:]:
    if i[-1].lower() == 'yes':
        for j in range(num_attribute):
            if i[j] != hypothesis[j]:
                hypothesis[j] = '?'

print("Maximally specific hypothesis:")
print(hypothesis)

print("\nThe maximally specific hypothesis for the given training examples:")
print(hypothesis)
