from layer import Layer

class Network:
    def __init__(s, topology):
        s.topology = topology
        s.layers = []
        for i in topology:
            s.layers.append(Layer(i))
            
