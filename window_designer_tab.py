# Import the required packages
import streamlit as st
import select_window as select
import numpy as np
import viz_spectral as viz


def design():
    # Select the window you want to design
    N = st.number_input(label='Specify the number of samples in the window',
                        min_value=1, value=500)

    design_window_option = select.select_window(N=N, key_='design')

    # Plot the time domain
    fig_design = viz.viz_spectral(x=np.arange(0, N),
                                  y=design_window_option,
                                  title='Window',
                                  ylabel='Amplitude',
                                  xlabel='sample',
                                  line_color='#FF0000')
    st.plotly_chart(fig_design, theme="streamlit", use_container_width=True)
