import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    # check that recognizer and microphone are appropriate SpeechRecognition instances
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("recognizer must be a SpeechRecognition Recognizer instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("microphone must be a SpeechRecognition Microphone instance")

    # adjust for ambient noise and record audio from microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    # initialise response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing speech from mic recording
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech unintelligible
        response["error"] = "Unable to recognize speech"

    return response

if __name__ == "__main__":
    # create recognizer and microphone instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    speech = recognize_speech_from_mic(recognizer, microphone)

    # if there was an error print error message
    if speech["error"]:
        print("ERROR: {}".format(speech["error"]))
    else:
        print("You said: {}".format(speech["transcription"]))