# Pinecone Embeddings Storage

## Overview

This repository contains code and examples for using Pinecone, a vector database, to store and manage embeddings. 

## Prerequisites

- Python 3.11 or higher
- Pinecone Python client

## Installation

I utilized poetry for this project. If you also are using poetry, you can simply do the following to setup your venv

```bash
C:\Users\You\Project> poetry init
C:\Users\You\Project> poetry shell
C:\Users\You\Project> poetry install
```

Or, you can use pip to install the requirements.txt

```bash
C:\Users\You\Project> pip install -r "requirements.txt"
```

You will need a `.env` file that has the following variables.
```bash
# .env format
OPENAI_API_KEY=openai_api_key_here
PINECONE_API_KEY=pinecone_api_key_here
PINECONE_INDEX_NAME=pinecone_index_name_here
```

## Setup

#### Pinecone

You will need to create an Index in Pinecone. Navigate to their [site](https://app.pinecone.io/), create an account, and create an Index using their free tier!

When creating this Index, note the name you use and add it the `.env` file we created. When you create you account, this is also where you will find the Pinecone API key we will use in the `.env` file.

If you intend to use the `text-embedding3-large` embedding model from OpenAI, we will want to use a dimensions of **3072**. Otherwise, if we are using `text-embedding-3-small` or older models, we will want to use a dimension of **1536**.

#### Adding to the Index

I have a provided file, `main.ipynb` which can be ran to insert a number of documents into our Pinecone index. Feel free to run this to insert some test data into our index.

## Chatbot

Now that we have populated our index, let's utilize a simple streamlit chatbot to pull data from our index.

To do this, we will need to open up our terminal and navigate to our project directory and run the following command.

```bash
C:\Users\You\Project> streamlit run app.py
```
