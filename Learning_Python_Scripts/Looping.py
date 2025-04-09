def main():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = []
    a = 0
    while a < len(list1):
        if list1[a] % 2 == 0:
            list2.append(list1[a])
            list1[a] = list1[a] * 2
            a += 1
        else:
            a += 1
    list1.append(list2)
    print(list1)
    print(list2)
main()
