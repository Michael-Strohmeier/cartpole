import gym
import numpy as np
import torch
import time
from random import choice
from PIL import Image


def save_screen_as_img(screen, file_name):
    img = Image.fromarray(screen, 'RGB')
    img = img.resize((64, 64), Image.ANTIALIAS)
    img.save(f"img/{file_name}.jpg")


def main():
    episodes = 100

    env = gym.make("CartPole-v1")
    for episode in range(episodes):
        state = env.reset()
        while True:
            screen = env.render(mode="rgb_array")

            action = choice([0, 1])

            #save_np_arr(screen)
            #time.sleep(5)

            _, reward, done, _ = env.step(action)
            if done:
                break


if __name__ == "__main__":
    main()

