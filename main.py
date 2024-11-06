from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process, Manager
import multiprocessing as mp


def dontCheck(url):
    if url.find("#")!=-1:
        return True
    if url.find("/wiki/")==-1:
        return True
    if url.find(".jpg")!=-1 or url.find(".ogg")!=-1 or url.find(".svg")!=-1 or url.find(".png")!=-1 or url.find(".jpeg")!=-1 or url.find(".gif")!=-1:
        return True
    if url.find("Help:")!=-1 or url.find(":")!=-1:
        return True
    if url.find("https")!=-1:
        return True
    if (url.find("commons") != -1 or url.find("_(identifier)") != -1):
        return True
        
    return False

def algorithm(subject, result):
    arr = np.array([])
    try:
        data = requests.get(subject)
        soup = BeautifulSoup(data.text, "html.parser")
        tags=soup.find(id="bodyContent").find_all("a")
        for tag in tags:
            s=tag.get('href', None)
            if (dontCheck(s)):
                continue
            ns = s[s.rfind("/")+1:]
            if s.find("https")==-1:
                s="https://en.wikipedia.org"+s
            if s.lower()==result.lower():
                print("Found")
                break
            arr = np.append(arr, ns)
        return arr
    except AttributeError:
        return arr
    
def scatter_plot(X, y):
    plt.scatter(X, y)
    plt.show()
    plt.close()
    
def plot_graph(X, y):
    plt.plot(X, y)
    plt.show(block = False)
    plt.close()

def new_weights(w, ind,k):
    toRet = (w*ind**(-1/k)) + 1
    return toRet

def algo2(subject):
    subject = "https://en.wikipedia.org/wiki/"+subject
    try:
        data = requests.get(subject)
        soup = BeautifulSoup(data.text, "html.parser")
        tags=soup.find(id="bodyContent").find_all("a")
        return len(tags)
    except AttributeError:
        return 0

if __name__ == '__main__':
    print("Starting")
    subject = "Wikipedia"
    result = "Paris"
    url = "https://en.wikipedia.org/wiki/"+subject
    check_url = "https://en.wikipedia.org/wiki/"+result

    arr = algorithm(url, check_url)
    uarr, uind = np.unique(arr, return_index=True)

    uarr = uarr[uind.argsort()]

    basew = np.array([1])
    weights = np.array([])
    weights = np.append(weights, basew)

    for i in range(1, len(uarr)):
        nw = new_weights(basew, i, 5)
        weights = np.append(weights, nw)
    
    #scatter_plot(range(0, len(weights)), weights)

    print("Starting processes")
    man = Manager()
    queue = man.Queue()
    with mp.Pool(processes=mp.cpu_count()) as pool:
        results = [pool.apply_async(algo2, args=(uarr[i],)) for i in range(len(uarr))]
        
        for ind, result in enumerate(results):
            print("Started process ", ind)
        
        output = [result.get() for result in results]
        
        for ind in range(len(results)):
            print("Joining process ", ind)
    
    print(output)
    scatter_plot(output, weights)
