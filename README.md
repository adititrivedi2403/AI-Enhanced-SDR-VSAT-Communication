# 📡 AI-Enhanced SDR for VSAT Communication

## 📌 Overview
This project simulates a Software Defined Radio (SDR) communication system for satellite (VSAT) channels using Python.

It implements digital modulation, noise simulation, and AI-based noise filtering to improve signal quality.

## 🛠️ Tech Stack
- Python
- NumPy, Matplotlib
- Scikit-learn
- Signal Processing Concepts

## ⚙️ Working

### 1. Data Generation
Random binary data is generated using NumPy.

### 2. Modulation
Binary data is converted into signal using BPSK modulation.

### 3. Channel Simulation
Noise (AWGN) is added to simulate real-world communication.

### 4. Demodulation
Signal is decoded back into binary data.

### 5. BER Calculation
Bit Error Rate is calculated to evaluate performance.

### 6. AI Noise Filtering
Machine learning model is used to reduce noise and improve signal quality.

## 📊 Results
- Improved signal quality after filtering
- Reduced BER using AI model

## 📸 Visualization
![Signal Graph](Images/graph.png)

## 🚀 Features
- BPSK Modulation
- AWGN Channel Simulation
- AI-based Noise Reduction
- BER Analysis

## 🔮 Future Scope
- QPSK Implementation
- Real-time SDR hardware integration
- Deep learning-based filtering
