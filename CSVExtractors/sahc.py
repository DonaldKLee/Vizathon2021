import csv

countries = ["United States", "Brazil", "South Korea"]
usalistx = []
usalisty = []
brazillistx = []
brazillisty = []
korealistx = []
korealisty = []

with open("csv/stay-at-home-covid.csv") as file:
    for row in file:
        line = row.split(',') # Converts each line into a list
        if line[0] == "United States":
            number = line[3].replace("\n","")
            line.pop(3) # Removes number
            line.append(number) # Adds it back
            usalistx.append(line[2])
            usalisty.append(line[3])

        elif line[0] == "Brazil":
            number = line[3].replace("\n","")
            line.pop(3) # Removes number
            line.append(number) # Adds it back
            brazillistx.append(line[2])
            brazillisty.append(line[3])

        elif line[0] == "South Korea":
            number = line[3].replace("\n","")
            line.pop(3) # Removes number
            line.append(number) # Adds it back
            korealistx.append(line[2])
            korealisty.append(line[3])
        
    from pyecharts.charts import Line
    linegraph = Line()
    linegraph.add_xaxis(usalistx)
    linegraph.add_yaxis("United States", usalisty)
    linegraph.add_yaxis("Brazil", brazillisty)
    linegraph.add_yaxis("South Korea", korealisty)
    linegraph.render("stay-at-home-covid.html")