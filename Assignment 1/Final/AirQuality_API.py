import requests
from tkinter import *

def writeHTMLHead(): 
    global myfile
    myfile = open("./Final/output.html","w")
    myfile.write("""<!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel = "stylesheet" type = "text/css" href = "style.css" />
    </head>
    """)

def writeHTMLNav():
    global myfile
    myfile.write("""    <body>
        <div class="header" id = "home">
            <h1>Air Quality by Country</h1>
        </div>
        <div class="navbar">
            <a href="#home">Home</a>
            <a href="#about">About</a>
    </div>
    """)

def writeHTMLTableTag():
    global myfile
    myfile.write("""<table>
            <tr>
                <th>City</th>
                <th>Air Quality Index</th>
                <th>Air Pollution Level</th>
                <th>Health Implications</th>
                <th>Cautionary Statement</th>
            </tr>""")

def writeHTMLTable(city,aqi,level,health,statement,color):
    global myfile
    myfile.write(f"""
            <tr style = "background-color: {color};">
                <td>{city}</td>
                <td>{aqi}</td>
                <td>{level}</td>
                <td>{health}</td>
                <td>{statement}</td>
            </tr>""")

def writeHTMLEnd():
    global myfile
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
germany = [""]

countries_str = ["canada","united_states","china","england"] #list of countries
countries = [canada,united_states,china,england] #list of list of cities

def enter():
    global gui_input
    print(e1.get())
    gui_input = e1.get()
    main()
    writeHTMLEnd()
    print("Successful!")

def main():
    writeHTMLHead()
    writeHTMLNav()
    writeHTMLTableTag()
    
    if gui_input in countries_str:
        for j in countries[countries_str.index(gui_input)]:
            response = requests.get(f"https://api.waqi.info/feed/{j}/?token=e6b58a3aa996953cceed553f70c04c07342ce32e")
            if (response.status_code == 200):
                print("Status Code: 200")
                data = response.json()
                
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
                    
                writeHTMLTable(j, data['data']['aqi'], level, health, statement, color)

            else:
                myfile = open("./Assignment 1/myapi.html","w")
                myfile.write("Error has occured")
                myfile.close()
    else:
        response = requests.get(f"https://api.waqi.info/feed/{gui_input}/?token=e6b58a3aa996953cceed553f70c04c07342ce32e")
        if (response.status_code == 200):
            print("Status Code: 200")
            data = response.json()

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
        else:
            myfile = open("./Assignment 1/myapi.html","w")
            myfile.write("Error has occured")
            myfile.close()
            




root = Tk()
root.title("photo tagger")
root.geometry("500x350")

def test(event):
    print(event) #ensure that this line is indented
topframe = Frame(root,bg='blue',height='20')
topframe.pack(fill=X)

can1 = Canvas(topframe,height='20',width='20',bg="blue",highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill='white')
can1.create_line(0, 10, 20, 10,fill='white')
can1.create_line(0, 15, 20, 15,fill='white')
can1.bind("<Button-1>",test ) # keyword 
can1.grid(row=0,column=0, padx=5, pady=5)

spaceframe = Frame(root,height=10) #invisible
spaceframe.pack()

frame = LabelFrame(root,borderwidth = 2, relief=RAISED, width=400,height=150)
frame.pack()

lab1 = Label(frame, text="fjkdsjkfsdjkfasdkfjkasd fdsakjfasj fkasjlf",width=40,height=5)
lab1.grid(row=0,column=0)

e1 = Entry(frame)
e1.grid(row=1,column=0,sticky=W,padx=60)

b = Button(frame, text="Sumbit",command=enter)
b.grid(row=1, column=0,sticky=E,padx=60)

root.mainloop()

