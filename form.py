import streamlit as st

name = st.text_input("Enter your name: ")
fname = st.text_input("Enter your Father name : ")
adr = st.text_area("Enter your text")
classdata = st.selectbox("Enter your class : ", (1,2,3,4,5))

# creating button
button = st.button("Submit")
if button :
    st.markdown(f"""
    \nName : {name}
    \nFather Name : {fname}
    \nAddress : {adr}
    \nClassData : {classdata}
    """)



# pip freeze > requirements.txt
# ye command requirements.txt file banati hai
