import csv

with open("trainingdata.csv") as f:
    data = []
    for row in f:
        row = row.strip().replace(',', ' ').split()
        data.append(row)

s = data[1][:-1]
g = [['?' for _ in range(len(s))] for _ in range(len(s))]

print(s)
print(g)

for i in range(1, len(data)):
    if data[i][-1].lower() == "yes":
        for j in range(len(s)):
            if data[i][j] != s[j]:
                s[j] = '?'
                g[j][j] = '?'

    elif data[i][-1].lower() == "no":
        for j in range(len(s)):
            if data[i][j] != s[j]:
                g[j][j] = s[j]
            else:
                g[j][j] = '?'

    print("\nstep", i, "of candidate elimination algorithm")
    print(s)
    print(g)

gh = []
for hypothesis in g:
    if any(value != '?' for value in hypothesis):
        gh.append(hypothesis)

print("\nFinal Specific Hypothesis:\n", s)
print("\nFinal General Hypothesis:\n", gh)
