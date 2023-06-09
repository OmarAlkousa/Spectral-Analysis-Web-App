# Import the required packages
import streamlit as st
import numpy as np
import select_window as select
import viz_spectral as viz
import Spectral as spec


def psd(signal, sampling_rate=100.00):

    # Apply Spectral class
    signal_spectrum = spec.Spectral(signal, sampling_rate)

    # Configuration of the periodogram
    with st.expander("Optional Configuration"):
        psd_title = st.text_input(label='Specify the title of the PSD plot:',
                                  value='Power Spectral Density (PSD)', placeholder="'Power Spectral Density (PSD)' By default")
        psd_xlabel = st.text_input(label='Specify the label of x-axis of the PSD plot:',
                                   value='Frequency [Hz]', placeholder="'Frequency [Hz]' By default")
        psd_ylabel = st.text_input(label='Specify the label of y-axis of the PSD plot:',
                                   value='Unit^2/Hz', placeholder="'Unit^2/Hz' By default")
        psd_line_color = st.color_picker(
            label='Specify the color of the line chart of the frequency domain:', value='#FF0000', key='c_psd')

    # Select the size of the window
    psd_window_size = st.number_input(label='Select the size of the window (the number of the samples in each window:',
                                      min_value=1, max_value=len(signal), value=len(signal)//2, key='i_nperseg_psd')

    # Select the number of overlapping samples between two successive windows
    psd_overlapping = st.number_input(label='Select the number of overlapping samples between two successive windows:',
                                      min_value=1, max_value=psd_window_size-1, value=psd_window_size//2, key='i_noverlap_psd')

    psd_window_option = select.select_window(N=psd_window_size, key_='psd')

    # Select the scaling method
    psd_scaling_option = st.selectbox('Select the scaling method apply on the signal',
                                      ('density', 'spectrum'), key='s_scaling_psd',
                                      help="Selects between computing the power spectral density ('density') where the \
                                            output has units of V^2/Hz and computing the power spectrum ('spectrum') where the output\
                                            has units of V^2")

    # Select the scaling averaging method
    psd_averaging_option = st.selectbox('Select the averaging method',
                                        ('mean', 'median'), key='s_averaging_psd')

    # Calculate the Power Spectral Density using Spectral class
    f, psd = signal_spectrum.psd(window=psd_window_option,
                                 scaling=psd_scaling_option,
                                 average=psd_averaging_option,
                                 samples_per_segment=psd_window_size,
                                 samples_overlap=psd_overlapping)

    # Choose if you want to normalize the amplitude by its maximum value
    normalize_max = st.checkbox(
        'Normalized by the Maximum', key='n_psd_max')
    if normalize_max:
        psd = psd/psd.max()

    # Choose if you want to represent y-axis in dB
    db = st.checkbox(label='dB', key='c_psd_dB')

    if db:
        psd = 10*np.log10(psd)

    fig2 = viz.viz_spectral(x=f,
                            y=psd,
                            title=psd_title,
                            ylabel=psd_ylabel,
                            xlabel=psd_xlabel,
                            line_color=psd_line_color)
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
