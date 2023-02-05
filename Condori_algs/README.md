# This directory contains an adaptation of the Tadano and Opizer-E extractive summarization methods by Roque Lopez

Both methods are aspect-based, meaning that they don't generate a general summary containing the most relevant sentences that could be extracted from it. Instead, they extract a given number of aspects from the annotated opinions, and for each of them, select the top ranked sentences that besides being the most informative, are also strongly related to the aspect in question.

## Running the code

Since the code has been tweaked to run on python 3 (last tested version was 3.8.10), running it on that environment should be relatively simple given that a colab notebook is provided. Just load this folder up on your google drive, change the paths on the cells to reflect where the main python executable is located, and click on `Runtime->Run all`. The results will be placed inside `resource/automatic_summaries/{opizere, tadano}/`.

Older results and annotated data from the first batches of summarizations and testing are also available for archiving purposes.

## Credits

Here are the links to the original repo, and the author's paper:

[Original Repository](https://github.com/roquelopez/opizer)
[Opinion summarization methods: Comparing and extending extractive and abstractive approaches](https://www.sciencedirect.com/science/article/pii/S0957417417300829).

The original readme from that repo is also available here as `Original_README.md`.
