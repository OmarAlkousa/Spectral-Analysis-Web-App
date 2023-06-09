# Import the required packages
import streamlit as st
import numpy as np
import viz_spectral as viz
import Spectral as spec


def calculate(signal, sampling_rate):

    # Apply Spectral class
    signal_spectrum = spec.Spectral(signal=signal, sampling_rate=sampling_rate)

    # Configuration of the frequency domain
    with st.expander("Optional Configuration"):
        f_title = st.text_input(label='Specify the title of the frequency domain:',
                                value='Frequency Spectrum', placeholder="'Frequency Spectrum' By default")
        f_xlabel = st.text_input(label='Specify the label of x-axis of the frequency spectrum plot:',
                                 value='Frequency [Hz]', placeholder="'Frequency [Hz]' By default")
        f_ylabel = st.text_input(label='Specify the label of y-axis of the frequency domain plot:',
                                 value='Amplitude', placeholder="'Amplitude' By default")
        f_line_color = st.color_picker(
            label='Specify the color of the line chart of the frequency domain:', value='#FF0000', key='c_frequency_spectrum')

    # Choose if you want to scale the spectrum by the number of the samples
    normalize = st.checkbox(
        'Normalized by N number of samples', key='n_frequency_spectrum')
    # Calculate the frequency spectrum using Spectral class
    amplitude = signal_spectrum.amplitude(normalize=normalize)

    # Choose if you want to normalize the amplitude by its maximum value
    normalize_max = st.checkbox(
        'Normalized by the Maximum', key='n_frequency_spectrum_max')
    if normalize_max:
        amplitude = amplitude/amplitude.max()

    # Choose if you want to represent y-axis in dB
    db = st.checkbox(label='dB', key='c_frequency_dB')
    if db:
        amplitude = 10*np.log10(amplitude)

    # Plot the frequency amplitude
    fig2 = viz.viz_spectral(x=signal_spectrum.frequencies,
                            y=amplitude,
                            title=f_title,
                            ylabel=f_ylabel,
                            xlabel=f_xlabel,
                            line_color=f_line_color)
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
