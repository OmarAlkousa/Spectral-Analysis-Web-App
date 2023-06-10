# Spectral Analysis Web App

[![**Open in Streamlit**](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://omaralkousa-spectral-analysis-web-app-app-yfnwbj.streamlit.app/)

"**Spectral analysis** is based on the Fourier theorem, which states that any waveform can be decomposed into a sum of sine waves at different frequencies with different amplitudes and different phase relationships. When summed, these waves reconstitute the original waveform." [(Walczak & Chokroverty, 2009)](https://doi.org/10.1016/B978-0-7506-7584-0.00012-4)

Spectral analysis can provide valuable insights into the behavior and characteristics of a system or signal. For example, it can be used to identify specific frequencies that are present in a signal, to determine the strength of those frequencies, and to identify any patterns or trends in the data. This information can be used to develop models and algorithms for a wide range of applications, from audio and image compression to medical diagnosis and treatment.

This web app allows you to decompose your signal data or time series using FFT and gives the opportunity to interactively investigate the signal and its spectrum (frequency spectrum, power spectrum, periodogram, and its power spectral density) using the advantage of **Plotly** package. All you have to do is to upload the file of the signal **(.csv)** and specify the **sampling rate**. Additional properties (optional) can be edited like the title of each time and freuquency figures, the labels of the y-axes, and the the color line of each time and frequency data.

As for the windowing implementation to calculate the periodogram and the power spectral density, the web app offers you to interactively apply windows with specified number of points, number of overlapping points between two successive windows, and special parameters for each window. The windows you can use are the same as the windows returned by scipy.signal.get_window() (check out the [link](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html) for more information).

You can choose if you want to normalize the y-axis by the number of samples and/or the maximum amplitude in the frequency domain. Also, a dB (Decibel) scale of the spectrum is provided.

#### Note:
Make sure to specify the exact sampling rate of the signal, otherwise you might end up with the wrong frequency resolution (or even worse...👻 **Aliasing** 👻).

The code is divided into 10 pyhton files. It could've been combined into 1 file but it's easier to edit and review this way.

The 10 python files are:
- **app.py:** The main file that runs the application.
- **Spectral.py:** This is a class built to calculate the basic parameters of the spectral analysis process. The inputs are only the signal data and the sampling rate. And the outputs are the time step, time axis, duration, frequency axis, and the FFT output. Based on this output data, we can now calculate the frequency spectrum, the power spectrum, the periodogram, and the power spectral density (PSD). We use this class to calculate each spectrum in a specific tab in the web app.
- **documentation.py:** To add a proper explanation of the web app.
- **frequency_spectrum_tab.py:** This file is for managing the frequency spectrum output where you can choose the color lines of the plots, type the proper titles and x/y labels of your signal and its spectrum.
- **power_spectrum_tab.py:** To calculate and manage the power spectrum of the signal and visualize it in a single tab.
- **periodogram_tab.py:** Calculate the periodogram of the signal using scipy.signal.periodogram and visualize it in a single tab. Also, a proper selection of the window used to calculate the periodogram has been added.
- **psd_tab.py:** Calculate the power spectral density (PSD) of the signal using scipy.signal.welch and visualize it in a singla tab. Also a proper selection of the window used to calculate the PSD has been added.
- **window_designer_tab.py:** This file is built to design and visualize the windows you might use to calculate the periodogram and the PSD of the signal.
- **select_window.py:** This file is used in three other files (periodogram_tab.py, psd_tab.py, and window_designer_tab.py). The aim of this file is to manage a proper selection of the window.
- **viz_spectral.py:** This file is used in four other files (frequency_spectrum_tab.py, power_spectrum_tab.py, periodogram_tab.py, and psd_tab.py). The aim of this file is to visualize the spectrum of each type easily.
