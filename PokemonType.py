from tkinter import * 
from tkinter import ttk 
import tkinter as tk
class PokeType():
    
    typename =["Fire",
    "Ice",
    "Electric",
    "Fighting",
    "Poison",
    "Water",
    "Bug",
    "Grass",
    "Dragon",
    "Rock",
    "Ground",
    "Normal",
    "Flying",
    "Psychic",
    "Ghost",
    "Dark",
    "Steel"]
         
class Fire():  
    Weak=["Water","Ground","Rock"]
    Strong= ["Fire","Grass","Ice","Bug","Steel"]    

class Ice():
    Weak=["Ice"]
    Strong=["Fire","Fighting","Rock","Steel"]

class Electric():
    Strong=["Water","Flying"]
    Weak=["Electric","Grass","Dragon"]
    Immune=["Ground"]
    
class Fighting():
    Weak=["Poison","Flying","Psychic","Bug"]
    Strong=["Normal","Ice","Rock","Dark","Steel"]
    Immune=["Ghost"]     

class Poison():
    Weak=["Poison","Ground","Rock","Ghost"]
    Strong=["Grass"]
    Immune=["Steel"]

class Water():
    Weak=["Electric","Grass"]
    Strong=["Fire","Water","Ice","Steel"]    
    
class Bug():
    Weak=["Grass","Fighting","Ground"]
    Strong=["Fire","Flying","Rock"]
    
class Grass():
    Weak=["Fire","Ice","Poison","Flying","Bug"]
    Strong=["Water","Electric","Grass","Ground"]
            
class Dragon():
    Weak=["Steel"]
    Strong=["Dragon"]
    
class Rock():
    Weak=["Fighting","Ground","Steel"]
    Strong=["Fire","Ice","Flying","Bug"]
    
class Ground():
    Weak=["Grass","Bug"]
    Strong=["Fire","Electric","Poison","Rock","Steel"]
    Immune=["Flying"]
    
class Normal():
    Weak=["Rock","Steel"]
    Immune=["Ghost"]

class Flying():
    Strong=["Grass","Fighting","Bug"]
    Weak=["Electric","Rock","Steel"]
    
class Psychic():
    Strong=["Fighting","Poison"]
    Weak=["Psychic","Steel"]
    Immune=["Dark"]

class Ghost():
    Strong=["Psychic","Ghost"]
    Weak=["Dark"]
    Immune=["Normal"]
        
class Dark():
    pass

class Steel():
    pass

#Setting window size and title of window
root = tk.Tk()  
root.geometry("600x400")
root.title("Pokemon Type Checker")  

#Setting Strong, Weak and Immunity variables to values specific to each type
def show():
    T1.delete("1.0","end")
    T2.delete("1.0","end")
    T3.delete("1.0","end")
    if cb.get()=="Fire":
        a=Fire()
        strong=a.Strong
        weak=a.Weak
        immune=""   
    if cb.get()=="Ice":
        a=Ice()
        strong=a.Strong
        weak=a.Weak
        immune=""
    if cb.get()=="Electric":
        a=Electric()
        strong=a.Strong
        weak=a.Weak
        immune=a.Immune
    if cb.get()=="Fighting":
        a=Fighting()
        strong=a.Strong
        weak=a.Weak
        immune=a.Immune
    if cb.get()=="Poison":
        a=Poison()
        strong=a.Strong
        weak=a.Weak
        immune=a.Immune
    if cb.get()=="Water":
        a=Water()
        strong=a.Strong
        weak=a.Weak
        immune=""
    if cb.get()=="Grass":
        a=Grass()
        strong=a.Strong
        weak=a.Weak
        immune=""
    if cb.get()=="Bug":
        a=Bug()
        strong=a.Strong
        weak=a.Weak
        immune=""
    if cb.get()=="Dragon":
        a=Dragon()
        strong=a.Strong
        weak=a.Weak
        immune=""   
    if cb.get()=="Rock":
        a=Rock()
        strong=a.Strong
        weak=a.Weak
        immune="" 
    if cb.get()=="Ground":
        a=Ground()
        strong=a.Strong
        weak=a.Weak
        immune=a.Immune   
    if cb.get()=="Normal":
        a=Flying()
        strong=""
        weak=a.Weak
        immune=a.Immune   
    if cb.get()=="Flying":
        a=Flying()
        strong=a.Strong
        weak=a.Weak
        immune="" 
    if cb.get()=="Psychic":
        a=Psychic()
        strong=a.Strong
        weak=a.Weak
        immune=a.Immune   
    if cb.get()=="Ghost":
        a=Ghost()
        strong=a.Strong
        weak=a.Weak
        immune=a.Immune  
    for x in strong:
        T1.insert(END,f"{x}\n")
    for x in weak:
        T2.insert(END,f"{x}\n")
    for x in immune:
        T3.insert(END,f"{x}\n")

# Dropdown options set to values in Pokemon Type class  
TypeCheck=PokeType()
poke_type = TypeCheck.typename  

# Dropdown menu  
cb=ttk.Combobox(root,values=poke_type,width=25)
cb.set("Select a Pokemon Type")
cb.pack(side=LEFT,padx=50) #side changes position of combobox

# Button to update label  
button=tk.Button(root, text="Click Me", command=show,height=2,width=12,) 
button.place(x=80,y=225)

#Setting up textboxes
T1 = Text(root, height=5, width=15)
T1.pack()
T1.place(x=400,y=45)
T1.insert(END, '')
T2 = Text(root, height=5, width=15)
T2.pack()
T2.place(x=400,y=170)
T2.insert(END, '')
T3 = Text(root, height=5, width=15)
T3.pack()
T3.place(x=400,y=295)
T3.insert(END, '')


lbl=tk.Label(root, text="Strong against")
lbl.place(x=315,y=75)

lbl=tk.Label(root, text="Weak against")
lbl.place(x=320,y=200)

lbl=tk.Label(root, text="No effect on")
lbl.place(x=325,y=325)


root.mainloop()


