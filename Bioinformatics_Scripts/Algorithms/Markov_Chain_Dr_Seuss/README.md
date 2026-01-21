#Markov Chain Text Generation (Dr. Seuss)

This project uses a Markov chain to generate new text in the style of Dr. Seuss’s One Fish Two Fish Red Fish Blue Fish. By learning which words tend to follow others, the model produces playful, loosely structured text that reflects the rhythm and vocabulary of the original book.

##Overview

A Markov chain treats text as a sequence of word transitions. The next word is chosen based only on a fixed number of previous words, not on grammar or meaning. Even with this simple assumption, the model can capture recognizable patterns and stylistic quirks from the source text.

This implementation builds word-based Markov models of increasing order (from 1 to 4) to show how added context improves coherence.

The workflow is straightforward:

###Load and Prepare Text

The input text is read from a file and split into an ordered list of words. This sequence is the training data for the model.

###Build the Markov Model

For a chosen order n, each group of n consecutive words becomes a state. The model counts which words follow each state and how often, forming transition probabilities.

###Generate New Text

Starting from a random state, the model repeatedly samples the next word based on learned probabilities and shifts the state window forward. This continues until the desired text length is reached.

###Format and Save Output

Generated text is formatted with line breaks every fixed number of words for readability and saved to disk. The script automatically produces outputs for orders 1 through 4, making it easy to compare how context length affects the results.

###Notes

Lower-order models tend to produce chaotic, surreal text, while higher-order models preserve longer phrases and feel more “Seussian.” The project highlights how simple probabilistic models can recreate stylistic patterns without any explicit understanding of language.
