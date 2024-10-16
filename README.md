# Cross-Linguistic Syntactic Evaluation of Word Prediction Models

This repository contains a replication of the paper *Cross-Linguistic Syntactic Evaluation of Word Prediction Models* by Aaron Mueller, Garrett Nicolai, Panayiota Petrou-Zeniou, Natalia Talmina, and Tal Linzen. The project replicates the experiments conducted in the paper, focusing on the syntactic evaluation of word prediction models across multiple languages, with a particular emphasis on **BERT** models.

## Paper Information

**Paper Title:** Cross-Linguistic Syntactic Evaluation of Word Prediction Models  
**Authors:** Aaron Mueller, Garrett Nicolai, Panayiota Petrou-Zeniou, Natalia Talmina, and Tal Linzen  
**Published in:** Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL 2020)  
**Link:** [Access the paper](https://aclanthology.org/2020.acl-main.490/)  

## Overview

This project replicates and extends the results from the original paper, which explores how neural word prediction models handle syntax in different languages. The paper introduces the **CLAMS** (Cross-Linguistic Assessment of Models on Syntax) dataset, focusing on subject-verb agreement across five languages: English, French, German, Hebrew, and Russian.

In addition to replicating the paper’s experiments, we evaluated the performance of **monolingual and multilingual BERT models** on these syntactic tasks.

The original paper investigates two main hypotheses:
1. Multilingual models should transfer syntactic knowledge across similar languages.
2. Models should perform better on languages with richer morphology due to more frequent cues to syntactic structure.

## Project Structure

- `data/`: Contains the preprocessed datasets for each language.
- `scripts/`: Python scripts for preprocessing, model training, and evaluation.
- `results/`: Model outputs and performance metrics.
- `tables/`: Tables with comparison across languages


## Experimental Setup

1. **Corpus:**
   - Wikipedia dumps for each language (English, French, German, Hebrew, Russian) were processed using `WikiExtractor` and tokenized using `TreeTagger`. Sentences with more than 5% unknown words were excluded.

2. **Modeling and Evaluation:**
   - We used pre-trained **BERT models** (both monolingual and multilingual) from Hugging Face, and evaluated their performance on subject-verb agreement and other syntactic tasks across languages.
   - Minimal pair analysis was used to evaluate models on different syntactic constructions, including **Simple Agreement**, **VP Coordination**, and **Relative Clauses**.

3. **Results:**
   - Our replication compared the accuracy of multilingual BERT with the original results for LSTMs and monolingual models. As expected, **monolingual BERT** outperformed **multilingual BERT** on English tasks, especially in syntactically complex tasks like object-relative clauses.
   - Multilingual BERT underperformed on morphologically rich languages like Hebrew and Russian, reflecting the original study's findings.

## Acknowledgments

This project is based on the paper by Mueller et al. (2020) and uses the CLAMS dataset. Special thanks to the authors for providing the original dataset and code for replication.

