import numpy as np
import pickle
import streamlit as st
import pandas as pd
from datetime import date

# loading the saved model
loaded_model = pickle.load(open('Project_UAE.sav', 'rb'))

# Function for Prediction
def Rent_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction

# Main function
def main():
    st.set_page_config(page_title="UAE Real Estate Rent Prediction", layout="wide", initial_sidebar_state="expanded")
    
    st.markdown("""
        <style>
            body {
                background-color: #f5f5f5;
                color: #333;
            }
            .main-title {
                background-color: #ff6347;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                margin-bottom: 20px;
            }
            .main-title h1, .main-title h2 {
                color: white;
                margin: 0;
            }
            .sidebar .sidebar-content {
                padding: 20px;
            }
            .input-container {
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }
            .stButton button {
                background-color: #ff6347;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 20px;
                cursor: pointer;
            }
            .stButton button:hover {
                background-color: #ff4500;
            }
        </style>
    """, unsafe_allow_html=True)

    # Main Title
    st.markdown('<div class="main-title"><h1>Department of Computer Science, BHU</h1></div>', unsafe_allow_html=True)
    
    # Image
    st.image("C:/Users/BIJAY KUMAR GUPTA/1.jpeg")
    
    # Subheading
    st.markdown('<div class="main-title"><h2>Streamlit UAE Real Estate Rent Prediction Web App</h2></div>', unsafe_allow_html=True)

    # Description
    st.markdown("""
        <div class="input-container">
            <p>This Webapp is to predict the rent of the property across various cities of UAE which are Abu Dhabi, Dubai, Sharjah, Ajman, Ras Al Khaimah, Umm Al Quwain, and Al Ain.</p>
        </div>
    """, unsafe_allow_html=True)

    # Sidebar for user inputs
    with st.sidebar:
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        City = st.selectbox('Select city', ['Dubai', 'Abu Dhabi', 'Sharjah', 'Ajman', 'Al Ain', 'Ras Al Khaimah', 'Umm Al Quwain', 'Fujairah'])
        City_features = {
            'City_Ajman': 0,
            'City_Al_Ain': 0,
            'City_Dubai': 0,
            'City_Fujairah': 0,
            'City_Ras_Al_Khaimah': 0,
            'City_Sharjah': 0,
            'City_Umm_Al_Quwain': 0
        }
        City_features[f'City_{City.replace(" ", "_")}'] = 1

        Type = st.radio('Property Type:', ['Apartment', 'Villa', 'Townhouse', 'Hotel Apartment', 'Penthouse', 'Villa Compound', 'Residential Building', 'Residential Floor', 'Residential Plot'])
        Type_map = {
            'Apartment': 0,
            'Villa': 7,
            'Townhouse': 6,
            'Hotel Apartment': 1,
            'Penthouse': 2,
            'Villa Compound': 1,
            'Residential Building': 3,
            'Residential Floor': 4,
            'Residential Plot': 5
        }
        Type = Type_map[Type]
        
        Rent_category = st.radio('Rent Category:', ['Medium', 'High', 'Low'])
        Rent_category_map = {'Medium': 1, 'High': 2, 'Low': 0}
        Rent_category = Rent_category_map[Rent_category]
        
        Beds = st.text_input('Number of Beds')
        Baths = st.text_input('Number of Baths')
        Area_in_sqft = st.text_input('Area in Sqft')
        Rent_per_sqft = st.text_input('Rent per Sqft')

        Furnishing = st.radio('Furnishing:', ['Unfurnished', 'furnished'])
        Furnishing_map = {'Unfurnished': 0, 'furnished': 1}
        Furnishing = Furnishing_map[Furnishing]
        
        Posted_Date = st.date_input('Posted Date')
        Posted_day = Posted_Date.day
        Posted_month = Posted_Date.month
        Posted_year = Posted_Date.year
        end_date = date(2024, 4, 21)
        Age_of_listing_in_days = (end_date - Posted_Date).days
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Prediction
    if st.button('Predict Rent'):
        input_data = [
            Beds, Baths, Type, Area_in_sqft, Rent_per_sqft, Rent_category, Furnishing, Age_of_listing_in_days, 
            Posted_day, Posted_month, Posted_year, City_features['City_Ajman'], City_features['City_Al_Ain'],
            City_features['City_Dubai'], City_features['City_Fujairah'], City_features['City_Ras_Al_Khaimah'], 
            City_features['City_Sharjah'], City_features['City_Umm_Al_Quwain']
        ]
        Prediction = Rent_prediction(input_data)
        st.success(f'The predicted rent is: {Prediction[0]}')

if __name__ == '__main__':
    main()
