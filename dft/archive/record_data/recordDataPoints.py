import glob
import pyaudio
import wave

NUM_SAMPLES = 5
chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
seconds = 3
filename = "adi"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)
samples = []
frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for dp in range(NUM_SAMPLES):
    print("sampling data point \n", dp)
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    samples.append(frames)
    frames = []
# Stop and close the stream
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
print("saving recordings")
for dp in range(NUM_SAMPLES):
    wf = wave.open("wavs/"+filename+"_"+str(dp)+".wav", 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(samples[dp]))
    wf.close()
print("finished saving recordings")
