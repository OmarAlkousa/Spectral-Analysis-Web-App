# Import the required package
import streamlit as st
import numpy as np

# Import the customized functions and modules
import Spectral as spec
import viz_spectral as viz
import window_designer_tab
import psd_tab
import periodogram_tab
import power_spectrum_tab
import frequency_spectrum_tab
import documentation


###########################################
############# Streamlit Code ##############
###########################################

# Add the documentation to explain the web app
documentation.add()
# Horizontal Separator Line
st.markdown("""---""")


######################################
# Import the file of the signal data #
######################################
# Fast Example of the app
st.markdown("### Import the signal file (.csv)")
st.markdown("If you want a fast try of this app and you don't have any signal file, you can download example file that is in the same \
            [**GitHub repository**](https://github.com/OmarAlkousa/Fourier-Analysis-as-Streamlit-Web-App/blob/main/example.csv) of the app. \
            The sampling rate of our example signal is **360.0** sample per second.")

# Upload the file of the signal (only .csv)
uploaded_file = st.file_uploader(
    label="Import the file of the signal (.csv)", type='csv')

# If the file is uploaded
if uploaded_file is not None:

    # Caching the data for faster implementation
    @st.cache_data
    def load_signal():
        sig = np.loadtxt(uploaded_file.name)
        return sig

    # Load the Data
    signal = load_signal()

    # Input the sampling rate of the signal
    sampling_rate = st.number_input(label='Sampling Rate [samples per second]',
                                    help='Specify the exact sampling rate of the signal',
                                    min_value=0.01,)

    ##############################
    # Time Domain Representation #
    ##############################

    # Optional Configuration
    with st.expander("Optional Configuration"):

        # Configuration of the time domain
        t_title = st.text_input(label='Specify the title of the time domain:',
                                value='Time Domain', placeholder="'Time Domain' By default")

        t_xlabel = st.text_input(label='Specify the label of x-axis of the time domain plot:',
                                 value='Time [sec]', placeholder="'Time [sec]' By default")

        t_ylabel = st.text_input(label='Specify the label of y-axis of the time domain plot:',
                                 value='Amplitude', placeholder="'Amplitude' By default")

        t_line_color = st.color_picker(
            label='Specify the color of the line chart of the time domain:', value='#0000FF')

    # Use Spectral Class
    signal_spectrum = spec.Spectral(
        signal=signal, sampling_rate=sampling_rate)

    # Plot the time domain
    fig1 = viz.viz_spectral(x=signal_spectrum.time_axis,
                            y=signal_spectrum.signal,
                            title=t_title,
                            ylabel=t_ylabel,
                            xlabel=t_xlabel,
                            line_color=t_line_color)
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

    ###################################
    # Frequency Domain Representation #
    ###################################

    # Customize the tabs
    frequency_spectrum, power_spectrum, periodogram, psd, design_window = st.tabs(['Frequency Spectrum',
                                                                                   'Power Spectrum',
                                                                                   'Periodogram',
                                                                                   'Power Spectral Density (PSD)',
                                                                                   'Window Designer'])

    ##########################
    # Frequency Spectrum Tab #
    ##########################
    with frequency_spectrum:
        # Apply frequency_spectrum_tab
        frequency_spectrum_tab.calculate(
            signal=signal, sampling_rate=sampling_rate)

    ######################
    # Power Spectrum Tab #
    ######################
    with power_spectrum:
        # Apply power_spectrum_tab
        power_spectrum_tab.calculate(
            signal=signal, sampling_rate=sampling_rate)

    ###################
    # Periodogram Tab #
    ###################
    with periodogram:
        # Apply periodogram_tab
        periodogram_tab.calculate(signal=signal, sampling_rate=sampling_rate)

    ##########################
    # Power Spectral Density #
    ##########################
    with psd:
        # Apply psd_tab
        psd_tab.psd(signal=signal, sampling_rate=sampling_rate)

    ###################
    # Window Designer #
    ###################
    with design_window:
        # Apply window_designer_tab
        window_designer_tab.design()
