import speech_recognition as sr

def recognise_speech_from_mic(recogniser, microphone):
    # check that recogniser and microphone are appropriate SpeechRecognition instances
    if not isinstance(recogniser, sr.Recogniser):
        raise TypeError("recogniser must be a SpeechRecognition Recogniser instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("microphone must be a SpeechRecognition Microphone instance")

    # adjust for ambient noise and record audio from microphone
    with microphone as source:
        recogniser.adjust_for_ambient_noise(source)
        audio = recogniser.listen(source)

    # initialise response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognising speech from mic recording
    try:
        response["transcription"] = recogniser.recognise_google(audio)
    except sr.RequestError:
        # API unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech unintelligible
        response["error"] = "Unable to recognise speech"

    return response

if __name__ == "__main__":
    # create recogniser and microphone instances
    recogniser = sr.Recogniser()
    microphone = sr.Microphone()

    speech = recognise_speech_from_mic(recogniser, microphone)

    # if there was an error print error message
    if speech["error"]:
        print("ERROR: {}".format(speech["error"]))
    else:
        print("You said: {}".format(speech["transcription"]))