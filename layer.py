from neuron import Neuron

class Layer:
    def __init__(s,size):
        s.size = size
        s.neurons = []
        for i in range(size):
            s.neurons.append(Neuron())
