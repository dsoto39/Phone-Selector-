# Program helps user choose a phone based on their needs and budgets
# Gui has yes and no button and buttons for phone brands and buttons for their price range and preferences 
import tkinter as tk
window1 = tk.Tk()
window1.geometry("500x70") #Used to configure our window size 
window1.configure(bg='#17202A') #This is used to select background color of our window

#This is how we name our title
window1.title("Phone Selector")
Welcome = tk.Label(window1,text="Welcome to the phone selector! Do you have have a phone brand in mind?")
# label.pack()
Welcome.place(x=1,y=1,height=15,width=500) #This is used to posotion the welcome prompt
yes=tk.Button(window1, text="Yes")#this is our yes button
yes.place(x=200,y=30)#this is used to position our yes button
no=tk.Button(window1, text="No")
no.place(x=250,y=30)
window1.mainloop() #tells Python to run the Tkinter event loop