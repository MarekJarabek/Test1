import tkinter #plátno
canvas = tkinter.Canvas()
canvas.pack()

subor = open('Zastávky.txt', 'r') #otvorí súbor z názvom Zastávky

def rozdel(vstup): #definícia rozdel
      pozicia = vstup.find(' ') #rozdelí text na medzere
      mesto = vstup[pozicia+3:] #vyhodí celý text za dvomi medzerami
      return mesto #vyhodí mesto
mesto = rozdel(canvas.readline()) #prečíta prvý riadok z textového súboru
canvas.create_text(100, 100, text=mesto) #napíše na určené súradnice prvý riadok súboru za dvomi medzerami
subor.close() #zatvorí súbor

y = 0 #nastaví premennú y na 0
def stvorceky(): #definícia stvorceky
      for i in range(1,9): #cyklus opakujúci sa 8 krát
            y = y + 20 #y sa každý krát zväčší o 20
            canvas.create_rectangle(90, y, 180, y+15) #vykreslí obdĺžnik 8 krát a vždy ho zmení podľa zadanej hodnoty

canvas.bind('<Button-1>',stvorceky) #ľavé tlačidlo myší spustí proces definícia
