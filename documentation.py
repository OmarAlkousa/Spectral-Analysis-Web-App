# Import the required package
import streamlit as st
from PIL import Image


def add():
    # Set a title of the app
    st.markdown("<h1 style='text-align: center; color: grey;'>Spectral Analysis</h1>",
                unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: grey;'>(Frequency Domain)</h1>",
                unsafe_allow_html=True)
    st.markdown('''
    Digital signal processing (DSP) is the computation of mathematical methods used to manipulate signal data.
    One of the most important tools in digital signal processing is the Discrete Fourier Transform (DFT).
    It is usually used to produce a signal's frequency-domain (spectral) representation.

    The **Fast Fourier Transform (FFT)** is the practical implementation of the Fourier Transform on Digital Signals.
    FFT is considered one of the [**top 10 algorithms**](https://doi.ieeecomputersociety.org/10.1109/MCISE.2000.814652)
    with the greatest impact on science and engineering in the 20th century.

    For more information about Fourier Transform, check out this
    [post](https://medium.com/towards-data-science/learn-discrete-fourier-transform-dft-9f7a2df4bfe9) on Towards Data Science
    and see the how it works mathematically. Also, if you are interested in how to implement the FFT algorithm in Python, follow this
    [post](https://towardsdatascience.com/fourier-transform-the-practical-python-implementation-acdd32f1b96a).

    This web app allows you to decompose your signal data or time series using FFT and gives the opportunity to
    interactively investigate the signal and its spectrum (frequency spectrum, power spectrum, periodogram, and its power spectral density)
    using the advantage of **Plotly** package. All you have to do is to upload the file of the signal **(.csv)** and specify the **sampling rate**.
    Additional properties (optional) can be edited like the title of each time and freuquency figures, the labels of the y-axes,
    and the the color line of each time and frequency data.

    As for the windowing implementation to calculate the periodogram and the power spectral density, the web app offers you to interactively apply 
    windows with specified number of points, number of overlapping points between two successive windows, and special parameters for each window.
    The windows you can use are the same as the windows returned by scipy.signal.get_window() (check out the 
    [link](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html) for more information). Additional tool is added to 
    plot the window which the user wants to apply.

    You can choose if you want to normalize the y-axis (by the number of samples) in the frequency domain. 
    Also, a dB (Decibel) scale of the spectrum is provided.
    #### Note:
    Make sure to specify the exact sampling rate of the signal, otherwise you might end up with the wrong frequency resolution
    (or even worse...👻 **Aliasing** 👻).

    Get the code of this web app following the [**GitHub link**](https://github.com/OmarAlkousa/Fourier-Analysis-as-Streamlit-Web-App.git).
    ''')

    image = Image.open('FFT_per_psd.png')
    st.image(image, use_column_width=True,
             caption='(FFT, Periodogram, PSD) when to use and how to apply using scipy python package. [Image by the Author]')
