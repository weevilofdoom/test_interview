from ddp.ddp import DDP
import pytest

'''
Digital Displacement pump has 2 services: SERVICE 1 and SERVICE 2.
Each service has assign different number of cylinders:
    * Service 1 has 3 cylinders
    * Service 2 has 9 cylinders.

Size of the cylinder is 0.01

New feature was implemente in the software which allows enable or disable the flow limit and set the limit value
for each service independently. Limit range is from 0 to 100. 

Flow is controlled by the shaft speed:
    FLOW_Sx = SHAFT_SPEED * NUM_OF_CYLINDERS * CYLINDER_SIZE


 * ddp.set_enable_limit(service=0, value=True) -> to enable flow limit on service 1
 * ddp.set_enable_limit(service=1, value=False) -> to disable flow limit on service 2

 * ddp.set_flow_limit(service=0, value=50) -> to set 50 limit on service 1
'''

def test_example(ddp):
    
    # 1. Setup controller
    # - speed
    # - flow value
    # - enable/ disable flow

    ddp.set_shaft_speed(1500)
    ddp.set_flow_limit(service=1, value=50)
    ddp.set_enable_flow_limit(service=1, value=True)

    # 2. Read actual flow
    actual_flow = ddp.read_actual_flow(service=1)

    # Assert the result with expected value
    print(f"Enable flow limit is {True}, flow limit = {50}, actual flow = {actual_flow}")
    assert actual_flow == 50
