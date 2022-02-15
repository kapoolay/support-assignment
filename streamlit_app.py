import streamlit as st
import wget

st.title("My Streamlit App!")

# Choose/Submit Prompt
with st.form("app_form"):
  status_code = st.radio("Pick a status code", ('101', '102', '405', '406', '407', '416', '417', '500', '502', '521'))

  submitted = st.form_submit_button("Submit")
  if submitted:
    st.write("You pressed submit!")


# Get the response
site_url = f"https://http.cat/{status_code}"

# Display the results
st.header("Results:")
st.image(site_url, caption='Cat')


# Celebrate
st.balloons()
