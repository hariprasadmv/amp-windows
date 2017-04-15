import os
from tkinter.filedialog import *

import pygame
from mutagen.id3 import ID3
from tkinter import *
from PyLyrics import *


listofsongs = []
realnames = []
songartist = []
index = 0

root = Tk()
root.minsize(300,300)
root.title("amp")
v = StringVar()
b = StringVar()
songlabel = Label(root,textvariable=v,width=35)
lyriclabel = Label(root,textvariable=b, width=35)
pygame.mixer.init()

def chooser():

    directory = askdirectory()
    os.chdir(directory)
    
    

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            artist = audio['TPE2'].text[0]
            songartist.append(artist)
            listofsongs.append(files)
            realnames.reverse()
            for items in realnames:
            	listbox.insert(0,items)
        else:
        	pass    





def choosefile():
	songfile = askopenfilename()
	if songfile.endswith(".mp3"):
		realfile = os.path.realpath(songfile)
		audio = ID3(realfile)
		artist = audio['TPE2'].text[0]
		name = audio['TIT2'].text[0]
		
		realnames.append(audio['TIT2'].text[0])
		listofsongs.append(songfile)
		songartist.append(artist)
		listbox.insert(0,realnames[0])
		
	else:
		pass


def play(event):
    global index
    index =0
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

    

def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    



def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    
def lyrics(event):
	global index
	name = realnames[index]
	artist = songartist[index]
	print(name)
	print(artist)
	lyricstext = PyLyrics.getLyrics(artist, name)
	print(lyricstext)
	b.set(lyricstext)


label = Label(root,text='Music Player')
label.pack()

listbox = Listbox(root)

listbox.pack(side = TOP, anchor = NW)


realnames.reverse()

for items in realnames:
    listbox.insert(0,items)


realnames.reverse()




nextbutton = Button(root,text = 'Next Song')
nextbutton.pack(side = LEFT)

previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack(side = LEFT)

stopbutton = Button(root,text='Stop Music')
stopbutton.pack(side = LEFT)


playbutton = Button(root,text='play')
playbutton.pack(side = LEFT)
lyricsbutton = Button(root,text='Get Lyrics')
lyricsbutton.pack(side = LEFT)

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
playbutton.bind("<Button-1>",play)
lyricsbutton.bind("<Button-1>",lyrics)


songlabel.pack(side = BOTTOM)
lyriclabel.pack(side = RIGHT)
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label = "open folder",command = chooser)
filemenu.add_command(label = "open file",command = choosefile)
filemenu.add_command(label = "exit",command=root.destroy)
menubar.add_cascade(label = "file", menu = filemenu)
root.config(menu=menubar)



root.mainloop()
