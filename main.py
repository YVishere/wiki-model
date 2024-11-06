import Scraper
import Slave
import numpy as np
import matplotlib.pyplot as plt
import time

    
def scatter_plot(X, y, blockProgram = False):
    plt.figure()
    plt.scatter(X, y)
    plt.show(block = blockProgram)
    
def plot_graph(X, y, blockProgram = False):
    plt.plot(X, y)
    plt.show(block = blockProgram)
    plt.close()

def new_weights(w, ind,k):
    toRet = (w*ind**(-1/k)) + 1
    return toRet

if __name__ == '__main__':
    print("Starting")
    subject = "Wikipedia"
    result = "Paris"

    #Scraping the data
    start = time.time()
    uarr = Scraper.startScraping(subject, result)
    end = time.time()
    print("Time taken to scrape",subject,": ", round(end-start, 3),"seconds")
    
    basewX = np.array([1])
    wX = np.array([])
    wX = np.append(wX, basewX)

    #Processing weights
    for i in range(1, len(uarr)):
        nw = new_weights(basewX, i, 5)
        wX = np.append(wX, nw)

    start = time.time()
    #Extracting number of links from each page
    output = Slave.main(uarr)
    end = time.time()
    print("Time taken: ", round(end-start, 3),"seconds")

    #Plot data
    scatter_plot(range(0, len(wX)), wX)
    scatter_plot(range(0,len(uarr)), output)
    scatter_plot(output, wX, True)
