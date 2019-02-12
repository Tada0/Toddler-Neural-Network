import unittest
from toddlernetwork import neural_network as NN
from toddlernetwork import nn_exceptions as nne


class TestNeuralNetwork(unittest.TestCase):

    def test_NN__init__(self):
        self.assertRaises(SystemExit, NN.NeuralNetwork, (1, 1, -1))
        self.assertRaises(SystemExit, NN.NeuralNetwork, (1, -1, 1))
        self.assertRaises(SystemExit, NN.NeuralNetwork, (-1, 1, 1))
        self.assertRaises(SystemExit, NN.NeuralNetwork, (1, 1, 0))
        self.assertRaises(SystemExit, NN.NeuralNetwork, (1, 0, 1))
        self.assertRaises(SystemExit, NN.NeuralNetwork, (0, 1, 1))
        self.assertRaises(SystemExit, NN.NeuralNetwork, (-1, 1, 1, 1))
        self.assertRaises(SystemExit, NN.NeuralNetwork, (-1, 1))
        self.assertRaises(SystemExit, NN.NeuralNetwork, (1, 1, "1"))
        self.assertRaises(SystemExit, NN.NeuralNetwork, (1, [1], 1))
        self.assertRaises(SystemExit, NN.NeuralNetwork, (True, 1, 1))
        self.assertRaises(SystemExit, NN.NeuralNetwork, (-1, 1.2, 1))
        self.assertIsInstance(NN.NeuralNetwork(1, 1, 1), NN.NeuralNetwork)
        self.assertIsInstance(NN.NeuralNetwork(1, 10, 1), NN.NeuralNetwork)

    def test_NN_set_learning_rate(self):
        test_object = NN.NeuralNetwork(1, 1, 1)
        test_object.set_learning_rate(0.01)
        self.assertEqual(test_object.learning_rate, 0.01)

    def test_sigmoid(self):
        self.assertEqual(NN.sigmoid(0), 0.5)
        self.assertTrue(NN.sigmoid(-1) < 0.5)
        self.assertTrue(NN.sigmoid(1) > 0.5)
        self.assertAlmostEqual(NN.sigmoid(10), 0.9999546)
        self.assertAlmostEqual(NN.sigmoid(-10), 0.00004539)

    def test_dsigmoid(self):
        self.assertEqual(NN.dsigmoid(0), 0)
        self.assertEqual(NN.dsigmoid(1), 0)
        self.assertEqual(NN.dsigmoid(0.5), 0.25)
        self.assertTrue(NN.dsigmoid(1.01) < 0)
        self.assertTrue(NN.dsigmoid(-0.01) < 0)
        self.assertTrue(NN.dsigmoid(10) < 0)
        self.assertTrue(NN.dsigmoid(-10) < 0)
