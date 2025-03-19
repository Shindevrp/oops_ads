def insertion_sort(arr):
    
    for i in range(len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    for i in arr:
        print(i)

def main():
    lt = []
    try:
        while True:
            s = input().strip()
            if s :
                lt.append(s)
    except:
        insertion_sort(lt)
        
main()