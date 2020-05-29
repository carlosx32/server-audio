import socket
import sys
import pyaudio
import wave
import pickle
from datetime import datetime


CHUNK = 1024
RECORD_SECONDS = 5
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
s = socket.socket()
s.bind((socket.gethostname(),3001))
s.listen(10) # Accepts up to 10 connections.
while True:
    sc, address = s.accept()
    print(address)
    fullMsg=b''
    # receive data and write it to file      
# #open in binary
    l = sc.recv(1024)
    fullMsg=fullMsg+l
    while (l):
        l = sc.recv(1024)
        fullMsg=fullMsg+l
    #el cliente termino el envio de datos
    #procesamos la salida:
    fullDataDic=pickle.loads(fullMsg)
    print(fullDataDic['datos'])
    wf = wave.open('file_'+fullDataDic['nombre']+str(address[1])+".wav",'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(fullDataDic['sampleSize'])
    wf.setframerate(RATE)
    wf.writeframes(fullDataDic['frames'])
    wf.close()
    sc.close()
s.close()