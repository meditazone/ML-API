# MACHINE LEARNING API-MODEL

## Description
This API leverages Flask a Python web framework, to predict text-based mental wellbeing. The system categoriez mental health into three main categories: Anxiety, Depression, and Stress

## How To Use This API-Model
If you want to run this API Server on your local machine, you need to do this steps:
- First, clone this repository using this command: `git clone https://github.com/meditazone/ML-API.git`.
- Second, open your terminal and go to your project's root directory.
- Third, type `pip install -r requirements.txt` on your terminal and hit `Enter`.
- Fourth, type `python app.py` on your terminal and hit `Enter`.
- Finally, you can run the server using postman or run on your web: `http://localhost:8080`

## API Endpoint
If you want to access our Machine Learning API endpoints, you must have already cloned this repository and completed the previous steps. If you have, you can see several Machine Learning API endpoints below and implement them. Here are the API endpoints along with their descriptions:

| Endpoint | Method | Description |
| ----- | ----- | ----- |
| / | GET | This endpoint have a function for checking if the response is success |
| /predict  | POST   | Predict if a user has some emotion based on emotion detection data |

## Example 
1.  Request for Emotion Detection using endpoint `/predict`
     ```js
     http://localhost:8080/predict
     ```
2.  Example of Text testing
    ```json
    {
    "text": "Saya tidak meminta untuk berada di sini. Saya tidak meminta untuk dilahirkan. Saya tidak datang ke dalam hidup ini dengan sukarela. Setidaknya seperti itulah rasanya. Saya diberitahu untuk menyesuaikan diri dengan masyarakat yang tidak memiliki tempat bagi saya, juga tidak menginginkan saya. Mengapa saya harus mendapatkan pekerjaan dan membayar pajak dan tagihan bodoh? Saya tidak mendaftar untuk ini."
    }
     ```
3.  Response for endpoint `/predict`
    ```json
    {
    "predicted_class": "depression",
    "predictions": [
        {
            "class": "anxiety",
            "probability": 0.007700295653194189
        },
        {
            "class": "depression",
            "probability": 0.90477454662323
        },
        {
            "class": "stress",
            "probability": 0.08752521127462387
        }
    ],
    "text": "Saya tidak meminta untuk berada di sini. Saya tidak meminta untuk dilahirkan. Saya tidak datang ke dalam hidup ini dengan sukarela. Setidaknya seperti itulah rasanya. Saya diberitahu untuk menyesuaikan diri dengan masyarakat yang tidak memiliki tempat bagi saya, juga tidak menginginkan saya. Mengapa saya harus mendapatkan pekerjaan dan membayar pajak dan tagihan bodoh? Saya tidak mendaftar untuk ini. "
    }
    ```
