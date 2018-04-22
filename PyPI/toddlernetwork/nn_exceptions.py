# __init__ exceptions

def ConstructorArgumentsExceptionHandler_ExecutionAborted():
    print("Object not created, critical error")
    print("Program execution aborted")
    exit(67656972)

def ConstructorArgumentsExceptionHandler_ArgumentsNumber():
    print("Wrong number of the parameters")
    ConstructorArgumentsExceptionHandler_ExecutionAborted()

def ConstructorArgumentsExceptionHandler_ArgumentsType():
    print("Wrong type of the parameters")
    ConstructorArgumentsExceptionHandler_ExecutionAborted()

def ConstructorArgumentsExceptionHandler_ArgumentsSign():
    print("Wrong value of the parameters")
    ConstructorArgumentsExceptionHandler_ExecutionAborted()


# set_learning_rate exceptions

def SetLearningRateExceptionHandler_ExecutionAborted():
    print("Could not change the learning rate value")


def SetLearningRateExceptionHandler_ArgumentType():
    print("Wrong type of the argument")
    SetLearningRateExceptionHandler_ExecutionAborted()


def SetLearningRateExceptionHandler_ArgumentSign():
    print("Wrong value of the learning rate")
    SetLearningRateExceptionHandler_ExecutionAborted()


# feedforward exceptions

def FeedforwardArgumentsExceptionHandler_ExecutionAborted():
    print("Execution of feedforward method aborted")


def FeedforwardArgumentsExceptionHandler_ArgumentType():
    print("Wrong type of the argument")
    FeedforwardArgumentsExceptionHandler_ExecutionAborted()


def FeedforwardArgumentsExceptionHandler_ListElementsType():
    print("Wrong type of list elements")
    FeedforwardArgumentsExceptionHandler_ExecutionAborted()


def FeedforwardArgumentsExceptionHandler_ListLength():
    print("Wrong length of the list")
    FeedforwardArgumentsExceptionHandler_ExecutionAborted()


# train exceptions

def TrainArgumentsExceptionHandler_ExecutionAborted():
    print("Execution of train method aborted")


def TrainArgumentsExceptionHandler_InputsListType():
    print("Wrong type of inputs_array list")
    TrainArgumentsExceptionHandler_ExecutionAborted()


def TrainArgumentsExceptionHandler_InputsListElementsType():
    print("Wrong type of inputs_array elements")
    TrainArgumentsExceptionHandler_ExecutionAborted()


def TrainArgumentsExceptionHandler_InputsListLength():
    print("Wrong length of the inputs_array")
    TrainArgumentsExceptionHandler_ExecutionAborted()


def TrainArgumentsExceptionHandler_TargetsListType():
    print("Wrong type of targets_array list")
    TrainArgumentsExceptionHandler_ExecutionAborted()


def TrainArgumentsExceptionHandler_TargetsListElementsType():
    print("Wrong type of targets_array elements")
    TrainArgumentsExceptionHandler_ExecutionAborted()


def TrainArgumentsExceptionHandler_TargetsListLength():
    print("Wrong length of the targets_array")
    TrainArgumentsExceptionHandler_ExecutionAborted()
