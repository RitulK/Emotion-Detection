"""
Emotion Detector Server Module

This module provides a Flask web application for analyzing emotions in given text
using the emotion_detector function from the EmotionDetection package.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():

    """
    Analyzes the given text to determine the emotions expressed in it.

    This function retrieves the text to analyze from the request arguments,
    processes it through the emotion_detector function, and returns the
    emotion scores along with the dominant emotion.

    Returns:
        str: A formatted string summarizing the emotion analysis or an error
             message if the dominant emotion is None.
    """

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the individual emotion scores and the dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # **Modified section for error handling**
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the emotion scores and dominant emotion
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():

    """
    Renders the index page of the emotion detector application.

    This function serves the HTML template for the index page where users can
    input their text for emotion analysis.

    Returns:
        str: The rendered HTML template for the index page.
    """

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
