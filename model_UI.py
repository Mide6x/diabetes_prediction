import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler #for data standardization

#loading our model
loaded_model = pickle.load(open('diabetes_pred_model.sav', 'rb'))

#for scaling our data
scaler = StandardScaler()

#creating a function to initialize our prediction
def db_prediction(input_data):


    #changing the input data into a numpy array
    diagnosis_numpy = np.asarray(input_data)

    #reshapign the array - telling the model that we only need the prediction for one data
    reshaped_diagnosis = diagnosis_numpy.reshape(1, -1)

    #standardize the data
    standardized_reshaped_data = scaler.fit_transform(reshaped_diagnosis)

    #predicting
    prediction = loaded_model.predict(standardized_reshaped_data)

    if prediction == 0:
        return'This user is non-Diabetic'
    elif prediction == 1:
        return'This patient is diabetic'
    
def main():

    st.title('Diabetes Prediction app')

    #get input data from user
    preg = st.number_input("How many times have the patient's being pregnant?", min_value=0, value=0, max_value=20, step=1)
    g_lvl = st.number_input("What is the patient's Glucose Level?", min_value=0, value=0, max_value=230, step=1)
    bp = st.number_input("What is the patient's Blood Pressure?", min_value=0, value=0, max_value=150, step=1)
    skt = st.number_input('How thick is the skin of the patient?', min_value=0, value=0, max_value=120, step=1)
    inl = st.number_input("What is the patient's insulin level?", min_value=0, value=0, max_value=910, step=1)
    bmi = st.text_input("What is the patient's BMI?")
    dpf = st.text_input("What is the patient's Diabetes Pedigree Function")
    age = st.number_input("How old is the patient?", min_value=0, value=0, max_value=100, step=1)

    #output
    diagnosis = " "

    if st.button("Check Diabetes Status"):
        diagnosis = db_prediction([preg, g_lvl, bp, skt, inl, bmi, dpf, age])

    st.success(diagnosis)


if __name__ == '__main__':
    main()