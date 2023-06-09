# Import the required packages
import scipy
import streamlit as st


###########################################
####### Window Selection function #########
###########################################
def select_window(window='hann', N=500, key_='periodogram'):

    # Select the window you want to apply on the signal
    window = st.selectbox('Select the window you want to apply on the signal',
                          ('blackman', 'boxcar', 'triang', 'hann', 'hamming', 'bartlett', 'flattop',
                           'parzen', 'bohman', 'blackmanharris', 'nuttall', 'barthann', 'cosine',
                           'lanczos', 'kaiser', 'tukey', 'gaussian', 'general_hamming', 'chebwin',
                           'general_gaussian', 'exponential', 'taylor', 'general_cosine'),
                          key=key_)

    no_params = ['boxcar', 'triang', 'blackman', 'hann', 'hamming', 'bartlett', 'flattop',
                 'parzen', 'bohman', 'blackmanharris', 'nuttall', 'barthann', 'cosine', 'lanczos']
    with_params = ['kaiser', 'tukey', 'gaussian', 'general_hamming', 'chebwin', 'general_gaussian',
                   'exponential', 'taylor', 'general_cosine']

    if window in no_params:
        window_option = scipy.signal.get_window(window=window, Nx=N)

    elif window in with_params:

        # kaiser window parameter
        if window == 'kaiser':
            beta = st.number_input(label='beta',
                                   help='Shape parameter, determines trade-off between main-lobe width and side lobe level. \
                                        As beta gets large, the window narrows.',
                                   min_value=0.0, key='kaiser_'+key_)
            window_option = scipy.signal.get_window(
                window=('kaiser', beta), Nx=N)

        # tukey window parameter
        elif window == 'tukey':
            alpha = st.number_input(label='alpha',
                                    help='Shape parameter of the Tukey window, representing the fraction of the window inside the cosine tapered region. \
                                            If zero, the Tukey window is equivalent to a rectangular window. If one, the Tukey window is equivalent to a Hann window.',
                                    min_value=0.0,
                                    value=0.5, key='tukey_'+key_)
            window_option = scipy.signal.get_window(
                window=('tukey', alpha), Nx=N)

        # gaussian window parameter
        elif window == 'gaussian':
            std = st.number_input(label='std',
                                  help='The standard deviation, sigma.',
                                  value=7.0, key='gaussian_'+key_)
            window_option = scipy.signal.get_window(
                window=('gaussian', std), Nx=N)

        # general_hamming window parameter
        elif window == 'general_hamming':
            alpha = st.number_input(label='alpha',
                                    help='The window coefficient. Both the common Hamming window and Hann window are special cases of the generalized Hamming\
                                          window with $$alpha$$ = 0.54 and $$alpha$$= 0.5, respectively',
                                    min_value=0.0,
                                    value=0.5, key='general_hamming_'+key_)
            window_option = scipy.signal.get_window(
                window=('general_hamming', alpha), Nx=N)

        # chebwin window parameter
        elif window == 'chebwin':
            at = st.number_input(label='at (Attenuation)',
                                 help='Attenuation (in dB)',
                                 value=100, key='chebwin_'+key_)
            window_option = scipy.signal.get_window(
                window=('chebwin', at), Nx=N)

        # exponential window parameters
        elif window == 'exponential':
            tau = st.number_input(label='tau',
                                  help='Parameter defining the decay. For center = 0 use tau = -(M-1) / ln(x) if x is the fraction of the \
                                        window remaining at the end.',
                                  value=1.0, key='exponential_tau_'+key_)
            center = st.number_input(label='center',
                                     help='Parameter defining the center location of the window function. The default value if not given is center = (M-1) / 2',
                                     value=(N-1)/2.0, key='exponential_center_'+key_)

            window_option = scipy.signal.windows.exponential(
                M=N, tau=tau, center=center, sym=False)

        # general_gaussian window parameters
        elif window == 'general_gaussian':
            sigma = st.number_input(label='sig',
                                    help='The standard deviation, sigma.',
                                    value=7.0, key='general_gaussian_sigma'+key_)
            parameter = st.number_input(label='p',
                                        help='Shape parameter. p = 1 is identical to gaussian, p = 0.5 is the same shape as the Laplace distribution.',
                                        value=1.5, key='general_gaussian_parameter'+key_)
            window_option = scipy.signal.windows.general_gaussian(
                M=N, p=parameter, sig=sigma)

        # taylor window parameters
        elif window == 'taylor':
            nbar = st.number_input(label='nbar',
                                   help='Number of nearly constant level sidelobes adjacent to the mainlobe. (Must be integer)',
                                   value=4, key='taylor_nbar_'+key_)
            sll = st.number_input(label='sll',
                                  help='Desired suppression of sidelobe level in decibels (dB) relative to the DC gain of the mainlobe.\
                                      This should be a positive number.',
                                  value=30.0, key='taylor_sll'+key_)
            norm = st.checkbox(label='norm',
                               help='When True (default), divides the window by the largest (middle) value for odd-length windows or the \
                            value that would occur between the two repeated middle values for even-length windows such that all values \
                                are less than or equal to 1. When False the DC gain will remain at 1 (0 dB) and the sidelobes will be sll dB down.',
                               key='taylor_norm'+key_)
            window_option = scipy.signal.windows.taylor(
                M=N, nbar=nbar, sll=sll, norm=norm)

        # general_cosine window parameters
        elif window == 'general_cosine':
            a = [1, 1.942604, 1.340318, 0.440811, 0.043097]
            a = st.experimental_data_editor(
                data=a, key='general_cosine'+key_)

            window_option = scipy.signal.windows.general_cosine(
                M=N, a=a)

    return window_option
