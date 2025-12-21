# Personality to Plant Classification - main idea

This project is an NLP-based personality classification application that maps user responses from a quiz to a symbolic “inner plant” archetype. The system analyzes free-text answers using sentiment analysis powered by a fine-tuned DistilBERT model and a k-nearest neighbors classifier.

The application is deployed as an interactive Streamlit web app and can be accessed via link: https://what-is-your-inner-plant.streamlit.app/


# What is the logic behind the classificatiton?
The questions in the quiz are mapped to specific traits of plants.
There are five groups of traits: Growth, Soil, Sunlight, Watering and Fertilizer
Each of the groups describe specifications of the plants, eg. how often do you need to water them.
Each of the groups also correspond to specific human traits:
Growth - how fast can one learn.
Soil - how much of an extrovert or a conformist one is.
Sunlight - how much does one like sunny and hot weather.
Watering - how much does one like water related activities such as swimming, etc.
Fertilization - how good and balanced is ones diet.

Via five question form, user is asked to answer one question from each group. The questions are created in a way that forces user to explain their attitude or liking towards the conserned topic, eg. Trait: Growth, Question: "How eager are you to learn new technologies?".

After form is submitted, the answers are encoded via fine-tuned DistilBert model (more about fine-tuning below) into sentiment analysis result where -1 stands for complitly negative, 0 for neutral and 1 for positive attitude.

Then using k-NN classifier that was trained on dataset consisting of over 200 entries of plants and their traits.

After the appropariate plant is selected, the results are displayed to user.

Along with the verdict user also gets to see the photo of the plant along with DataFrame showing the results of sentimnet analysis along with apropariate question, answer and trait of the plant it concerns. The app also displays first paragraph of wikipedia page, briefly describing the obtained plant.

# Technologies used in project
## Machine Learning
## DistilBert fine-tuning
The fine tuning of DistilBert was performed using dataset of short answers that were obtained from responses to forms. To make the dataset bigger, similar responses were then added.

## k-Nearest Neighbours
The model was trained on a dataset from kaggle :. Before training the model, appropariate data cleansing was performed. (the code can be seen in file 'data_cleansing.py' in catalog 'scripts')
**Data cleansing steps I did:**
Droping duplicates of the same plant entries
Fixing typos in column naming
Keeping only one row if many entries have the same trait values in every column
For each column, create a separate dictionary that sorts all values in order from least to most (eg. from rarest watering frequency to the most often one)
Map each column, so each value has an assigned numerical value form -1 to 1

After performing the data cleansing I used knn model available in sklearn python library with number of neighbours set to one to always obtain only one result, I chose minkowski method with p = 4 as I wanted to penalize large differencess between traits to prevent significant mismatching of traits. The goal is to get result in which each of the traits matches user answers.
