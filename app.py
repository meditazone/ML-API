from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences
from flask_cors import CORS
import numpy as np
import pickle
import logging
import os

app = Flask(__name__)
CORS(app)

# Load model di awal aplikasi
app.config['MODEL_PATH'] = os.environ.get('MODEL_PATH', 'model.h5')
model = load_model(app.config['MODEL_PATH'])

# Tambahkan layer softmax
num_classes = 3  # Sesuaikan dengan jumlah kelas Anda
model.add(Dense(num_classes, activation='softmax', name='output'))

# Load the saved Tokenizer
app.config['TOKENIZER_PATH'] = os.environ.get('TOKENIZER_PATH', 'tokenizer.pkl')
with open(app.config['TOKENIZER_PATH'], 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Validasi input
        data = request.get_json(force=True)
        if 'text' not in data or not isinstance(data['text'], str):
            return jsonify({'error': "'text' key not found or not a valid string in data"})
        user_text = data['text']

        # Load the saved Tokenizer
        with open(app.config['TOKENIZER_PATH'], 'rb') as tokenizer_file:
            tokenizer = pickle.load(tokenizer_file)

        # Pre-process the input data
        sequences = tokenizer.texts_to_sequences([user_text])
        padded_data = pad_sequences(sequences, maxlen=250, padding='post', truncating='post')

        # Make predictions using the loaded model
        predictions = model.predict(padded_data)

        # Define labels here
        labels = ["Anxiety", "Depression", "Stress"]

        # Process predictions and return the results
        results = []
        result = {
            'text': user_text,
            'predictions': [
                {
                    'class': labels[j], 'probability': float(predictions[0][j])
                }
                for j in range(len(predictions[0]))
            ],
            'predicted_class': labels[np.argmax(predictions[0])]
        }
        results.append(result)

        # Log request and response
        logging.info('Received request: %s', data)
        logging.info('Sending response: %s', jsonify(results).json)

        return jsonify(results)

    except Exception as e:
        logging.error('Error: %s', str(e))
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
