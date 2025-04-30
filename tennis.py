import sounddevice as sd
import numpy as np
import scipy.signal as signal
import time
import queue

# Parameters
SAMPLE_RATE = 44100  # Sampling frequency (Hz)
DURATION = 0.5       # Duration of each recording chunk (seconds)
FREQ_MIN = 500       # Minimum frequency of interest (Hz)
FREQ_MAX = 3000      # Maximum frequency of interest (Hz)
THRESHOLD = 0.01     # Amplitude threshold for detection
BLOCK_SIZE = 2048    # Block size for audio processing
COOLDOWN_PERIOD = 0.02  # Cooldown time (20 ms) to detect fast bounces
FILTER_CUTOFF = 300   # High-pass filter cutoff frequency (Hz)

# Global variables
dodge_count = 0
last_detection_time = 0  # Tracks the time of the last detection
audio_queue = queue.Queue()


def high_pass_filter(data, cutoff, fs, order=5):
    """
    Apply a high-pass filter to remove low-frequency (bass) sounds.
    """
    sos = signal.butter(order, cutoff, btype='highpass', fs=fs, output='sos')
    filtered = signal.sosfilt(sos, data)
    return filtered


def process_audio(indata):
    """
    Process the audio data to check for dodge-like sounds.
    """
    global dodge_count, last_detection_time

    # Apply a high-pass filter to remove bass-like sounds
    filtered_data = high_pass_filter(indata.flatten(), FILTER_CUTOFF, SAMPLE_RATE)

    # Perform FFT (Fast Fourier Transform)
    fft_result = np.fft.rfft(filtered_data)
    freqs = np.fft.rfftfreq(len(filtered_data), 1 / SAMPLE_RATE)

    # Focus on specific frequency range
    freq_mask = (freqs >= FREQ_MIN) & (freqs <= FREQ_MAX)
    relevant_amplitudes = np.abs(fft_result[freq_mask])

    # Calculate average amplitude in the range of interest
    avg_amplitude = np.mean(relevant_amplitudes)

    # Check if the amplitude exceeds the threshold
    current_time = time.time()
    if avg_amplitude > THRESHOLD and (current_time - last_detection_time > COOLDOWN_PERIOD):
        dodge_count += 1
        last_detection_time = current_time
        print(f"Dodge detected! Total dodges: {dodge_count}")


def audio_callback(indata, frames, time, status):
    """
    Callback function for real-time audio processing.
    """
    if status:
        print(f"Audio stream error: {status}")
    try:
        audio_queue.put_nowait(indata.copy())  # Send data to the queue for processing
    except queue.Full:
        print("Audio queue is full! Skipping this frame.")


def main():
    """
    Main function to start the dodge counter.
    """
    print("Listening for dodges...")
    with sd.InputStream(callback=audio_callback, channels=1, samplerate=SAMPLE_RATE, blocksize=BLOCK_SIZE):
        while True:
            try:
                # Process audio from the queue
                indata = audio_queue.get_nowait()
                process_audio(indata)
            except queue.Empty:
                pass


if __name__ == "__main__":
    main()
