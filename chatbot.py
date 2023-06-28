import openai
import streamlit as st
from streamlit_chat import message
from decouple import config

openai.api_key = config('OPENAI_API_KEY')


def generate_response(prompt):
    completions = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    result = completions.choices[0].text
    return result


st.title('chatBot: Streamlit + openAI')

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# Get user input


def get_input():
    input_text = st.text_input(
        'You: ', 'Hi, what is your name?', key='input')
    return input_text


user_input = get_input()

if user_input:
    output = generate_response(user_input)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i)+'_user')
