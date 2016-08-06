
import wikipedia
import webbrowser

def list_display(topic):
    for x in topic:
        print x
def content_display(t):
    ch = input("PLEASE ENTER YOUR CHOICE...")
    i = input("PRESS 1 TO VIEW IN TERMINAL AND 2 TO VIEW IN BROWSER \n 1.TERMINAL \n 2-BROWSER")
    if i==1:
        content_terminal(t[ch-1][2: ])
    elif i==2:
        content_webpage(t[ch-1][2: ])
    else:
        print "Sorry, You have made a invalid choice"
    
def content_terminal(k):  #this function helps to view the summary of the selected topic
    wikipedia.set_lang("en")
    data = wikipedia.summary(k, sentences=1000000, chars=100000000, auto_suggest=True, redirect=True)
    print data


def content_webpage(a):
    ny = wikipedia.page(a)
    var = ny.url
    webbrowser.open_new_tab(var)


title = "WELCOME TO WIKIAPI"
a = "_________________________________________________________________________________________________________________________________________"
print a
print title.center(130," ")
print a

i = 1
while i==1:
    print "                                                                                                "
    print "-----------------------------------------------CATEGORIES------------------------------------------------------"
    print "SELECT YOUR CATEGORIES"    
    topic = ["1->Wonders of world" , "2->Programming languages","3->India","4.Sports","5->Entertainment"]
    list_display(topic)
    ch = input("Your choice please...")
 
    if ch==1:
        t = ["1 Great Pyramid of Giza","2 Hanging Gardens of Babylon","3 Statue of Zeus at Olympia","4 Temple of Artemis at Ephesus","5 Mausoleum at Halicarnassus","6 Colossus of Rhodes","7 Lighthouse of Alexandria"]
        list_display(t)
        content_display(t)    
    elif ch==2:
        t = ["1 C language","2 C++","3 Python language","4 Java ","5 HTML","6 PHP"]
        list_display(t)
        content_display(t)
    elif ch==3:
        t = ["1 languages in India","2 Religions in India","3 Dance in India","4  Musics of India","5.Architecture of India","6 Foods of India"]        
        list_display(t)
        content_display(t)
    elif ch==4:
        t = ["1 Cricket","2 Foodball","3 Chess","4 Hockey","5 Tennis"]
        list_display(t)
        content_display(t)
    elif ch==5:
        t = ["1 movies","2 songs","3 dance"]
        list_display(t)    
        content_display(t)
    elif ch==0:
        break
        print "Thank you...(*~*)..Vist again"
    else:
        print "Sorry, You have made an invalid choice"

    i=input("                            PRESS 1 TO CONTINUE OR PRESS 0 TO EXIT                           ")
