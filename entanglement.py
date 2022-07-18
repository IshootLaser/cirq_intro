import cirq
import numpy as np


a = cirq.NamedQubit('a')
b = cirq.NamedQubit('b')

ops = [
    cirq.H(a), cirq.CNOT(a, b),
    cirq.measure(a, key='m0'), cirq.measure(b, key='m1')
]

# entanglement working
circuit = cirq.Circuit(ops)
print(circuit)
simulator = cirq.Simulator()
results = simulator.run(circuit, repetitions=20)
measure_a = results.measurements['m0'].ravel()
measure_b = results.measurements['m1'].ravel()
print(measure_a)
print(measure_b)
print(f'Are a and b equal? {np.equal(measure_a, measure_b).all()}')
