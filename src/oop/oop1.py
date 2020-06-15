# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class



class Vehicle:
    pass

# EXTENDS VEHICLE


class FlightVehicle(Vehicle):
    pass

# EXTENDS VEHICLE


class GroundVehicle(Vehicle):
    pass

# EXTENDS FLIGHTVEHICLE


class Starship(FlightVehicle):
    pass

# EXTENDS GROUNDVEHICLE


class Car(GroundVehicle):
    pass

# EXTENDS GROUNDVEHICLE


class Motorcycle(GroundVehicle):
    pass

# EXTENDS FLIGHTVEHICLE


class Airplane(FlightVehicle):
    pass
