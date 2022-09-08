import csv
import matplotlib.pyplot as plt 
# 时间模块
from datetime import datetime
# 让中文标题显示出来
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

filename = "sitka_weather_2018_simple.csv"
with open(filename) as f:
	# 创建阅读器对象
	reader = csv.reader(f)
	# next返回文件的下一行
	header_row = next(reader)

	lows,highs,dates = [], [],[]
	# 遍历文件的各行
	for row in reader:
		current_date = datetime.strptime(row[2],'%Y-%m-%d')	
		low = int(row[6])	
		high = int(row[5])
		lows.append(low)
		highs.append(high)
		dates.append(current_date)

# 创建图表
# plt.style.use('seaborn')  #出现中文乱码
fig,ax = plt.subplots()
ax.fill_between(dates,highs,lows,facecolor = 'yellow',alpha = 0.1)
ax.plot(dates,highs,c='red')
ax.plot(dates,lows,c = 'blue')

ax.set_title('2018年每日最高温',fontsize = 24)
ax.set_xlabel("时间",fontsize = 14)
ax.set_ylabel("温度（F）",fontsize = 14)
ax.tick_params(axis = 'both',which= 'major',labelsize = 16)

plt.show()
# print(highs)