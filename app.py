import streamlit as st
import os

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

if st.session_state.step == 2:           
    st.write(st.session_state.info) 
    st.button('rerun', on_click=rerun_quiz)

     

# pressed =st.button('press')
# print(pressed)
# st.image(os.path.join(os.getcwd(),'static','bamboo.jpg'), width=70)