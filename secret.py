
secret = 83

print "Errate die Geheim Zahl, gib deinen Tip ab"
print "Die Zahl befindet sich zwischen 0 und 100"
guess = int(raw_input("Gib deinen Tip ab:  "))

if guess == secret:
    print "Dein Tip war richtig"

elif guess < secret:
    print "Deine Tip war zu klein. Versuch es nochmal"

elif guess > secret:
    print "Dein Tip war zu gross. Versuche es nochmal"

# Wie kann ich verhindern, das ein fehlercode erscheint wenn ich buchstaben eingebe #
"""else:
    print "Gib bitte eine Zahl ein" """