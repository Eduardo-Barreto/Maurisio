import speech_recognition as sr
from gtts import gTTS

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('ouvindo...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language='pt-BR')
        command = command.lower()
        if 'maurício' in command:
            print(command)
            speech = gTTS(command, lang='pt', tld='com.br')
            speech.save('reproducao.mp3')

except:
    print('Não foi possível reconhecer nenhuma mensagem')
