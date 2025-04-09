import numpy as np
import random
from collections import defaultdict

def load_sonnets(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().split()

def build_markov_model(words, order=7):

    markov_model = defaultdict(lambda: defaultdict(int))

    for i in range(len(words) - order):
        prefix = tuple(words[i:i+order])  # Current state.
        next_word = words[i+order]  # Next word in sequence.
        markov_model[prefix][next_word] += 1  # Increment count.

    return markov_model

def get_next_word(current_state, markov_model):

    if current_state not in markov_model:
        return random.choice(list(markov_model.keys()))[0]

    next_words = markov_model[current_state]
    total = sum(next_words.values())
    probabilities = {word: count / total for word, count in next_words.items()}
    return np.random.choice(list(probabilities.keys()), p=list(probabilities.values()))

def generate_sonnet_text(markov_model, order=7, total_words=14990):
    "Generate structured Shakespearean-style sonnets with 14-line formatting."
    current_state = random.choice(list(markov_model.keys()))
    generated_words = list(current_state)
    word_count = order
    sonnets = []
    current_sonnet = []
    line = []

    while word_count < total_words:
        next_word = get_next_word(current_state, markov_model)
        generated_words.append(next_word)
        current_state = tuple(generated_words[-order:])  # Update state.
        word_count += 1

        # Add 10 words to the current line.
        line.append(next_word)
        if len(line) >= 10:
            current_sonnet.append(" ".join(line))
            line = []

        # When a sonnet reaches 14 lines, store it and reset.
        if len(current_sonnet) == 14:
            sonnets.append("\n".join(current_sonnet))
            current_sonnet = []

    if current_sonnet:
        sonnets.append("\n".join(current_sonnet))

    return "\n\n".join(sonnets)

if __name__ == "__main__":

    file_path = "sonnets.txt"

    words = load_sonnets(file_path)

    # Generate and save for Markov orders 7-10.
    for order in range(7, 11):
        markov_model = build_markov_model(words, order)
        generated_text = generate_sonnet_text(markov_model, order, total_words=14990)

        output_path = f"generated_shakespeare_sonnets_order_{order}.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(generated_text)

        print(f"Generated text saved to {output_path}")
