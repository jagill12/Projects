def main():
    while True:
        sequence_type = input("Do you want to design a forward primer or a reverse primer? Type 1 for forward, 2 for reverse, or 3 for both: ")
        while sequence_type not in ["1", "2", "3"]:
            sequence_type = input("Sorry, that was not 1 or 2. Type 1 for a forward primer, type 2 for a reverse primer, or type 3 for both: ")
        gene_sequence = input("Great! Now give me a gene sequence: ")
        complement_strand = ""
        valid = True
        
        for i in gene_sequence:
            if i not in ["a", "g", "c", "t"]:
                print("You gave an invalid input! Make sure to give me a sequence that only contains letters of nucleotide base pairs (a, c, g, or t).")
                valid = False
                break

            if i == "a":
                complement_strand += "t"
            elif i == "g":
                complement_strand += "c"
            elif i == "c":
                complement_strand += "g"
            elif i == "t":
                complement_strand += "a"

        if valid:
            if sequence_type == "1":
                print("The complement strand of your forward primer is", complement_strand)
            elif sequence_type == "2":
                reverse_primer = ""
                for i in range(len(complement_strand) - 1, -1, -1):
                    reverse_primer += complement_strand[i]
                print("The complement strand of your reverse primer is", reverse_primer)
            elif sequence_type == "3":
                print("The complement strand of your forward primer is", complement_strand)
                reverse_primer = ""
                for i in range(len(complement_strand) - 1, -1, -1):
                    reverse_primer += complement_strand[i]
                print("And the complement strand of your reverse primer is", reverse_primer)
            break

main()
