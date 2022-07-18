import cirq
import numpy as np


a = cirq.NamedQubit('a')
b = cirq.NamedQubit('b')
c = cirq.NamedQubit('c')
d = cirq.NamedQubit('d')

ops = [
    cirq.H(a), cirq.H(b), cirq.H(c), cirq.H(d),
    cirq.rz(np.pi / 4).on(a), cirq.rz(np.pi / 2).on(b), cirq.rz(np.pi).on(c),  # encode data with phase
    # region QFT
    cirq.H(d), cirq.cphase(-np.pi / 2)(c, d), cirq.cphase(-np.pi / 4)(b, d), cirq.cphase(-np.pi / 8)(a, d),
    cirq.H(c), cirq.cphase(-np.pi / 2)(b, c), cirq.cphase(-np.pi / 4)(a, c),
    cirq.H(b), cirq.cphase(-np.pi / 2)(a, b),
    cirq.H(a), cirq.SWAP(a, d),
    cirq.SWAP(b, c),
    # endregion QFT
    cirq.measure((a, b, c, d), key='m')
]

circuit = cirq.Circuit(ops)
print(circuit)
simulator = cirq.Simulator()
results = simulator.run(circuit, repetitions=3)
print(results.measurements['m'])

binary = results.measurements['m'][0].ravel()
integer = 0
for n, i in enumerate(binary):
    integer += i * np.power(2, n)
print(integer)
