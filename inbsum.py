x = list(map(int, input("Enter multiple values: ").split()))
print("List of number: ", x)
x_rem = [i for i in x if i > 9]
print(x_rem)
print(sum(x_rem))
