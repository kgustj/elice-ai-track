import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

# 시각화 함수
def Visulaize(histories, key="binary_crossentropy"):
    # plt.figure(figsize=(,20))
    for name, history in histories:
        val = plt.plot(history.epoch, history.history["val_" + key], "--", label=name.title() + " Val")
        plt.plot(history.epoch, history.history[key], color=val[0].get_color(), label=name.title() + " Train")

    plt.xlabel("Epochs")
    plt.ylabel(key.replace("_", " ").title())

    plt.legend()
    plt.xlim([0, max(history.epoch)])
