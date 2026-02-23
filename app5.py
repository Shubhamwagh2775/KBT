import streamlit as st

st.title("Welcome to basic streamlit app")

age = st.slider("Select your age", 1, 100)
city = st.selectbox("Select your city", ["Delhi", "Mumbai", "Nashik", "Pune"])

if st.button("Show Details"):
    st.write("Age:", age)
    st.write("City:", city)

st.markdown("""
<style>
.stButton > button {
    background-color: orange;
    color: blue;
    border-radius: 50%;
    
}
</style>
""", unsafe_allow_html=True)