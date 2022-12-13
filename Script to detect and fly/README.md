Both of these scripts are implemented using a Mission class from the skymission.mission module, which is a subclass of grpc.server, and uses a DroneController class from the skyengine.drone module to control the drone. The start_mission method is to be the main entry point for the mission, and it takes a list of waypoints as input and makes the drone fly to them in sequence. The start_location_log method logs the drone's location to a log file using a DirectLogger from the skylog.logger module.

The idea of this design is to allow the drone to first fly a default route to detect flowers (in this case, a straight line for 6 meters in total.) and then it also allows the user to manually input the location of the target(s) so that it will also fly to assigned locations.

The autodrone script just defines the default route and it is meant to be tested to see if the drone can fly in default routes and also fly towards assigned locations.

The flower_search script added in the connection to the grpc to allow the camera to detect the box which represent the flower in the frame and move to the center of the flower as well as do the operation (in this case, lower the height to 0.5 meter) before moving on to finish the rest of the route.
