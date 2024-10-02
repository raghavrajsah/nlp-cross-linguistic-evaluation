# Cross-Linguistic Syntactic Evaluation of Word Prediction Models

This repository contains a replication of the paper *Cross-Linguistic Syntactic Evaluation of Word Prediction Models* by Aaron Mueller, Garrett Nicolai, Panayiota Petrou-Zeniou, Natalia Talmina, and Tal Linzen. The project replicates the experiments conducted in the paper, with a focus on syntactic evaluation of word prediction models across multiple languages.

## Paper Information

**Paper Title:** Cross-Linguistic Syntactic Evaluation of Word Prediction Models  
**Authors:** Aaron Mueller, Garrett Nicolai, Panayiota Petrou-Zeniou, Natalia Talmina, and Tal Linzen  
**Published in:** Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL 2020)  
**Link:** [Access the paper](https://aclanthology.org/2020.acl-main.490/)  

## Overview

This project replicates the results from the original paper, which explores how neural word prediction models handle syntax in different languages. The paper introduces the **CLAMS** (Cross-Linguistic Assessment of Models on Syntax) dataset, focusing on subject-verb agreement across five languages: English, French, German, Hebrew, and Russian.

The models evaluated include:
- Monolingual LSTM models
- Multilingual LSTM models
- Multilingual BERT

The original paper investigates two main hypotheses:
1. Multilingual models should transfer syntactic knowledge across similar languages.
2. Models should perform better on languages with richer morphology due to more frequent cues to syntactic structure.

## Project Structure

- will update soon

## Experimental Setup

1. **Corpus:**
   - The Wikipedia dumps for each language (English, French, German, Hebrew, Russian) were processed using `WikiExtractor` and tokenized using `TreeTagger`. Sentences with more than 5% unknown words were excluded.

2. **Training and Evaluation:**
   - Monolingual LSTM models were trained for each language, using hyperparameters from van Schijndel et al. (2019). A multilingual LSTM was also trained using a concatenation of the five languages’ corpora.
   - The models were evaluated using a subject-verb agreement test set across syntactic constructions such as **Simple Agreement**, **VP Coordination**, **Relative Clauses**, and **Object-Relative Clauses**.

3. **Results:**
   - The accuracy of monolingual and multilingual LSTMs, as well as multilingual BERT, was compared across languages. The multilingual models generally underperformed compared to monolingual ones.


## Acknowledgments

This project is based on the paper by Mueller et al. (2020) and uses the CLAMS dataset. Special thanks to the authors for providing the code and dataset used for replication.

