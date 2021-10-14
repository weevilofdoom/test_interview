from typing import List

class DDP:

    def __init__(self):
        self.shaft_speed = 0
        self.flow_limit = [0, 0]
        self.enable_flow_limit = [False, False]
        self.__cylinder_size = 0.01
        self.__num_of_cylinders = [3, 9]

    @property
    def cylinder_size(self) -> float:
        return self.__cylinder_size

    @property
    def num_of_cylinders(self) -> List[int]:
        return self.__num_of_cylinders

    def set_shaft_speed(self, value: int) -> None:
        self.shaft_speed = value

    def set_flow_limit(self, service: int, value: int) -> None:
        self.flow_limit[service] = value

    def set_enable_flow_limit(self, service: int, value: bool) -> None:
        self.enable_flow_limit[service] = value

    def __calc_req_flow(self, service) -> int:
        return (self.shaft_speed * self.num_of_cylinders[service] * self.cylinder_size)

    def read_actual_flow(self, service) -> int:
        if self.enable_flow_limit[service] and self.__calc_req_flow(service) > self.flow_limit[service]:
            return self.flow_limit[service]
        else:
            return self.__calc_req_flow(service)

    
        

    