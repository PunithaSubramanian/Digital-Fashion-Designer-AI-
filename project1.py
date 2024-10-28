import streamlit as st
import openai
openai.api_key="sk-tF6vHEhRmkLuboUepPug8CVCzSn_1CLwJWZzFQUvbAT3BlbkFJ4bCU-_3m9svOuTaiflZ62XrqnhgHfnJgW6tWjUQUcA"
st.title("Digital Fashion Designer AI")
description = st.text_input("Desribe your Fashion Design : ")

if st.button("Generate Design"):
    if description:
        with st.spinner("Generating Design . . ."):
            try:
                response=openai.Image.create(
                    prompt=description,n=1,size="1024x1024"
                )
                image_url=response['data'][0]['url']
                st.image(image_url,caption="Generated Fashion Desgn",use_column_width=True)
            except Exception as e:
                st.error(f"An Error Occured : {e}")
    else:
        st.warning("Please enter a description to generate a design")