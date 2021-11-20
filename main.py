from  pycreate2 import Create2
import time

# Create a Create2.
port = "/dev/serial"  # where is your serial port?
bot = Create2(port)

# Start the Create 2
bot.start()

# Put the Create2 into 'full' mode so we can drive it
bot.full()



def moveForward(robot, speed):
  # Function to move the robot forward
  
def moveBackward(robot, speed):
  # Function to move the robot backwards
  
def moveTurn(robot, degrees):
  # Function to turn the robot 

def playSound(robot, sound):
  # Function to play sound


While True:
  # Do some cool stuff
