import cirq
import numpy as np
import matplotlib.pyplot as plt


a = cirq.GridQubit.rect(3, 1)

ops = [
    cirq.X(a[0]), cirq.H(a[2]),
    cirq.X(a[0]), cirq.CNOT(a[0], a[1]), cirq.CCNOT(a[0], a[1], a[2]),
    cirq.measure(a[0], key='m0'), cirq.measure(a[1], key='m1'), cirq.measure(a[2], key='m2')
]
circuit = cirq.Circuit(ops)
print(circuit)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1000)
for i, j in zip(['0x1', '0x2', '0x4'], ['m0', 'm1', 'm2']):
    arr = result.measurements[j].ravel()
    chance_of_1 = np.count_nonzero(arr) / len(arr) * 100
    print(f'{i} chance of 1: {chance_of_1}')

binary_list = np.vstack([result.measurements[x].ravel() for x in ['m0', 'm1', 'm2']])

integer_list = []
for j in binary_list.T:
    integer = 0
    for n, i in enumerate(j):
        integer += i * np.power(2, n)
    integer_list.append(integer)
print(np.mean(integer_list))
plt.hist(integer_list, bins=(-0.5, 0.5, 3.5, 4.5), density=True)
plt.title('Simultaneous subtract')
plt.show()


ops = [
    cirq.X(a[0]), cirq.H(a[2]),
    cirq.measure(a[0], key='m0'), cirq.measure(a[1], key='m1'), cirq.measure(a[2], key='m2'),
    cirq.X(a[0]), cirq.CNOT(a[0], a[1]), cirq.CCNOT(a[0], a[1], a[2]),
    cirq.measure(a[0], key='m3'), cirq.measure(a[1], key='m4'), cirq.measure(a[2], key='m5')
]
circuit = cirq.Circuit(ops)
result = simulator.run(circuit, repetitions=1000)
ix_1 = np.where(result.measurements['m2'].ravel() == 0)[0]
binary_list = np.vstack([result.measurements[x].ravel() for x in ['m3', 'm4', 'm5']])
integer_list = []
for j in binary_list.T[ix_1]:
    integer = 0
    for n, i in enumerate(j):
        integer += i * np.power(2, n)
    integer_list.append(integer)
print(np.mean(integer_list))
plt.hist(integer_list,  density=True)
plt.title('Read then subtract')
plt.show()
