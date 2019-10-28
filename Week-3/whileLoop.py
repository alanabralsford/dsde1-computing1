up = 0
while up <= 10:
    print(up)
    up = up + 1
down = 10
while down >= 0:
    print(down)
    down = down - 1

for num in range(100):
    if num % 3 == 0:
        if num % 5 == 0:
            print('fizz-buzz')
        else:
            print('fizz')
    else:
        if num % 5 == 0:
            print('buzz')
        else:
            print(num)
        