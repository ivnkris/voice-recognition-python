import speech_recognition as sr

def recognise_speech_from_mic(recogniser, microphone):
    #check that recogniser and microphone are appropriate SpeechRecognition instances
    if not isinstance(recogniser, sr.Recogniser):
        raise TypeError("recogniser must be a SpeechRecognition Recogniser instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("microphone must be a SpeechRecognition Microphone instance")

    # adjust for ambient noise and record audio from microphone
    with microphone as source:
        recogniser.adjust_for_ambient_noise(source)
        audio = recogniser.listen(source)