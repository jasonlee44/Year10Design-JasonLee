import requests
from tkinter import *
import webbrowser
import os

#each "section" of the html code is split up into different functions
#this makes it eaiser for me to troubleshoot my code
def writeHTMLHead():
    myfile = open("output.html","w")
    myfile.write("""<!DOCTYPE html>
    <html>
    <head>
    <title>Air Quality API</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel = "stylesheet" type = "text/css" href = "style.css" />
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro&display=swap" rel="stylesheet">
    </head>
    """)
    myfile.close()

def writeHTMLNav():
    myfile = open("output.html","a")
    myfile.write("""    <body id="skyline">
        <div id = "home">
            <img class = "icon" src="icon.png" alt="Trulli" width="50" height="50">
            <p class="header">Air Quality by City</p>
        </div>
        <div class="navbar">
            <a class="active" href="output.html">Data</a>
            <a href="about.html">About</a>
            <a href="home.html">Home</a>
        </div>
    """)
    myfile.close()

def writeHTMLTableTag():
    myfile = open("output.html","a")
    myfile.write("""<table>
            <tr>
                <th>City</th>
                <th>Air Quality Index</th>
                <th>Air Pollution Level</th>
                <th>Health Implications</th>
                <th>Cautionary Statement</th>
            </tr>""")
    myfile.close()

def writeHTMLTable(city,aqi,level,health,statement,color):
    #these variables are used to write the json data to the html file
    myfile = open("output.html","a")
    myfile.write(f"""
            <tr style = "background-color: {color};">
                <td>{city}</td>
                <td>{aqi}</td>
                <td>{level}</td>
                <td>{health}</td>
                <td>{statement}</td>
            </tr>""")
    myfile.close()

def writeHTMLEnd():
    myfile = open("output.html","a")
    myfile.write("""
           </table> 
        </body>
    </html>
    """)
    myfile.close()

#list of cities
canada = ["Toronto","Montreal","Vancouver","Calgary","Edmonton","Ottawa","Winnipeg","Quebec","Saskatoon"]
united_states = ["New York City","San Francisco","Los Angeles","Seattle","Chicago","Boston","Portland","Miami","Las Vegas","Philadelphia"]
china = ["Shanghai","Beijing","Chengdu","Hangzhou","Chongqing","Guangzhou","Shenzhen","Ürümqi","Xiamen"]
england = ["London","Bristol","Liverpool","Manchester","Birmingham","Brighton","Oxford","Cambridge","Norwich"]
France = ["Paris","Nice","Bordeaux","Lyon","Marseille","Toulouse","Strasbourg","Lille","Nantes"]


countries_str = ["Canada","United States","China","England","France"] #list of countries
countries = [canada,united_states,china,england,France] #list of list of cities

def entry_enter(): #submiting a city from gui
    global gui_input
    print(e1.get())
    gui_input = e1.get()
    v.set("You will be redirected shortly")
    root.update()
    main()
    writeHTMLEnd()
    #opens the default web broswer
    webbrowser.open_new('file://' + os.getcwd() + '/home.html')
    v.set("")

def menu_enter(): #sumbiting a country from gui
    global gui_input
    print(variable.get())
    gui_input = variable.get()
    v.set("You will be redirected shortly")
    root.update()
    main()
    writeHTMLEnd()
    #opens the default web broswer
    webbrowser.open_new('file://' + os.getcwd() + '/home.html')
    v.set("")

