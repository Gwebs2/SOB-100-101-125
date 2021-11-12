pattern = '********************'

for i in range(len(pattern)):
    for j in range(len(pattern)):
        if i == j:
            print(pattern[i], end="")
        else:
            print(' ', end="")
    print()


