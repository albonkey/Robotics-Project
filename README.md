# Robotics Project
This is a robot project in our class CS4540.

## Setting up Rasberry Pi
### You will need
1. Rasberry Pi 3 or Rasberry Pi 4
2. Micro-sd card with atleast 32 Gb
3. `Balena-Etcher` which is a program for writing software images to usb drives. [Download Link](https://www.balena.io/etcher/)

### Set up SD Card with Ubuntu Mate
1. Go to `https://ubuntu-mate.org/raspberry-pi/download/`
2. Download the `arm64` version.
3. Write the software image you just downloaded on to the micro-sd card with `Balena- Etcher`
4. Insert micro sd into the Rasberry Pi.

### Initalizing the Rasberry Pi
#### Init
1. Start the Rasberry Pi
2. Go through the system configuration and setup

#### Setting up swapfile (For Rasberry Pi 3)
The Pi-3 only has 1Gb of memory, starting a web browser uses more memory than that. The swap file is needed to run heavy memory usage programs.

In the terminal: 
1. `sudo fallocate -l 2G /swapfile`
2. `sudo chmod 600 /swapfile`
3. `sudo swapon /swapfile`
4. `sudo swapon /swapfile`
5. `sudo nano /etc/fstab` and paste the following line: `/swapfile swap swap defaults 0 0`
6. `sudo sysctl vm.swappiness=10`
7. `sudo nano /etc/sysctl.conf` add the line: `vm.swappiness=10`
8. `sudo reboot`

[Read More](https://linuxize.com/post/how-to-add-swap-space-on-ubuntu-20-04/)

#### Stop automatic upgrades
We don't want automatic upgrades to run without warning, so we will disable this in this step.

Run the command `sudo dpkg-reconfigure -plow unattended-upgrades` in your terminal. 

#### Setting up Wifi
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

#### Get rid of some Ubuntu bloat
Removing some stuff we don't need to free up space.
1. `snap list`
2. `sudo snap remove software-boutique`
3. `sudo snap remove ubuntu-mate-pi`
4. `sudo snap remove ubuntu-mate-welcome`
5. `sudo su`
6. `sudo snap remove snapd`
7. `sudo systemctl stop snapd.service`
8. `sudo apt update`
9. `sudo apt remove snapd --purge`
10. `sudo apt autoremove`


[Read More](https://www.addictivetips.com/ubuntu-linux-tips/disable-snaps-ubuntu/ )

#### Upgrading Ubuntu
This can take up to an hour.

Best to do this from the startup terminal

1. `sudo apt update`
2. `sudo apt upgrade`

#### Adding Python Extras
Python3 sould already be installed, we just need to add some python3 extras

1. `sudo apt install python3-pip`
2. `sudo apt install python3-dev`
3. `sudo apt install idle3`

#### Install ROS2 Foxy Fitzroy
Download and install ROS2 Foxy Fitzroy

[Download Link](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Binary.html)

## Design


