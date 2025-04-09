def increasing_sequence(n):
    if n == 1:
        print("n=1, returning [1]")
        return [1]
    else:
        prev_sequence = increasing_sequence(n-1)
        current_num = prev_sequence[-1] + n - 1
        print(f"n={n}, prev_sequence={prev_sequence}, current_num={current_num}")
        while current_num in prev_sequence:
            current_num += 1
            print(f"n={n}, prev_sequence={prev_sequence}, current_num={current_num} (incremented)")
        result = prev_sequence + [current_num]
        print(f"n={n}, result={result}")
        return result
def main():
    print(increasing_sequence(6))
main()
