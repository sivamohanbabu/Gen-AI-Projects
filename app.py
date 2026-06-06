import streamlit as st
from transformers import pipeline



st.title("AI Story Generator")
prompt = st.text_input("Enter a prompt to start your story:")
model = pipeline("text-generation", model="gpt2")

if st.button("Generate Story"):
    if prompt:
        with st.spinner("Generating story..."):
            story = model(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
            st.subheader("Generated Story:")
            st.write(story)
    else:
        st.warning("Please enter a prompt to generate a story.")