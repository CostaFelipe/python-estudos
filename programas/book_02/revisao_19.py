magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title(), "\n")

print("Thank you, everyone. That was a great magic show!") 

for value in range(1, 5):
    print(value)

#converter range in lists
numbers = list(range(1,6)) 
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

#numeros perfeitos
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)

print("oi\n")

#numeros perfeitos mais enxuto
for value in range(1, 11):
    squares.append(value ** 2)
    print(squares)