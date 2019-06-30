odd_numbers = []
for i in range(3, 18): # range doesn't return the last number (because it is an "exclusive" range)
  if i % 2 == 1:
    odd_numbers.append(i)
print("Odd Numbers:", odd_numbers)

for x in range(len(odd_numbers)):
  odd_numbers[x] = odd_numbers[x] * 2
print("Times Two:", odd_numbers)
