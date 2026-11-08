import numpy as np
import tensorflow as tf
from visual import *
import logging, os
from dataloader import load_data

logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
np.random.seed(100)
tf.random.set_seed(100)


def Develop():
    return tf.keras.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(64, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(0.001)),
            tf.keras.layers.Dense(128, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(0.001)),
            tf.keras.layers.Dense(256, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(0.001)),
            tf.keras.layers.Dense(512, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(0.001)),
            tf.keras.layers.Dense(1024, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(0.001)),
            tf.keras.layers.Dropout(0.4),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )


def main():
    # Fashion-MNIST 데이터를 불러오고 전처리하는 부분입니다.
    (train_images, train_labels), (test_images, test_labels) = load_data()

    train_images = train_images / 255.0
    test_images = test_images / 255.0

    develop_model = Develop()
    develop_model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    develop_model.summary()

    history = develop_model.fit(
        train_images, train_labels, epochs=20, batch_size=500, validation_data=(test_images, test_labels), verbose=0
    )

    scores = develop_model.evaluate(test_images, test_labels, verbose=0)
    print("\naccuracy_develop: ", scores[-1])

    Visulaize([("Develop", history)])

    return history


if __name__ == "__main__":
    main()

