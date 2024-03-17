import openai
import streamlit as st

# Load your API key from an environment variable or secret management
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Creative Story Generator")

prompt = st.text_area("Enter a prompt for the story:")
submit = st.button("Generate Story")

if submit and prompt:
    with st.spinner("Generating your story..."):
        response = openai.Completion.create(
            engine="text-davinci-004",
            prompt=prompt,
            max_tokens=150
        )
        story = response.choices[0].text.strip()
        st.text_area("Generated Story:", story, height=250)
