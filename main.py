# USING MATPLOTLIB
import random
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import time
import csv

#BASE INPUTS
NO_OF_LANES = 3
LENGTH_OF_ROAD = 100 #in meters
TIME_INTERVAL_PER_FRAME = 0.1 #in seconds
LANE_WIDTH = 3.5 #in meters
FREQUENCY_OF_SPAWN = 0.2 #number less than 1 greater than 0, the higher the number the larger vehicles spawned 
CAPACITY = 1800
FREE_FLOW_SPEED = 100
JAM_DENSITY = 120
LCV_PROP = 50
HCV_PROP = 10
T_W_PROP = 30
TH_W_PROP = 10
NUM_VEH_CLASS = 4
NUM_VEH_SIM = 100
VEH_SPAWNED = []
filename = "vehicles_spawned.csv"


class Traffic:
    def __init__(self,lcv,hcv,T_W,Th_W):
        self.lcv = lcv
        self.hcv = hcv
        self.T_W = T_W
        self.Th_W = Th_W

    def Lis_veh_type(self):
        # veh_types = random.randomint(1,NUM_VEH_CLASS)
        veh = []
        # if veh_types == 1:
        veh.append(self.lcv*NUM_VEH_SIM/100) 
        veh.append(self.hcv*NUM_VEH_SIM/100) 
        # if veh_types == 3:
        veh.append(self.T_W*NUM_VEH_SIM/100) 
        # if veh_types == 4:
        veh.append(self.Th_W*NUM_VEH_SIM/100) 
        return veh

# def VEH_CHAR():
    


class Vehicle:
    def __init__(self, id ,lane, speed, accln, length, width, time_update):
        self.id = id
        self.lane = lane
        self.speed = speed
        self.accln = accln
        self.x = 0
        self.time_update = time_update
        self.length = length
        self.width = width

    # def deccelerate(self, vehicles_ahead):
    #     vehicles_ahead = [v for v in vehicles_ahead if v.x > self.x and v.lane == self.lane]
    #     vehicle = vehicles_ahead[0]
    #     if self.speed > vehicles_ahead[0].speed:
    #         self.accln = -1
    
    def move(self,vehicles):
        # if random.random()<0.8:
        #     self.deccelerate(vehicles)
        self.speed += self.accln
        self.x += self.speed
                    
        
    def change_lane(self, vehicles):
        possible_lanes = [i for i in range(sim.num_lanes) if i != self.lane]
        for lane in possible_lanes:
            vehicles_ahead = [v for v in vehicles if v.x > self.x and v.lane == lane]
            if not vehicles_ahead or min(vehicles_ahead, key = lambda v: v.x).x - self.x >= self.length:
                self.lane = lane
                break




