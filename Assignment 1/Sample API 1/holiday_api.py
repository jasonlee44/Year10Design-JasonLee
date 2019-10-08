import requests

def headerHTML():
    myfile = open("./Assignment 1/myapi.html","w")
    myfile.write("<!DOCTYPE html>")
    myfile.write("\n<html>")
    myfile.write("\n<head>")
    myfile.write("\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
    myfile.write("\n<h1>Public Holidays in Canada</h1>")
    myfile.write("\n<link rel = \"stylesheet\" type = \"text/css\" href = \"style.css\" />")
    myfile.write("\n</head>")
    myfile.close()

def bodyHTML():
    myfile = open("./Assignment 1/myapi.html","a")
    myfile.write("\n<body>\n<table id=\"myTable\">\n<tr>\n<th onclick=\"sortTable(0)\">Name</th>\n<th onclick=\"sortTable(1)\">Date</th>\n<th onclick=\"sortTable(2)\">Country Wide</th>\n<th onclick=\"sortTable(3)\">Regions(provinces, territories, states etc.)</th>\n</tr>")
    myfile.close()

def endBodyHTML():
    myfile = open("./Assignment 1/myapi.html","a")
    myfile.write("\n</table>")
    myfile.write("\n</body>")
    myfile.write("\n</html>")
    myfile.write("\n<p>API: <a href=\"https://date.nager.at\">https://date.nager.at<a></p>")
    myfile.close()

def writeHTML(name,date,country,province):
    myfile = open("./Assignment 1/myapi.html","a")
    myfile.write("\n<tr>")
    myfile.write(f"\n<td>{name}</td>")
    myfile.write(f"\n<td>{date}</td>")
    myfile.write(f"\n<td>{country}</td>")
    myfile.write(f"\n<td>{province}</td>")
    myfile.write("\n</tr>")
    myfile.close()

def writeAlertHTML():
    myfile = open("./Assignment 1/myapi.html","a")
    myfile.write("\n<div class=\"alert\"><span class=\"closebtn\" onclick=\"this.parentElement.style.display=\'none\';\">&times;</span>") 
    myfile.write("<strong>Hello There!</strong> Welcome to my website. You can change the view of the table by clicking on the headers.</div>")
    myfile.close()

def writeScript():
    myfile = open("./Assignment 1/myapi.html","a")
    myfile.write("\n<script>function sortTable(n){var table,rows,switching,i,x,y,shouldSwitch,dir,switchcount=0;table=document.getElementById(\"myTable\");switching=true;dir=\"asc\";while(switching){switching=false;rows=table.rows;for(i=1;i<(rows.length-1);i++){shouldSwitch=false;x=rows[i].getElementsByTagName(\"TD\")[n];y=rows[i+1].getElementsByTagName(\"TD\")[n];if(dir==\"asc\"){if(x.innerHTML.toLowerCase()>y.innerHTML.toLowerCase()){shouldSwitch=true;break}}else if(dir==\"desc\"){if(x.innerHTML.toLowerCase()<y.innerHTML.toLowerCase()){shouldSwitch=true;break}}}if(shouldSwitch){rows[i].parentNode.insertBefore(rows[i+1],rows[i]);switching=true;switchcount++}else{if(switchcount==0&&dir==\"asc\"){dir=\"desc\";switching=true}}}}</script>")
    myfile.close()

def main():
    response = requests.get("https://date.nager.at/api/v2/publicholidays/2020/CA")

    headerHTML() #writes the header HTML code
    bodyHTML() #writes the body HTML code
    writeAlertHTML()



    if (response.status_code == 200):
        datajson = response.json()
        for i in range(len(datajson)):
            holidayName = datajson[i]['localName']
            date = datajson[i]['date']

            countryWide = datajson[i]['global']
            if countryWide:
                countryWide = "Yes"
            else:
                countryWide = "No"

            provinces = datajson[i]['counties']
            if provinces == None:
                strProvince = "ALL"

            else:   #elif type(provinces).__name__ == "list":
                for j in provinces:
                    strProvince += j[3:5] + ", "

            writeHTML(holidayName,date,countryWide,strProvince.rstrip(", "))
            strProvince = ""
        writeScript()
        endBodyHTML()
        print("Successful!")

    else:
        myfile = open("./Assignment 1/myapi.html","w")
        myfile.write("Error has occured")
        myfile.close()

main()