import random
import hangman
import ordlista

svar = random.choice(ordlista.frukter)
svar = list(svar)

game_over = False

# skapa tomt ord
ord = []
for i in range(0,len(svar)):
    if svar[i] == " ":
        ord.append(" ")
    else:
        ord.append("_")

gissade_bokstäver = []


while not game_over:
    # skriv ut gjorda gissningar
    if len(gissade_bokstäver) > 0:
        print("Gissade bokstäver: " + "".join(gissade_bokstäver))

    #rita ut gubbe
    print("\n".join(hangman.hangmans[len(gissade_bokstäver)]))


    #skriv ut ord
    print("".join(ord))

    #ange en gissning
    gissning = ""
    while not len(gissning) == 1:
        gissning = input("Ange en bokstav: ")


    # antar att gissningen är fel
    gissade_fel = True

   # kollar om bokstaven finns i svaret
    i = 0
    for bokstav in svar:
        if bokstav == gissning:
            ord[i] = bokstav
            gissade_fel = False
        i += 1

    # Lägg in fel gissning i listan
    if gissade_fel:
        gissade_bokstäver.append(gissning)

    # kolla om spelet är slut
    if not "_" in ord:
        game_over = True
        print( '\n Bra jobbat! Du vann! ')
    elif len(gissade_bokstäver) == len(hangman.hangmans)-1:
        game_over = True
        print("\n".join(hangman.hangmans[len(gissade_bokstäver)]))
        print( '\n Du förlorade! ')

# skriv ut ordet när spelet är över
print("ordet var :" + "".join(svar))