# fruits = {}
#
# fruits["apple"] = "A sweet red fruit"
#
# fruits["mango"] = "King of all"
#
# print(fruits["apple"])

line = input()

letter = {}

for ch in line:
    if ch in letter:
        letter[ch] += 1
    else:
        letter[ch] = 1

print(letter)

print(letter.keys())
