# USING MATPLOTLIB
import random
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import time

class Vehicle:
    def __init__(self, lane, speed, accln, length, width, time_update):
        self.lane = lane
        self.speed = speed
        self.accln = accln
        self.x = 0
        self.time_update = time_update
        self.length = length
        self.width = width
        
    def move(self):
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
        self.vehicles.append(Vehicle(lane, speed, acceleration,length, width, self.time_interval))

    def run(self):
        for i in range(self.length):
            if random.random() < 0.1:
                self.spawn_vehicle()
            for v in self.vehicles:
                v.move()
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

sim = Simulation(2, 100, 0.1, 3.5)
sim.run()
plt.show()
