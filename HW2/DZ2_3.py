k = int(input("Введите число: ")) 

def squerence(k):
    return [round((1 + 1 / k)**k, 5) for k in range (1, k + 1)]

print(squerence(k))
print(round(sum(squerence(k)), 5))