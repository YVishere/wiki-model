import Scraper
import numpy as np
import matplotlib.pyplot as plt
import Slave
    
def scatter_plot(X, y):
    plt.scatter(X, y)
    plt.show()
    plt.close()
    
def plot_graph(X, y):
    plt.plot(X, y)
    plt.show()
    plt.close()

def new_weights(w, ind,k):
    toRet = (w*ind**(-1/k)) + 1
    return toRet

if __name__ == '__main__':
    print("Starting")
    subject = "Wikipedia"
    result = "Paris"

    uarr = Scraper.startScraping(subject, result)

    print(len(uarr))
    
    basew = np.array([1])
    weights = np.array([])
    weights = np.append(weights, basew)

    for i in range(1, len(uarr)):
        nw = new_weights(basew, i, 5)
        weights = np.append(weights, nw)
    
    #scatter_plot(range(0, len(weights)), weights)

    output = Slave.main(uarr)
    
    print(output)
    scatter_plot(output, weights)
