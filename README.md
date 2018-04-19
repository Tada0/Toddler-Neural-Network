Toddler Neural Network
======================

## Build status [![Travis](https://travis-ci.org/Tada0/Toddler-Neural-Network.svg?branch=master)]()

## About

Toddler Neural Network is a simple neural network python library that is easy to use
and fun to play with when you are taking your first steps in machine learning.

- **PyPI (Release history):** https://pypi.org/project/tada0-toddler-neural-network/#history
- **Source:** https://github.com/Tada0/Toddler-Neural-Network
- **Bug reports:** https://github.com/Tada0/Toddler-Neural-Network/issues
- **Author:** https://github.com/Tada0
- **Contact:** <a href="mailto:tomekholda@gmail.com">@</a>

It provides:

- simple single hidden layer neural network
- feedforward and backpropagation methods
- load/save possibility

Installation with ``pip``:

    pip install tada0-toddler-neural-network
    
Example code in ``python``

    # Import the library
    from toddlernetwork import neural_network as NN
    
    # Create Neural Network object with 3 inputs, 2 hidden nodes and 1 output
    network = NN.NeuralNetwork(3, 2, 1)
    
    # Create Neural Network from existing file
    network = NN.NeuralNetwork('filename')
    
    # Use of network methods 
    network.feedforward(inputs_list)
    network.train(inputs_list, answers_list)
    
    # Saving the network to file
    network.save()
    
    # filename example:
    # 2018_04_18___13_21_23___3_2_1
    
## License
    
Toddler Neural Network is licensed under the [MIT License](http://opensource.org/licenses/MIT).
