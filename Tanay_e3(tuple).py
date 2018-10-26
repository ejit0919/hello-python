user_input = input("Enter a comma separated list of numbers: ")

index = 0
sum = 0

for x in user_input:
    sum += float(user_input[index])**2
    index += 1

print("Sum of squares:", sum)