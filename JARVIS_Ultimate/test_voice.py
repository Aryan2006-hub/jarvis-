from voice.listener import Listener
from voice.speaker import Speaker

speaker = Speaker()
speaker.speak("This is the JARVIS voice test.")
listener = Listener()
command = listener.listen()
print("Heard:", command)
speaker.speak("Voice test finished.")
