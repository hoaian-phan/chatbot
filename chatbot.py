import openai
import streamlit as st
from streamlit_chat import message
from decouple import config

openai.api_key = config('OPENAI_API_KEY')


def generate_response(prompt):
    completions = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stope=None,
        temparature=0.5,
    )
    message = completions.choices[0].text
    return message


st.title('chatBot: Streamlit + openAI')
