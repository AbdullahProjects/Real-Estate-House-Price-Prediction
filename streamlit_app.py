import streamlit as st
import pandas as pd
import pickle as pk
# import base64

# Load the background image
# image = Image.open("image.jpg")

# Convert the image to base64
# encoded_image = base64.b64encode(image.tobytes()).decode("utf-8")

# Set the background image
# st.markdown(
    # f'<style>body {{background-image: url(data:image/jpg;base64,{encoded_image})}}</style>'
# )

# Load the dataset and pre-trained model
dataset = pk.load(open("dataset.pkl","rb"))
pipeline = pk.load(open("pipeline.pkl","rb"))

# Set the title and background of the web app
st.set_page_config(
    page_title="Real Estate House Price Prediction",
    page_icon="🏠"
    # layout="wide",
    # initial_sidebar_state="expanded",
)

# bg_image_url = "https://images.unsplash.com/photo-1568242629525-62b0c3d77fb7?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
# Add background image
# st.markdown(
#     """
#     <style>
#         [data-testid="stAppViewContainer"] {
#             background-image: url('data:image/jpg;base64,{img}');
#             background-size: cover;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# set title and header for web app
st.title("Real State House Price Prediction")
st.header("User Input Features")

# Area type
area_type = st.selectbox("Select Area Type:", dataset["area_type"].unique())
# Location
location = st.selectbox("Location:", dataset["location"].unique())
# Number of Bedrooms
size = st.number_input("Number of Bedrooms BHK (0-30):", step=1, min_value=1, max_value=30)
# Number of Bathrooms
bath = st.number_input("Number of Bathrooms (0-25):", step=1, min_value=1, max_value=25)
# Number of Balconies
balcony = st.number_input("Number of Balconies(0-5):", step=1, min_value=1, max_value=5)
# Area in Square Feet
sqft = st.number_input("Enter area in Square feet(0-35,000):", step=1, min_value=100, max_value=35000)


# Prediction Button
if st.button("Predict Price"):

    # Create a dataframe with user input for prediction
    user_input = pd.DataFrame({
        "area_type":[area_type],
        "location":[location],
        "size":[size],
        "total_sqft":[sqft],
        "bath":[bath],
        "balcony":[balcony]})
    
    # Make prediction using the pre-trained model
    predicted_price = pipeline.predict(user_input)

    # Displaying the predicted price
    st.subheader(f"Predicted Price: {int(predicted_price)} $")