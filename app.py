import streamlit as st

st.set_page_config(page_title="Alme.ai", page_icon=":beers:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Alme.ai :brain:")
    st.title("A Danish team of ai enthusiasts!")
    st.text("We are a team of 2 people who are passionate about ai and currently studying it-architecture at Aarhus Business Academy")
    st.markdown("##")
    st.button("Contact us")

# ---- MAIN SECTION (SERVICES) ----
with st.container():
    st.markdown("##")
    st.header("Services")
    st.markdown("##")
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader("Chatbot Development")
        st.text("We offer a wide range of services")

    with middle_column:
        st.subheader("Business Process Automation")
        st.text("We offer a wide range of services")

    with right_column:
        st.subheader("Enterprise Consulting")
        st.text("We offer a wide range of services")

    st.markdown("##")
