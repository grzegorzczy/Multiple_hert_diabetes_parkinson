# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:30:08 2026

@author: Grzesiek
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved model

diabetes_model = pickle.load(open('trained_model.sav', 'rb'))
heart_disease_model = pickle.load(open('trained_heart_disease_model.sav', 'rb'))
parkinson_model = pickle.load(open('trained_parkinson_model.sav', 'rb'))

# sidebar for navigare

with st.sidebar:
    
    selected = option_menu('Multiple Disease Predition System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Disease Prediction'],
                           icons = ['activity','heart', 'person'], #ikony dla tych zakłądek
                           default_index = 0) # to jest w którym miejscu, na ktorym modelu otwiera nam się strona

# Diabetes Prediction Page

if (selected == 'Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction usnig ML')
    
    # getting th einput data from user
    # columns for input fields
    
    col1, col2, col3 = st.columns(3)  #ustawienie w 3 kolumnach danych
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin value')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    diab_diagnosis =' '
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age ]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The Person is Diabetic'
        else:
            diab_diagnosis = 'The Person is Not Diabetic'
        
    st.success(diab_diagnosis)
    
    
    
if (selected == 'Heart Disease Prediction'):
    #pae title
    st.title('Hert Disease Predcition using ML')
    
    # getting th einput data from user
    # columns for input fields
    
    col1, col2, col3 = st.columns(3)  #ustawienie w 3 kolumnach danych
    
    with col1:
        Age = st.text_input('Age')
    with col2:
        Sex = st.text_input('Sex')
    with col3:
        Cp = st.text_input('Chest pain types')
    with col1:
        trestbps = st.text_input('Resting Blood pressure')
    with col2:
        chol = st.text_input('Serum cholestoral in mg/dl')
    with col3:
        FBS = st.text_input('Fasting Blood Sugar > 120mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardigraphic result')
    with col2:
        thalach = st.text_input('Maxium Heart Rate achieved')
    with col3:
        Exang = st.text_input('Exercise induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        Ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        Thal = st.text_input('thal 0=normal;1=fixed defect;2=reversable defect')
    
    
    heart_diagnosis =' '
    
    if st.button('Heart Diabetes Test Result'):
        heart_prediction = heart_disease_model.predict([[Age, Sex, Cp, trestbps, chol, FBS, restecg, thalach, Exang, oldpeak, slope, Ca, Thal]])
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The Person has Heart Disease'
        else:
            heart_diagnosis = 'The Person has Heart Disease'
        
    st.success(heart_diagnosis)
    
    
    
if (selected == 'Parkinson Disease Prediction'):
    #page title
    st.title("Parkinson Disease Prediction using ML")
    
    # getting th einput data from user
    # columns for input fields
    
    col1, col2, col3, col4, col5 = st.columns(5)  #ustawienie w 3 kolumnach danych
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col4:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        MDVP_Shimmer_Db = st.text_input('MDVP:Shimmer(Db)')
    with col1:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        Shimmer_APQ5 = st.text_input('Shimmer:APG5')
    with col3:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col4:
        SHimmer_DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('Spread1')
    with col5:
        spread2 = st.text_input('Spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')
    
    parkinson_diagnosis =' '
    
    if st.button('Parkinson Test Result'):
        parkinson_prediction = parkinson_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, Jitter_DDP,
                                                   MDVP_Shimmer, MDVP_Shimmer_Db, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, SHimmer_DDA, NHR, HNR,
                                                   RPDE, DFA, spread1, spread2, D2, PPE]])
        
        if (parkinson_prediction[0] == 1):
            parkinson_diagnosis = 'The Person is Diabetic'
        else:
            parkinson_diagnosis = 'The Person is Not Diabetic'
        
    st.success(parkinson_diagnosis)

