def sort_by_length(arr):
    arr.sort(key=len)
    result = []

    for i in arr:
        result.append(i)
    print result
       
sort_by_length(["My", "turtle", "is", "old"])
