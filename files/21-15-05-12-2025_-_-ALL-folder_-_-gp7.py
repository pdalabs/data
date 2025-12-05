import csv

with open("a.csv") as f:
    csv_file = csv.reader(f)
    data = list(csv_file)

# Initial S: first positive example
s = data[1][:-1]
print("Initial S:", s)

# Initial G: matrix of '?'
g = [['?' for i in range(len(s))] for j in range(len(s))]
print("Initial G:", g)

step = 1

for row in data[1:]:
    attributes = row[:-1]
    result = row[-1]

    print(f"\nStep {step}: Training Example = {row}")

    if result == "yes":
        # Generalize S
        for j in range(len(s)):
            if attributes[j] != s[j]:
                s[j] = '?'
                g[j][j] = '?'  # Maintain consistency

    elif result == "no":
        # Specialize G
        for j in range(len(s)):
            if attributes[j] != s[j]:
                g[j][j] = s[j]
            else:
                g[j][j] = '?'

    print("S:", s)
    print("G:", g)

    step += 1


# Extract valid general hypotheses
gh = []
for row in g:
    if any(val != '?' for val in row):
        gh.append(row)

print("\nFinal Specific Hypothesis:\n", s)
print("\nFinal General Hypothesis:\n", gh)
