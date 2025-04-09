from collections import Counter, defaultdict

def suffix_array(string: str) -> list[int]:
    """Compute the suffix array of a string."""
    return sorted(range(len(string)), key=lambda i: string[i:])

def BWT_from_suffix_array(text: str, suffix_positions: list[int]) -> str:
    """Compute the Burrows-Wheeler Transform from a suffix array."""
    return "".join(text[i - 1] if i > 0 else "$" for i in suffix_positions)

def cal_count(string: str) -> dict[str, int]:
    """Compute the count of lexicographically smaller characters."""
    sorted_chars = sorted(set(string))
    count = {}
    cumulative_count = 0
    char_counts = Counter(string)

    for char in sorted_chars:
        count[char] = cumulative_count
        cumulative_count += char_counts[char]

    return count

def cal_occur(bwt_string: str) -> dict[str, list[int]]:
    """Compute occurrences of each character up to each position."""
    occur = {char: [0] * len(bwt_string) for char in sorted(set(bwt_string))}

    for i, char in enumerate(bwt_string):
        if i > 0:
            for key in occur:
                occur[key][i] = occur[key][i - 1]  
        occur[char][i] += 1
    
    return occur

def update_range(
    lower: int, 
    upper: int, 
    count: dict[str, int], 
    occur: dict[str, list[int]], 
    a: str
) -> tuple[int, int]:
    """Update the range given character a."""
    if a not in count:
        return -1, -1
    if upper >= len(occur[a]):
        upper = len(occur[a]) -1

    new_lower = count[a] + (occur[a][lower - 1] if lower > 0 else 0)
    new_upper = count[a] + occur[a][upper]

    return (new_lower, new_upper) if new_lower <= new_upper else (-1, -1)

def find_match(query: str, reference: str) -> list[int]:
    """Find exact matches using Burrows-Wheeler Transform."""
    suffix_positions = suffix_array(reference)
    bwt_string = BWT_from_suffix_array(reference, suffix_positions)
    print(bwt_string)
    count = cal_count(bwt_string)
    occur = cal_occur(bwt_string)
    print(occur)
    
    lower, upper = 0, len(reference) - 1 

    print(f"Searching for '{query}' in '{reference}'")
    
    for char in reversed(query):
        lower, upper = update_range(lower, upper, count, occur, char)
        print(f"After processing '{char}': lower={lower}, upper={upper}")
        if lower == -1 or upper == -1:
            return []

    raw_matches = suffix_positions[lower:upper + 1]
    print(f"Raw match positions {raw_matches}")


    matches = sorted(pos for pos in raw_matches if pos > 0 and pos < len(reference) - 1)

    print(f"Final match positions: {matches}")
    print("Burrows-Wheeler Transform:", bwt_string)
    print("Suffix Array:", suffix_positions)
    print("Match positions:", matches if matches else "None.")
    return matches

def main():
    reference = input("Enter the reference string: ") + "$"
    query = input("Enter the query string: ")
    find_match(query, reference)
if __name__ == "__main__":
    main()
