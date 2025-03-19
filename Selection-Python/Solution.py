def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    for item in arr:
        print(item)


def main():
    elements = []
    try:
        while True:
            user_input = input().strip()
            if user_input:
                elements.append(user_input)
    except:
        selection_sort(elements)


main()
