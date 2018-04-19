class ConstructorArgumentsException(Exception):
    pass


class SetLearningRateException(Exception):
    pass


class TrainArgumentsException(Exception):
    pass


class FeedforwardArgumentsException(Exception):
    pass


def ConstructorArgumentsExceptionHandler():
    print("Wrong number or type of parameters")
    print("Object not created")
    exit(67656972)


def SetLearningRateExceptionHandler():
    print("Wrong type or value of learning rate")
    print("Could not change the learning rate value")


def FeedforwardArgumentsExceptionHandler():
    print("Wrong number or type of parameter : inputs_array: list")
    print("inputs_array should contain only int or float types")
    print("Execution of feedforward method aborted")


def TrainArgumentsExceptionHandler():
    print("Wrong number or type of parameters : inputs_array: list, targets_array: list")
    print("inputs_array and targets_array should contain only int or float types")
    print("Execution of train method aborted")
