# ----------------------------------------------------------------------------------------------------------------------
# Plot Date Data
# ----------------------------------------------------------------------------------------------------------------------

# imports
import matplotlib.pyplot as plot
import numpy as np
import datetime


def create_date_plot(x_data, y_data, title, x_label, y_label):
    """
    Attempts to create a plot with dates for the x axis.

    :param x_data:
    :param y_data:
    :param title:
    :param x_label:
    :param y_label:
    :return:
    """
    print(type(x_data[0]))
    fig, ax = plot.subplots()
    plot.plot_date(x_data, y_data)
    ax.xaxis.set_tick_params(rotation=30, labelsize=10)
    plot.show()

# ----------------------------------------------------------------------------------------------------------------------
# End
# ----------------------------------------------------------------------------------------------------------------------
