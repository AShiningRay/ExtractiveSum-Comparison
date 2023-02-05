# This repository contains an adaptation of the Maximal Marginal Relevance summarization method by Suhas Nithyanand

The Maximal Marginal Relevance method aims to reduce as much redundancy as it can from the sentences retrieved from a cluster of documents, maintaining their query (or in our case, summary) relevance along the way.

Being a method mostly tailored for search engine queries, it excels at returning the intormation that's most relevant to users, which means it doesn't follow the usual logic of ranking sentences by similarity and redundancy, making it a novel way of tackling opinion summarization, known to rely on redundancy as a means of reinforcing a sentence's importance.

## Running the code

This technique's original implementation was adapted to Python 3 (last tested version was 3.9.4). To run the code, copy this folder to your google drive, change the `documents` and `summaries` paths present in `main_mmr.py` to match the location of those folders in your drive, fire up the colab notebook and change the paths in there as well, then run `Runtime->Run all`. The results will be placed on the `/summaries` subfolder.

## Credits

Here are the links to the original repo, and a paper introducing MMR for summarization tasks:

[Original Repository](https://github.com/suhas-nithyanand/Text-Summarization-MMR)
[The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries](https://www.cs.cmu.edu/~jgc/publication/The_Use_MMR_Diversity_Based_LTMIR_1998.pdf)