class Simulation:
    def __init__(self, num_lanes, length, time_interval, lane_width):
        self.num_lanes = num_lanes
        self.length = length
        self.time_interval = time_interval
        self.vehicles = []
        self.sim_traffic = Traffic(LCV_PROP,HCV_PROP,T_W_PROP,TH_W_PROP).Lis_veh_type()
        self.lane_width = lane_width
    
    # Set of functions to spawn a particular type of vehicle with limits to their movements
    def spw_lcv(self):
        ch = []
        ma_l = 5
        ma_w = 2.5
        mi_l = 3
        mi_w = 1.5
        ma_speed = int(80*5/18)
        mi_speed = int(20*5/18)
        ma_accln = 4
        l = random.randint(mi_l,ma_l)
        w = random.uniform(mi_w,ma_w)
        s = random.randint(mi_speed,ma_speed)
        a = random.randint(0,ma_accln)
        ch.append(l)
        ch.append(w)
        ch.append(s)
        ch.append(a)
        ch.append(0)
        if self.sim_traffic[0] == 0:
            ch[4] = 1
        
        return ch

    def spw_hcv(self):
        ch = []
        ma_l = 12
        ma_w = 4
        mi_l = 10
        mi_w = 2
        ma_speed = int(60*5/18)
        mi_speed = int(10*5/18)
        ma_accln = 2
        l = random.randint(mi_l,ma_l)
        w = random.randint(mi_w,ma_w)
        s = random.randint(mi_speed,ma_speed)
        a = random.randint(0,ma_accln)
        ch.append(l)
        ch.append(w)
        ch.append(s)
        ch.append(a)
        ch.append(1)
        if self.sim_traffic[0] == 0:
            ch[4] = 2

        return ch

    def spw_tw(self):
        ch = []
        ma_l = 3
        ma_w = 1.1
        mi_l = 2
        mi_w = 0.5
        ma_speed = int(60*5/18)
        mi_speed = int(10*5/18)
        ma_accln = 2
        l = random.randint(mi_l,ma_l)
        w = random.uniform(mi_w,ma_w)
        s = random.randint(mi_speed,ma_speed)
        a = random.randint(0,ma_accln)
        ch.append(l)
        ch.append(w)
        ch.append(s)
        ch.append(a)
        ch.append(2)
        if self.sim_traffic[0] == 0:
            ch[4] = 3

        return ch

    def spw_thw(self):
        ch = []
        ma_l = 12
        ma_w = 4
        mi_l = 10
        mi_w = 2
        ma_speed = int(60*5/18)
        mi_speed = int(10*5/18)
        ma_accln = 2
        l = random.randint(mi_l,ma_l)
        w = random.randint(mi_w,ma_w)
        s = random.randint(mi_speed,ma_speed)
        a = random.randint(0,ma_accln)
        ch.append(l)
        ch.append(w)
        ch.append(s)
        ch.append(a)
        ch.append(3)
        if self.sim_traffic[0] == 0:
            ch[4] = 0

        return ch



    def spawn_vehicle(self,INDEX):
        t = random.randint(0,NUM_VEH_CLASS-1)
        lane = random.randint(0, self.num_lanes - 1)
        char = []
        g = None
        if self.sim_traffic[t]>0:        
            if t == 0:
                print(f'{t} Generating lcv')
                char = self.spw_lcv()
                g = char[4]
            if t == 1 or g == 1:
                print(f'{t} Generating hcv')
                char = self.spw_hcv()
                g = char[4]
            if t == 2 or g == 2:
                print(f'{t} Generating 2-wheeler')
                char = self.spw_tw()
                g = char[4]
            if t == 3 or g == 3:
                print(f'{t} Generating 3-wheeler')
                char = self.spw_thw()
                g = char[4]
            self.sim_traffic[t] -= 1
            length = char[0]
            width = char[1]
            speed = char[2]
            acceleration = char[3]
            id = str(INDEX) + "_" + str(length) + "_" + str(width)
            self.vehicles.append(Vehicle(id, lane, speed, acceleration,length, width, self.time_interval))
            VEH_SPAWNED.append(Vehicle(id, lane, speed, acceleration,length, width, self.time_interval))
        
    def vehicles_ahead(self):
        veh_ahead=[] 
        for v in range(len(self.vehicles)-1):
            if self.vehicles[v].x < self.vehicles[v+1].x and self.vehicles[v].lane == self.vehicles[v+1].lane: 
                veh_ahead.append(self.vehicles[v])
                # print(veh_ahead[0].id, veh_ahead[0].x , veh_ahead[0].lane, veh_ahead[0].speed, veh_ahead[0].accln)
        return veh_ahead
    
    def csv_print_vehicles(self):
        rows =[[]]
        with open(filename, 'w', newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            # for v in self.vehicles:
            #     temp = [v.id, v.x, v.lane, v.speed, v.accln, v.length, v.width]
            #     # rows.append(temp)
            #     csvwriter.writerow(temp)
            for v in VEH_SPAWNED:
                temp = [v.id, v.x, v.lane, v.speed, v.accln, v.length, v.width, v.time_update]
                csvwriter.writerow(temp)


    def run(self):
        index = 1
        for i in range(self.length):

            if random.random() < FREQUENCY_OF_SPAWN:
                self.spawn_vehicle(index)
                index+=1


            for v in self.vehicles:
                v.move(self.vehicles)
                if random.random() < 0.1:
                    v.change_lane(self.vehicles)
                self.vehicles[:] = [v for v in self.vehicles if v.x < self.length]
            
            self.visualize()
            time.sleep(self.time_interval)
        
        self.csv_print_vehicles()

    def visualize(self):
        plt.clf()
        for v in self.vehicles:
            plt.gca().add_patch(plt.Rectangle((v.x, v.lane*self.lane_width-v.width/2), v.length, v.width, fill=True))
        plt.xlim(0, self.length)
        plt.ylim(-1, self.num_lanes*self.lane_width)
        plt.pause(0.01)


sim = Simulation(NO_OF_LANES, LENGTH_OF_ROAD, TIME_INTERVAL_PER_FRAME, LANE_WIDTH)

sim.run()
# print(sim.vehicles)
plt.show()
