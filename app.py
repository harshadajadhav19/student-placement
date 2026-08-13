import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Placement Package Prediction")

cgpa = st.number_input("CGPA", 0.0, 10.0, 7.0)
aptitude = st.number_input("Aptitude Score", 0, 100, 70)
communication = st.number_input("Communication Score", 0, 100, 70)
projects = st.number_input("Projects", 0, 10, 2)
internships = st.number_input("Internships", 0, 10, 1)
certifications = st.number_input("Certifications", 0, 20, 2)
technical = st.number_input("Technical Skill Score", 0, 100, 70)

if st.button("Predict Package"):
    input_df = pd.DataFrame([[cgpa, aptitude, communication,
                              projects, internships,
                              certifications, technical]],
                            columns=[
                                'cgpa',
                                'aptitudescore',
                                'communicationscore',
                                'projects',
                                'internships',
                                'certifications',
                                'technicalskillscore'
                            ])

    prediction = model.predict(input_df)

    st.success(f"Predicted Package: {prediction[0]:.2f} LPA")
