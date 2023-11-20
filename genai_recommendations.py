import streamlit as st
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from external_items import temp_log_items, template1, template2
from external_items import possible_outputs, possible_categories, possible_tools
import openai
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is not None:
    openai.api_key = openai_api_key
else:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")



# GenAI function to handle recommendation retrieval of issue
def get_rec_category(logItem):

    if openai_api_key is None:
        st.error("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
        return None

    llm1 = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.5)

    prompt1 = PromptTemplate(
        input_variables=['log_item', 'possible_outputs'],
        template=template1
    )

    chain = LLMChain(llm=llm1, prompt=prompt1)
    category = chain.run({
        'log_item': logItem, 
        'possible_outputs': possible_outputs
        })

    return category




# GenAI function to handle recommendation retrieval of suggested tool
def get_rec_tool(issueItem):

    if openai_api_key is None:
        st.error("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
        return None
   
    llm2 = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.1)

    prompt2 = PromptTemplate(
        input_variables=['issue_item', 'possible_categories', 'possible_tools'],
        template=template2
    )

    chain = LLMChain(llm=llm2, prompt=prompt2)
    rec_tool = chain.run({
        'issue_item': issueItem, 
        'possible_categories': possible_categories,
        'possible_tools': possible_tools
        })

    return rec_tool
