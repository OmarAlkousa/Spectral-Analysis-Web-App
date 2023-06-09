# Import the required packages
import streamlit as st
import viz_spectral as viz
import numpy as np
import Spectral as spec


def calculate(signal, sampling_rate):

    # Apply Spectral class
    signal_spectrum = spec.Spectral(signal, sampling_rate)

    # Configuration of the frequency domain
    with st.expander("Optional Configuration"):
        # Figure Configuration
        ps_title = st.text_input(label='Specify the title of the power spectrum plot:',
                                 value='Power Spectrum', placeholder="'Power Spectrum' By default")
        ps_xlabel = st.text_input(label='Specify the label of x-axis of the power spectrum plot:',
                                  value='Frequency [Hz]', placeholder="'Frequency [Hz]' By default")
        ps_ylabel = st.text_input(label='Specify the label of y-axis of the power spectrum plot:',
                                  value='Unit^2', placeholder="'Unit^2' By default")
        ps_line_color = st.color_picker(
            label='Specify the color of the line chart of the frequency domain:', value='#FF0000', key='c_power_spectrum')

    # Choose if you want to scale the spectrum by the number of the samples
    normalize = st.checkbox(
        'Normalized by N number of samples', key='n_power_spectrum')
    # Calculate the frequency spectrum using Spectral class
    ps = signal_spectrum.power_spectrum(normalize=normalize)

    # Choose if you want to normalize the power spectrum by its maximum value
    normalize_max = st.checkbox(
        'Normalized by the Maximum', key='n_power_spectrum_max')
    if normalize_max:
        ps = ps/ps.max()

    # Choose if you want to represent y-axis in dB
    db = st.checkbox(label='dB', key='c_ps_dB')
    if db:
        ps = 10*np.log10(ps)

    # Plot the power spectrum
    fig2 = viz.viz_spectral(x=signal_spectrum.frequencies,
                            y=ps,
                            title=ps_title,
                            ylabel=ps_ylabel,
                            xlabel=ps_xlabel,
                            line_color=ps_line_color)
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
