import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Function: BPSK BER Calculation
# -------------------------------
def bpsk_ber(snr_db):
    N = 10000
    data = np.random.randint(0, 2, N)
    bpsk = 2*data - 1

    snr_linear = 10**(snr_db/10)
    noise_std = np.sqrt(1/(2*snr_linear))

    noise = noise_std * np.random.randn(N)
    received = bpsk + noise

    demod = (received > 0).astype(int)
    ber = np.sum(data != demod)/N

    return ber

# -------------------------------
# Function: QPSK BER Calculation
# -------------------------------
def qpsk_ber(snr_db):
    N = 10000
    data = np.random.randint(0, 2, N)

    # Group bits into pairs
    data = data.reshape(-1, 2)

    # Mapping (Gray coding)
    mapping = {
        (0,0): 1+1j,
        (0,1): -1+1j,
        (1,1): -1-1j,
        (1,0): 1-1j
    }

    symbols = np.array([mapping[tuple(b)] for b in data])

    snr_linear = 10**(snr_db/10)
    noise_std = np.sqrt(1/(2*snr_linear))

    noise = noise_std * (np.random.randn(len(symbols)) + 1j*np.random.randn(len(symbols)))
    received = symbols + noise

    # Demodulation
    detected = []
    for r in received:
        detected.append([
            0 if r.real > 0 else 1,
            0 if r.imag > 0 else 1
        ])

    detected = np.array(detected)
    detected = detected.reshape(-1)

    original = data.reshape(-1)

    ber = np.sum(original != detected)/len(original)

    return ber

# -------------------------------
# BER vs SNR
# -------------------------------
snr_range = np.arange(0, 11, 1)
bpsk_results = []
qpsk_results = []

for snr in snr_range:
    bpsk_results.append(bpsk_ber(snr))
    qpsk_results.append(qpsk_ber(snr))

# -------------------------------
# Plot BER Graph
# -------------------------------
plt.figure()
plt.semilogy(snr_range, bpsk_results, marker='o', label="BPSK")
plt.semilogy(snr_range, qpsk_results, marker='s', label="QPSK")

plt.title("BER vs SNR (BPSK vs QPSK)")
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.legend()
plt.grid()

plt.show()

# -------------------------------
# Signal Visualization (BPSK)
# -------------------------------
N = 100
data = np.random.randint(0, 2, N)
bpsk = 2*data - 1
noise = np.random.normal(0, 0.5, N)
received = bpsk + noise

plt.figure()
plt.plot(received, label="Noisy Signal")
plt.plot(bpsk, label="Original Signal")
plt.title("BPSK Signal")
plt.legend()
plt.show()

# -------------------------------
# QPSK Constellation Plot
# -------------------------------
N = 1000
data = np.random.randint(0, 2, N).reshape(-1,2)

mapping = {
    (0,0): 1+1j,
    (0,1): -1+1j,
    (1,1): -1-1j,
    (1,0): 1-1j
}

symbols = np.array([mapping[tuple(b)] for b in data])

noise = 0.3 * (np.random.randn(len(symbols)) + 1j*np.random.randn(len(symbols)))
received = symbols + noise

plt.figure()
plt.scatter(received.real, received.imag)
plt.title("QPSK Constellation Diagram")
plt.xlabel("In-phase")
plt.ylabel("Quadrature")
plt.grid()
plt.show()
