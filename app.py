from flask import Flask, request, jsonify
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle

app = Flask(__name__)

labels = ["anxiety", "depression", "stress"]

# Load the tokenizer and model from local storage
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = keras.models.load_model('model.h5')

def prepare_input(text):
    sequences = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequences, maxlen=250, truncating='post', padding='post')

    return padded

def get_prediction(text):
    # Prepare the input text
    input_text = prepare_input(text)

    # Use the model to perform predictions
    predictions = model.predict(input_text)

    # Find the index of the class with the highest probability
    prediction_index = np.argmax(predictions, axis=1)[0]

     # Create the result dictionary
    result = {
        'text': text,
        'predictions': [
            {'class': labels[j], 'probability': float(predictions[0][j]) * 100}  # Multiply by 100 for percentage
            for j in range(len(predictions[0]))
        ],
        'predicted_class': labels[prediction_index],
        'predicted_probability': float(predictions[0][prediction_index] * 100)
    }
    
    return result

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input text from the request data
    data = request.get_json()
    text = data['text']

    # Perform predictions using the input text
    prediction = get_prediction(text)

    # Return the prediction as a JSON response
    response = {
        'prediction': prediction
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
