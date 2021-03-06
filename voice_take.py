#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import speech_recognition as sr

def googlesr():
    rospy.init_node('voice_rec', anonymous=True)
    pub = rospy.Publisher('take_photo', String, queue_size=10)

    while not rospy.is_shutdown():
        # obtain audio from the microphone
        x = raw_input("Enter for run Recording:")
        r = sr.Recognizer()
        with sr.Microphone(device_index=0) as source:
            print(">>> Say something!")
            #audio = r.listen(source)
            audio = r.record(source, duration=2.5)
            
        # recognize speech using Google Speech Recognition
        try:
            global result
            result = r.recognize_google(audio)
            print("SR result: " + result)
        except sr.UnknownValueError:
            print("SR could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
        pub.publish(result)

if __name__ == '__main__':
    try:
        googlesr()
    except rospy.ROSInterruptException:
        pass