import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('models/diabetes_model.sav','rb'))
heart_model = pickle.load(open('models/heart_model.sav','rb'))
parkinson_model = pickle.load(open('models/parkinson_model.sav','rb'))

with st.sidebar:
    selected = option_menu('Multi Prediction in ML',['Diabetes','Heart','Parkinson'],icons=['activity','heart','person'],default_index=0)


if selected == 'Diabetes':
    st.title('Diabetes prediction')

    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies = st.number_input('No. of Pregnancies')
        Glucose = st.number_input('Glucose level')
        BloodPressure = st.number_input('BloodPressure level')
    with col2:
        SkinThickness = st.number_input('Skin Thickness')
        Insulin = st.number_input('Insulin level')
        BMI = st.number_input('BMI')
    with col3:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function')
        Age = st.number_input('Age')

    diabetes_diagnosis=''
    if st.button('predict'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if diabetes_prediction[0]==0:
            diabetes_diagnosis = 'Not diabetes'
        else:
            diabetes_diagnosis='diabetes'

    st.success(diabetes_diagnosis)
if selected == 'Heart':
    st.title('Heart Disease prediction')

    #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
    col1,col2,col3=st.columns(3)
    with col1:
        age = st.number_input('age')
        sex = st.number_input('sex')
        cp = st.number_input('cp')
        trestbps = st.number_input('trestbps')
    with col2:
        chol = st.number_input('chol')
        fbs = st.number_input('fbs')
        restecg = st.number_input('restecg')
        thalach = st.number_input('thalach')
    with col3:
        exang=st.number_input('exang')
        oldpeak=st.number_input('oldpeak')
        slope=st.number_input('slope')
        ca=st.number_input('ca')
        thal=st.number_input('thal')

    heart_diagnosis=''
    if st.button('predict'):
        heart_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if heart_prediction[0]==0:
            heart_diagnosis = 'good heart'
        else:
            heart_diagnosis='bad heart'

    st.success(heart_diagnosis)
if selected == 'Parkinson':
    st.title('Parkinson prediction')

    
    col1,col2,col3=st.columns(3)
    with col1:
        MDVP_Fo = st.number_input('MDVP:Fo(Hz)',format="%.5f")
        MDVP_Fhi = st.number_input('MDVP:Fhi(Hz)',format="%.5f")
        MDVP_Flo = st.number_input('MDVP:Flo(Hz)',format="%.5f")
        MDVP_Jitter = st.number_input('MDVP:Jitter(%)',format="%.5f")
        MDVP_Jitter_Abs = st.number_input('MDVP:Jitter(Abs)',format="%.5f")
        MDVP_RAP = st.number_input('MDVP:RAP',format="%.5f")
        MDVP_PPQ = st.number_input('MDVP:PPQ',format="%.5f")
    with col2:
        Jitter_DDP = st.number_input('Jitter:DDP',format="%.5f")
        MDVP_Shimmer=st.number_input('MDVP:Shimmer',format="%.5f")
        MDVP_Shimmer_db=st.number_input('MDVP:Shimmer(dB)',format="%.5f")
        Shimmer_APQ3=st.number_input('Shimmer:APQ3',format="%.5f")
        Shimmer_APQ5=st.number_input('Shimmer:APQ5',format="%.5f")
        MDVP_APQ=st.number_input('MDVP:APQ',format="%.5f")
        Shimmer_DDA=st.number_input('Shimmer:DDA',format="%.5f")
    with col3:
        NHR=st.number_input('NHR',format="%.5f")
        HNR=st.number_input('HNR',format="%.5f")
        RPDE=st.number_input('RPDE',format="%.5f")
        DFA=st.number_input('DFA',format="%.5f")
        spread1=st.number_input('spread1',format="%.5f")
        spread2=st.number_input('spread2',format="%.5f")
        D2=st.number_input('D2',format="%.5f")
        PPE=st.number_input('PPE',format="%.5f")

    parkinson_diagnosis=''
    if st.button('predict'):
        parkinson_prediction = parkinson_model.predict([[MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_Jitter,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_db,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if parkinson_prediction[0]==0:
            parkinson_diagnosis = 'good heart'
        else:
            parkinson_diagnosis='bad heart'

    st.success(parkinson_diagnosis)







    