def main():
    writeHTMLHead()
    writeHTMLNav()
    writeHTMLTableTag()
    
    if gui_input in countries_str:
    #checks if the input from GUI is a country
        for j in countries[countries_str.index(gui_input)]:
            try: #checks for error
                response = requests.get(f"https://api.waqi.info/feed/{j}/?token=e6b58a3aa996953cceed553f70c04c07342ce32e")
            except:
                response = None
                print("Error occured")
            if (response):
                data = response.json()
                
                if type(data['data']['aqi']).__name__ != "int":
                    level = "N/A"
                    health = "N/A"
                    statement = "N/A"
                    color = "grey"

                else:
                    if data['data']['aqi'] <= 50:
                        level = "Good"
                        health = "Air quality is considered satisfactory, and air pollution poses little or no risk"
                        statement = "None"
                        color = "rgb(51, 211, 51)"#green

                    elif data['data']['aqi'] <= 100:
                        level = "Moderate"
                        health = "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
                        statement = "Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion."
                        color = "rgb(255, 255, 100)"#yellow

                    elif data['data']['aqi'] <= 150:
                        level = "Unhealthy for Sensitive Groups"
                        health = "Members of sensitive groups may experience health effects. The general public is not likely to be affected."
                        statement = "Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion."
                        color = "rgb(245, 125, 45)"#orange

                    elif data['data']['aqi'] <= 200:
                        level = "Unhealthy"
                        health = "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects"
                        statement = "Active children and adults, and people with respiratory disease, such as asthma, should avoid prolonged outdoor exertion; everyone else, especially children, should limit prolonged outdoor exertion"
                        color = "rgb(140, 0, 0)" #red
                        
                    writeHTMLTable(j, data['data']['aqi'], level, health, statement, color)

            else:
                myfile = open("output.html","w")
                myfile.write("Error has occured")
                myfile.close()

    else:
    #if the input from GUI is a city
        try: #checks for error
            response = requests.get(f"https://api.waqi.info/feed/{gui_input}/?token=e6b58a3aa996953cceed553f70c04c07342ce32e")
        except:
            response = None
        if (response):
            data = response.json()

            if data['status'] == 'error': #if city entered causes an error
                print("Error")
                myfile = open("output.html","w")
                myfile.write("Error has occured")
                myfile.close()

            else:
                if type(data['data']['aqi']).__name__ != "int":
                        level = "N/A"
                        health = "N/A"
                        statement = "N/A"
                        color = "grey"

                elif data['data']['aqi'] <= 50:
                    level = "Good"
                    health = "Air quality is considered satisfactory, and air pollution poses little or no risk"
                    statement = "None"
                    color = "rgb(51, 211, 51)"#green

                elif data['data']['aqi'] <= 100:
                    level = "Moderate"
                    health = "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
                    statement = "Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion."
                    color = "rgb(255, 255, 100)"#yellow

                elif data['data']['aqi'] <= 150:
                    level = "Unhealthy for Sensitive Groups"
                    health = "Members of sensitive groups may experience health effects. The general public is not likely to be affected."
                    statement = "Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion."
                    color = "rgb(245, 125, 45)"#orange

                elif data['data']['aqi'] <= 200:
                    level = "Unhealthy"
                    health = "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects"
                    statement = "Active children and adults, and people with respiratory disease, such as asthma, should avoid prolonged outdoor exertion; everyone else, especially children, should limit prolonged outdoor exertion"
                    color = "rgb(140, 0, 0)" #red
                    
                writeHTMLTable(data['data']['city']['name'], data['data']['aqi'], level, health, statement, color)
                print("Successful!")
        else:
            myfile = open("output.html","w")
            myfile.write("Error has occured")
            myfile.close()

#-------------GUI-------------
root = Tk()
root.title("Air Quality API")
root.geometry("400x250")

root.configure(background = 'Deep sky blue')

frame1 = LabelFrame(root,borderwidth = 2, relief=RAISED, width=400,height=150)
frame1.pack(pady=20)

lab1 = Label(frame1, text="Enter a city",width=30,height=0)
lab1.grid(row=0,column=0)

e1 = Entry(frame1)
e1.grid(row=1,column=0,sticky=W,padx=10)

b1 = Button(frame1, text="Sumbit",command=entry_enter)
b1.grid(row=1, column=0,sticky=E,padx=10)

lab2 = Label(root,text="- OR -")
lab2.configure(background = 'Deep sky blue')
lab2.pack()

frame2 = LabelFrame(root,borderwidth = 2, relief=RAISED, width=400,height=150)
frame2.pack(pady=20,anchor=CENTER)

variable = StringVar(frame2)
variable.set("    ") # default value

m1 = OptionMenu(frame2, variable, "Canada", "United States", "China","England","France")
m1.config(width=17)
m1.grid(row=1,column=0,sticky=W,padx=10)

lab3 = Label(frame2, text="Select a country",width=30)
lab3.grid(row=0,column=0)

b2 = Button(frame2, text="Sumbit",command=menu_enter)
b2.grid(row=1, column=0,sticky=E,padx=10)

v = StringVar()
lab4 = Label(root, textvariable=v)
lab4.configure(background = 'Deep sky blue')
lab4.pack(pady=5)

root.mainloop()
