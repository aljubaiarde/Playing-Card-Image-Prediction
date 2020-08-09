# Playing-Card-Image-Classification
![](card2.gif)



## Overview
Transfer Learning based Image prediction model which identifies playing card from 52 different classes. 

## Data
- Manually Collected (Picture captured, Video converted to Image)
- Web Scraping ( Download Google Image)
- Data Augmentation (ImageDataGenerator)

## Data Cleaning
- I had to manually cleaned the data several times. Data collection and cleaning took a lot portion of time.

## Tools
#### Environment
- Google Colaboratory
#### Libraries
- Keras
- Transfer Learning (resnet50, vgg16, vgg19)
- Pandas


## Installation
The Code is written in Python 3.7. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```
## Directory Tree 

```
├── ImageDataGenerator 
│   ├── ImageDataGenerator.ipynb
│   ├── info.txt
├── static
│   ├── css
│   │   ├──main.css
│   ├── js
│   │   ├──main.js
├── templates
│   ├── base.html
│   ├── index.html
├── Playnig Card.ipynb
├── Procfile
├── READNE.md
├── app.py
├── card2.gif
└── requirements.txt
```
## To Do
1. Generate more images in the dataset to get a way more good accuracy.
2. Deployment of this project.
3. This project is only based on CNN and Transfer learning, later with the same data I will use YOLO to predict.

## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/aljubaiarde/Playing-Card-Image-Prediction/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/aljubaiarde/Playing-Card-Image-Prediction/issues/new). Please include sample queries and their corresponding results.
## Credits
- [Udemy Machine Learning Course](https://www.udemy.com/course/machinelearning) 
- [Krish Naik](https://www.youtube.com/user/krishnaik06) 

