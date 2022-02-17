def fig_params():
    import matplotlib.pyplot as plt
    
    large = 28; med = 24; small = 15
    params = {'axes.titlesize': small,
          'legend.fontsize': 10,
          'figure.figsize': (8, 4),
          'axes.labelsize': small,
          'axes.titlesize': small,
          'xtick.labelsize': small,
          'ytick.labelsize': small,
          'figure.titlesize': med,
          'axes.titlepad': 10}
    plt.rcParams.update(params)