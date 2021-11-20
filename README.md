# Robotics-Project

## How to get started

## Setting up Rasberry Pi
### You will need
1. Rasberry Pi 3 or Rasberry Pi 4
2. Micro-sd card with atleast 32 Gb
3. `Balena-Etcher` which is a program for writing software images to usb drives. [Download Link](https://www.balena.io/etcher/)

### Set up SD Card with Ubuntu Mate
1. Go to `https://ubuntu-mate.org/raspberry-pi/download/`
2. Download the `arm64` version.
3. Write the software image you just downloaded on to the micro-sd card with `Balena- Etcher`
4. Insert micro sd into the rasberry pi.

### Initalizing the Rasberry Pi
#### Init
1. Start the Rasberry Pi
2. Go through the system configuration and setup

#### Stop automatic upgrades
We don't want automatic upgrades to run without warning, so we will disable this in this step.
Run the command 'sudo dpkg-reconfigure -plow unattended-upgrades' in your terminal. 

#### Set-up Wifi
Just use the Mate desktop Network Manager for this

#### Configure Ubuntu- Mate to start in a terminal
This step is so the Rasberry Pi starts in a terminal window instead of the Desktop Environment.

Run the following commands in your terminal:
1. `sudo systemctl enable multi-user.target --force`
2. `sudo systemctl set-default multi-user.target`
3. `sudo reboot` This will reboot the system
4. After the system is rebooted run `sudo apt install xinit`
5. Now if you want to run the desktop environment you can use the command `startx`.
6. Run `sudo reboot` again to make sure all the changes are installed

[Read More](https://askubuntu.com/questions/16371/how-do-i-disable-x-at-boot-time-so-that-the-system-boots-in-text-mode)
## Design


