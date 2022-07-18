import cirq
import numpy as np


a = cirq.NamedQubit('a')
# read it
ops = [cirq.measure(a, key='m')]
circuit = cirq.Circuit(ops)

simulator = cirq.Simulator()
results = simulator.run(circuit, repetitions=20)
item = results.measurements['m'].ravel()
print(item)


b = cirq.NamedQubit('b')
angles = [np.pi, np.pi / 4, np.pi / 2, 2 * np.pi / 3]
funcs = [cirq.rx, cirq.ry, cirq.rz]
for i in angles:
    for j in funcs:
        ops = [j(i).on(b), cirq.measure(b, key='m')]
        circuit = cirq.Circuit(ops)
        results = simulator.run(circuit, repetitions=1000)
        item = results.measurements['m'].ravel()
        print(f'Function {j.__name__}, '
              f'rotation angle {int(i / np.pi * 180)}')
        chance_of_1 = np.count_nonzero(item) / len(item) * 100
        print(f'{chance_of_1}% of the outcomes are 1.')

ops = [cirq.H(b), cirq.H(b), cirq.measure(b, key='m')]
circuit = cirq.Circuit(ops)
results = simulator.run(circuit, repetitions=20)
print(f'A quantum op\'s reverse op is often itself. bs are all {np.max(results.measurements["m"].ravel())}')
