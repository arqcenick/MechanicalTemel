## Welcome to Mechanical Temel Project Site

This is a project which aims to generate and classifiy Turkish jokes also known as "fıkra" using recurrent neural networks.

### Authors
This Project is authored by

Yarkın Deniz Çetin

Lütfi Kerem Şenel

for CS 578 Natural Language Processing Course(FALL 2018)
Bilkent University

### References
[Kao, J. T., Levy, R., & Goodman, N. D. (2013). The Funny Thing About Incongruity: A Computational Model of Humor in Puns. In CogSci.](https://web.stanford.edu/~ngoodman/papers/KaoLevyGoodman.pdf)

They used a KL-divergence model for measuring the funniness, 
Their model did not generate new puns instead they propose a method to correlate funniness to objective metrics such as ambiguity of a word(defined objectively) and distinctiveness(also defined). 
We believe quantitative metrics are useful in our project.



[Petrovic, S., & Matthews, D. (2013, August). Unsupervised joke generation from big data. In ACL](http://aclweb.org/anthology/P13-2041)

This work is one of the main approaches we can take in this project, however we believe the scope of  Unsupervised joke generation from big data is too narrow. The model described in the paper limits itself into jokes which in the form of " I like my X like I like my Y,Z". The Turkish Fıkra are long and often has a story. Still we can use the metrics described in the paper for evaluation of humor in our model.

[Y. Kim, Y. Jernite, D. Sontag, and A. M. Rush, “Character-Aware Neural Language Models,” ArXiv e-prints, Aug. 2015.](https://arxiv.org/pdf/1508.06615.pdf)

Language modelling is the core of our project. In this work by kim et al., they propose a language model which makes use of character level information. Their model includes a concolutional neural network (CNN) a highway network over the characters and a long short-term memory (LSTM). Neural language models (NLMs) such as RNNs or LSTMs have been shown to outperform traditional count based n-gram language models. Most of the models make use of only word level information, however using subword information (morphemes) can be also benificial especially for morphologically rich languages such as Turkish. Model presented in this paper achieves state-of-the-art performance with 60% fewer parameters which is also important for us since our dataset will be relatively small for training a language model. We can use this model as the backbone of our project.

[Sutskever, I., Martens, J., & Hinton, G. E. (2011). Generating text with recurrent neural networks.
In Proceedings of the 28th International Conference on Machine Learning ](http://www.cs.toronto.edu/~ilya/pubs/2011/LANG-RNN.pdf)

[Serban, I. V., García-Durán, A., Gulcehre, C., Ahn, S., Chandar, S., Courville, A., & Bengio, Y.
(2016). Generating factoid questions with recurrent neural networks: The 30m factoid question-answer
corpus. arXiv preprint arXiv:1603.06807.](https://pdfs.semanticscholar.org/f802/a78c9f2491e9ccd1c9123f92f68eabf36f5d.pdf)

[Gu, J., Lu, Z., Li, H., & Li, V. O. (2016). Incorporating copying mechanism in
sequence-to-sequence learning. arXiv preprint arXiv:1603.06393.](https://arxiv.org/abs/1603.06393)

In this study they propose a new model called COPYNET, which integrates the regular way of word generation in the decoder with the new copyingmechanism which can choose subsequences in the input sequence and put them at proper places in the output sequence. We are planning to use a similiar mechanism to enable user to decide on the topic of the joke (fıkra). With such a mechanism we can force our network to generate a joke around some particular words specified by the user.


Await further updates...


