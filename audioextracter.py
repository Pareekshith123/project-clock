import moviepy.editor
from tkinter.filedialog import *


video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
x=input("enter the name to be representing audio in .mp3 format(type.mp3 after the name)")
audio=video.audio
audio.write_audiofile(x)
print ("completed!!: your audio file is ready,Can see in trial folder(search for trial folder in windows search bar)")