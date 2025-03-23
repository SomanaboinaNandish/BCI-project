import os
import mne
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Define the base path to the EDF files
base_path = 'files'

# Function to load EEG data, apply FFT, and plot the frequency spectrum
def plot_fft(subject, record, channel=0):
    edf_path = os.path.join(base_path, subject, f'{subject}{record}.edf')

    if not os.path.exists(edf_path):
        print(f"File not found: {edf_path}")
        return None

    # Load EEG data
    raw = mne.io.read_raw_edf(edf_path, preload=True)
    
    # Extract data from the specified channel
    data, times = raw[channel, :]
    eeg_signal = data[0]  # Extract 1D array

    # Apply FFT
    N = len(eeg_signal)
    fft_result = fft(eeg_signal)
    frequencies = np.fft.fftfreq(N, d=1/raw.info['sfreq'])  # Compute frequency bins

    # Plot FFT results
    plt.figure(figsize=(10, 5))
    plt.plot(frequencies[:N // 2], np.abs(fft_result)[:N // 2])  # Only positive frequencies
    plt.title(f"FFT of EEG Signal ({raw.ch_names[channel]}) - {subject}{record}")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.show()

# Example usage
subject = 'S004'
record = 'R01'
plot_fft(subject, record, channel=0)  # Change 'channel' as needed
