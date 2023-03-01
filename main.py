# USING MATPLOTLIB
import random
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import time

#BASE INPUTS
NO_OF_LANES = 3
LENGTH_OF_ROAD = 100 #in meters
TIME_INTERVAL_PER_FRAME = 0.1 #in seconds
LANE_WIDTH = 3.5 #in meters
FREQUENCY_OF_SPAWN = 0.7 #number less than 1 greater than 0, the higher the number the larger vehicles spawned 

class Vehicle:
    def __init__(self, id, lane, speed, accln, length, width, time_update):
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
    #     if self.speed < vehicles_ahead:
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
        self.lane_width = lane_width
        
    def spawn_vehicle(self):
        lane = random.randint(0, self.num_lanes - 1)
        speed = random.randint(2, 10)
        acceleration = random.randint(2,3)
        length = random.randint(2, 5)
        width = random.randint(1, 2)
        id = str(length) + "_" + str(width)
        self.vehicles.append(Vehicle(id, lane, speed, acceleration,length, width, self.time_interval))
        

    def vehicles_ahead(self):
        veh_ahead=[] 
        for v in range(len(self.vehicles)-1):
            if self.vehicles[v].x < self.vehicles[v+1].x and self.vehicles[v].lane == self.vehicles[v+1].lane: 
                veh_ahead.append(self.vehicles[v])
                # print(veh_ahead[0].id, veh_ahead[0].x , veh_ahead[0].lane, veh_ahead[0].speed, veh_ahead[0].accln)
        return veh_ahead
    
    def print_vehicles(self):
        for v in self.vehicles:
            print(v.id, v.x, v.lane, v.speed, v.accln, v.length, v.width)

    def run(self):
        for i in range(self.length):
            if random.random() < FREQUENCY_OF_SPAWN:
                self.spawn_vehicle()
                veh = self.vehicles_ahead()
                self.print_vehicles()
            for v in self.vehicles:
                v.move(self.vehicles)
                if random.random() < 0.1:
                    v.change_lane(self.vehicles)
                self.vehicles[:] = [v for v in self.vehicles if v.x < self.length]
            self.visualize()
            time.sleep(self.time_interval)

    def visualize(self):
        plt.clf()
        for v in self.vehicles:
            plt.gca().add_patch(plt.Rectangle((v.x, v.lane*self.lane_width-v.width/2), v.length, v.width, fill=True))
        plt.xlim(0, self.length)
        plt.ylim(-1, self.num_lanes*self.lane_width)
        plt.pause(0.01)


sim = Simulation(NO_OF_LANES, LENGTH_OF_ROAD, TIME_INTERVAL_PER_FRAME, LANE_WIDTH)
sim.run()
plt.show()
