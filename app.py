from flask import Flask, request, jsonify, render_template
import pickle

# Initialize the Flask app
app = Flask(__name__)

# Load the saved model and vectorizer
with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

with open('spam_classifier_model.pkl', 'rb') as f:
    spam_classifier_model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    # Get the SMS text from the form
    sms_text = request.form.get('sms_text')

    if not sms_text.strip():
        return jsonify({'is_spam': False, 'message': 'Please enter a valid SMS text.'})

    # Transform the input text using the vectorizer
    input_tfidf = tfidf_vectorizer.transform([sms_text])

    # Predict using the model
    prediction = spam_classifier_model.predict(input_tfidf)[0]

    # Prepare the response message
    if prediction == 1:
        return jsonify({'is_spam': True, 'message': 'This message is classified as SPAM.'})
    else:
        return jsonify({'is_spam': False, 'message': 'This message is classified as HAM (not spam).'})

if __name__ == '__main__':
    app.run(debug=True)
