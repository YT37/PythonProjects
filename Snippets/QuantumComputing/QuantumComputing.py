from qiskit import IBMQ, Aer, QuantumCircuit, execute
from qiskit.tools.visualization import plot_bloch_multivector
from qiskit.tools.monitor import job_monitor
from qiskit.visualization import plot_histogram
import math

# Save & Load Account
"""IBMQ.save_account("Enter Auth Key Here")
IBMQ.load_account()
"""

# Provider
"""provider = IBMQ.get_provider("ibm-q")"""

# Getting Backends
"""for backend in provider.backends():
    try:
        qubitCount = len(backend.properties().qubits)
    except:
        qubitCount = "Simulated"

    print(
        f"{backend.name()} Has {backend.status().pending_jobs} Qued and {qubitCount} Qubits"
    )"""

# Circuit
""""circuit = QuantumCircuit(2, 2)
# circuit.x(0)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])"""

# Simulator Backend
"""sim = Aer.get_backend("qasm_simulator")"""

# Backend & Execution
"""backend = provider.get_backend("ibmq_london")
job = execute(circuit, backend=backend, shots=500)
job_monitor(job)

result = job.result()
counts = result.get_counts(circuit)

plot_histogram([counts])"""

# StateVector
"""def doJob(circuit):
    qasm = Aer.get_backend("qasm_simulator")
    sv = Aer.get_backend("statevector_simulator")

    job = execute(circuit, backend=sv)

    result = job.result()
    statevec = result.get_statevector()

    nQubits = circuit.n_qubits
    circuit.measure([i for i in range(nQubits)], [i for i in range(nQubits)])

    jobQ = execute(circuit, backend=qasm, shots=1024).result()
    counts = jobQ.get_counts()

    return statevec, counts


circuit = QuantumCircuit(4, 4)
circuit.h(0)
circuit.h(1)
circuit.rx(math.pi / 4, 2)
circuit.rz(math.pi, 2)
circuit.ry(math.pi, 2)
circuit.cx(2, 3)
circuit.ccx(0, 1, 2)
circuit.barrier()
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.h(3)

statevec, counts = doJob(circuit)

plot_bloch_multivector(statevec)"""
