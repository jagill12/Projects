# Markov Chain Sonnet Generation (Shakespeare)

This project uses a higher-order Markov chain to generate Shakespearean-style sonnets from a piece of Shakespeare’s original work. It builds on the same core idea as a simpler Markov text generator, but applies it at a larger scale with stronger structural constraints.

## Overview

A Markov chain models text as a sequence of probabilistic word transitions. Given a fixed number of previous words, the model samples the next word based on how often that transition appeared in the training text. This project uses the same underlying approach as a basic Markov chain text generator, but increases the context length and enforces sonnet-like formatting to better match Shakespeare’s style.

Longer word histories are especially important here, since Shakespeare’s language relies heavily on repeated phrases, rhythm, and syntactic structure.

The process works as follows:

### Load and Prepare Text

The full sonnet corpus is read from a file and split into an ordered list of words. This word stream serves as the training data for the model.

### Build the Markov Model

For a chosen order n, each state consists of n consecutive words. The model records how frequently each state is followed by a particular next word, producing transition probabilities used during generation.

Higher-order models preserve longer phrases and result in more coherent output, at the cost of increased repetition.

### Generate Sonnet-Style Text

Generation begins from a random state and proceeds one word at a time using probabilistic sampling. As words are produced, they are grouped into lines of ten words. Every fourteen lines are collected into a sonnet-like block.

This structure is imposed during generation rather than learned from the data, allowing the output to resemble traditional sonnet form without explicitly modeling meter or rhyme.

### Output and Comparison

The script generates text using Markov orders from seven through ten and writes each result to a separate file. Lower orders tend to drift and feel unstable, while higher orders produce more recognizable Shakespearean phrasing.

### Notes

This project demonstrates how increasing context length and adding simple structural rules can significantly change the behavior of a Markov text generator. While the output can sound stylistically convincing, it remains purely statistical and does not encode meaning, rhyme, or poetic intent.
