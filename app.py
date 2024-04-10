import streamlit as st
from langchain import PromptTemplate
from langchain.llms import CTransformers

#Function to get response from the model
def getllamaresponse(input_text, no_words, blog_style):
    
    #LLMS model
    llm = CTransformers(model='D:\Blog Generation\Models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01,})
    
    #Prompt Template
    
    template ="""
    Write a blog for {blog_style} on the topic {input_text} with {no_words} words.
    """
    
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                            template =template)
    
    #Generate the response from the llama2 model
    response=llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response





st.set_page_config(page_title="Generate blogs",
                   page_icon="🧊",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Generate blogs🧊")

input_text = st.text_input("Enter the Blog topic")

#Creating a two more colums for additional two fields

col1, col2 = st.columns([5,5])  

with col1:
    no_words = st.text_input("Enter the number of words")
    
with col2:
    blog_style = st.text_input('Writing the blog for',
                               ('Student','Professional','Casual'))

    
submit=st.button("Generate Blog")

# Function to get response from the model

if submit:
    st.write(getllamaresponse(input_text, no_words, blog_style))