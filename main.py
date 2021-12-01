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
  sensors = robot.get_sensors()
  if sensors.cliff_front_left or sensors.cliff_front_right: 
    robot.drive_direct(0, 0)
    return False
    
  robot.drive_direct(speed, speed)
  
  return True
  
def moveBackward(robot, speed):
  # Function to move the robot backwards
  robot.drive_direct(-speed, -speed)
  
def moveTurn(robot, degrees):
  # Function to turn the robot 
  robot.drive_direct(100, -100)
  time.sleep(0.1 * degrees)
  robot.drive_direct(0,0)

def playSong(robot, song):
  # Function to play sound
  robot.play_sound(song)

WAIT = 0
MOVEFORWARD = 1
MOVEBACK = 2
TURN = 3

state = MOVEFORWARD

While True:
  # Do some cool stuff
  if state == MOVEFORWARD:
    if(not moveForward(bot, 100)):
      state = TURN
  
  if state == TURN:
    moveTurn(bot, 200)
    state = WAIT
  
  playSong(bot, 2)
    
