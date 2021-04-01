import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
x= range(2,9,2)
#font = {'family':'MicroSoft YaHei'}
y= [5,3,11,5]
plt.plot(x,y,ls = "--",lw = 1,c ="orange",label="good")
list1 = range(1,10)
list2 = range(1,20)
plt.xticks(list1)
plt.yticks(list2)
#plt.xticks(list1,list2,rotation = 90)
plt.xlabel("shijian")
plt.ylabel('good')
plt.title("helleo")
plt.grid(alpha=0.4)



x = range(1,9)
y = range(1,9)
plt.plot(x,y)
plt.plot(x,y)
plt.legend()
plt.show()
