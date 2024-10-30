# import requests
# import json

# def emotion_detector(text_to_analyse):
#     # URL of the sentiment analysis service
#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
#     # Constructing the request payload in the expected format
#     myobj = { "raw_document": { "text": text_to_analyse } }
    
#     # Custom header specifying the model ID for the sentiment analysis service
#     header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

#     response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

#     # Parsing the JSON response from the API
#     formatted_response = json.loads(response.text)

#     # Extracting sentiment label and score from the response
#     anger = formatted_response['emotionPredictions']['anger']
#     disgust = formatted_response['emotionPredictions']['disgust']
#     fear = formatted_response['emotionPredictions']['fear']
#     joy = formatted_response['emotionPredictions']['joy']
#     sadness = formatted_response['emotionPredictions']['sadness']

#     return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness}


#this below code works properly
# import requests
# import json

# def emotion_detector(text_to_analyse):
#     # URL of the sentiment analysis service
#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
#     # Constructing the request payload in the expected format
#     myobj = { "raw_document": { "text": text_to_analyse } }
    
#     # Custom header specifying the model ID for the sentiment analysis service
#     header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

#     response = requests.post(url, json=myobj, headers=header)  # Send a POST request to the API with the text and headers

#     # Parsing the JSON response from the API
#     formatted_response = json.loads(response.text)

#     # Ensure 'emotionPredictions' is a list and extract the first element
#     if 'emotionPredictions' in formatted_response and isinstance(formatted_response['emotionPredictions'], list):
#         # Accessing the emotion data within the 'emotion' key
#         emotion_data = formatted_response['emotionPredictions'][0]['emotion']

#         # Extracting emotion scores
#         anger = emotion_data.get('anger', 0)
#         disgust = emotion_data.get('disgust', 0)
#         fear = emotion_data.get('fear', 0)
#         joy = emotion_data.get('joy', 0)
#         sadness = emotion_data.get('sadness', 0)

#         # Finding the dominant emotion
#         emotions = {
#             'anger': anger,
#             'disgust': disgust,
#             'fear': fear,
#             'joy': joy,
#             'sadness': sadness
#         }
#         dominant_emotion = max(emotions, key=emotions.get)  # Find the emotion with the highest score

#         return {
#             'anger': anger,
#             'disgust': disgust,
#             'fear': fear,
#             'joy': joy,
#             'sadness': sadness,
#             'dominant_emotion': dominant_emotion
#         }
#     else:
#         return "Unexpected response format or empty response."




#this below code is updated version of above for incorporating error handling

import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header)

    # Check for status code 400 (blank entries or invalid requests)
    if response.status_code == 400:
        # Return a dictionary with None values for all emotions in case of an error
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Ensure 'emotionPredictions' is a list and extract the first element
    if 'emotionPredictions' in formatted_response and isinstance(formatted_response['emotionPredictions'], list):
        # Accessing the emotion data within the 'emotion' key
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']

        # Extracting emotion scores
        anger = emotion_data.get('anger', 0)
        disgust = emotion_data.get('disgust', 0)
        fear = emotion_data.get('fear', 0)
        joy = emotion_data.get('joy', 0)
        sadness = emotion_data.get('sadness', 0)

        # Finding the dominant emotion
        emotions = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotions, key=emotions.get)  # Find the emotion with the highest score

        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    else:
        return "Unexpected response format or empty response."


