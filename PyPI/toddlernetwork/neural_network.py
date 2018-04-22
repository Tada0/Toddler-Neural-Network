import numpy as np
import pickle
from toddlernetwork import nn_exceptions as nne
from time import localtime, strftime


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def dsigmoid(x):
    return x * (1 - x)


class NeuralNetwork:

    def __init__(self, *args):

        if not len(args) == 3:
            nne.ConstructorArgumentsExceptionHandler_ArgumentsNumber()
            return

        if not all(isinstance(param, int) for param in args):
            nne.ConstructorArgumentsExceptionHandler_ArgumentsType()
            return

        if not all(param > 0 for param in args):
            nne.ConstructorArgumentsExceptionHandler_ArgumentsSign()
            return

        self.inputs = args[0]
        self.hidden = args[1]
        self.outputs = args[2]
        self.weights_ih = np.random.rand(self.hidden, self.inputs) * 2 - 1  # Values (-1, 1)
        self.weights_ho = np.random.rand(self.outputs, self.hidden) * 2 - 1  # Values (-1, 1)
        self.bias_h = np.random.rand(self.hidden, 1) * 2 - 1  # Values (-1, 1)
        self.bias_o = np.random.rand(self.outputs, 1) * 2 - 1  # Values (-1, 1)
        self.learning_rate = 0.1

    def set_learning_rate(self, n: float):

        def functionality():
            self.learning_rate = n

        if not (isinstance(n, float) or isinstance(n, int)):
            nne.SetLearningRateExceptionHandler_ArgumentType()
            return

        if not n > 0:
            nne.SetLearningRateExceptionHandler_ArgumentSign()
            return

        functionality()

    def feedforward(self, inputs_array: list) -> list:

        def functionality():
            inputs = np.array(inputs_array).reshape(len(inputs_array), 1)
            hidden = np.matmul(self.weights_ih, inputs)
            hidden += self.bias_h
            hidden = np.array([*map(sigmoid, hidden)]).reshape(len(hidden), 1)
            outputs = np.matmul(self.weights_ho, hidden)
            outputs += self.bias_o
            outputs = np.array([*map(sigmoid, outputs)]).reshape(len(outputs), 1)
            return outputs.reshape(1, len(outputs))[0]

        if not isinstance(inputs_array, list):
            nne.FeedforwardArgumentsExceptionHandler_ArgumentType()
            return

        if not (all((isinstance(element, int) or isinstance(element, float)) for element in inputs_array)):
            nne.FeedforwardArgumentsExceptionHandler_ListElementsType()
            return

        if not len(inputs_array) == self.inputs:
            nne.FeedforwardArgumentsExceptionHandler_ListLength()
            return

        functionality()

    def train(self, inputs_array: list, targets_array: list):

        def functionality():
            # Thanks for numpy Travis Oliphant
            # Generating the hidden outputs
            # Make vector out of input list
            inputs = np.array(inputs_array).reshape(len(inputs_array), 1)
            hidden = np.matmul(self.weights_ih, inputs)
            hidden += self.bias_h
            # Normalize hidden (-1 ; 1)
            # Call sigmoid function for every element in hidden vector
            hidden = np.array([*map(sigmoid, hidden)]).reshape(len(hidden), 1)
            # Generating the outputs
            outputs = np.matmul(self.weights_ho, hidden)
            outputs += self.bias_o
            # Call sigmoid function for every element in outputs vector
            outputs = np.array([*map(sigmoid, outputs)]).reshape(len(outputs), 1)
            # Make vector out of targets list
            targets = np.array(targets_array).reshape(len(targets_array), 1)
            # Calculate the output error
            # Error = Targets - Outputs
            output_errors = targets - outputs
            # Calculate gradient
            gradients = np.array([*map(dsigmoid, outputs)]).reshape(len(outputs), 1)
            gradients = np.multiply(gradients, output_errors)
            gradients *= self.learning_rate
            # Calculate deltas
            hidden_transposed = np.transpose(hidden)
            weights_ho_deltas = np.matmul(gradients, hidden_transposed)
            self.weights_ho = np.add(self.weights_ho, weights_ho_deltas)
            self.bias_o += gradients[0]
            # Calculate the hidden layer error
            weights_ho_transposed = np.transpose(self.weights_ho)
            hidden_errors = np.matmul(weights_ho_transposed, output_errors)
            hidden = np.array([*map(dsigmoid, hidden)]).reshape(len(hidden), 1)
            # Calculate hidden gradient
            hidden_gradient = np.array([*map(dsigmoid, hidden)]).reshape(len(hidden), 1)
            hidden_gradient = np.multiply(hidden_gradient, hidden_errors)
            hidden_gradient *= self.learning_rate
            # Calculate input -> hidden deltas
            inputs_transposed = np.transpose(inputs)
            weight_ih_deltas = np.matmul(hidden_gradient, inputs_transposed)
            self.weights_ih = np.add(self.weights_ih, weight_ih_deltas)
            self.bias_h += hidden_gradient

        if not isinstance(inputs_array, list):
            nne.TrainArgumentsExceptionHandler_InputsListType()
            return

        if not (all((isinstance(element, int) or isinstance(element, float)) for element in inputs_array)):
            nne.TrainArgumentsExceptionHandler_InputsListElementsType()
            return

        if not len(inputs_array) == self.inputs:
            nne.TrainArgumentsExceptionHandler_InputsListLength()
            return

        if not isinstance(targets_array, list):
            nne.TrainArgumentsExceptionHandler_TargetsListType()
            return

        if not (all((isinstance(element, int) or isinstance(element, float)) for element in targets_array)):
            nne.TrainArgumentsExceptionHandler_TargetsListElementsType()
            return

        if not len(targets_array) == self.outputs:
            nne.TrainArgumentsExceptionHandler_TargetsListLength()
            return

        functionality()

    def save(self):
        global pickle_out

        date = strftime("%Y_%m_%d___%H_%M_%S", localtime())
        file_name = date + '___{0}_{1}_{2}.tnn'.format(self.inputs, self.hidden, self.outputs)

        try:
            pickle_out = open(file_name, "wb")
            pickle.dump(self, pickle_out)
        except IOError:
            print("Could not create file:", file_name)
            exit(9911099102)
        finally:
            pickle_out.close()

    @staticmethod
    def load(file_name: str):
        global pickle_in
        global object_from_pickle

        try:
            pickle_in = open(file_name, "rb")
            object_from_pickle = pickle.load(pickle_in)
        except IOError:
            print("Could not open file", file_name)
            exit(99110111102)
        finally:
            pickle_in.close()

        if object_from_pickle is not None:
            return object_from_pickle
