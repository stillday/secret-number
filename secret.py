import random
import Tkinter
import tkMessageBox


secret = random.randint(0, 100)
list = []

window = Tkinter.Tk()

def quit():
    global window
    window.quit()

greeting = Tkinter.Label(window, text="Errate die Geheim Zahl, gib deinen Tip ab.")
greeting.pack()
greeting = Tkinter.Label(window, text="Die Zahl befindet sich zwischen 0 und 100.")
greeting.pack()
greeting = Tkinter.Label(window, text="Du hast 10 Versuche.")
greeting.pack()



guess = Tkinter.Entry(window)
guess.pack()

for x in range(10):

    def guess_check():

        if int(guess.get()) == secret:
            result_text = "Dein Tip war richtig. Folgende Zahlen hast du eingeben %s." % list
            window.quit()

        elif int(guess.get()) < secret:
            result_text = "Deine Tip war zu klein. Versuch es nochmal."

        else:
            result_text = "Dein Tip war zu gross. Versuche es nochmal"

        tkMessageBox.showinfo("Result", result_text)

# submit button
submit = Tkinter.Button(window, text="Submit", command= guess_check)  # check_guess, not check_guess()
submit.pack()

window.mainloop()