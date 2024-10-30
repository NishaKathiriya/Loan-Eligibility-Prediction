# Loan Eligibility Prediction

This project is a **Loan Eligibility Prediction** web application built with **Streamlit**. It predicts loan eligibility based on user inputs such as income, loan amount, credit history, and other factors. The application uses a **Machine Learning model** trained on relevant data to classify applicants as eligible or not eligible for a loan.

## Features

- **User-Friendly Interface**: Simple and intuitive interface for entering input data.
- **Real-Time Predictions**: Instantly predicts loan eligibility based on user input.
- **Probability Output**: Displays the prediction probability to indicate model confidence.
- **Data Preprocessing**: Includes one-hot encoding for categorical variables and scaling for numerical features.

## Installation

To run the application, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/NishaKathiriya/loan-eligibility-prediction.git
   cd loan-eligibility-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the app and enter the required information in the provided fields, such as **income**, **loan amount**, **credit history**, etc.
2. Click on the **Predict** button to see the loan eligibility status.
3. View the prediction result and probability score displayed by the app.

## Model and Data

The machine learning model used for predictions is a **Random Forest Classifier**. Data preprocessing includes one-hot encoding for categorical features and scaling for numerical features. The model was trained using historical data on loan applications, considering key financial and personal factors influencing loan eligibility.

## Requirements

- Python 3.7+
- Streamlit
- Scikit-learn
- Pandas
- Numpy

Refer to `requirements.txt` for exact package versions.

## Future Enhancements

- **Expanded Feature Set**: Include additional financial factors to improve prediction accuracy.
- **Model Tuning**: Experiment with other algorithms or hyperparameter tuning for better performance.
- **Deployment**: Deploy the app on cloud platforms like Streamlit Cloud, Heroku, or AWS for easy access.

## Project Link

You can access the live version of the Loan Eligibility Prediction web app at the following link:

[Loan Eligibility Prediction App](https://loaneligibility-prediction.streamlit.app/)

