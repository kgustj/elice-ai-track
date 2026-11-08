import numpy as np
import tensorflow as tf
from visual import *
import logging, os

logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
np.random.seed(100)


def OUR_model():
    return tf.keras.Sequential(
        [
            tf.keras.layers.Dense(256, activation="relu"),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )


def main():
    # Fashion mnist data 를 load 합니다.
    train_data = np.loadtxt("./data/train_images.csv", delimiter=",", dtype=np.float32)
    train_labels = np.loadtxt("./data/train_labels.csv", delimiter=",", dtype=np.float32)
    test_data = np.loadtxt("./data/test_images.csv", delimiter=",", dtype=np.float32)
    test_labels = np.loadtxt("./data/test_labels.csv", delimiter=",", dtype=np.float32)

    train_data = train_data / 255.0
    test_data = test_data / 255.0

    our_model = OUR_model()
    opt = tf.keras.optimizers.Adam(lr=0.01, beta_1=0.9, beta_2=0.999)
    our_model.compile(
        optimizer=opt, loss="sparse_categorical_crossentropy", metrics=["accuracy", "sparse_categorical_crossentropy"]
    )

    history = our_model.fit(
        train_data, train_labels, epochs=20, batch_size=500, validation_data=(test_data, test_labels), verbose=2
    )

    scores = our_model.evaluate(test_data, test_labels)
    print("\nscores: ", scores[-1])

    Visulaize([("our_model", history)])

    return history


if __name__ == "__main__":
    main()
