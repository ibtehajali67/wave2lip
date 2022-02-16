
import scipy, cv2, os, sys
import pyaudio
import wave
import pyautogui
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
# RECORD_SECONDS =5
WAVE_OUTPUT_FILENAME = "output.wav"

def audio_r():#use for audio record and save
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
	frames = []
	try:
		while True:
			data = stream.read(CHUNK)
			frames.append(data)
	except KeyboardInterrupt:
		print("Done recording")
	except Exceptions as e:
		print(str(e))
	stream.stop_stream()
	stream.close()
	p.terminate()
	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
from inference import MyClass
audio_r()
video="/home/ibtehaj/Documents/ibtehaj/Deepfake-voice/213.mp4"
# user_input = input("Enter the path of your file: ")# for input path of audio
# assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
auido =WAVE_OUTPUT_FILENAME
model = MyClass(auido,video)#model load and initialize
model.main()
print("---------------------Done audio-------------------------------------")
while True:
	# user_input = input("Enter the path of your file: ")
	# assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
	audio_r()
	model.auido_path =WAVE_OUTPUT_FILENAME # audio update 
	model.main()
	print("-----------------------------------Done-----------------------------------")
