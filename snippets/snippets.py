
class Environment:
    """
    The environment is a model of the world that is external to the
    agent and has the responsibility of providing observations and giving
    rewards. It changes state based on the agent's actions
    """
    def __init__(self):
        self.steps_left = 10
