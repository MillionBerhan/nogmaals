# name of student: Million
# number of student:99065113
# purpose of program: de €1 en €2 munten toevoegen
# function of program:het wisselgeld teruggeven met munten.
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #dit rekent uit wat er betaalt wordt
paid = int(float(input('Paid amount: ')) * 100) #dit is de prijs van wat iets betaalt wordt
if paid < toPay:
  print ("u heeft niet genoeg betaalt u moet bijbetalen!")
  print(f'U moet nog {toPay-paid} centen betalen!')
  exit()
else:
  print("je krijgt wisselgeld!")

change = paid - toPay  # dit is het wisselgeld wat terruggeven moet worden


nrcvalue: (200 or 100 or 50 or 20 or 10 or 5 or 2 or 1)
amounts = [0, 0, 0, 0, 0, 0, 0, 0] 
i = 0

if change > 0: # laagste wisselgeld is 0
  coinValue = 200 # hoogste €munt wat teruggeven kan worden is de 2 munt.
  
  while change > 0 and coinValue > 0: #terwijl alles groter dan 0 is 
    nrCoins = change // coinValue #scheid het wisselgeld en de waarde 
    
    if nrCoins > 0: #als het groter is dan nul dan pakt hij het hoogste bedrag wat het systeem kan pakken.
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #het maximale aantal centen wat teruggeven kan en moet worden.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? '))
      amounts[i] = nrCoinsReturned
      

      change -= nrCoinsReturned * coinValue # wisselgeld is geld wat teruggeven moet worden keer de waarde van het bedrag
    
# comment on code below: 

    if coinValue == 200:    
      nrCoinsReturned200 = nrCoinsReturned
      coinValue = 100
    elif coinValue == 100:
      nrCoinsReturned100 = nrCoinsReturned
      coinValue = 50
    elif coinValue == 50:
      nrCoinsReturned50 = nrCoinsReturned
      coinValue = 20
    elif coinValue == 20:
      nrCoinsReturned20 = nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      nrCoinsReturned10 = nrCoinsReturned
      coinValue = 5
    elif coinValue == 5:
      nrCoinsReturned5 = nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      nrCoinsReturned2 = nrCoinsReturned
      coinValue = 1
    elif coinValue == 1:
      nrCoinsReturned1=nrCoinsReturned
      coinValue = 0

print ("-------------------------------------------------------------------------------------------")
print (f"""u hebt van de €2 munt/munten terug gegeven:   {nrCoinsReturned200}""")
print (f"""u hebt van de €1 munt/munten terug gegeven:   {nrCoinsReturned100}""")
print (f"""u hebt van de €0,50 munt/munten terug gegeven:{nrCoinsReturned50}""")
print (f"""u hebt van de €0,20 munt/munten terug gegeven:{nrCoinsReturned20}""")
print (f"""u hebt van de €0,10 munt/munten terug gegeven:{nrCoinsReturned10}""")
print (f"""u hebt van de €0,05 munt/munten terug gegeven:{nrCoinsReturned5}""")
print (f"""u hebt van de €0,02 munt/munten terug gegeven:{nrCoinsReturned2}""")
print (f"""u hebt van de €0,01 munt/munten terug gegeven:{nrCoinsReturned1}""")
print ("-------------------------------------------------------------------------------------------")
  
