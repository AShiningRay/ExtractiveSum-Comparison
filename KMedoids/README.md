# Implementation of the K-Medoids text summarization technique

Text summarization through the selection of the K-Medoids from a graph is one of the oldest means of obtaining a text summary, and it works by coding sentences into nodes and weighing them with TF-IDF to create a graph where important sentences are calculated by means of euclidean distance and the Partitioning Around Medoids (PAM) algorithm.

## Running the code

Running this one is as simple as LexRank's, just copy the folder into your Google Drive, updating the paths on the given Colab Notebook (the path containing `Corpus_TXT_PFC2` refers to the folder containing the base documents), and running `Runtime->Run all`. The results will be available on the `Sumarios_PFC2` subfolder.

## Credits

Here's a link to the book that introduced the concept of clustering with K-Medoids:

[Clustering by Means of Medoids](https://www.researchgate.net/publication/243777819_Clustering_by_Means_of_Medoids)
