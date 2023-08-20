import streamlit as st
import subprocess
import sys
st.set_page_config(page_title="ecoChoice", page_icon="ecoChoice.png", layout="wide", initial_sidebar_state="auto")
logo_image = "ecoChoice.png"

st.image(logo_image, width=100)
st.title("ecoChoice -  An Intelligent Recommendation system")

hide_streamlit_style = """
<style>
footer {visibility: hidden;}
</style>
"""
tabs = st.tabs(["Overview","Statistics"])
st.markdown("",unsafe_allow_html=False)
tab_ove=tabs[0]
tab_dyn=tabs[1]

with tab_ove:
    m1,m2=st.columns(2)
    with m1:
        st.header("Why ecoChoice?")
        st.write("""EcoChoice is an advanced recommendation system designed to assist individuals in making eco-friendly and sustainable choices in their daily lives. By leveraging cutting-edge technologies such as machine learning and data analysis, EcoChoice offers personalized recommendations that align with environmental values and goals.""")
        st.header("Model-based collaborative filtering")
        st.write("""A subfield of recommendation systems that focuses on creating predictive models to make recommendations. It addresses the limitations of traditional collaborative filtering methods, such as user-based and item-based approaches, by using sophisticated algorithms to uncover latent factors and patterns in the data. """)



# Add widgets for user input
user_input = st.text_input("Enter user id:")


#API call to retreive the first product id from purchase index
import requests

# URL of the API
url = "https://flipkart-grid-kw57.onrender.com/high_rating"

# Parameters to include in the GET request
params = {
    "user_id": user_input
    
}

# Make the GET request with parameters




#
# Display the result of your model based on user input
loading_placeholder = st.empty()
import json

# Load data from the JSON file


if st.button("Suggest Items"):
    c=0
    while(c<1):
        response = requests.get(url, params=params)
        print(response)
        first_product_id = None

        
        if response.status_code == 200:
            data = response.json()
            first_product_id=data['product_id']
        

        else:
            st.write(f"Past products are not detected: {response.status_code}, May be a new user!")
        c+=1


    with st.spinner('Wait for it...'):
        try:
            # Replace 'another_notebook.py' with the actual name of your converted notebook script
            cmd = [sys.executable, 'rum_mode.py', first_product_id]
            output = subprocess.check_output(cmd, universal_newlines=True)
            output_list = output.strip().split('\n')
            
            # Display the output list in Streamlit UI
            st.write("Suggested product Id List:")
            for item in output_list:
                st.write(item)
            with open('merged.json', 'r') as f:
                data = json.load(f)

            # Search and retrieve matching entries

            matching_entries = []
            matching_entries = [entry for entry in data if any(term in entry["asin"] for term in output_list)]



            # Print the matching entries
            for entry in matching_entries:
                st.write(entry)
                
        except subprocess.CalledProcessError as e:
            st.error("An error occurred while running the notebook.")
    st.success('Done!')