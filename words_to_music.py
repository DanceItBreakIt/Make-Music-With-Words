# Make Music With Words!
# by DanceItBreakIt
# 100% original code
# just a musical toy
# have fun

import winsound as ws
import tkinter as tk
import time
import keyboard
import webbrowser as wb

# aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789 a!a?a?a?a?A?a.a!a!a!a!a!a (for debug purposes)

def instructions(): # creates popup for instructions
    popup = tk.Tk()
    popup.title("Instructions...")
    popupscreenwidth = popup.winfo_screenwidth() # sets popup in center of screen
    popupscreenheight = popup.winfo_screenheight()
    popupcenterx = int(popupscreenwidth/2 - 200)
    popupcentery = int(popupscreenheight/2 - 225)
    popup.geometry(f"{400}x{450}+{popupcenterx}+{popupcentery}")
    popup["bg"] = "papaya whip"
    tk.Label(popup,
             text = "Each letter and number corresponds to a specific musical note.\nThe default notes of each character are as follows:",
             font = ("Comic Sans MS", 10),
             bg = "papaya whip",
             justify = "left",
             padx = "15",
             pady = "10",
             ).pack(anchor = "w")
    tk.Label(popup,
             text = "\"A\" = C4 \n\"B\" = C#4 \n\"C\" = D4 \n\"D\" = D#4 \n\"E\" = E4 \n\"F\" = F4 \n\"G\" = F#4 \n\"H\" = G4 \n\"I\" = G#4 \n\"J\" = A4 \n\"K\" = A#4 \n\"L\" = B4 \n\"M\" = C5",
             font = ("Comic Sans MS", 10),
             bg = "papaya whip",
             justify = "left",
             ).place(x = 50, y = 60)
    tk.Label(popup,
             text = "\"N\" = C#5 \n\"O\" = D5 \n\"P\" = D#5 \n\"Q\" = E5 \n\"R\" = F5 \n\"S\" = F#5 \n\"T\" = G5 \n\"U\" = G#5 \n\"V\" = A5 \n\"W\" = A#5 \n\"X\" = B5 \n\"Y\" = C6 \n\"Z\" = C#6",
             font = ("Comic Sans MS", 10),
             bg = "papaya whip",
             justify = "left",
             ).place(x = 165, y = 60)
    tk.Label(popup,
             text = "\"0\" = D6 \n\"1\" = D#6 \n\"2\" = E6 \n\"3\" = F6 \n\"4\" = F#6 \n\"5\" = G6 \n\"6\" = G#6 \n\"7\" = A6 \n\"8\" = A#6 \n\"9\" = B6",
             font = ("Comic Sans MS", 10),
             bg = "papaya whip",
             justify = "left",
             ).place(x = 280, y = 60)
    tk.Label(popup,
             text = "\"!\" is used to raise the octave by 1. \n\"?\" is used to lower the octave by 1. \n\".\" is used to set the octave to the default value. \n\nSongs are automatically copied to clipboard when \"Play!\" is \npressed. \nHold the \"Escape\" key while playing to cancel playback.",
             font = ("Comic Sans MS", 10),
             bg = "papaya whip",
             justify = "left",
             ).place(x = 10, y = 310)

notelength = 1 # how fast the notes play, default is 1/4 note
octave = 1 # what pitch everything is set to (default is octave 4, but this is a multiplier, so it counts as the number 1)

def changenotelength():
    global notelength
    match (notelength):
        case 4:
            notelength = 2
            length["text"] = "1/2"
        case 2:
            notelength = 1
            length["text"] = "1/4"
        case 1:
            notelength = 0.5
            length["text"] = "1/8"
        case 0.5:
            notelength = 0.25
            length["text"] = "1/16"
        case 0.25:
            notelength = 4
            length["text"] = "1/1"

