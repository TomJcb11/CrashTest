from random import choice, randint

from models.Vanilla import Vanilla


randomOffset = randint(1,25)

#Create a random offset  for each encoded message



message = 'Dont show this to anyone'
a = Vanilla(message)

cypher=a.cyphering(offset=randomOffset)

tries_uncyphering = a.uncyphering(cypher)

print(tries_uncyphering)
