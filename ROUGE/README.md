# ROUGE, the automatic evaluation metrics used to compare generated summaries to human-made ones

Recall-Oriented Understudy for Gisting Evaluation (ROUGE) was first envisioned to be a package of multiple measurement metrics useful for comparing the quality of automatic summaries when compared to "ideal" summaries created by humans. It is oriented towards journalistic and scientific papers as those are longer and usually factual by nature, however, it can also be applied on opinative texts, although the resulting scores will be lower due to how ROUGE evaluates the summaries, which is through the matching of n-grams and longest common subsequence between them.

## Running the code

This one's rather simple: The colab notebook will give you all that's needed to compare a pair of summaries, all you need to do is give it the paths to the candidate (or system) summaries, the reference (or gold standard) summaries and the path to the resulting file, in that order.

## Credits

Here's a link to the article that first introduced ROUGE for automatic summary evaluation:

[ROUGE: A Package for Automatic Evaluation of Summaries](https://aclanthology.org/W04-1013.pdf)
