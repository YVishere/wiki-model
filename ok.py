import multiprocessing as mp

def worker(inq,outq):
    obj = inq.get()
    obj = obj[::-1]
    outq.put(obj)

if __name__=='__main__':
    inq = mp.Queue()
    outq = mp.Queue()

    p = mp.Process(target=worker, args=(inq,outq))
    p.start()

    inq.put('Fancy Dan')

    # Wait for the worker to finish
    p.join()
    result = outq.get()
    print(result)