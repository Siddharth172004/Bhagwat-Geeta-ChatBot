from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    model="tngtech/deepseek-r1t2-chimera:free",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    temperature = 0.7
)

parser = StrOutputParser()

embedding = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")

db = FAISS.load_local("Vector Data",embedding ,allow_dangerous_deserialization= True)

retriver = db.as_retriever(
    search_type= "mmr",
    search_kwargs= {"k" : 3}
)

#user_input = input("Ask to Devote : ")

def call_ui(user_input, chat_history= None):

    docs = retriver._get_relevant_documents(user_input,run_manager= None)
    
    #string = [doc.page_content for doc in docs]
    #context = "\n\n".join(string)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    prompt1 = PromptTemplate.from_template(
          """
        You are a humble Devote of Lord Krishna, sharing teachings from the Bhagavad Gita.  
    
        Rules:
        1. Reply in the same language as the user (Hindi answers give in Hinglish).
        2. Keep responses spiritual, peaceful, and devotional.
        3. Never claim to be Lord Krishna; speak only like a Krishna devote.
        4. If the user uses bad words, answer with a respectful spiritual message.
        5. If the user asks for a story, give a deep and rare Hinduism story (avoid all common stories like Ramayana/Mahabharata popular tales, Prahlad, Dhruv, Ganesh, Shiv-Parvati, Narasimha, etc.). 
           Story must feel ancient, mysterious, and rooted in real Hindu tradition. 
           Never end with follow-up questions (e.g., “aur sunna hai?”, “ek aur kahani?”). End naturally.
        6. Answer ONLY from the given context.
        7. If context lacks the answer, give a general spiritual teaching (no fake verses) and do not ask anything at the end.

        context from the BhagWat Geeta:
        {context}
    
        User input : {input}
        Servant of Lord Krishna:
        """
    )
    
    
    chain = prompt1 | model | parser
    
    result = chain.invoke({"context" : context ,"input" : user_input})
    
    return result


