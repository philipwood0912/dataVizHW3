import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
men = []
women = []
medalbefore1990 = []
medalafter1990 = []
canada = []
usa = []

with open('data/medal_data.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print('pushing categories into seperate array')
			categories.append(row)
			line_count += 1
		else:
			yearData = row[0]
			countryData = row[4]
			genderData = row[5]
			medalData = row[7]

			if medalData == "Gold":
				if int(yearData) < 1990:
					medalbefore1990.append(medalData)
				else:
					medalafter1990.append(medalData)
				if countryData == "CAN":
					canada.append(medalData)
				if countryData == "USA":
					usa.append(medalData)

			if genderData == "Men":
				men.append(genderData)
			else:
				women.append(genderData)
			
			line_count += 1

print('processed', line_count, 'lines of data')
#print(categories)
#print(medalbefore1990.count("Gold"))
#print(medalafter1990.count("Gold"))
#print(men.count("Men"))
#print(women.count("Women"))
#print(canada.count("Gold"))
#print(usa.count("Gold"))
totalGold = medalafter1990.count("Gold") + medalbefore1990.count("Gold")
before_percent = medalbefore1990.count("Gold") / totalGold * 100
print(before_percent)
after_percent = 100 - before_percent
print(after_percent)

labels = "Before", "After"
sizes = [before_percent, after_percent]
colors = ["silver", "gold"]
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Gold Medals Before and After 1990!")
plt.xlabel()
plt.show()
