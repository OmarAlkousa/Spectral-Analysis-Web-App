# Import the required package
import scipy
import numpy as np

# Define the class


class Spectral:

    ###########################################
    ######### Initialize the class ############
    ###########################################
    def __init__(self, signal, sampling_rate):
        """
        Initialize the Spectral class.

        Args:
            - signal (np.ndarray): The samples of the signal
            - sampling_rate (float): The sampling per second of the signal

        Additional parameters,which are required to generate Fourier calculations, are
        calculated and defined to be initialized here too:
            - time_step (float): 1.0/sampling_rate
            - time_axis (np.ndarray): Generate the time axis from the duration and
                                    the time_step of the signal. The time axis is
                                    for better representation of the signal.
            - duration (float): The duration of the signal in seconds.
            - frequencies (numpy.ndarray): The frequency axis to generate the spectrum.
            - fourier (numpy.ndarray): The DFT using rfft from the scipy package.
        """

        self.signal = signal
        self.sampling_rate = sampling_rate
        self.time_step = 1.0/self.sampling_rate
        self.duration = len(self.signal)/self.sampling_rate
        self.time_axis = np.arange(0, self.duration, self.time_step)
        self.frequencies = scipy.fft.rfftfreq(
            len(self.signal), d=self.time_step)
        self.fourier = scipy.fft.rfft(self.signal)

    ###########################################
    ########## Frequency Spectrum #############
    ###########################################
    def amplitude(self, normalize=True):
        """
        Method of Spectral class to calculate the amplitude of the spectrum.
        You can choose if the amplitudes are normalized or not by modifying the
        choice of the normalization.

        Args:
            normalize (Boolean): Choose if the amplitudes are normalized or not.
                - normalize=True  --> The amplitudes are normalized by
                                      half of N (the number of samples)
                - normalize=False --> No normalization is applied.

        Returns:
            numpy.ndarray of the actual amplitudes of the sinusoids.
        """
        # Choose if you want the output normalized by the number of samples
        if normalize:
            return 2*(np.abs(self.fourier))/len(self.signal)
        else:
            return np.abs(self.fourier)

    ###########################################
    ##### Power Spectrum (Direct Method) ######
    ###########################################
    def power_spectrum(self, normalize=True):
        """
        Method of Spectral class to calculate the power spectrum.
        The method is the direct method (the square of the amplitudes of FFT).
        You can choose if the amplitudes are normalized or not by modifying the
        choice of the normalization.

        Args:
            normalize (Boolean): Choose if the power spectrum is normalized or not.
                - normalize=True  --> The amplitudes are normalized by
                                      half of N (the number of samples)
                - normalize=False --> No normalization is applied.

        Returns:
            numpy.ndarray of the power spectrum of the signal.
        """
        # Calculate the power spectrum of the signal
        self.Pxx = (np.real(self.fourier*np.conj(self.fourier)))

        # Choose if you want the output normalized by the number of samples
        if normalize:
            return 2*self.Pxx/len(self.signal)
        else:
            return self.Pxx

    ###########################################
    ##### Periodogram (FFT + Windowing) #######
    ###########################################
    def periodogram(self, window='hann', scaling='spectrum'):
        """
        Method of Spectral class to calculate the power spectrum using the periodogram method.

        Args:
            - window (str) : Choose what kind of windowing you want to apply on the input signal.
                             By default, it is set to the window 'hanning' as same as the default
                             window used in scipy.signal.periodogram()
            - scaling (str): Choose if you want the power spectrum using FFT+windowing (the unit is U^2)
                             or the power spectral density (the unit becomes U^2/Hz).
                             By default, it is set to calculate the power spectrum.

        Returns:
            - numpy.ndarray of the periodogram of the signal.
            - numpy.ndarray of the frequency components of the periodogram.
        """

        # Calculate the frequency components and the periodogram of the signal
        self.f_periodogram, self.ps_periodogram = scipy.signal.periodogram(x=self.signal,
                                                                           fs=self.sampling_rate,
                                                                           scaling=scaling,
                                                                           window=window)
        return self.f_periodogram, self.ps_periodogram

    ###########################################
    # Power Spectral Density (Welch's Method) #
    ###########################################
    def psd(self, scaling='density', window='hann', samples_per_segment=None, samples_overlap=None, average='mean'):
        """
        Method of Spectral class to calculate the power spectral density (PSD) using the Welch's method.

        Args:
            - window (str) : Choose what kind of windowing you want to apply on the input signal.
                             By default, it is set to the window 'hanning' as same as the default
                             window used in scipy.signal.welch()
            - scaling (str): Choose if you want the power spectrum using FFT+windowing (the unit is U^2)
                             or the power spectral density (the unit becomes U^2/Hz).
                             By default, it is set to calculate the PSD.
            - samples_per_segment (int): The number of samples in each window to apply the windowing and
                                         calculate the PSD.
                                         By default, it is set to None, the same as the default of scipy.signal.welch(),
                                         which is 256 sample in each window.
            - samples_overlap (int): The number of samples overlapped between two successive windows to calculate the PSD.
                                     By default, it is set to None, the same as the default of scipy.signal.welch(),
                                     which is equal to the half of samples_per_segment (50% Overlapping).
            - average (str): Choose the averaging method to calculate the PSD.

        Returns:
            - numpy.ndarray of the PSD of the signal.
            - numpy.ndarray of the frequency components of the PSD.
        """

        # Calculate the frequency components and the power spectral density of the signal
        self.f_welch, self.psd_welch = scipy.signal.welch(x=self.signal,
                                                          fs=self.sampling_rate,
                                                          scaling=scaling,
                                                          window=window,
                                                          nperseg=samples_per_segment,
                                                          noverlap=samples_overlap,
                                                          average=average)
        return self.f_welch, self.psd_welch
