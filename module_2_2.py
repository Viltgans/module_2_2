first = int(input())
second = int(input())
third = int(input())
couple_1 = first == second
couple_2 = second == third
couple_3 = first == third
if first == second == third:
    print('3')
elif couple_1 or couple_2 or couple_3:
    print('2')
else:
    print('0')
