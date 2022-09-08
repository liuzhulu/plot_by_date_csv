import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "death_valley_2018_simple.csv"
with open(filename) as f:
	# 创建阅读器对象
	reader = csv.reader(f)
	# next返回文件的下一行
	header_row = next(reader)

	lows,highs,dates = [], [],[]

	for row in reader:
		current_date = datetime.strptime(row[2],'%Y-%m-%d')
		try:
			low = int(row[5])	
			high = int(row[4])
		except ValueError:
			print(f"Missing date for {current_date}")
		else:
			lows.append(low)
			highs.append(high)
			dates.append(current_date)

fig,ax = plt.subplots()
ax.fill_between(dates,highs,lows,facecolor = 'yellow',alpha = 0.1)
ax.plot(dates,highs,c='red')
ax.plot(dates,lows,c = 'blue')

ax.set_title('2018年每日最高温',fontsize = 24)
ax.set_xlabel("时间",fontsize = 14)
ax.set_ylabel("温度（F）",fontsize = 14)
ax.tick_params(axis = 'both',which= 'major',labelsize = 16)

plt.show()

# print(header_row)