from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle

app = Flask(__name__)

# Load the model and tokenizer
model = load_model('model.h5')
with open('tokenizer.pkl', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

# Define labels
labels = ["anxiety", "depression", "stress"]

def predict_emotion(text):
    # Preprocess the input data
    sequences = tokenizer.texts_to_sequences([text])
    padded_data = pad_sequences(sequences, maxlen=250, padding='post', truncating='post')

    # Make predictions using the loaded model
    predictions = model.predict(padded_data)

    # Process predictions and return the results
    result = {
        'text': text,
        'predictions': [
            {'class': labels[j], 'probability': float(predictions[0][j])}
            for j in range(len(predictions[0]))
        ],
        'predicted_class': labels[np.argmax(predictions[0])]
    }

    return result

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Validation input
        data = request.get_json(force=True)
        if 'text' not in data or not isinstance(data['text'], str):
            return jsonify({'error': "'text' key not found or not a valid string in data"})

        user_text = data['text']
        result = predict_emotion(user_text)

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
