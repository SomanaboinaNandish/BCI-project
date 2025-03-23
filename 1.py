import os
import mne
import matplotlib.pyplot as plt

# Define the base path to the EDF files
base_path = 'files'

# List of subjects and records
subjects = [f'S{i:03d}' for i in range(1, 110)]
records = [f'R{i:02d}' for i in range(1, 15)]

# Function to load and plot raw vs clean data
def plot_raw_vs_clean(subject, record):
    edf_path = os.path.join(base_path, subject, f'{subject}{record}.edf')
    raw = mne.io.read_raw_edf(edf_path, preload=True)
    
    # Plot raw data
    fig_raw = raw.plot(n_channels=10, scalings='auto', title=f'Raw EEG Signal - {subject}{record}', show=False)
    
    # Apply a band-pass filter to clean the data
    raw.filter(1., 40., fir_design='firwin')
    
    # Plot clean data
    fig_clean = raw.plot(n_channels=10, scalings='auto', title=f'Clean EEG Signal - {subject}{record}', show=False)
    
    return fig_raw, fig_clean

# Function to plot channel-wise data
def plot_channel_wise(subject, record):
    edf_path = os.path.join(base_path, subject, f'{subject}{record}.edf')
    raw = mne.io.read_raw_edf(edf_path, preload=True)
    fig = raw.plot(n_channels=len(raw.ch_names), scalings='auto', title=f'Channel-wise EEG Signal - {subject}{record}', show=False)
    return fig

# Function to plot subject-wise data
def plot_subject_wise(subject):
    figs = []
    for record in records:
        edf_path = os.path.join(base_path, subject, f'{subject}{record}.edf')
        raw = mne.io.read_raw_edf(edf_path, preload=True)
        fig = raw.plot(n_channels=10, scalings='auto', title=f'Subject-wise EEG Signal - {subject}{record}', show=False)
        figs.append(fig)
    return figs

# Example usage for a specific subject and record
subject = 'S001'
record = 'R01'

# Plot raw vs clean data
fig_raw, fig_clean = plot_raw_vs_clean(subject, record)

# Plot channel-wise data
fig_channel_wise = plot_channel_wise(subject, record)

# Plot subject-wise data
figs_subject_wise = plot_subject_wise(subject)

# Show all plots
plt.show()

