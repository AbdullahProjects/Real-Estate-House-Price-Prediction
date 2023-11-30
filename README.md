# 🔥Real Estate House Price Prediction

Welcome to the **Real Estate House Price Prediction** project! This project is designed to predict price of a house based on user preferences. It utilizes datasets from Kaggle, specifically the **Real Estate House Prices Dataset** available in the repository.

## Live Demo

Check out the live demo [here](https://akk-real-estate-house-price-prediction.streamlit.app/).

## Project Development Steps

1. **Download Dataset from Kaggle:** Obtain the necessary datasets for movies and Indian foods.
2. **Preprocessing:** Clean the datasets by handling null values, removing duplicates, unnecessary features, and overall data cleaning.
3. **EDA:** Perform Exploratory Data Analysis to check outliers and data distribution.
4. **Pipeline:** Applying ColumnTransformers to handle Categorical Features and Scaling the Features. And then make Pipeline of all transformers.
5. **Model Building:** Try different regression algorithms such as LinearRegression, DecisionTreeRegressor, RandomForestRegressor, KNearestNeighbors and SupportVectorRegressor.
6. **Selecting Best Algorithm:** I found best algorithm from previous ones which is RandomForestRegressor.
7. **Model Deployment:** Import the Pipeline and Dataset in Binary format using Pickle. And then, Build streamlit app using these Binary Files.

## Learning Outcomes

1. **Problem-Solving:** Overcome challenges, errors, and difficulties encountered during the project.
2. **Logic-Building**: I apply different functions and techniques to remove outliers.
3. **Model Deployment:** Successfully deploy the Real Estate Price Predictor Model in a Streamlit app.

## How to Run on Your Machine

1. **Clone the Repository:** Download all files and folders from this repository.
2. **Create Virtual Environment:**
   ```bash
   py -3 -m venv virtualEnv
3. **Run this command:**
   ```bash
   pip freeze > requirements.txt
4. **Finally start the streamlit app:**
   ```bash
   streamlit run streamlit_app.py
