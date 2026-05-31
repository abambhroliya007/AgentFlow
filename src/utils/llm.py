import os

from dotenv import load_dotenv
from openai import OpenAI

try:
    import streamlit as st
except ImportError:
    st = None


load_dotenv()


def get_api_key():
    if st:
        try:
            return st.secrets["OPENAI_API_KEY"]
        except Exception:
            pass

    return os.getenv("OPENAI_API_KEY")


client = OpenAI(
    api_key=get_api_key()
)


def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content