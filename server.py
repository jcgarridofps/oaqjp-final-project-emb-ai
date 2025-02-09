''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/', methods=['GET'])
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.route("/emotionDetector", methods = ['GET'])
def emotion_detection():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions and its confidence 
        score for the provided text, as well as the dominant emotion found.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    analysis_result = emotion_detector(text_to_analyze)

    if analysis_result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 200

    formatted_result = \
    f"For the given statement, the system response is \
    'anger': {analysis_result['anger']}, \
    'disgust': {analysis_result['disgust']}, \
    'fear': {analysis_result['fear']}, \
    'joy': {analysis_result['joy']}, \
    'sadness': {analysis_result['sadness']}. \
    The dominant emotion is {analysis_result['dominant_emotion']}"

    return formatted_result, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
