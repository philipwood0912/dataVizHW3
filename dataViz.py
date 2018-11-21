import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
men = []
women = []
goldbefore1990 = []
goldafter1990 = []
silverbefore1990 = []
silverafter1990 = []
bronzebefore1990 = []
bronzeafter1990 = []
canadaGold = []
usaGold = []
canadaSilver = []
usaSilver = []
canadaBronze = []
usaBronze = []


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

			if countryData == "CAN":
				if medalData == "Gold":
					if int(yearData) < 1990:
						goldbefore1990.append(medalData)
					else:
						goldafter1990.append(medalData)

				if medalData == "Silver":
					if int(yearData) < 1990:
						silverbefore1990.append(medalData)
					else:
						silverafter1990.append(medalData)

				if medalData == "Bronze":
					if int(yearData) < 1990:
						bronzebefore1990.append(medalData)
					else:
						bronzeafter1990.append(medalData)

			if medalData == "Gold":
				if countryData == "CAN":
					canadaGold.append(medalData)
				if countryData == "USA":
					usaGold.append(medalData)

			if medalData == "Silver":
				if countryData == "CAN":
					canadaSilver.append(medalData)
				if countryData == "USA":
					usaSilver.append(medalData)

			if medalData == "Bronze":
				if countryData == "CAN":
					canadaBronze.append(medalData)
				if countryData == "USA":
					usaBronze.append(medalData)

			if genderData == "Men":
				men.append(genderData)
			else:
				women.append(genderData)
			
			line_count += 1

print('processed', line_count, 'lines of data')
#print(categories)
print("CAN Gold before and after")
goldbefore = goldbefore1990.count("Gold")
print(goldbefore)
goldafter = goldafter1990.count("Gold")
print(goldafter)

print("CAN Silver before and after")
silverbefore = silverbefore1990.count("Silver")
print(silverbefore)
silverafter = silverafter1990.count("Silver")
print(silverafter)

print("CAN Bronze before and after")
bronzebefore = bronzebefore1990.count("Bronze")
print(bronzebefore)
bronzeafter = bronzeafter1990.count("Bronze")
print(bronzeafter)

print("Men vs Women")
print(men.count("Men"))
print(women.count("Women"))

print("CAN vs USA Gold")
print(canadaGold.count("Gold"))
print(usaGold.count("Gold"))

print("CAN vs USA Silver")
print(canadaSilver.count("Silver"))
print(usaSilver.count("Silver"))

print("CAN vs USA Bronze")
print(canadaBronze.count("Bronze"))
print(usaBronze.count("Bronze"))

#print("CAN before and after Gold %")
totalGold = goldafter1990.count("Gold") + goldbefore1990.count("Gold")
#goldBefore_percent = goldbefore1990.count("Gold") / totalGold * 100
#print(goldBefore_percent)
#goldAfter_percent = 100 - goldBefore_percent
#print(goldAfter_percent)

#print("CAN before and After Silver %")
totalSilver = silverafter1990.count("Silver") + silverbefore1990.count("Silver")
#silverBefore_percent = silverbefore1990.count("Silver") / totalSilver * 100
#print(silverBefore_percent)
#silverAfter_percent = 100 - silverBefore_percent
#print(silverAfter_percent)

#print("CAN before and after Bronze %")
totalBronze = bronzeafter1990.count("Bronze") + bronzebefore1990.count("Bronze")
#bronzeBefore_percent = bronzebefore1990.count("Bronze") / totalBronze * 100
#print(bronzeBefore_percent)
#bronzeAfter_percent = 100 - bronzeBefore_percent
#print(bronzeAfter_percent)

print("Men vs Women %")
totalGender = men.count("Men") + women.count("Women")
men_percent = men.count("Men") / totalGender * 100
print(men_percent)
women_percent = 100 - men_percent
print(women_percent)

print("CAN vs USA Gold %")
totalG = canadaGold.count("Gold") + usaGold.count("Gold")
canadaGold_percent = canadaGold.count("Gold") / totalG * 100
print(canadaGold_percent)
usaGold_percent = 100 - canadaGold_percent
print(usaGold_percent)

print("CAN vs USA Silver %")
totalS = canadaSilver.count("Silver") + usaSilver.count("Silver")
canadaSilver_percent = canadaSilver.count("Silver") / totalS * 100
print(canadaSilver_percent)
usaSilver_percent = 100 - canadaSilver_percent
print(usaSilver_percent)

print("CAN vs USA Bronze %")
totalB = canadaBronze.count("Bronze") + usaBronze.count("Bronze")
canadaBronze_percent = canadaBronze.count("Bronze") / totalB * 100
print(canadaBronze_percent)
usaBronze_percent = 100 - canadaBronze_percent
print(usaBronze_percent)

np_medal = 3
before = (bronzebefore, silverbefore, goldbefore)
after = (bronzeafter, silverafter, goldafter)
fig, ax = plt.subplots()
index = np.arange(np_medal)
bar_width = 0.35
opacity = 0.4
error_config = {"ecolor": "0.3"}
rects1 = ax.bar(index, before, bar_width,
                alpha=opacity, color="k",
                error_kw=error_config,
                label="Before")

rects2 = ax.bar(index + bar_width, after, bar_width,
                alpha=opacity, color="g", 
                error_kw=error_config,
                label="After")

ax.set_xlabel("Medals")
ax.set_ylabel("# of Medals")
ax.set_title("Canadian Medals Before and After 1990")
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(("Bronze", "Silver", "Gold"))
ax.legend()

fig.tight_layout()
plt.show()









labels = "Men", "Women"
sizes = [men_percent, women_percent]
colors = ["blue", "pink"]
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Men vs Women in Olympics")
plt.xlabel("Total Men: 3944 Total Women: 1826")
plt.show()
