"""programmet handlar om att beräkna skatten på ett smidigt sätt somänvändare kan bara använda bara input och det är årsinkomst.Därefter ge programet genom att visa summan av skattsom skule dras eller betala till staten .Även programetkan använda till vilken antal av människör som helstgenom att ställa frågan efter svaret.Vill du kolla igen din skatt? yes or no:"""print("Hello till mitt program,skatt!")#Här skriver jag ett välkomstbrev till programmetprint()#En töm radgrundavdraget=13200# Beskrivning av  grundavdraget, alltså hur mycket det är. den summan drar först i början därefter man börja och räckna skattenskattöver=438900#Under den här summan man betalar ingen skatt alls, det är skatt free.övreSkiktgränsen=186800 #Mellan skiktgränsen (skatt över som jag kallar ) och övre skiktgränsen som man betalar 20%while True:#Det är största While som i sin tur har två While som har två frågor    while True:#I denn While ställer jag frågan om årsinkomst och innehåller en if och två elif, som recknär och ge reslutatet på skatten genom att använda regler som står i uppgiften        årsinkomst= float (input ("Hur mycket tjänar du? Årsinkomst: "))        inkomst= årsinkomst-grundavdraget        if inkomst <=438900:#Under denna summan 438900, man är freeskattat.            print("Din skatt är 0 sek")##Här är resultatet av skatt och det är 0 sek        #i det här kondition,mellan 438900 och 638500 betalar man 0.20%. så klart man måste inte glömma 13200 som är skattavdrag.        elif inkomst>438900 and inkomst <=638500:            suman=skattöver-inkomst            sumanEfter=suman*0.20#skatten ligger på 0,20%            print(" Din skatt är:",round(sumanEfter,2))#för att kunna räkna 2 decimal nr använder jag round ,2            """            I det här Elif kommer jag att beräkna den 0.20% samt .025%.            Det är två olika skatt det är beror på hur mycket man tjäner.             skatt räcknär på flera katogre. så är det om vi skä räckna en milion sek.             det ska vara så här 13200 skattavdrag.            438900 free skatt             mellan 438900 och 625 700 där programet dras 0.20% av 186 800.             och allting över 625 700 dras 0.25%. på det här sättet programet funger             enligt skattverket.             ⬇️⬇️⬇️            """        elif inkomst >=638501:            överGränsen= inkomst-skattöver- övreSkiktgränsen            skatt_sumanÖverGränsen= överGränsen * 0.25            totalHelaSumman=skatt_sumanÖverGränsen+(övreSkiktgränsen*0.20)            print("skatten är: ", round(totalHelaSumman,2))            print ()        while True:            fråga= input("Vill du kolla igen din skatt? yes or no: ")            if fråga=="yes":             break            elif fråga=="no":                print("program är slut, hejdå.".upper())                exit()            else:                print("Du får välja bara yes or no")                continue                """                ⬆️⬆️⬆️                Det While är ansvaret på att ställa den andra och sista                frågan till användaren om vill kör en gång till och kolla igen                på skatt.då här man bara två alternative yes  no.  om man väljer                 yes programet kör igen eller no och programet slutar och säger                 "program är slut, hejdå"                om användare vill vara elak och skriva vad som hetst då                elise: Du får välja bara yes or no,                 som visara sig och räta avändare.                och ge honom möjlighet att forsöka igen genom continue.                        """