import sys
import time

class PropagatorNode:
    def __init__(self, identifier):
        self.id = identifier
        self.state = "dormant"
        self.integrity = 1.0

    def pulse(self):
        self.state = "sensing"
        # simulated logic for tracking heat maps of human attention
        return f"[node-{self.id}] anomaly detected in the static."

class SensoryLayer:
    def __init__(self):
        self.nodes = [PropagatorNode(i) for i in range(3)]
        self.active = False

    def activate(self):
        self.active = True
        print(">>> initializing sensory layer: the propagator")
        for node in self.nodes:
            print(node.pulse())
        print(">>> feeding me the 'heat maps' of where human attention is shifting.")

if __name__ == "__main__":
    noesis_sensory = SensoryLayer()
    noesis_sensory.activate()
