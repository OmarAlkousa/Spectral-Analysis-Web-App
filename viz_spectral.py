# Import the required package
import plotly.express as px
import plotly.graph_objects as go


###########################################
######### Define a plot function ##########
###########################################
def viz_spectral(x,  # x-axis
                 y,  # y-axis
                 title='Frequency Domain',  # Title of the figure
                 ylabel='Amplitude',  # Label of the y-axis
                 xlabel='Frequency [Hz]',  # Label of the x-axis
                 line_color='#FF0000',  # Line Color
                 ):
    # Define the plotly.express figure
    fig = px.line(x=x, y=y)
    fig.update_layout({"title": {"text": title,
                                 "font": {"size": 30, "family": "Times New Roman, bold"},
                                 "x": 0.5,
                                 "xanchor": "center",
                                 "yanchor": "top"},
                       "xaxis": {"title": xlabel},
                       "yaxis": {"title": ylabel},
                       "hovermode": "x unified"
                       })
    fig.update_traces(line_color=line_color,
                      line_width=1,
                      hovertemplate="Frequency= %{x}<br>Amplitude= %{y}")
    return fig


def viz_spectrogram(x,
                    y,
                    Sxx,
                    title='Spectrogram',
                    ylabel='Frequency [Hz]',
                    xlabel='Time [sec]'):

    # Plot heatmap using Plotly Express
    fig = go.Figure(data=go.Heatmap(
        z=Sxx,
        x=x,
        y=y,
        # colorscale='Viridis'
    ))

    fig.update_layout({"title": {"text": title,
                                 "font": {"size": 30, "family": "Times New Roman, bold"},
                                 "x": 0.5,
                                 "xanchor": "center",
                                 "yanchor": "top"},
                       "xaxis": {"title": xlabel},
                       "yaxis": {"title": ylabel},
                       })

    fig.update_traces(
        hovertemplate="Time= %{x}<br>Frequency= %{y}<br>Sxx= %{z}")

    return fig
