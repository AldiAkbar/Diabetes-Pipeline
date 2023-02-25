"""
Nama: Aldi Akbar Alimi
Username dicoding: alldinosaur

usage: Transform feature and label data in TFX pipeline
"""

import tensorflow as tf
import tensorflow_transform as tft

NUMERICAL_FEATURES = [
    "HighBP",
    "HighChol",
    "CholCheck",
    "BMI",
    "Smoker",
    "Stroke",
    "HeartDiseaseorAttack",
    "PhysActivity",
    "Fruits",
    "Veggies",
    "HvyAlcoholConsump",
    "AnyHealthcare",
    "NoDocbcCost",
    "GenHlth",
    "MentHlth",
    "PhysHlth",
    "DiffWalk",
    "Sex",
    "Age",
    "Education",
    "Income"
]

LABEL_KEY = "Diabetes_binary"


def transformed_name(key):
    """Renaming transformed features"""
    return key + "_xf"


def replace_nan(tensor):
    """Replace nan value with zero number
    Args:
        tensor (list): list data with na data that want to replace
    Returns:
        list with replaced nan value
    """
    tensor = tf.cast(tensor, tf.float64)
    return tf.where(
        tf.math.is_nan(tensor),
        tft.mean(tensor),
        tensor
    )


def preprocessing_fn(inputs):
    """Preprocess input features into transformed features
    Args:
        inputs (dict): map from feature keys to raw features
    Returns:
        dict: map from features keys to transformed features
    """

    outputs = {}

    for feature in NUMERICAL_FEATURES:
        inputs[feature] = replace_nan(inputs[feature])
        outputs[transformed_name(feature)] = tft.scale_to_0_1(inputs[feature])

    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)

    return outputs
