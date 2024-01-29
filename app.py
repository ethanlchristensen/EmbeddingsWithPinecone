# streamlit run app.py

import os

import openai
from openai import OpenAI

import pinecone
from pinecone import Pinecone, ServerlessSpec, PodSpec

import streamlit as st

from dotenv import load_dotenv
env_loaded = load_dotenv()


if not st.session_state.get("pinecone"):
    st.session_state["pinecone_index"] = pinecone.Pinecone().Index(name=os.getenv("PINECONE_INDEX_NAME"))
    
if not st.session_state.get("embedding_function"):
    def embedding_function(text: str) -> list[float]:
        return openai.embeddings.create(input=[text], model="text-embedding-3-large").data[0].embedding
    st.session_state["embedding_function"] = embedding_function

if not st.session_state.get("messages"):
    st.session_state["messages"] = [("assistant", "How can I help you today?")]


for role, message in st.session_state.get("messages"):
    st.chat_message(name=role).write(message)

query = st.chat_input(placeholder="Enter your message")

if query:
    st.chat_message("user").write(query)
    
    with st.chat_message(name="assistant"):
        matches = None
        response = "Sorry, I couldn't find any matches!"
        with st.spinner("Calling Pinecone Index to get results ..."):
            try:
                query_embeddings = st.session_state.get("embedding_function")(text=query)
                matches = st.session_state.get("pinecone_index").query(
                    vector=query_embeddings,
                    top_k=3,
                    include_metadata=True
                )["matches"]
            except Exception as e:
                print(f"ERROR: {e}")
        if matches:
            response = f"Here is a match I found! <br/><br/>{matches[0]['metadata']['text']}"
            st.markdown(response, unsafe_allow_html=True)
                
    st.session_state["messages"].append(("user", query))
    st.session_state["messages"].append(("assistant", response))
