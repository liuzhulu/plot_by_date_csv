# 导入作图module
import matplotlib.pyplot as plt 
# 让中文标题显示出来
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

# 数据输入
input_values= [1,2,3,4,5]
squares = [1,4,9,16,25]
# fig表示整张照片，ax表示各个图表
fig,ax = plt.subplots()
# 设置图片参数增加可读性
ax.plot(input_values,squares,linewidth = 3)
ax.set_title("平方数",fontsize = 24)
ax.set_xlabel("值",fontsize = 14)
ax.set_ylabel("值的平方",fontsize = 14)
ax.tick_params(axis = 'both',labelsize = 14)
plt.show()