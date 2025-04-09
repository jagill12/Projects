def main():
    my_list = [[1, 2, 3, 4, 5]]
    i = 0
    while i < 4:
        list_copy = my_list[-1].copy()
        a = 0
        while a < len(list_copy):
            list_copy[a] *= 2
            a += 1
        my_list.append(list_copy)
        i += 1
    print(my_list)
main()
