print ("Welkom bij de mini game Millioniplace!")
print ("Veel plezier met het spelen!")
import os
file = "Aaron Smith - Dancin (KRONO Remix) - Lyrics-KIAZWfSmNOU(1).mp3"
os.system ("https://mp3.to/downloads/21b4d7940ada47dcb" + file)

print ("""-------------------------------------------------------""")
import random
aantalronden = 20
aantalbeurten = 10
randomgetal = (random.randint(1,1001))
for x in range (20):   
    for x in range (10):
        getalvraag = int(input("welk getal kies je?"))
        if getalvraag < randomgetal:
            print ("u zit onder het getal")
        else:
            print ("u zit boven het getal")
        if abs(getalvraag-randomgetal)>50:
            print ("je bent niet heel warm")
        elif abs(getalvraag-randomgetal)>20:
            print ("je bent warm")
        elif abs(getalvraag-randomgetal)>0:
            print ("je bent heel dichtbij")
        else:
            print (f"gefeliciteerd, u heeft het getal {randomgetal} goed geraden!")
            print ("1 punt erbij")
            break                                    
    print ("vergeet me niet te volgen op Youtube Fifanoobs_010. Alvast bedankt!")
    if randomgetal != getalvraag:
        print (f"u heeft het getal {randomgetal} helaas niet kunnen raden!")
        print ("Voor deze ronde heeft u helaas geen punten gescoord!")
    for x in range (1):
        answer = input('run again? (Ja/Nee)').lower()
        if answer == 'ja':
            ("press enter to continue")
        else: 
            print ("bedankt voor het spelen van de game")
            exit()
            
    
