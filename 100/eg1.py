

couter = 0

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k:
                print("{}{}{}".format(i,k,k), end=" ")

                couter +=1

print("一共有{}个数".format(couter))


