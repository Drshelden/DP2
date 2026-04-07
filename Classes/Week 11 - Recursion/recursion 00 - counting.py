#! python3

def iter(aLevel):
    #prints before iterating in - while going down
    print(f"going down: {aLevel}") 

    if (aLevel):
        iter(aLevel - 1)

    #prints after iterating in - while coming up
    print(f"coming up: {aLevel}") 

iter(10)
