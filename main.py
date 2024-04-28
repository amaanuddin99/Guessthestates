from turtle import Turtle,Screen
from statecl import estate
import pandas as pd
scrn=Screen()
new="blank_states_img.gif"
scrn.bgpic(new)
q=pd.read_csv("50_states.csv")
states=q["state"].to_list()
guessed=0
while(guessed<50):
    st=scrn.textinput("State Identifier","Enter a name of state which you know")
    st=st.title()
    if(st=="Exit"):
        kl=pd.DataFrame(states)
        kl.to_csv("unguessedstates.csv")

        
        exit()
    
    if st in states:
        newdf=q[q["state"]==st]
        reqx=newdf["x"].to_list()[0]
        reqy=newdf["y"].to_list()[0]
        new=estate(st,reqx,reqy)
        guessed=guessed+1
        states.remove(st)
    scrn.delay(3)
scrn.exitonclick()
