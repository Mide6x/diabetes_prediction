# Diabetes Prediction Web App
Predicting Diabetes is not particularly a new innovation, but being able to classify who - with a ML algorithm - could be a new thing.

# About Dataset
The dataset used in building this model is the PIMA Indian Dataset

## Context
This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.

## Content
The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.

## Acknowledgements
Smith, J.W., Everhart, J.E., Dickson, W.C., Knowler, W.C., & Johannes, R.S. (1988). Using the ADAP learning algorithm to forecast the onset of diabetes mellitus. In Proceedings of the Symposium on Computer Applications and Medical Care (pp. 261--265). IEEE Computer Society Press.

## Inspiration
Can you build a machine learning model to accurately predict whether or not the patients in the dataset have diabetes or not?

## License
CC0: Public Domain

## Expected update frequency
Not specified

link to: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

# About App
This web app built with python and hosted on streamlit uses a Support Vector Machine(SVM) to predict an 'Outcome'. The data has been preprocessed and has been further standardized using StandardScaler library.

# Prediction Variables
Prediction variables includes the number of pregnancies the patient has had (int), their Glucose level(int), their Blood Pressure(int), skin thickness(int), their BMI(float), insulin level(int), Diabetes Pedigree Function(float), and Age(int).

# Dependencies
--> streamlit
--> pandas
--> numpy
--> scikit-learn

# Link to test the deployed App
https://mide6x-diabetes-prediction-model-ui-lnucdd.streamlit.app/