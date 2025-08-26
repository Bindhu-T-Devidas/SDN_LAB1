import numpy as np
import matplotlib.pyplot as plt

def random_plot():
    x = np.linspace(0,10,100)
    y = np.sin(x)
    plt.plot(x, y, label="sin(x)")
    plt.legend()
    plt.savefig("plot.png")
    print("Plot saved as plot.png")

if __name__ == "__main__":
    random_plot()
