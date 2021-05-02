import tensorflow as tf
import streamlit as st


class CustomModel(tf.keras.Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.conv1 = tf.keras.models.Sequential((
            tf.keras.layers.Conv2D(3, 3, padding='same'),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.ReLU()
        ))
        self.conv2 = tf.keras.models.Sequential((
            tf.keras.layers.Conv2D(3, 3, padding='same'),
            tf.keras.layers.BatchNormalization(),
        ))
        self.activation = tf.keras.layers.Softmax()
        self.add = tf.keras.layers.Add()
    
    def call(self, inputs):
        x = self.conv1(inputs)
        x = self.conv2(x)
        x = self.add((x, inputs))
        x = self.activation(x)
        return x


def build_model():
    model = CustomModel()
    return model


def main():
    model = build_model()

    input = tf.keras.Input((224, 224, 3))
    output = model.call(input)
    graph = tf.keras.utils.model_to_dot(
        tf.keras.Model(input, output),
        show_shapes=True,
        expand_nested=False,
        dpi=72
    )
    st.graphviz_chart(str(graph))


if __name__ == '__main__':
    main()