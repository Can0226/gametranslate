import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random

duration = 5
sample_rate = 44100
print("------!ÇEVİRME OYUNUNA HOŞGELDİNİZ!------")
print("Oyunun amacı:Size verilen kelimeyi İngilizce doğru bir şekilde telaffuz etmeye çalışmak")

k_kelimeler = ["kedi" , "kitap" , "dondurma" , "ağaç" , "ev"]
o_kelimeler = ["olası" , "karmaşık" , "başarmak" , "paket ulaştırmak" , "devam etmek"]
z_kelimeler = ["gözlemlemek" , "tavsiye etmek" , "yaygın" , "verimli" , "gayret"]

secim=input("Hangi türden kelime istersin?(kolay orta zor)")
if secim == "kolay":
    cevirilecek_kolay = random.choice(k_kelimeler)
    print(cevirilecek_kolay)

if secim == "orta":
    cevirilecek_orta = random.choice(o_kelimeler)
    print(cevirilecek_orta)

if secim == "zor":
    cevirilecek_zor = random.choice(z_kelimeler)
    print(cevirilecek_zor)


print("Şimdi konuşun...(Konuşmanız bittiğinde sonuç çıkana kadar bir daha konuşmayın!)")

recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="int16")
sd.wait()

wav.write("output.wav", sample_rate, recording)

print("Kayıt tamamlandı, şimdi tanıma işlemi devam ediyor...")

recognizer = sr.Recognizer()

with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language="en")
    print("Şunu söylediniz:", text)
    if text == k_kelimeler:
        print ("Kelimeniz doğru")
    else:
        print("Kelimeniz yanlış")

    text = recognizer.recognize_google(audio, language="en")
    print("Şunu söylediniz:", text)
    if text == o_kelimeler:
        print ("Kelimeniz doğru")
    else:
        print("Kelimeniz yanlış")


    text = recognizer.recognize_google(audio, language="en")
    print("Şunu söylediniz:", text)
    if text == z_kelimeler:
        print ("Kelimeniz doğru")
    else:
        print("Kelimeniz yanlış")

    

except sr.UnknownValueError:
    print("Konuşma tanınamadı.")

except sr.RequestError as e:
    print(f"Hizmet hatası: {e}")
