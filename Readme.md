# API Machine Learning
This API leverages Flask, a Python web framework, to predict text-based mental wellbeing. The system categorizes mental health into three main categories: Anxiety, Depression, and Stress.

## Installation Resources
```
pip install tensorflow flask numpy flask-cors scikit learn
```

## API Documentation
| Method | Endpoint | Description |
|-----|-----|-----|
| POST | /predict | Used to perform predictions from user input in the form of text. |

## Example Using API

```py
1.  Request using POST method
    http://localhost:5000/predict

2.  Body request
    {
      "text": "Saya putus asa karena tidak memiliki ekonomi yang cukup"
    }

3.  Response
    [
        {
            "predicted_class": "Anxiety",
            "predictions": [
            {
                "class": "Anxiety",
                "probability": 0.3584612011909485
            },
            {
                "class": "Depression",
                "probability": 0.30249297618865967
            },
            {
                "class": "Stress",
                "probability": 0.33904582262039185
            }
        ],
        "text": "Saya merasa tanda - tanda kecemasan ketika berada di   tempat keramaian"
      }
    ]
```

## Python script for a Flask application
1. Flask Application Setup 
    ```py 
    ## The script creates a Flask web application instance.
    app = Flask(__name__)
    CORS(app)
    ```
2. Model Loading
    ```py
    ## The pre-trained machine learning model is loaded at the beginning of the application.
    app.config['MODEL_PATH'] = os.environ.get('MODEL_PATH', 'model.h5')
    model = load_model(app.config['MODEL_PATH'])
    ```
3. Model Modification
    ```Py
    ## A softmax layer is added to the loaded model.
    num_classes = 3
    model.add(Dense(num_classes, activation='softmax', name='output'))
    ```
