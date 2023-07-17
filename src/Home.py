import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="Takweed GPT | Chat-Bot 🤖")
# st.set_config('browser.uiDirection', 'RTL')
#Contact
with st.sidebar.expander("📬 Contact"):

    st.write("**Medium:** "
"[@ahmedkhaled4d](https://medium.com/@ahmedkhaled4d)")

    st.write("**Twitter:** [@ahmedkhaled4d](https://twitter.com/ahmedkhaled4d)")

#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Takweed GPT, your data-aware assistant 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>
    Takweed GPT 🤖  for chat with CSV, PDF, TXT files robot and YTB videos 🔴 | using Langchain 🐦 | OpenAI 🧠 | Streamlit 
    </h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


 

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 




