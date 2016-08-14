family={'Sam':'Ton','Jack':'Ton','Jones':'Sam','Dan':'Sam','Cam':'Jack'}
grandso = ["Dan","Cam","Jones"]
while True:
    number = int(raw_input("0 - Quit 1 - Find a Father 2 - Find a GrandFather"))
    if not number:
        break
    if number == 0:
        break
    if number == 1:
        son=str(raw_input("What's the son's name?"))
        if son in family:
                    print "Your Father's name is",family[son]
        else:
             print "No father found, Sorry."

    if number == 2:
        grandson = str(raw_input("What's the name of your Grandson: "))

        if grandso.__contains__(grandson):
            a = family[grandson]
            b = family[a]
            print "Your Grandfather's name is ", b
        else:
            print "Sorry you dont have grandfather, try finding your father first by pressing 1"



