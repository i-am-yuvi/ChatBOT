# This is a sample Python script.
import streamlit as st
import openai
import os

# Set your OpenAI API key here
api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = api_key

# Press the green button in the gutter to run the script.
def main():
    st.title("ChatBOT")
    # st.file_uploader("Open", type="mp3")
    #
    # st.chat_message("assistant").write("Ask me anything!")
    #
    # if user_query := st.chat_input(placeholder="Ask me anything!"):
    #     st.chat_message("user").write(user_query)
    model_lst = openai.Model.list()
    models = []

    for i in model_lst['data']:
        models.append(i['id'])

    if model_lst:
        selected_model = st.selectbox("Select a model:", models)
        st.write(f"You selected: {selected_model}")
    else:
        st.warning("No models available.")




if __name__ == "__main__":
    main()