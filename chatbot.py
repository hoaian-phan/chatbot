import openai
import streamlit as st
from streamlit_chat import message
from decouple import config

openai.api_key = config('OPENAI_API_KEY')
