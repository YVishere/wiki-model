from multiprocessing import Process, Manager
import multiprocessing as mp
import Scraper

def main(uarr):
    print("Starting processes")
    with mp.Pool(processes=mp.cpu_count()) as pool:
        results = [pool.apply_async(Scraper.startScraping, args=(uarr[i],' ',True)) for i in range(len(uarr))]
        
        for ind, result in enumerate(results):
            print("Started process ", ind)
        
        output = [result.get() for result in results]
        
        for ind in range(len(results)):
            print("Joining process ", ind)

        return output