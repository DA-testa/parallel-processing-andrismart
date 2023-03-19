# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    thread=[]
    for i in range(n):
        thread.append((i, 0))

    for j in range(m):
        nxt, time=min(thread, key=lambda x:x[1])
        thread[nxt]=(nxt, time+data[j])
        output.append((nxt, time))
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m=map(int, input().split())


    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data=list(map(int, input().split()))


    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()
