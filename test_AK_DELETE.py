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

def calc_speed_for_flow(flow: int, no_cyl: int) -> float:
    return (flow/(no_cyl * 0.01))

# def test_example(ddp):
    
#     # 1. Setup controller
#     # - speed
#     # - flow value
#     # - enable/ disable flow

#     ddp.set_shaft_speed(1500)
#     ddp.set_flow_limit(service=1, value=50)
#     ddp.set_enable_flow_limit(service=1, value=True)

#     # 2. Read actual flow
#     actual_flow = ddp.read_actual_flow(service=1)

#     # Assert the result with expected value
#     print(f"Enable flow limit is {True}, flow limit = {50}, actual flow = {actual_flow}")
#     assert actual_flow == 50


@pytest.mark.parametrize(
    "flow_limit, flow_sp, expected_flow, flow_limit_en, no_cyl, act_service",
    [
        pytest.param(50, 55, 50, True, 3, 0, id="TC01"),
        pytest.param(45, 55, 45, True, 3, 0, id="TC02"),
        pytest.param(30, 75, 75, False, 3, 0, id="TC03"),
    ]
)
def test_flow_limit(ddp: DDP, flow_limit: int, flow_sp: int, expected_flow: int, flow_limit_en: bool, no_cyl: int, act_service: int):
    print(f"speed = {calc_speed_for_flow(flow_sp, no_cyl)}")
    ddp.set_shaft_speed(calc_speed_for_flow(flow_sp, no_cyl))
    ddp.set_flow_limit(service=act_service, value = flow_limit)
    ddp.set_enable_flow_limit(service=act_service, value = flow_limit_en)
    act_flow = ddp.read_actual_flow(service=act_service)
    
    print(f"Enable flow limit is {flow_limit_en}, flow limit = {flow_limit}, actual flow = {act_flow}")
    assert expected_flow == act_flow