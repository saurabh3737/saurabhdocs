import time
from multiprocessing import Process


def test(fname):
    f = open(fname, "w")
    f.write("hi")
    f.write("hi")
    f.write("hi")
    f.write("hi")
    f.close()


if __name__ == "__main__":
    starttime = time.time()
    processlist = []
    p1 = Process(target=test, args=("sample1.txt",))
    p2 = Process(target=test, args=("sample2.txt",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    endtime = time.time()
    print(f"Time taken {endtime-starttime} seconds")