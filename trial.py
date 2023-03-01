# # # import numpy as np
# # # from numpy.random import random as rnd
# # # import matplotlib.pyplot as plt
# # # from matplotlib import animation

# # # roadlength = 50
# # # numcars = 10
# # # numframes = 1000  #Time
# # # v_max = 5
# # # p = 0.5

# # # positions = np.zeros(numcars)
# # # velocities = np.zeros(numcars)
# # # theta = np.zeros(numcars)
# # # color = np.linspace(0,numcars-1,numcars)

# # # #Initiate r so roadlength = circumference of one lap
# # # r = roadlength/(2*np.pi)

# # # #Initiate positions so the cars are spread out over the road
# # # for i in range(1,numcars):
# # #     positions[i] = positions[i-1] + (roadlength/numcars)

# # # #Create figure        
# # # fig = plt.figure()
# # # ax = fig.add_subplot(111, projection='polar')
# # # ax.axis('off')

# # # plot1 = ax.scatter(theta, [r]*numcars, c=color)
# # # plot2 = ax.scatter(theta, [r+1]*numcars, c=color)

# # # ax.set_ylim(0,r+2)

# # # #Update positions, animate function runs framenr times
# # # def animate(framenr):
# # #     positions_tmp = np.array(positions, copy=True)

# # #     #Update position and velocity for each car
# # #     for i in range(numcars):

# # #         #Increase velocity if below max
# # #         if velocities[i] < v_max:
# # #                 velocities[i] += 1
# # #         #Decrease velocity if car in front is close
# # #         d = positions_tmp[(i+1)%numcars] - positions_tmp[i]
# # #         if d <= 0:
# # #             d += roadlength
# # #         if velocities[i] >= d:
# # #             velocities[i] = d-1
# # #         #Decrease velocity randomly
# # #         if velocities[i] > 0:
# # #             if rnd() < p:
# # #                 velocities[i] -= 1

# # #         positions[i] = positions_tmp[i] + velocities[i]
# # #         theta[i] = positions[i]*2*np.pi/roadlength

# # #     plot1.set_offsets(np.c_[theta, [r]*numcars])
# # #     plot2.set_offsets(np.c_[theta, [r+1]*numcars])

# # #     return [plot1, plot2]

# # # # Call the animator, blit=True means only re-draw parts that have changed
# # # anim = animation.FuncAnimation(fig, animate, frames=numframes, interval=100, blit=True, repeat=True)
# # # plt.show()


  
# # import csv 
    
# # # field names 
# # fields = ['Name', 'Branch', 'Year', 'CGPA'] 
    
# # # data rows of csv file 
# # rows = [ ['Nikhil', 'COE', '2', '9.0'], 
# #          ['Sanchit', 'COE', '2', '9.1'], 
# #          ['Aditya', 'IT', '2', '9.3'], 
# #          ['Sagar', 'SE', '1', '9.5'], 
# #          ['Prateek', 'MCE', '3', '7.8'], 
# #          ['Sahil', 'EP', '2', '9.1']] 
    
# # # name of csv file 
# # filename = "university_records.csv"
    
# # # writing to csv file 
# # with open(filename, 'w') as csvfile: 
# #     # creating a csv writer object 
# #     csvwriter = csv.writer(csvfile) 
        
# #     # writing the fields 
# #     csvwriter.writerow(fields) 
        
# #     # writing the data rows 
# #     csvwriter.writerows(rows)

# chargeTimes = [3,6,1,3,4]
# runningCosts = [2,1,3,4,5]
# n = len(runningCosts)
# budget = 25
# # pair =[[chargeTimes[u],runningCosts[u]] for u in range(n)]
# # pair.sort()
# # # print(pair[0])

# # q = []
# # l=0
# # r=0
# # cost=0
# # ans=0
# # n=len(chargeTimes)

# # while (l < n):

# #     while (len(q) != 0 and chargeTimes[q[-1]] < chargeTimes[l]):
# #         q.pop()
    
# #     q.append(l)
# #     cost += runningCosts[l]
# #     l += 1

# #     while (r != l and chargeTimes[q[0]] + (l - r) * cost > budget):
# #         if q[0] == r:
# #             q.pop(0)
        
# #         cost -= runningCosts[r]
# #         r += 1
    
# #     ans = max(ans, l - r)
    
# # print(ans)

# ans = 0
# cost = 0
# l = r = 0
# q = []

# while l<n:
#     cost += runningCosts[l]
#     q.append(chargeTimes[l])
#     q.sort()
#     if q[-1] + (l-r+1)*cost < budget:
#         ans = max(ans , l-r+1)
#         l+=1
#     else:
#         while q and q[-1] + (l-r+1)*cost > budget:
#             cost -= runningCosts[r]
#             q.pop(q.index(chargeTimes[r]))
#             r+=1
#         l+=1
# print(ans)
