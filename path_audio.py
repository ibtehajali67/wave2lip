
import scipy, cv2, os, sys


from inference import MyClass
video="/home/ibtehaj/Documents/ibtehaj/Deepfake-voice/213.mp4"
user_input = input("Enter the path of your file: ")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
auido =str(user_input)
model = MyClass(auido,video)
model.main()
while True:
	user_input = input("Enter the path of your file: ")
	assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
	model.auido_path =str(user_input)
	model.main()
