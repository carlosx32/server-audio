import socket
import sys
import pyaudio
#import wave
import pickle
from datetime import datetime


CHUNK = 1024
RECORD_SECONDS = 5
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
#WAVE_OUTPUT_FILENAME = "outputCliente.wav"

while True:
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("sending data:")
    s = socket.socket()
    s.connect((socket.gethostname(),3001))#se conecta al servidor
    d={
        'datos':"DATOS",
        'frames':b''.join(frames),
        'sampleSize':p.get_sample_size(FORMAT),
        'nombre':'Cliente1'
    }#crea la estructura a enviar
    msg = pickle.dumps(d)
    s.send(msg)
    s.close()
    print("end")
