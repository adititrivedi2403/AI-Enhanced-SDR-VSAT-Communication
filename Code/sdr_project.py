import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# -------------------------------
# STEP 1: Generate Binary Data
# -------------------------------
np.random.seed(0)
data = np.random.randint(0, 2, 1000)

# -------------------------------
# STEP 2: BPSK Modulation
# 0 -> -1, 1 -> +1
# -------------------------------
bpsk_signal = 2*data - 1

# -------------------------------
# STEP 3: Add Noise (AWGN)
# -------------------------------
noise = np.random.normal(0, 0.5, len(bpsk_signal))
received_signal = bpsk_signal + noise

# -------------------------------
# STEP 4: Demodulation
# -------------------------------
demodulated = (received_signal > 0).astype(int)

# -------------------------------
# STEP 5: BER Calculation
# -------------------------------
errors = np.sum(data != demodulated)
ber = errors / len(data)

print("BER without AI:", ber)

# -------------------------------
# STEP 6: AI Noise Filtering
# -------------------------------
model = LinearRegression()
x = received_signal.reshape(-1,1)
y = bpsk_signal

model.fit(x, y)
filtered_signal = model.predict(x)

# Demodulate filtered signal
demod_filtered = (filtered_signal > 0).astype(int)

# BER after filtering
errors_filtered = np.sum(data != demod_filtered)
ber_filtered = errors_filtered / len(data)

print("BER with AI:", ber_filtered)

# -------------------------------
# STEP 7: Visualization
# -------------------------------
plt.figure()

plt.plot(received_signal[:100], label="Noisy Signal")
plt.plot(filtered_signal[:100], label="Filtered Signal")

plt.title("SDR Signal Comparison (Noisy vs Filtered)")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.legend()

plt.show()
