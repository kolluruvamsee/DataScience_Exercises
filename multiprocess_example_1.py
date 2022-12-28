import time
from multiprocessing.pool import Pool

a=[[2, 3, 4, 5], [6, 9, 10, 12], [11, 12, 13, 14], [21, 24, 25, 26]]

def normalizing_data(l):
    res=[]
    max_val=max(l)
    min_val=min(l)
    for each in l:
        res.append((each-min_val)/(max_val-min_val))
    print(res) 

if __name__ == '__main__':
    start = time.perf_counter()
    print("Executing with Multiprocessing")
    with Pool(4) as pool:
        pool.map(normalizing_data, a)   
    end = time.perf_counter()
    print("Time taken to execute {}".format(end-start))