def playsong(text):
    song = text.get(1.0, "end-1c")
    root.clipboard_append(song) # copies song to clipboard
    print(song)
    global octave
    octave = 1
    # play["text"] = "Playing..."
    # play["bg"] = "burlywood2"
    for char in range(len(song)):
        match song[char]: # plays note in accordance to character
            case "a":
                ws.Beep(int(261 * octave), int(250 * notelength))
            case "A":
                ws.Beep(int(261 * octave), int(250 * notelength))
            case "b":
                ws.Beep(int(277 * octave), int(250 * notelength))
            case "B":
                ws.Beep(int(277 * octave), int(250 * notelength))
            case "c":
                ws.Beep(int(293 * octave), int(250 * notelength))
            case "C":
                ws.Beep(int(293 * octave), int(250 * notelength))
            case "d":
                ws.Beep(int(311 * octave), int(250 * notelength))
            case "D":
                ws.Beep(int(311 * octave), int(250 * notelength))
            case "e":
                ws.Beep(int(329 * octave), int(250 * notelength))
            case "E":
                ws.Beep(int(329 * octave), int(250 * notelength))
            case "f":
                ws.Beep(int(349 * octave), int(250 * notelength))
            case "F":
                ws.Beep(int(349 * octave), int(250 * notelength))
            case "g":
                ws.Beep(int(369 * octave), int(250 * notelength))
            case "G":
                ws.Beep(int(369 * octave), int(250 * notelength))
            case "h":
                ws.Beep(int(392 * octave), int(250 * notelength))
            case "H":
                ws.Beep(int(392 * octave), int(250 * notelength))
            case "i":
                ws.Beep(int(415 * octave), int(250 * notelength))
            case "I":
                ws.Beep(int(415 * octave), int(250 * notelength))
            case "j":
                ws.Beep(int(440 * octave), int(250 * notelength))
            case "J":
                ws.Beep(int(440 * octave), int(250 * notelength))
            case "k":
                ws.Beep(int(466 * octave), int(250 * notelength))
            case "K":
                ws.Beep(int(466 * octave), int(250 * notelength))
            case "l":
                ws.Beep(int(493 * octave), int(250 * notelength))
            case "L":
                ws.Beep(int(493 * octave), int(250 * notelength))
            case "m":
                ws.Beep(int(523 * octave), int(250 * notelength))
            case "M":
                ws.Beep(int(523 * octave), int(250 * notelength))
            case "n":
                ws.Beep(int(554 * octave), int(250 * notelength))
            case "N":
                ws.Beep(int(554 * octave), int(250 * notelength))
            case "o":
                ws.Beep(int(587 * octave), int(250 * notelength))
            case "O":
                ws.Beep(int(587 * octave), int(250 * notelength))
            case "p":
                ws.Beep(int(622 * octave), int(250 * notelength))
            case "P":
                ws.Beep(int(622 * octave), int(250 * notelength))
            case "q":
                ws.Beep(int(659 * octave), int(250 * notelength))
            case "Q":
                ws.Beep(int(659 * octave), int(250 * notelength))
            case "r":
                ws.Beep(int(698 * octave), int(250 * notelength))
            case "R":
                ws.Beep(int(698 * octave), int(250 * notelength))
            case "s":
                ws.Beep(int(739 * octave), int(250 * notelength))
            case "S":
                ws.Beep(int(739 * octave), int(250 * notelength))
            case "t":
                ws.Beep(int(783 * octave), int(250 * notelength))
            case "T":
                ws.Beep(int(783 * octave), int(250 * notelength))
            case "u":
                ws.Beep(int(830 * octave), int(250 * notelength))
            case "U":
                ws.Beep(int(830 * octave), int(250 * notelength))
            case "v":
                ws.Beep(int(880 * octave), int(250 * notelength))
            case "V":
                ws.Beep(int(880 * octave), int(250 * notelength))
            case "w":
                ws.Beep(int(932 * octave), int(250 * notelength))
            case "W":
                ws.Beep(int(932 * octave), int(250 * notelength))
            case "x":
                ws.Beep(int(987 * octave), int(250 * notelength))
            case "X":
                ws.Beep(int(987 * octave), int(250 * notelength))
            case "y":
                ws.Beep(int(1046 * octave), int(250 * notelength))
            case "Y":
                ws.Beep(int(1046 * octave), int(250 * notelength))
            case "z":
                ws.Beep(int(1108 * octave), int(250 * notelength))
            case "Z":
                ws.Beep(int(1108 * octave), int(250 * notelength))
            case "0":
                ws.Beep(int(1174 * octave), int(250 * notelength)) # numbers continue after Z
            case "1":
                ws.Beep(int(1244 * octave), int(250 * notelength))
            case "2":
                ws.Beep(int(1318 * octave), int(250 * notelength))
            case "3":
                ws.Beep(int(1396 * octave), int(250 * notelength))
            case "4":
                ws.Beep(int(1479 * octave), int(250 * notelength))
            case "5":
                ws.Beep(int(1567 * octave), int(250 * notelength))
            case "6":
                ws.Beep(int(1661 * octave), int(250 * notelength))
            case "7":
                ws.Beep(int(1760 * octave), int(250 * notelength))
            case "8":
                ws.Beep(int(1864 * octave), int(250 * notelength))
            case "9":
                ws.Beep(int(1975 * octave), int(250 * notelength))
            case "!":
                if octave < 4:
                    octave *= 2
            case "?":
                if octave > 0.25:
                    octave /= 2
            case ".":
                octave = 1
            case _:
                time.sleep(int(0.25 * notelength)) # rest for unknown characters
        if keyboard.is_pressed("esc"):
            play["text"] = "Play Song!"
            play["bg"] = "burlywood1"
            break
        
    # play["text"] = "Play Song!"
    # play["bg"] = "burlywood1"

