# CRF++0.58
--tested on Ubuntu 16.04

# Prerequisits
1. C++ compiler (gcc 3.0 or higher)
2. System requirements - preferably Linux

# Getting Started
 Installation - download the zip file from the official documentation website https://taku910.github.io/crfpp/

## Important Files
1. Training set - all rows of the training set must contain same number of columns, specifically --word tab POS tag
2. Testing set - same as training set
3. Template - defines the set of features to be used while training the tagger

## Run your tagger
```crf
crf_learn template train.txt model
crf_test model test.txt
```
