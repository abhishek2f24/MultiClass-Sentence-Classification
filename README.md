# MultiClass-Sentence-Classification
This repository contains file from preprocessing to deployment(as Azure HTTP trigger function)


## Dataset used for model training
Text classification is the fundamental machine learning technique behind applications featuring natural language processing, sentiment analysis, spam & intent detection, and more. This critical function is especially useful for language detection, which allows organizations and individuals to understand things like customer feedback in ways that will inform future approaches.
Training an ML model for text classification brings with it challenges. I have compiled some list to ensure you have a seamless and highly-efficient journey getting it done.

Dataset Category | Link 
--- | --- 
*Sentiment Analysis and Review Datasets* | [Twitter US Airline Sentiment](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment), [Paper Reviews](https://archive.ics.uci.edu/ml/datasets/Paper+Reviews), [Amazon Product Data](http://jmcauley.ucsd.edu/data/amazon/),[Multi-Domain Sentiment Analysis ](https://www.cs.jhu.edu/~mdredze/datasets/sentiment/), [Large Movie Review ](http://ai.stanford.edu/~amaas/data/sentiment/), [Opin-Rank Review](http://archive.ics.uci.edu/ml/datasets/opinrank+review+dataset) 
*Online Content Evaluation Datasets* | [Spambase](http://archive.ics.uci.edu/ml/machine-learning-databases/spambase/), [Stop Clickbait](https://github.com/bhargaviparanjape/clickbait), [Hate Speech and Offensive Language](https://github.com/t-davidson/hate-speech-and-offensive-language)
*News Datasets* | [The 20 Newsgroups](http://qwone.com/~jason/20Newsgroups/), [AG’s New Topic Classification](https://github.com/mhjabreel/CharCnn_Keras/tree/master/data/ag_news_csv), [Reuters Text Categorization](http://kdd.ics.uci.edu/databases/reuters21578/reuters21578.html)


If you have any other dataset, preprocess dataset to follow below format. 

Sentence | Label
--- | --- 
*Sample 1* | `label1` 
*Sample 2* | `label2` 
*Sample 3* | `label3` 
*Sample 4* | `label4` 
*Sample 5* | `label1` 

# Model
In this repository, we have used following models for sentence classification

Tokenizer/Embedder | Model | Rank (based on Precision/Recall/f1-score)
--- | --- | ---
*Elmo* | `Bi-Directional LSTM` |   `2`
*word2vec* | `LSTM/RNN` | `3`
*Bert* | `CNN` | `1`
