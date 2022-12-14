from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket
import exceptions
import math
import argparse
 
#####FUNCTIONS#####
 
def connectMyCopter():
 
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()
    connection_string = args.connect
 
    if not connection_string:
        import dronekit_sitl
        sitl = dronekit_sitl.start_default()
        connection_string = sitl.connection_string()
 
    vehicle = connect(connection_string, wait_ready=True)
 
    return vehicle
 
#####MAIN EXECUTABLE#####
 
vehicle = connectMyCopter()
 
#Version of the autopilot
vehicle.wait_ready('autopilot_version')
print('AutoPilot version: %s' % vehicle.version)
 
#Position
print('Position: %s' % vehicle.location.global_relative_frame)
 
#Attitude
print('Attitude: %s' % vehicle.attitude)
 
#Velocity
print('Velocity: %s' % vehicle.velocity)
 
#Last heartbeat
print('Last heartbeat: %s' % vehicle.last_heartbeat)
 
#Is the vehicle good to arm
print('Is the vehicle good to arm: %s' % vehicle.is_armable)
 
#Flight mode
print('Flight mode: %s' % vehicle.mode.name)
 
#Is the vehicle armed
print('Armed: %s' % vehicle.armed)
 
vehicle.close()
