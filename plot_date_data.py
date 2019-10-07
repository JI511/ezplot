# ----------------------------------------------------------------------------------------------------------------------
# Plot Date Data
# ----------------------------------------------------------------------------------------------------------------------

# imports
import matplotlib.pyplot as plot


def create_date_plot(x_data, y_data, title, x_label, y_label):
    """
    Attempts to create a plot with dates for the x axis.

    :param list x_data:
    :param list y_data:
    :param str title:
    :param str x_label:
    :param str y_label:
    :return:
    """
    fig = plot.figure(figsize=(6, 8))
    plot.plot_date(x_data, y_data)
    plot.tick_params('x', labelsize=8, labelrotation=90, direction='out')
    plot.title(title)
    plot.ylabel(y_label)
    plot.xlabel(x_label)
    plot.show()

# ----------------------------------------------------------------------------------------------------------------------
# End
# ----------------------------------------------------------------------------------------------------------------------
