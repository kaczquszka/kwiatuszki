import streamlit as st
import os
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

pipe = pipeline("text-classification", model="kaczquszka/fine-tuned-on-1000-answers-distilbert-base-uncased", top_k = 3, batch_size=10)

tokenizer = AutoTokenizer.from_pretrained("kaczquszka/fine-tuned-on-1000-answers-distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("kaczquszka/fine-tuned-on-1000-answers-distilbert-base-uncased")

if 'step' not in st.session_state:
    st.session_state.step = 1
if 'info' not in st.session_state:
    st.session_state.info = {
    'Growth':None,
    'Soil':None,
}


# form_answers ={
#     'Growth':None,
#     'Soil':None,
# }

Questions ={
    'Growth':'growth question',
    'Soil':'soil question',
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

def getPrediction():
    result = pipe([item for item in st.session_state.info.values()])
    res_dict = [{item['label']: item['score'] for item in item_list} for item_list in result]
    return res_dict

if st.session_state.step == 2:  

    st.write(getPrediction()) 
    st.button('rerun', on_click=rerun_quiz)

     

# pressed =st.button('press')
# print(pressed)
# st.image(os.path.join(os.getcwd(),'static','bamboo.jpg'), width=70)