import streamlit as st
# import os
# import torch
import wikipediaapi
import wikipedia
from transformers import pipeline
import pandas as pd
import pickle
import time


if 'sentiment' not in st.session_state:
    st.session_state.sentiment = {
    'Growth':None,
    'Soil':None,
    'Sunlight':None,
    'Watering':None,
    'Fertilizer':None
}

if 'page' not in st.session_state:
    st.session_state.page = None
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
    
if 'plant' not in st.session_state:
    st.session_state.plant = None     

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
    st.stop()

def rerun_quiz():
    st.session_state.step=1 


def calculate_result(res_dict):
  copy = res_dict.copy() #zeby nie nadpisywac
  multiplier = {
      'neutral': 0,
      'negative': -1,
      'positive': 1
  }
  sentiment_value =[]
  key_sentiment_dict = list(st.session_state.sentiment.keys())
  x = 0
  for results in copy:
    for key in results:
      results[key] = results[key] * multiplier[key]
    sentiment_value.append(sum(results.values()))
    st.session_state.sentiment[key_sentiment_dict[x]] = sum(results.values())
    x = x+1


  
  return sentiment_value

def getPrediction():
    pipe = pipeline("text-classification", model="kaczquszka/fine-tuned-on-1000-answers-distilbert-base-uncased", top_k = 3, batch_size=10)
    result = pipe([item for item in st.session_state.info.values()])
    res_dict = [{item['label']: item['score'] for item in item_list} for item_list in result]
    results = calculate_result(res_dict)
    with open('content/knn_classifier.svn', 'rb') as f:
        classifier = pickle.load(f)
    return(classifier.predict([results])[0])
    
def findPage():
    query = st.session_state.plant + ' plant'
    page_name = wikipedia.search(query,1)
    wiki = wikipediaapi.Wikipedia('plant-character-classification 1.0', language='en', extract_format=wikipediaapi.ExtractFormat.HTML)
    return wiki.page(page_name[0])

if st.session_state.step == 1:
    title_placeholder = st.empty()
    form_placeholder = st.empty()
    with title_placeholder.container():
        st.title('What is your inner plant?')
        st.markdown('_super serious project_')
        st.divider()
    
#https://docs.streamlit.io/develop/api-reference/layout/st.empty
    with form_placeholder.form("quiz_answers"):
        for name in st.session_state.info.keys():
            st.session_state.info[name] = st.text_input(Questions[name])

        submit_button = st.form_submit_button("Submit")

    if submit_button:
        if not all(st.session_state.info.values()):
            st.warning('fill all of the fileds, please :)')
        else:
            form_placeholder.empty()
            title_placeholder.empty()
            go_to_step2()

        
elif st.session_state.step == 2:  
    st.write('hi')
    st.session_state.plant = getPrediction()
    st.session_state.page = findPage()
    time.sleep(2)
    st.session_state.step = 3
    st.rerun()

elif st.session_state.step == 3: 
    html_text = st.session_state.page.summary
    source_text = st.session_state.page.fullurl
    if(st.session_state.page.exists()):
        df = pd.read_csv('datasets/plants_unique.csv', encoding = "latin1")
        st.write(df[df['Plant Name']==st.session_state.plant].iloc[:,:6]) 
        st.markdown(st.session_state.sentiment)
        st.markdown(st.session_state.info)
        st.subheader(f'Learn more about {st.session_state.plant}!')
        st.html(html_text)
        st.write('Source: ', source_text)
    st.button('rerun', on_click=rerun_quiz)