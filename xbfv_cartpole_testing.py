"""
This is a testing script to make sure I have the
ability to capture video of my agent's performance.

make sure you have the correct dependencies:
sudo apt install ffmpeg xvfb

run the following command from the command line:
xvfb-run -s "-screen 0 640x480x24" python3 xbfv_cartpole_testing.py
"""

import gym

if __name__ == '__main__':
    env = gym.make("CartPole-v0")
    env = gym.wrappers.Monitor(env, "recording")

    total_reward: float = 0.0
    total_steps: int = 0
    obs = env.reset()

    while True:
        action = env.action_space.sample()
        _, reward, done, _ = env.step(action)

        total_reward += reward
        total_steps += 1

        if done:
            break

    print(f'Episode done in {total_steps} steps, total reward {round(total_reward, 2)}')

    env.close()
    env.env.close()
