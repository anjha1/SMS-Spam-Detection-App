# SMS Spam Detection App  

An easy-to-use **SMS Spam Detection App** that classifies messages as **Spam** or **Ham (Not Spam)** using machine learning and Natural Language Processing (NLP) techniques.  

## Features  
- **Real-time Spam Classification**: Instantly identify whether an SMS is spam or legitimate.  
- **Pre-trained Machine Learning Model**: Built using TF-IDF vectorization and advanced classification algorithms.  
- **Interactive User Interface**: A user-friendly interface powered by **Flask** or **Streamlit**.  
- **Lightweight and Efficient**: Optimized for fast performance and minimal resource usage.  

---

## Demo  
[Link to the live app here](https://sms-spam-detection-app.onrender.com/)]  

---

## How It Works  
1. **Data Preprocessing**: SMS messages are cleaned, tokenized, and vectorized using **TF-IDF**.  
2. **Model Training**: A supervised machine learning model (e.g., Naive Bayes, Logistic Regression) is trained to classify messages as spam or ham.  
3. **Prediction**: The trained model predicts the class of a new SMS message entered by the user.  

---

## Tech Stack  
- **Programming Language**: Python  
- **Libraries**:  
  - **NLP**: scikit-learn, NLTK  
  - **Data Manipulation**: Pandas, NumPy  
  - **Deployment**: Flask or Streamlit  
- **Model**: Naive Bayes or Logistic Regression  

---

## Installation and Setup  
Follow these steps to run the app locally:  

1. Clone the repository:  
   ```bash
   git clone https://github.com/anjha1/SMS-Spam-Detection-App.git
   cd sms-spam-detection-app
