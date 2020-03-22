n = int(input())
max = n
count1 = 1
count2 = 1
while n != 0:
    n = int(input())
    if n > max:
        max = n
        if count1 > count2:
            count2 = count1
        count1 = 1
    elif n == max:
        count1 += 1
    elif n < max:
        max = n
        if count1 > count2:
            count2 = count1
        count1 = 1
print(count2)
