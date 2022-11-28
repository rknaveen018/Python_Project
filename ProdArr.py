l = [1, 2, 3, 4, -1, 23]

l_product = []

for i in range(len(l)):
    val = 1
    for j in range(len(l)):
        if j != i:
            val *= l[j]
        else:
            pass
    l_product.append(val)

print("Product Array: ",l_product)
