from enum import Enum

base_path = '/sent'

class RoutesEnum(Enum):
    PING = base_path + '/ping'
    PREDICT = base_path + '/predict'