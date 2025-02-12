# federated_learning/model_training/server.py
import tensorflow_federated as tff

# Updated federated averaging process
def create_federated_process(model_fn):
    return tff.learning.algorithms.build_unweighted_fed_avg(
        model_fn,
        client_optimizer_fn=tf.keras.optimizers.SGD(0.02),
        server_optimizer_fn=tf.keras.optimizers.SGD(1.0)