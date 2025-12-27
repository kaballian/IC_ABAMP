import pandas as pd
import matplotlib.pyplot as plt

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
