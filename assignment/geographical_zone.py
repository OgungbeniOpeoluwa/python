from enum import Enum


class Geographical_zone(Enum):
    NORTHCENTRAL = ["BENUE", "FCT", "KOGI", "KWARRA", "NASARAWA", "NIGER", "PLATEU"]
    NORTHEAST = ["ADAMAWA", "BAUCHI", "BORNO", "GOMBE", "TARABA", "YOBE"]
    NORTHWEST = ["KADUNA", "KASTINA", "KANO", "KEBBI", "SOKOTO", "JIGAWA", "ZAMFARA"]
    SOUTHEAST = ["ABIA", "ANAMBRA", "EBONYI", "ENUGU", "IMO"]
    SOUTHSOUTH = ["AKWA IBOM", "BAYELSA", "CROSS RIVER", "DELTA", "EDO", "RIVERS"]
    SOUTHWEST = ["EKITI", "LAGOS", "OSUN", "ONDO", "OGUN", "OYO"]


def find_state(result):
    for zone in Geographical_zone:
        for index in zone.value:
            if index == result.upper():
                return zone.name



