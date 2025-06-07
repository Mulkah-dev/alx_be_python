animal = "elephant"

def counting():
    animal = "hippopotamus"

    print("Local:", animal)

    print("global:", globals()['animal'])

# LEGB Rule:
    # L - Local: looks for 'animal' inside the function
    # E - No enclosing function here
    # G - Global: if not found locally, it would look here
    # B - Built-in: last resort

counting()