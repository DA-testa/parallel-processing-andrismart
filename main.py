# python3

def parallel_processing(n, m, data):
    output = []
    thread=[]
    for i in range(n):
        thread.append((i, 0))

    for j in range(m):
        nxt, time=min(thread, key=lambda x:x[1])
        thread[nxt]=(nxt, time+data[j])
        output.append((nxt, time))
    return output

def main():
    n, m=map(int, input().split())

    data=list(map(int, input().split()))

    result = parallel_processing(n,m,data)
   
    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()
