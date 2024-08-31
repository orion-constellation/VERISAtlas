import streamlit as st
import uuid
import qdrant_client
from langchain import LLMChain, GPT4
from pymongo import MongoClient
import matplotlib.pyplot as plt
import seaborn as sns
import random
import time

# Initialization
st.set_page_config(page_title="VERISAtlas", layout="wide", initial_sidebar_state="expanded")
session_id = st.session_state.get("session_id", str(uuid.uuid4()))
st.session_state["session_id"] = session_id

# Sidebar
def render_sidebar():
    st.sidebar.title("VERISAtlas")
    project = st.sidebar.selectbox("Choose a Project", ["Project A", "Project B", "Project C"])
    veris_incident = st.sidebar.selectbox("Choose a VERIS Incident", ["Incident 1", "Incident 2", "Incident 3"])
    st.sidebar.button("Clear Output 🧹", on_click=clear_output)
    return project, veris_incident

def clear_output():
    st.session_state.clear()

# Page 1: Overview with Output Boxes and Charts
def page1():
    st.title("📊 VERIS Incident Analysis")
    project, veris_incident = render_sidebar()

    # Output Box 1
    st.subheader("Incident Overview 💬")
    output_box1 = st.empty()
    with output_box1:
        st.write("Initializing incident overview...")
        time.sleep(1)
        for i in range(10):
            st.write(f"Loading data for {veris_incident}... {i+1}/10 🧠")
            time.sleep(0.2)

    # Output Box 2
    st.subheader("Incident Details 🧾")
    output_box2 = st.empty()
    with output_box2:
        st.write("Fetching detailed insights...")
        time.sleep(1)
        for i in range(10):
            st.write(f"Analyzing metrics for {veris_incident}... {i+1}/10 🔍")
            time.sleep(0.2)

    # Charts
    st.subheader("Visual Analysis 📈")
    col1, col2 = st.columns(2)

    with col1:
        st.write("Scatter Plot 📊")
        x = [random.randint(1, 100) for _ in range(10)]
        y = [random.randint(1, 100) for _ in range(10)]
        plt.scatter(x, y, c='blue')
        st.pyplot(plt)

    with col2:
        st.write("Bar Chart 📊")
        data = [random.randint(1, 100) for _ in range(5)]
        sns.barplot(x=list(range(5)), y=data)
        st.pyplot(plt)

# Page 2: Chat Interface with Contextual Knowledge
def page2():
    st.title("💬 Chat with VERISAtlas")
    project, veris_incident = render_sidebar()

    # Chat Interface
    st.subheader("Chat Interface 🤖")
    user_input = st.text_input("Ask VERISAtlas:", "")
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    if user_input:
        response = query_llm(user_input, project, veris_incident)
        st.session_state["chat_history"].append((user_input, response))
        save_conversation(user_input, response, session_id)

    for question, answer in st.session_state["chat_history"]:
        st.write(f"**You:** {question} 🤔")
        st.write(f"**VERISAtlas:** {answer} 😊")

# Query the LLM using LangChain and GPT-4
def query_llm(user_input, project, veris_incident):
    client = qdrant_client.QdrantClient()  # Replace with actual client setup
    # Example of how to call LangChain with GPT-4
    chain = LLMChain(llm=GPT4(model="gpt-4"))
    query_context = f"Project: {project}, Incident: {veris_incident}. Question: {user_input}"
    response = chain.run(query_context)
    return response

# Save conversation to NoSQL Database (MongoDB as fallback)
def save_conversation(user_input, response, session_id):
    mongo_client = MongoClient("mongodb://localhost:27017/")
    db = mongo_client["veris_atlas"]
    conversations = db["conversations"]
    conversations.insert_one({
        "session_id": session_id,
        "question": user_input,
        "answer": response
    })

# Main app logic to route between pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Page 1: Incident Analysis", "Page 2: Chat Interface"])

    if page == "Page 1: Incident Analysis":
        page1()
    elif page == "Page 2: Chat Interface":
        page2()

if __name__ == "__main__":
    main()
