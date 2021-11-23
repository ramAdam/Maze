from collections import namedtuple
import pdb

Direction = namedtuple("Direction", "NORTH, SOUTH, EAST, WEST")
Map = namedtuple(
    "Map", "NW, NE, SW, SE, NORTH, SOUTH, EAST, WEST, MID_NORTH, MID_SOUTH, MID_EAST, MID_WEST, MID")
direction = Direction(NORTH="north", SOUTH="south",
                      EAST="east", WEST="west")


map = Map(NW="NW", NE="NE", SW="SW", SE="SE", NORTH="NORTH", SOUTH="SOUTH", EAST="EAST", WEST="WEST",
          MID_NORTH="MID_NORTH", MID_SOUTH="MID_SOUTH", MID_EAST="MID_EAST", MID_WEST="MID_WEST", MID="MID")
