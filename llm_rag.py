import argparse
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
import google.generativeai as genai
import os
import glob
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter,RecursiveCharacterTextSplitter
import gradio as gr
from dotenv import load_dotenv

#  
load_dotenv()
api_key =os.getenv('GEMINI_API_KEY')
model_name =os.getenv('GEMINI_API_KEY')

genai.configure(api_key=api_key)
text_loader_kwargs = {'encoding': 'utf-8'}

def add_metadata(doc, doc_type):
    doc.metadata["doc_type"] = doc_type
    return doc

def read_docs(path):
    folders = glob.glob(path)
    documents = []
    for folder in folders:
        doc_type = os.path.basename(folder)
        loader = DirectoryLoader(folder, glob="**/*.md", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
        folder_docs = loader.load()
        documents.extend([add_metadata(doc, doc_type) for doc in folder_docs])
    return documents


# 
def process_llms (docs_path):

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )
    llm = ChatGoogleGenerativeAI(model=model_name, api_key=api_key)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(read_docs(docs_path))
    vector_store = FAISS.from_documents(chunks, embedding=embeddings)

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, 
                                                            retriever=vector_store.as_retriever(search_kwargs={'k': 3}),
                                                            memory=memory,
                                                            )
    return conversation_chain





def main():
    
    # Create the parser
    parser = argparse.ArgumentParser(
        description='Process input file and write results to output file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Add arguments
    parser.add_argument(
        '--folders_path',
        help='Path to the input file'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Use the arguments in your program
    
    conversation_chain = process_llms(args.folders_path)
    def chat(question, history):
        result = conversation_chain.invoke({"question": question, "chat_history": history})
        return result['answer']

    view = gr.ChatInterface(chat).launch()

if __name__ == '__main__':
    main()