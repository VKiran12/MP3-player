from pygame import mixer
from tkinter import Tk
from tkinter import Label  
from tkinter import Button
from tkinter import filedialog
current_volume=float(0.5)
def play_song():
    filename=filedialog.askopenfilename(initialdir="C:/",title="Please select a file")
    current_song= filename
    song_title = filename.split("/")
    song_title = song_title[-1]
    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="green",text="Now Playing : "+ str(song_title))
        volume_label.config(fg="green",text="Volume : " + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="Error playing track")
        

def reduce_volume():
    try:
        global current_volume
        if current_volume<=0:
            volume_label.config(fg="red",text="Volume : Muted")
            return
        current_volume= current_volume - float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green",text=" Volume : "+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="Track hasn't been selected yet!")


def increase_volume():
    try:
        global current_volume
        if current_volume>=1:
            volume_label.config(fg="green",text="Volume : Max")
            return
        current_volume= current_volume + float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green",text=" Volume : "+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="Track hasn't been selected yet!")

def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="Track hasn't been selected")
        

def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="Track hasn't been selected")


#main screen
root=Tk()
root.title=("Music Player")
Label(root,text="Custom Music Player",font=("Calibri",15),fg="violet").grid(sticky="N",row=0,padx=120)
Label(root,text="Select your favourite music track!!",font=("Calibri",12),fg="purple").grid(sticky="N",row=1)
Label(root,text="Volume",font=("Calibri",12),fg="purple").grid(sticky="N",row=4)
song_title_label = Label(root,font=("Calibri",12))
song_title_label.grid(stick="N",row=3)
volume_label=Label(root,font=("Calibri",12))
volume_label.grid(sticky="N",row=5)

#Buttons
Button(root,text="Select Song",font=("Calibri",12),command=play_song).grid(row=2,sticky="N")
Button(root,text="Pause",font=("Calibri",12),command=pause).grid(row=3,sticky="E")
Button(root,text="Resume",font=("Calibri",12),command=resume).grid(row=3,sticky="W")
Button(root,text="-",font=("Calibri",12),width=5,command=reduce_volume).grid(row=5,sticky="W")
Button(root,text="+",font=("Calibri",12),width=5,command= increase_volume).grid(row=5,sticky="E")




root.mainloop()
