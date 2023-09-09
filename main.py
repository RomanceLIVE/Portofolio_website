import streamlit as st

st.set_page_config(layout="wide")
#we make page wider for content

col1, col2 = st.columns(2)
# we return 2 column objects



with col1:
    st.image("images/profilepic.png")
#adds pic to column

with col2:
    st.title("Robert Horvat")
    content = """
    I am passionate about technology and aviation. These two fields are constantly evolving, and I have always enjoyed learning about the latest innovations. I believe that technology and aviation are closely connected, and I am excited to see how they will continue to develop in the future.   
    """
    st.info(content)
    # we repalce st.write(content) with st.info(content)