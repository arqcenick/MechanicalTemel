## Welcome to Mechanical Temel Project Site

This is a project which aims to generate and evaluate Turkish jokes also known as "fıkra" using recurrent neural networks.

### Authors
This Project is authored by

Yarkın Deniz Çetin

Lütfi Kerem Şenel

for CS 578 Natural Language Processing Course(FALL 2018)
Bilkent University

### Source Material
---
### Posted on: 14.11.2017

[Sutskever, I., Martens, J., & Hinton, G. E. (2011). Generating text with recurrent neural networks.
In Proceedings of the 28th International Conference on Machine Learning ](http://www.cs.toronto.edu/~ilya/pubs/2011/LANG-RNN.pdf)




[Serban, I. V., García-Durán, A., Gulcehre, C., Ahn, S., Chandar, S., Courville, A., & Bengio, Y.
(2016). Generating factoid questions with recurrent neural networks: The 30m factoid question-answer
corpus. arXiv preprint arXiv:1603.06807.](https://pdfs.semanticscholar.org/f802/a78c9f2491e9ccd1c9123f92f68eabf36f5d.pdf)



[![Generating Language with Attention](https://img.youtube.com/vi/ah7_mfl7LD0/hqdefault.jpg)](https://www.youtube.com/watch?v=ah7_mfl7LD0)

Generating Language with Attention Lecture:

"This lecture introduces one of the most important and influencial mechanisms employed in Deep Neural Networks: Attention. Attention augments recurrent networks with the ability to condition on specific parts of the input and is key to achieving high performance in tasks such as Machine Translation and Image Captioning."

We believe this video provides some great insights about constructing our own generative model. 

---
### Posted on: 16.10.2017

[Kao, J. T., Levy, R., & Goodman, N. D. (2013). The Funny Thing About Incongruity: A Computational Model of Humor in Puns. In CogSci.](https://web.stanford.edu/~ngoodman/papers/KaoLevyGoodman.pdf)

They used a KL-divergence model for measuring the funniness, 
Their model did not generate new puns instead they propose a method to correlate funniness to objective metrics such as ambiguity of a word(defined objectively) and distinctiveness(also defined). The model uses three types of sentences, which are puns, de-puns and non-puns. The puns are simple homonym based jokes, the de-puns are puns where the "distinct" verb or object is replaced with more common word, making it non-funny. The non-puns are just normal sentences with no funniness intened. The word relatedness measure in these different type of sentences create quantitative features which can be used to classifiy sentences in to the aforementioned catagories.
We believe quantitative metrics are useful in our project.


[Petrovic, S., & Matthews, D. (2013, August). Unsupervised joke generation from big data. In ACL](http://aclweb.org/anthology/P13-2041)

This work is one of the main approaches we can take in this project, however we believe the scope of  Unsupervised joke generation from big data is too narrow. The model described in the paper limits itself into jokes which in the form of " I like my X like I like my Y,Z". The Turkish Fıkra are long and often has a story. Still we can use the metrics described in the paper for evaluation of humor in our model.


[Y. Kim, Y. Jernite, D. Sontag, and A. M. Rush, “Character-Aware Neural Language Models,” ArXiv e-prints, Aug. 2015.](https://arxiv.org/pdf/1508.06615.pdf)

Language modelling is the core of our project. In this work by kim et al., they propose a language model which makes use of character level information. Their model includes a concolutional neural network (CNN) a highway network over the characters and a long short-term memory (LSTM). Neural language models (NLMs) such as RNNs or LSTMs have been shown to outperform traditional count based n-gram language models. Most of the models make use of only word level information, however using subword information (morphemes) can be also benificial especially for morphologically rich languages such as Turkish. Model presented in this paper achieves state-of-the-art performance with 60% fewer parameters which is also important for us since our dataset will be relatively small for training a language model. We can use this model as the backbone of our project.


[Gu, J., Lu, Z., Li, H., & Li, V. O. (2016). Incorporating copying mechanism in
sequence-to-sequence learning. arXiv preprint arXiv:1603.06393.](https://arxiv.org/abs/1603.06393)

In this study they propose a new model called COPYNET. Their model integrates the regular way of word generation in the decoder with the new copying mechanism which can choose subsequences in the input sequence and put them at proper places in the output sequence. They evaluate their model specifically for the text summarization task. Although our aim in this project is not to summarize the jokes, we can make use of their model to enable user to decide on the topic of the joke (fıkra). Using specific parts of their COPYNET model, we can force our network to generate a joke around some particular words specified by the user.


Await further updates...


