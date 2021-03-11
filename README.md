# Spotify_Project

## Summary

## Table of contents

|File Name|Type|Description|
|---|---|---|
|Data_EDA.ipynb|Jupiter Notebook|This notebook contains the Data cleaning and EDA perfomed on the spotify data.||
|modeling.ipynb|Jupiter Notebook|This notebook contains the Modeling process to find a songs genre based on data about the song.|
|data|folder||

# Data Dictionary 
                
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
|liveness|float|Base cost of item in row. (will use other column)||
|valence|float|This is a percentage value that describes how happy a song sounds.||
|tempo|float|individual record id for each item||
|id|object|These are string ids for the songs in the dataset. These values should be dropped as there are too many unique values that will make the model over fit.||
|uri|object|This column contains similar data as in the id column. This coulmn should be dropped as well to prevent creating too many features when dummying the columns.||
|track_href|object|track_href is the url for the specific track. This column will not make give good data fro the model and will be dropped.||
|analysis_url|object|This column contains similar data as in the track_href column. This column should be dropped as well to prevent creating too many features when dummying the columns.||
|duration_ms|int64| These are the song durations in milliseconds. These are numeric values.||
|time_signature|int64|This is a class like integer that shows the time signature of the song.||
|genre  |object|Actual price of item at time of sale (This changes when items are marked on sale.)||
|song_name|object|Name of the song.||
