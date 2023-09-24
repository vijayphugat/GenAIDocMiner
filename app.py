from typing import Set

from qa.qa_openai_faiss import run_qa_chain_openai_faiss
import streamlit as st
from streamlit_chat import message

# st.header("Chat with PDF")
html_temp = """
    <div style ="background-color:yellow;padding:12px">
    <h1 style ="color:black;text-align:center;">Talk to your files</h1>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)

st.header("")
prompt = st.text_input("Input Query", placeholder="Enter your query here..")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []


def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string


if prompt:
    with st.spinner("Generating response.."):
        generated_response = run_qa_chain_openai_faiss(query=prompt)

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(generated_response)

        # if reading from pinecone
        # sources = set(
        #     [doc.metadata["source"] for doc in generated_response["source_documents"]]
        # )
        #
        # formatted_response = (
        #     f"{generated_response['result']} \n\n {create_sources_string(sources)}"
        # )
        # st.session_state["user_prompt_history"].append(prompt)
        # st.session_state["chat_answers_history"].append(formatted_response)

if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
        message(user_query, is_user=True)
        message(generated_response)
