"""
Exercise 1: Identify all needed classes

Answer:
1. Train
2. Stop light
3. Station
"""

"""
Exercise 2: Build the classes

a) Build the Train class
Trains have a specific number of wagons
Trains go in a specific direction “east” or “west”
Trains can go. Print in the console if the train is going and direction.
Trains can give you its specifications. Write a method that prints the number of wagons and the direction

b) Stop light:
Stop lights have a state: “Red” or “Green”, default is red
Method switches the light state.
Method returns the state of the light.



c) Station:
A station has two trains and two stop lights. The trains are defined outside of the class and passed when contructing. The stop lights are created in the class, one should be red and the second one green
Method changes the state of the two lights and print the new state in the console
Method makes a random train go. Use the method randint() of the library random. The station of course checks if the light is green for that train, in the case that the light is red print a message in the console
Stations have the ability to join two trains. Create a static method and return the new joined train. The new train should go west. Print the specifications of the new train.
"""
import random

class Train:
    def __init__(self, num_wagons, direction):
        self.num_wagons = num_wagons
        self.direction = direction

    def go(self):
        print(f"Train is going {self.direction}")

    def specifications(self):
        print(f"Train specifications:\n\tNumber of wagons: {self.num_wagons}\n\tTrain direction: {self.direction}")

    @staticmethod
    def average_speed(time, distance):
        avg_speed = distance / time
        return avg_speed


class StopLight:
    def __init__(self, state="Red"):
        self.state = state

    def change_state(self):
        if self.state == "Red":
            self.state = "Green"
        else:
            self.state = "Red"

    def get_state(self):
        return self.state


class Station:
    def __init__(self, train1, train2):
        # Set the trains
        self.train1 = train1
        self.train2 = train2
        # Create stop lights
        self.light1 = StopLight("Red")
        self.light2 = StopLight("Green")

    def change_light_state(self):
        self.light1.change_state()
        self.light2.change_state()
        print(f"New light state:\n\tLight 1:{self.light1.get_state()}\n\tLight 2: {self.light2.get_state()}")

    def random_train_go(self):
        random_train_nr = random.randint(1, 2)
        if random_train_nr == 1:
            if self.light1.get_state() == "Green":
                self.train1.go()
            else:
                print("Train 1 can't go. Light is red")
        else:
            if self.light2.get_state() == "Green":
                self.train2.go()
            else:
                print("Train 2 can't go. Light is red")

    @staticmethod
    def join_trains(trainA, trainB):
        new_wagons = trainA.num_wagons + trainB.num_wagons
        new_train = Train(new_wagons, "west")
        return new_train


"""
Exercise 3: Create a simulation

a) Create a main method that simulates a station. 
   The Station initializes with two trains going west.

b) Make two random trains go

c) Change the stop light state

d) Make two random trains go

e) Join the two trains

f) Print the new train's specifications

"""


def main():
    # Create two trains
    train1 = Train(4, "west")
    train2 = Train(3, "west")

    # Create a station
    marienplaz = Station(train1, train2)

    # Make trains go
    marienplaz.random_train_go()
    marienplaz.random_train_go()

    # Change light state and make trains go
    marienplaz.change_light_state()
    marienplaz.random_train_go()
    marienplaz.random_train_go()

    # Use static method
    train3 = Station.join_trains(train1, train2)
    train3.specifications()


main()