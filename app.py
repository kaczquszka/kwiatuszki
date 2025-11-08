import streamlit as st
# import os
# import torch
import wikipediaapi
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
pipe = pipeline("text-classification", model="kaczquszka/fine-tuned-on-1000-answers-distilbert-base-uncased", top_k = 3, batch_size=10)

tokenizer = AutoTokenizer.from_pretrained("kaczquszka/fine-tuned-on-1000-answers-distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("kaczquszka/fine-tuned-on-1000-answers-distilbert-base-uncased")

if 'step' not in st.session_state:
    st.session_state.step = 1
if 'info' not in st.session_state:
    st.session_state.info = {
    'Growth':None,
    'Soil':None,
    'Sunlight':None,
    'Watering':None,
    'Fertilizer':None
}

Questions ={
    'Growth':'growth question',
    'Soil':'soil question',
    'Sunlight':'sunlight q',
    'Watering':'watering q',
    'Fertilizer':'fertilizer q'
}

def go_to_step2():
    st.session_state.step=2
    st.rerun()

def rerun_quiz():
    st.session_state.step=1 
    

if st.session_state.step == 1:
    st.title('What is your inner plant?')
    st.markdown('_super serious project_')
    st.divider()
    with st.form(key='quiz_answers'):
        for name in st.session_state.info.keys():
            st.session_state.info[name] = st.text_input(Questions[name])
        
        submit_button = st.form_submit_button()
        if submit_button:
            if not all(st.session_state.info.values()):
                st.warning('fill all of the fileds, please :)')
            else:
                st.balloons() 
                go_to_step2()

# def getAnswers():
#     return [item for item in st.session_state.info.values()]

def calculate_result(res_dict):
  copy = res_dict.copy() #zeby nie nadpisywac
  multiplier = {
      'neutral': 0,
      'negative': -1,
      'positive': 1
  }
  sentiment_value =[]
  for results in copy:
    for key in results:
      results[key] = results[key] * multiplier[key]
    sentiment_value.append(sum(results.values()))

  return sentiment_value

def getPrediction():
    result = pipe([item for item in st.session_state.info.values()])
    res_dict = [{item['label']: item['score'] for item in item_list} for item_list in result]
    results = calculate_result(res_dict)
    return(classifier.predict([results])[0])
    

import pickle

with open('content/knn_classifier.svn', 'rb') as f:
  classifier = pickle.load(f)

if st.session_state.step == 2:  
    plant = getPrediction()
    df = pd.read_csv('datasets/plants_unique.csv', encoding = "latin1")
    st.write(df[df['Plant Name']==plant].iloc[:,:6]) 
    wiki = wikipediaapi.Wikipedia('plant-character-classification 1.0', language='en', extract_format=wikipediaapi.ExtractFormat.HTML)
    page = wiki.page(plant)
    if(page.exists()):
        st.subheader(f'Learn more about {plant}!')
        st.html(page.summary)
        st.write('Source: ', page.fullurl)
    st.button('rerun', on_click=rerun_quiz)

     

# pressed =st.button('press')
# print(pressed)
# st.image(os.path.join(os.getcwd(),'static','bamboo.jpg'), width=70)