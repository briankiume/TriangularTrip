def tri_triplets(a):
    triplets = []
    for x in range(len(a)):
        for y in range(x + 1, len(a)):
            for z in range(y + 1, len(a)):
                if (a[x] + a[y] > a[z]) & (a[y] + a[z] > a[x]) & (a[z] + a[x] > a[y]):
                    triplets.append((x, y, z))

    if len(triplets) < 1:
        num = 0
    else:
        num = 1

    return num


print(tri_triplets([10, 2, 5, 1, 8, 20]))
print(tri_triplets([10, 2, 5, 1]))
