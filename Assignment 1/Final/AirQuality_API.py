#***-----------IMPORTANT-----------***
#Make you have the css code downloaded

import requests

def writeHTMLHead(country): #country variable: outputs to different HTML files
    myfile = open(f"./Final/{country}.html","w")
    myfile.write("""<!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel = "stylesheet" type = "text/css" href = "style.css" />
    </head>
    """)
    myfile.close()

def writeHTMLNav(country):
    myfile = open(f"./Final/{country}.html","a")
    myfile.write("""    <body>
        <div class="header" id = "home">
            <h1>Air Quality by Country</h1>
        </div>
        <div class="navbar">
            <a href="#home">Home</a>
            <a href="#about">About</a>
        <div class="dropdown">
            <button class="dropbtn">Country 
                <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-content">
                <a href="./canada.html">Canada</a>
                <a href="./china.html">China</a>
                <a href="./united_states.html">United States</a>
            </div>
        </div> 
    </div>
    """)
    myfile.close()

def writeHTMLTableTag(country):
    myfile = open(f"./Final/{country}.html","a")
    myfile.write("""<table>
            <tr>
                <th>City</th>
                <th>Air Quality Index</th>
                <th>Air Pollution Level</th>
                <th>Health Implications</th>
                <th>Cautionary Statement</th>
            </tr>""")

def writeHTMLTable(country,city,aqi,level,health,statement,color):
    myfile = open(f"./Final/{country}.html","a")
    myfile.write(f"""
            <tr style = "background-color: {color};">
                <td>{city}</td>
                <td>{aqi}</td>
                <td>{level}</td>
                <td>{health}</td>
                <td>{statement}</td>
            </tr>""")
    myfile.close()

def writeHTMLEnd(country):
    myfile = open(f"./Final/{country}.html","a")
    myfile.write("""
           </table> 
        </body>
    </html>
    """)

#list of cities
canada = ["Toronto","Montreal","Vancouver","Calgary","Edmonton","Ottawa","Winnipeg","Quebec","Saskatoon"]
china = ["Shanghai","Beijing","Chengdu","Hangzhou","Chongqing","Guangzhou","Shenzhen","Ürümqi","Xi\'an","Xiamen"]
united_states = ["New York City","San Francisco","Los Angeles","Seattle","Chicago","Boston","Portland","Miami","Las Vegas","Philadelphia"]

countries_str = ["canada","china","united_states"] #list of countries
countries = [canada,china,united_states] #list of list of cities

def main():
    for i in countries_str:
        writeHTMLHead(i) #writes the header HTML code
        writeHTMLNav(i)
        writeHTMLTableTag(i)
    for i in range(len(countries)):
        for j in countries[i]:
            response = requests.get(f"https://api.waqi.info/feed/{j}/?token=e6b58a3aa996953cceed553f70c04c07342ce32e")
            if (response.status_code == 200):
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
                    
                print((countries_str[i],j, data['data']['aqi'], level, color))
                writeHTMLTable(countries_str[i],j, data['data']['aqi'], level, health, statement, color)

            else:
                myfile = open("./Assignment 1/myapi.html","w")
                myfile.write("Error has occured")
                myfile.close()

main()
for i in countries_str:
    writeHTMLEnd(i)
print("Successful!")