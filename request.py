import requests

url = "http://127.0.0.1:8000/predict"
test_audio = 'D:\FINALMLAPI\closer, the chainsmokers..wav'
audio_file = open(test_audio,"rb")
values = {"file":(test_audio,audio_file,"audio/wav")}
resp = requests.post(url=url,files={'file': 'D:\FINALMLAPI\closer, the chainsmokers..wav'})
print(resp)