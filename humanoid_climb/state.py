

class State:
    def __init__(self, climber):
        self.climber = climber
        self.joint_positions = dict()
        self.joint_velocities = dict()
        self.base_position = None
        self.base_orientation = None

    def get_current_state(self, client, robot_id):
        pos, ori = client.getBasePositionAndOrientation(robot_id)
