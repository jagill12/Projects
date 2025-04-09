import numpy as np
import random
from collections import defaultdict

def load_text(file_path):
    "Load text from a file and return as a list of words."
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text.split()

def build_markov_model(words, order=1):
    "Build a Markov model of given order from a list of words."
    markov_model = defaultdict(lambda: defaultdict(int))

    for i in range(len(words) - order):
        prefix = tuple(words[i:i+order]) 
        next_word = words[i+order]  
        markov_model[prefix][next_word] += 1 

    return markov_model

def get_next_word(current_state, markov_model):
    "Get next word based on transition probabilities."
    if current_state not in markov_model:
        return random.choice(list(markov_model.keys()))[0]

    next_words = markov_model[current_state]
    total = sum(next_words.values())
    probabilities = {word: count / total for word, count in next_words.items()}
    return np.random.choice(list(probabilities.keys()), p=list(probabilities.values()))

def format_text_with_newlines(text, words_per_line=15):
    "Format text by inserting a new line every `words_per_line` words."
    words = text.split()
    formatted_lines = [" ".join(words[i:i+words_per_line]) for i in range(0, len(words), words_per_line)]
    return "\n".join(formatted_lines)

def generate_random_text(markov_model, order=1, length=1200):
    "Generate random text using the Markov model."
    current_state = random.choice(list(markov_model.keys()))
    generated_words = list(current_state)

    for _ in range(length - order):
        next_word = get_next_word(current_state, markov_model)
        generated_words.append(next_word)
        current_state = tuple(generated_words[-order:]) 
    
    return format_text_with_newlines(" ".join(generated_words), words_per_line=15)

if __name__ == "__main__":
    file_path = "one_fish_two_fish.txt"
    words = load_text(file_path)

    for order in range(1, 5):
        markov_model = build_markov_model(words, order)
        generated_text = generate_random_text(markov_model, order, length=1200)
        
        output_path = f"generated_Seuss_text_order_{order}.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(generated_text)

        print(f"\nGenerated text saved to {output_path}")
