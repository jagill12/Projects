def main():
    first = {1, 2, 3, 4, 5, 5, 6, 7, 8, 9}
    second = {10, 11, 12, 13, 14, 15, 16, 7, 8, 9}
    print("The first set contains the numbers: " + str(first))
    print("The second set contains the numbers: " + str(second))
    intersected = first.intersection(second)
    combined = first.union(second)
    distinctions = first.difference(second)
    print("The common items between the two sets are: " + str(intersected) + ".")
    print("The two sets combined into one contains the set of numbers: " + str(combined))
    print("The numbers found only in the first set are: " + str(distinctions))
    print("\n")
    print("Now it's time to run the add, update, discard, and " + "\n"
          "clear functions on the first set." + "\n")
    first.add(12)
    print(first)
    first.update({13, 14})
    print(first)
    first.discard(1)
    print(first)
    first.clear()
    print(first)
main()
