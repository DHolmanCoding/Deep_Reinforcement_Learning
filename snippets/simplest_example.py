import random


class Environment:
    """
    The environment is a model of the world that is external to the
    agent and has the responsibility of providing observations and giving
    rewards. It changes state based on the agent's actions
    """
    def __init__(self):
        """Initialize the environment's internal state"""
        self.steps_left = 10  # number of steps agent can take in environment

    @staticmethod  # only valid if obs is independent of env
    def get_observations():
        """Return the current environment's observation to the agent"""
        return [0., 0., 0.]  # This effectively means the agent is a blind agent.

    @staticmethod
    def sample_action():
        return [0, 1]

    def is_done(self):
        return self.steps_left == 0

    def perform_action(self, action):
        if self.is_done():
            raise Exception('Game is over')
        self.steps_left -= 1
        return random.random()  # elt of [0, 1]


class Agent:
    def __init__(self):
        self.total_reward = 0.0

    def step(self, env):
        """
        1. Obtains a observation from the model of the environment.
        2. Samples (perhaps selects is a better word depending on the context)
           an action that can be performed.
        3. Performs an action and receives the corresponding reward.
        4. Adds reward to the total reward.
        """
        current_obs = env.get_observation()  # observations are ignored in this example
        actions = env.sample_action()
        reward = env.perform_action(random.choice(actions))
        self.total_reward += reward


if __name__ == '__main__':
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)
