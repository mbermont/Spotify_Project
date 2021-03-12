An executive summary:
What is your goal?
* To Assign the genre of a song based on the characteristics of the song. 

Where did you get your data?
* Kaggle (https://www.kaggle.com/mrmorj/dataset-of-songs-in-spotify)

What are your metrics?
* Accuracy and Cross Entropy score.

What were your findings?
* I found that I was able to assign genres with ~67% accuracy. Which is 10 times better than the baseline accurtacy 
  score of 6.667%
  
What risks/limitations/assumptions affect these findings?
* The main limitation is the unbalance of the target data.  The top value fo rthe target apears over 6000 times in the 
dataset, while the smallest target value only appears 1000 times in the dataset.  

Summarize your statistical analysis, including:
implementation
evaluation
inference

My model uses a Multiclass classification neural network to find genre of a song given the songs atttributes. I have been 
experimenting with multiple different settings for the neural network, including changing the number of hidden layer, 
the number of nodes, and the number of epochs. I have found the best result with 4 hidden layers, 2 layers with 32 nodes
and two other hidden layers with 64 nodes, and 90 epochs. This model is ~67% accurate, with a cross entropy score close 
to one.   This tells me that the model is limited by the data. As stated the 

Clearly document and label each section of your notebook(s)

Logically organize your information in a persuasive, informative manner.
Include notebook headers and subheaders, as well as clearly formatted markdown for all written components.
Include graphs/plots/visualizations with clear labels.
Comment and explain the purpose of each major section/subsection of your code.
Document your code for your future self, as if another person needed to replicate your approach.


Clearly document all of your decision points in the relevant sections
How did you acquire your data?
* I aquired my data by downloading it form kaggle

How did you transform or engineer your data? Why?
* I engineered my data by combining the song name and title columns as there was no overlap in values. I then created to 
feature from the titles by counting the words in the title and the number of characters. The addition of this data lead
to a 5% accuracy gain for my model.
  
How did you select your model?
* I selected my model because I wanted to push myself to use pytorch, as I have not used this package in prodcution 
  before. I then used trial and error adding and subtracting layers, nodes and epochs, to find the best model. I also 
  chose a neural network because it would be the most useful model to determine multiclass classification.
  

How did you optimize hyperparameters?
* I used trial and error adding and subtracting layers, nodes and epochs, to find the best model. I also 
  chose a neural network because it would be the most useful model to determine multiclass classification.

Host your notebook and any other materials in your own public Github Repository.

You repo should have README file that guides us through the repository and links to important files.
Include links and explanations to any outside libraries or source code used.
Host a copy of your dataset or include a link to a remotely hosted version.