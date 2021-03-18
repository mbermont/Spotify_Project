# Spotify Project



## Summary

For my capstone project I chose to tackle the problem of assigning genres to songs based on the attributes of the song. 
In this scenario, Spotify is looking at publishing music similarly to how SoundCloud allows users to post content. 
In preparation of users adding music to the platform, **Spotify is requesting a method to categorize these new songs into 
their respective genres.** I have chosen to build a MultiClass Classification Model utilizing PyTorch to create a Neural 
Network. The data from kaggle is restricted by being unbalanced in regards to the target value, genre. Given this deficit, I 
was able to exceed baseline accuracy by tenfold. This repository contains all materials related to this project. 


## Table of contents

|File Name|Type|Description|
|---|---|---|
|code/Data_EDA.ipynb|Jupiter Notebook|This notebook contains the Data cleaning and EDA perfomed on the spotify data.||
|code/modeling.ipynb|Jupiter Notebook|This notebook contains the Modeling process to find a songs genre based on data about the song.|
|data|folder|This folder contains the original data from kaggle and the cleaned data for modeling|
|imgs|folder|This folder contains the images and plots used for this project.| 
|docs|folder|This folder contains documents relating to the project.|


# Data
The data for this project came from a Kaggle competition (https://www.kaggle.com/mrmorj/dataset-of-songs-in-spotify).
The data had one limitation which was the uneven distribution of target values for the model. However, since most models
in the real world do not get the perfect training data, this projects offers to be an excersize working with real life data. 

## Data Dictionary 
                
|Column|Type|Description|
|---|---|---|
|danceability|float|These are percentage values that describe the danceability of the song.||
|energy  |float|These are percentage values that describe the energy in the song.||
|key|int64|This is the key of the song denoted by numbers from 0-11.||
|loudness|float|These are numeric values that describe the loudness of the song.||
|mode |int64|This is a column made up of ones and zeros depicting the mode of the song, where 1 is the song is on the major scale and 0 is not||
|speechiness|float|These are numeric percentages that describe the speechiness quality of the song.||
|acousticness|float|These are numeric percentages that describe the acouticness of the song.||
|instrumentalness|float64|These are numeric percentages that describe the instrumental percentage of the song.||
|liveness|float|The percent of song that is live.||
|valence|float|This is a percentage value that describes how happy a song sounds.||
|tempo|float|The beats per minute of the song.||
|id|object|These are string ids for the songs in the dataset. These values should be dropped as there are too many unique values that will make the model over fit.||
|uri|object|This column contains similar data as in the id column. This coulmn should be dropped as well to prevent creating too many features when dummying the columns.||
|track_href|object|track_href is the url for the specific track. This column will not make give good data fro the model and will be dropped.||
|analysis_url|object|This column contains similar data as in the track_href column. This column should be dropped as well to prevent creating too many features when dummying the columns.||
|duration_ms|int64| These are the song durations in milliseconds. These are numeric values.||
|time_signature|int64|This is a class like integer that shows the time signature of the song.||
|genre  |object|This is the genre of the song, there are 15 unique values for genre. This will be the target of the model.||
|song_name|object|Name of the song.||



# Conclusions and Recommendations

* I created a neural network model to predict the genre of a song given attribute data about the song.


* This model without regularization is over ten fold better than the baseline model.


* Utilizing Dropout Regularization did not improve the model in terms of accuracy, due to the data deficiency. It did improve the model by making the model less over fit and far less erratic. However, regardless of the model set up, I have never been able to achieve an accuracy score above 70%


 

# References 
* https://www.kaggle.com/mrmorj/dataset-of-songs-in-spotify



* https://pytorch.org/docs/stable/torch.html#parallelism


* https://en.wikipedia.org/wiki/Spotify