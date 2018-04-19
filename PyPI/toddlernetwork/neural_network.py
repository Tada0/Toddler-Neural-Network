import numpy as np
import csv
from toddlernetwork import nn_exceptions as nne
from time import localtime, strftime


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def dsigmoid(x):
    return x * (1 - x)


class NeuralNetwork:

    def __init__(self, *args):

        try:
            if len(args) == 3 and all(isinstance(param, int) for param in args) and all(param > 0 for param in args):
                self.inputs = args[0]
                self.hidden = args[1]
                self.outputs = args[2]
                self.weights_ih = np.random.rand(self.hidden, self.inputs) * 2 - 1  # Values (-1, 1)
                self.weights_ho = np.random.rand(self.outputs, self.hidden) * 2 - 1  # Values (-1, 1)
                self.bias_h = np.random.rand(self.hidden, 1) * 2 - 1  # Values (-1, 1)
                self.bias_o = np.random.rand(self.outputs, 1) * 2 - 1  # Values (-1, 1)
                self.learning_rate = 0.1
            elif len(args) == 1 and isinstance(args[0], str):
                self.load_network_weights(args[0])
            else:
                raise nne.ConstructorArgumentsException
        except nne.ConstructorArgumentsException:
            nne.ConstructorArgumentsExceptionHandler()

    def set_learning_rate(self, n: float):

        def functionality():
            self.learning_rate = n

        try:
            if (isinstance(n, float) or isinstance(n, int)) and n > 0:
                functionality()
            else:
                raise nne.SetLearningRateException
        except nne.SetLearningRateException:
            nne.SetLearningRateExceptionHandler()

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

        try:
            if isinstance(inputs_array, list) and \
                    (all((isinstance(element, int) or isinstance(element, float)) for element in inputs_array)) and \
                    len(inputs_array) == self.inputs:
                return functionality()
            else:
                raise nne.FeedforwardArgumentsException
        except nne.FeedforwardArgumentsException:
            nne.FeedforwardArgumentsExceptionHandler()

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

        try:
            if isinstance(inputs_array, list) and \
                    (all((isinstance(element, int) or isinstance(element, float)) for element in inputs_array)) and \
                    len(inputs_array) == self.inputs and isinstance(targets_array, list) and \
                    (all((isinstance(element, int) or isinstance(element, float)) for element in targets_array)) and \
                    len(targets_array) == self.outputs:
                functionality()
            else:
                raise nne.TrainArgumentsException
        except nne.TrainArgumentsException:
            nne.TrainArgumentsExceptionHandler()

    def save(self):
        date = strftime("%Y_%m_%d___%H_%M_%S", localtime())
        file_name = date + '___{0}_{1}_{2}'.format(self.inputs, self.hidden, self.outputs)

        with open(file_name, 'w', newline='') as csvfile:
            fieldnames = ['inputs', 'hidden', 'outputs', 'weights_ih',
                          'weights_ho', 'bias_h', 'bias_o', 'rate']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'inputs': self.inputs})
            writer.writerow({'hidden': self.hidden})
            writer.writerow({'outputs': self.outputs})

            for x in range(self.weights_ih.shape[0]):
                for y in range(self.weights_ih.shape[1]):
                    writer.writerow({'weights_ih': self.weights_ih[x][y]})

            for x in range(self.weights_ho.shape[0]):
                for y in range(self.weights_ho.shape[1]):
                    writer.writerow({'weights_ho': self.weights_ho[x][y]})

            for x in range(len(self.bias_h)):
                writer.writerow({'bias_h': self.bias_h[x][0]})

            for x in range(len(self.bias_o)):
                writer.writerow({'bias_o': self.bias_o[x][0]})

            writer.writerow({'rate': self.learning_rate})

    def load_network_weights(self, file: str):

        data = []

        with open(file, newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)

            for row in reader:
                data.append(row)

        self.inputs = int(data[1][0])
        self.hidden = int(data[2][1])
        self.outputs = int(data[3][2])

        index = 4

        self.weights_ih = np.empty((self.hidden, self.inputs), dtype=float)
        self.weights_ho = np.empty((self.outputs, self.hidden), dtype=float)
        self.bias_h = np.empty((self.hidden, 1), dtype=float)
        self.bias_o = np.empty((self.outputs, 1), dtype=float)

        for x in range(self.weights_ih.shape[0]):
            for y in range(self.weights_ih.shape[1]):
                self.weights_ih[x][y] = float(data[index][3])
                index += 1

        for x in range(self.weights_ho.shape[0]):
            for y in range(self.weights_ho.shape[1]):
                self.weights_ho[x][y] = float(data[index][4])
                index += 1

        for x in range(len(self.bias_h)):
            self.bias_h[x][0] = float(data[index][5])
            index += 1

        for x in range(len(self.bias_o)):
            self.bias_o[x][0] = float(data[index][6])
            index += 1

        self.learning_rate = data[index][7]
