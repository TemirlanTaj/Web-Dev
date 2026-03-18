from models import Entity, Turtle, Villain

# Create objects
leonardo =      Turtle("Leonardo",     15, "M", "katanas",                 "blue")
donatello =     Turtle("Donatello",    15, "M", "просто палка ¯_ (ツ)_/¯", "purple")
raphael =       Turtle("Raphael",      15, "M", "вилки для салата",        "red")
michelangelo =  Turtle("Michelangelo", 15, "M", "nunchucks",               "orange")

shredder =  Villain("Shredder",     50, "M", "conquer New York and eat turtle soup")
april =     Entity( "April O'Neil", 25, "F", is_mutated=False)

characters = [leonardo, donatello, raphael, michelangelo, shredder, april]

for character in characters:
    print(character.introduce())
    print(character.status())
    print()

print("=" * 40)

for character in characters:
    if isinstance(character, Turtle):
        print(character.fight())
    elif isinstance(character, Villain):
        print(character.threaten())

print("=" * 40)

for character in characters:
    print(character)
