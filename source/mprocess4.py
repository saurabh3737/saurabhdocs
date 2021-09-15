import time
from multiprocessing import Pool


def test(fname):
    f = open(fname, "w")
    f.write("hi")
    f.write("hi")
    f.write("hi")
    f.write("hi")
    f.close()


if __name__ == "__main__":
    starttime = time.time()
    pool = Pool()
    a = pool.apply_async(test, args=("sample1.txt",))
    b = pool.apply_async(test, args=("sample2.txt",))
    a.wait()
    b.wait()
    endtime = time.time()
    print(f"Time taken {endtime-starttime} seconds")