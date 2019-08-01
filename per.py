def permute(list, s):
    if list == 1:
        return s
    else:
        return [ y + x
                 for y in permute(1, s)
                 for x in permute(list - 1, s)
                 ]

print(permute(1, [4,5,1,5,1,9,4,5]))
print(permute(2, [4,5,1,5,1,9,4,5]))