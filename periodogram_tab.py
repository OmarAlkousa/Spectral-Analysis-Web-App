# Import the required packages
import numpy as np
import streamlit as st
import select_window as select
import Spectral as spec
import viz_spectral as viz


def calculate(signal, sampling_rate):

    # Apply Spectral class
    signal_spectrum = spec.Spectral(signal, sampling_rate)

    # Configuration of the periodogram
    with st.expander("Optional Configuration"):

        # Figure Configuration
        per_title = st.text_input(label='Specify the title of the periodogram plot:',
                                  value='Periodogram', placeholder="'Periodogram' By default")
        per_xlabel = st.text_input(label='Specify the label of x-axis of the periodogram plot:',
                                   value='Frequency [Hz]', placeholder="'Frequency [Hz]' By default")
        per_ylabel = st.text_input(label='Specify the label of y-axis of the periodogram plot:',
                                   value='Unit^2', placeholder="'Unit^2' By default")
        per_line_color = st.color_picker(
            label='Specify the color of the line chart of the frequency domain:', value='#FF0000', key='c_periodogram')

        # Select the window you want to apply on the signal
        # per_selection_window = st.selectbox('Select the window you want to apply on the signal',
        #                                    ('blackman', 'boxcar', 'triang', 'hann', 'hamming', 'bartlett', 'flattop',
        #                                     'parzen', 'bohman', 'blackmanharris', 'nuttall', 'barthann', 'cosine',
        #                                     'lanczos', 'kaiser', 'tukey', 'gaussian', 'general_hamming', 'chebwin',
        #                                     'general_gaussian', 'exponential', 'taylor', 'general_cosine'),
        #                                    key='s_window_periodogram')

    per_window_option = select.select_window(
        N=len(signal), key_='periodogram')

    # Select the scaling
    per_scaling_option = st.selectbox('Select the scaling method apply on the signal',
                                      ('spectrum', 'density'), key='s_scaling_per',
                                      help="Selects between computing the power spectral density ('density') where the \
                                            output has units of V^2/Hz and computing the power spectrum ('spectrum') where the output\
                                            has units of V^2")

    f, periodogram = signal_spectrum.periodogram(
        window=per_window_option, scaling=per_scaling_option)

    # Choose if you want to normalize the periodogram by its maximum value
    normalize_max = st.checkbox(
        'Normalized by the Maximum', key='n_periodogram_max')
    if normalize_max:
        periodogram = periodogram/periodogram.max()

    # Choose if you want to represent y-axis in dB
    db = st.checkbox(label='dB', key='c_periodogram_dB')

    if db:
        periodogram = 10*np.log10(periodogram)

    fig2 = viz.viz_spectral(x=f,
                            y=periodogram,
                            title=per_title,
                            ylabel=per_ylabel,
                            xlabel=per_xlabel,
                            line_color=per_line_color)
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
