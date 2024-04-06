import matplotlib.pyplot as plt


def generate_plot(time: int, y, data_type: str) -> plt.figure:
    """
    :param data_type: 'points' lub 'visits'
    :param time
    :param y
    """
    fig, ax = plt.subplot()
    if data_type == 'points':
        ax.set_ylabel('Punkty')
    elif data_type == 'visits':
        ax.set_ylabel('Liczba wizyt')
    ax.scatter(time, y)
    ax.set_xlabel('Czas')
    ax.grid(True)
    fig.savefig('plot.jpg')
