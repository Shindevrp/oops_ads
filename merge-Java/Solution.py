def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        lo = arr[:mid]
        rh = arr[mid:]

        merge_sort(lo)
        merge_sort(rh)

        merged = []
        i = j = 0
        for a in range(len(arr)):
            if i < len(lo) and (j >= len(rh) or lo[i] < rh[j]):
                merged.append(lo[i])
                i += 1
            else:
                merged.append(rh[j])
                j += 1

        for i in range(len(arr)):
            arr[i] = merged[i]
    
    return arr

def main():
    lt = []
    try:
        while True:
            s = input().strip()
            if s:
                lt.append(s)
    except:
        sorted_arr = merge_sort(lt)
        for i in sorted_arr:
            print(i)

main()
