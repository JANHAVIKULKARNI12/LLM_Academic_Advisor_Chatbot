import os
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI
from utils import load_docs

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def build_chain():
    chunks = load_docs()

    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(
        llm=OpenAI(temperature=0),
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return chain
