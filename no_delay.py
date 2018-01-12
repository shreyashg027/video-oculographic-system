import numpy as np
import cv2
import time
import pyttsx

#engine = pyttsx.init()  #initialize speach sysnthesizer 

maxr = 1000
maxl = 1000
arr_len = 150
l = 1
r = 505
d = 70

def speech(arg):
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-7)
    engine.say(arg)
    engine.say("   ")
    engine.runAndWait()

#function to convert order of blinks into speech
def speak( x, y, z ):

	if x == 0  and y == 0 and z == 0:
		speech('hello')
			
	elif x == 2 and y == 3 and z == 0:
		speech('hi welcome!')
		
	elif x == 2 and y == 3 and z == 1:
		speech('good morning')
		
				
	elif x == 2 and y == 3 and z == 2:
		speech('hai. where are you?')
				
	elif x == 2 and y == 0 and z == 3:
		speech('had your lunch')
		
		
	elif x == 2 and y == 0 and z == 2:
		speech('I want help')
		
	
	elif x == 2 and y == 0 and z == 1:
		speech('Good afternoon')
		
		
	elif x == 2 and y == 1 and z == 3:
		speech('Good evening')
		
	
	elif x == 2 and y == 1 and z == 2:
		speech('Good night')
		
	
	elif x == 2 and y == 1 and z == 0:
		speech('Can I have a glass of water?')
		
	
	elif x == 1 and y == 3 and z == 2:
		speech('Can I have a cup of tea?')
		
	
	elif x == 1 and y == 3 and z == 1:
		speech('I need to use the restroom')
		
	
	elif x == 1 and y == 3 and z == 0:
		speech('Can you please switch on the TV?')
		
	
	elif x == 1 and y == 0 and z == 3:
		speech('Can you please switch on the fan?')
		
	
	elif x == 1 and y == 0 and z == 2:
		speech('Can you please open the door?')
		

	elif x == 1 and y == 0 and z == 1:
		speech('Can you please open the windows?')
		

	elif x == 1 and y == 2 and z == 3:
		speech('Can you please switch off the TV?')
		

	elif x == 1 and y == 2 and z == 1:
		speech('Can you please switch off the fan?')
		

	elif x == 1 and y == 2 and z == 0:
		speech('I have a headache')
		

	elif x == 0 and y == 3 and z == 2:
		speech('I need my medications')
		

	elif x == 0 and y == 3 and z == 1:
		speech('Can you take me out?')
		

	elif x == 0 and y == 3 and z == 0:
		speech('I need to take a shower')
		

	elif x == 0 and y == 2 and z == 3:
		speech('I need some snacks')
		
		
	elif x == 0 and y == 2 and z == 1:
		speech('I am sleepy')
		

	elif x == 0 and y == 2 and z == 0:
		speech('What is the time now?')
		

	elif x == 0 and y == 1 and z == 3:
		speech('I need to call a friend')
		
	elif x == 0 and y == 1 and z == 2:
		speech('I am feeling cold')
		

	elif x == 0 and y == 1 and z == 0:
		speech('I am not well')
			
	else:
		speech('')
		
	
	return 0

#function to detect the eye blinkings
def blink():
	
	cap=cv2.VideoCapture(0)  #provide the source
	
	countr = 0
	countl = 0
	eye = 0
	m = 0
	i = 0
	j = 0
	k = 0
	n = 0
	p = 0
	temp = 99
	val = [0]*15
	arr = [0]*150
	
	status = cap.isOpened()  #check camera is operating or not
	print status
	
	while( status ):
		ret,frame=cap.read()  #read video frame from camera
		
		if ret:
			y = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #extract the Y-component
			roi = y[205:275,75:580]  #crop the region of interest
			seg = cv2.inRange(roi,10,30)  #in cropped region get the specific pixel range
			
			se = np.ones((5,5),np.uint8)  #define structuring element
			di = cv2.dilate(seg,se,iterations = 1)  #use dilation technique
			cv2.imshow('Live_Steam_Window',di)
			
			#get the number of white pixcels in left part and right part
			for i in range (l, d):
				for j in range (l, r/2):
					if di[i,j] == 255:
						countr = countr + 1
			#print countr
			#time.sleep(0.5)
			
			for i1 in range (l, d):
				for j1 in range ((r/2)+1, r):
					if di[i1,j1] == 255:
						countl = countl + 1
			
			#print countl
			#time.sleep(0.5)
			
			#max = ( countl + countr ) / 2
			
			#both eyes are opened
			if countr > maxr and countl > maxl:
				eye = 3
			#right eye open; left eye close  
			elif countr > maxr and countl < maxl:
				eye = 2
			#left eye open; right eye close
			elif countr < maxr and countl > maxl:
				eye = 1 
			#both eyes are closed
			else:
				eye = 0
			
			#print eye
			
			#time delay to get the response 
			if m < arr_len:
				arr[m] = eye
				m = m + 1
			#process the response array
			else:
				for k in range(0,arr_len - 2):
					if arr[k] == arr[k+1]:
						n = n+1
						#print n
					#to get the frequency array
					else:
						if n > 10 and p < 15 and temp != arr[k]:
							val[p] = arr[k]
							temp = val[p]
							p = p+1
						n = 0
				speak( val[1], val[2], val[3])		
				print val
				
				#call the function to provide output voice
				
				break
		countr = 0
		countl = 0		
			#print m
			
		# else:	
			# print "can't read image frames!!!"
			# break
		
		#press 'q' to exit from the process
		if (cv2.waitKey(1) & 0xFF==ord('q')):
			cap.release()
			cv2.destroyAllWindows()
			exit(0)
			
	blink()

blink()

