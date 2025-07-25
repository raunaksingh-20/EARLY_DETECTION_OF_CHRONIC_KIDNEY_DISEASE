# Chronic Kidney Disease (CKD) Prediction

## Description

This project is a web application that predicts the likelihood of a patient having Chronic Kidney Disease (CKD) based on their health metrics. It uses a logistic regression model trained on a standard dataset to provide a binary classification (CKD or Normal).

The application is built with Flask and allows users to input their medical information through a simple web form to get an instant prediction.

## Dataset

The model was trained on the **Chronic Kidney Disease Dataset** from Kaggle. This dataset contains 400 instances with 25 attributes related to various blood and urine tests.

  - **Source:** [Chronic Kidney Disease Dataset](https://www.kaggle.com/datasets/mansoordaku/ckdisease)

## Features Used

The model uses the following 8 features for prediction:

1.  Red Blood Cells (Normal/Abnormal)
2.  Pus Cell (Normal/Abnormal)
3.  Blood Glucose Random (in mg/dL)
4.  Blood Urea (in mgs/dL)
5.  Pedal Edema (Yes/No)
6.  Anemia (Yes/No)
7.  Diabetes Mellitus (Yes/No)
8.  Coronary Artery Disease (Yes/No)

## Technology Stack

  - **Backend:** Python, Flask
  - **Machine Learning:** Scikit-learn
  - **Data Handling:** Pandas, NumPy
  - **Development Environment:** Jupyter Notebook

## File Structure

```
.
├── app.py                  # Main Flask application
├── ckd_final.ipynb         # Jupyter Notebook for model training
├── CKD.pkl                 # Saved logistic regression model file
├── scaler.pkl              # Saved standard scaler file
├── requirements.txt        # Python dependencies
└── templates/
    ├── home.html           # Landing page
    ├── indexview.html      # Prediction form page
    └── result.html         # Prediction result page
```

## Setup and Installation

Follow these steps to set up and run the project locally.

**1. Clone the Repository**

```bash
git clone https://github.com/raunaksingh-20/EARLY_DETECTION_OF_CHRONIC_KIDNEY_DISEASE.git
cd EARLY_DETECTION_OF_CHRONIC_KIDNEY_DISEASE
```

**2. Create a Virtual Environment**

It's recommended to create a virtual environment to manage dependencies.

```bash
# For Mac/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

**3. Create `requirements.txt`**

Create a file named `requirements.txt` and paste the following content into it:

```
Flask==2.2.2
pandas==1.5.2
numpy==1.23.5
scikit-learn==1.2.0
```

**4. Install Dependencies**

Install all the required Python libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

**5. Run the Model Training Notebook (Optional)**

If you wish to see how the model was trained, you can run the `ckd_final.ipynb` notebook using Jupyter. This step is optional as the trained model (`CKD.pkl`) and scaler (`scaler.pkl`) are already provided.

**6. Run the Flask Application**

Execute the `app.py` script to start the local web server.

```bash
python app.py
```

The application will be running at `http://127.0.0.1:5000`.

## How to Use

1.  Open your web browser and navigate to `http://127.0.0.1:5000`.
2.  Click on the "Prediction" button.
3.  Fill out the form with the patient's medical details.
4.  Click "Predict" to submit the form.
5.  The next page will display the prediction result: "Chronic Kidney Disease" or "Normal".
