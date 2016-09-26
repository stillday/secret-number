import random
def main():
    secret = random.randint(0, 100)

    print "Errate die Geheim Zahl, gib deinen Tip ab"
    print "Die Zahl befindet sich zwischen 0 und 100"
    print "Du hast 5 Versuche"

    list = []

    for x in range(10):
        try:
            guess = int(raw_input("Gib deinen Tip ab:  "))
            list.append(guess)

            if guess == secret:
                print "Dein Tip war richtig"
                break

            elif guess < secret:
                print "Deine Tip war zu klein. Versuch es nochmal"

            elif guess > secret:
                print "Dein Tip war zu gross. Versuche es nochmal"

        except ValueError:
            print "Gib bitte eine Zahl ein."

    print "Das waren alle deine Eingaben: %s" % list
    print "Du hast %s Versuche gebraut" % len(list)
    print "Ende"
if __name__ == '__main__':
    main()