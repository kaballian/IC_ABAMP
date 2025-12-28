import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def rms(values):
    return np.sqrt(np.mean(np.sqrt(values)))
# --- Load data, ignoring the metadata header ---
df = pd.read_csv(
    "waveform_data.txt",
    comment='#',
    skip_blank_lines=True
)

# --- Known offsets from acquisition settings ---
ch1_offset = 0   # +200 mV
ch2_offset = +2.000  # -2 V

# --- Apply offset correction ---
df["Channel 1 (V) - corrected"] = df["Channel 1 (V)"] - ch1_offset
df["Channel 2 (V) - corrected"] = df["Channel 2 (V)"] - ch2_offset



ch1_peak = df["Channel 1 (V)"].max()
ch1_rms = ch1_peak/np.sqrt(2)
in_peak = 20e-3
in_rms = in_peak/np.sqrt(2)
print(f"Channel 1 peak: {ch1_peak:.6f} V")
print(f"Channel 1 RMS: {ch1_rms:.6f} V")
print(f"input peak: {in_peak:.6f} V")
print(f"input RMS: {in_rms:.6f} V")
rms_ratio = ch1_peak / in_peak
print(f"signal gain [RMS]: {rms_ratio:.6f} V")




# --- Plot corrected signals ---
plt.figure()
plt.plot(df["Time (s)"], df["Channel 1 (V) - corrected"], label="Output")
plt.plot(df["Time (s)"], df["Channel 2 (V) - corrected"], label="After differential amp")

plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Digilent WaveForms — Offset-Corrected Signals")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