def yt():
    wb.open("https://www.youtube.com/@danceitbreakit")



root = tk.Tk()
root.title("Create Music With Words!")
windowwidth = 500
windowheight = 400
root.resizable(False, False)
root['bg'] = "papaya whip"

screenwidth = root.winfo_screenwidth() # places window in center of screen
screenheight = root.winfo_screenheight()
centerx = int(screenwidth/2 - windowwidth/2)
centery = int(screenheight/2 - windowheight/2)
root.geometry(f"{windowwidth}x{windowheight}+{centerx}+{centery}")

tk.Label(root,
         text = "Make Music With Words!",
         bg = "papaya whip",
         padx = "30",
         pady = "25",
         font = ("Comic Sans MS", 25),
         ).pack()
tk.Label(root,
         text = "by DanceIt",
         bg = "papaya whip",
         font = ("Comic Sans MS", 9),
         ).place(x = 390, y = 65)
text = tk.Text(root,
        bg = "floral white",
        font = ("Comic Sans MS", 10),
        padx = "15",
        pady = "5",
        width = 35,
        height = "10",
        )
text.pack()
tk.Button(root,
          text = "Instructions",
          font = ("Comic Sans MS", 15),
          activebackground = "burlywood3",
          bg = "burlywood1",
          padx = "5",
          pady = "5",
          command = instructions,
          ).place(x = 50, y = 320)
tk.Label(root,
         text = "Note\nLength:",
         font = ("Comic Sans MS", 8),
         bg = "papaya whip",
         justify = "center",
         ).place(x = 230, y = 305)
length = tk.Button(root,
          text = "1/4",
          activebackground = "burlywood3",
          bg = "burlywood1",
          font = ("Comic Sans MS", 10),
          command = changenotelength,
          )
length.place(x = 235, y = 345)
play = tk.Button(root,
          text = "Play Song!",
          activebackground = "burlywood3",
          bg = "burlywood1",
          font = ("Comic Sans MS", 15),
          padx = "10",
          pady = "5",
          command = lambda: playsong(text),
          )
play.place(x = 320, y = 320)
tk.Button(root,
          text = "YouTube!",
          font = ("Comic Sans MS", 8),
          bg = "red3",
          fg = "snow",
          activebackground = "red4",
          activeforeground = "snow",
          command = yt,
          justify = "right",
          ).place(x = 430, y = 265)

root.mainloop()