# ProfQ-Sorting

## Usage

You can import the module like any other with:

```python
import profq_sorting
```

Then you have access to all kinds of sorting [algorithms](#algorithms).

For example, merge sort:

```python
import profq_sorting

arr = [5, 2, 6, 1, 5]
sorted_arr = profqu_sorting.merge_sort(arr)

print(sorted_arr)
```

```none
Output: [1, 2, 5, 5, 6]
```

There are many more algorithms which I have implemented, but here is a few that may interest you: `mergesort`, `quicksort`, `radixsort` and `timsort`.

## Algorithms

### Bubble Sort

```python
from profq_sorting import bubble_sort
```

Bubble sort loops over the array, and for every iteration it loops over the array again, only offset by one. Then it checks every two elements and swaps them if they are out of order.

### Bucket Sort

```python
from profq_sorting import bucket_sort
```

My implementation for bucket sort can only handle values between 0 and 1. Bucket sort works by creating buckets for every tenth, then it categorizes each element by multiplying it by 10 to get the index. Then it sorts each bucket using [insertion sort](#insertion-sort). Finally it appends all the buckets together to create one array that is sorted.

### Counting Sort

```python
from profq_sorting import counting_sort
```

Counting sort works by creating a table of each element in the array and then **counts** their occurrences. After that it does a cumulative sum to figure out what each elements index is. Then it loops over the array and each time an item comes up it adds it to the output array at the index calculated and then subtracts one from that index.

### Insertion Sort

```python
from profq_sorting import insertion_sort
```

Insertion sort divides the array into two parts: the sorted part and the unsorted part. The first array element begins as the first item in the sorted array. Then we just loop over the unsorted part of the array and **insert** each element at the right place in the sorted part.

### Merge Sort

```python
from profq_sorting import merge_sort
```

Merge sort splits the array into two parts through the middle, then it does so again and again until there is only one item left in each part. Then the algoritm **merges** the items back in the correct order until it reaches the sorted array.

### Quick Sort

```python
from profq_sorting import quick_sort
```

Quick sort starts with a pivot, it's an item that can be chosen in multiple ways as long as it's close to the median of the array. After being chosen every item to the left of the pivot should be less than it, and every item to the right should be greater. Then just repeat for the left side and the right side and continue doing so until you have reached a sorted array.

### Radix Sort

```python
from profq_sorting import radix_sort
```

Radix sort depends on [counting sort](#counting-sort) to work. It basically sorts the array using the ones, then the tens and so on. It sorts these using the counting sort algorithm while keeping the order before.

### Selection Sort

```python
from profq_sorting import selection_sort
```

Selection sort works by looping over the array and with each iteration it will loop over the unsorted portion of the array. When it loops the first time it will **select** the minimum number in the array and put it first, then it just repeats this but without taking the sorted part into account.

### Shell Sort

```python
from profq_sorting import shell_sort
```

Shell sort works by sorting the items in an array with gaps in between, then it keeps decreasing these gaps until they are 0.

### Timsort

```python
from profq_sorting import timsort
```

This algorithm is really complicated and it took me a couple of days to wrap my head around so don't feel the need to understand it right away [Gaurav Sen](https://www.youtube.com/c/GauravSensei) made a [great series](https://www.youtube.com/playlist?list=PLMCXHnjXnTntLcLmA5SqhMspm7burHi3m) about Timsort and I highly suggest you to check it out.

What it does is it seperates the array into runs and sorts each run using [insertion sort](#insertion-sort), then it [merges](#merge-sort) the runs back into one big array using the merge function from merge sort. It's a hybrid sorting algortithm. And I know sounds really simple, but I can assure you it's not.

P.S. it's named timsort because [**Tim**](https://en.wikipedia.org/wiki/Tim_Peters_(software_engineer)) invented it in 2002 actually.

## Conclusion

This is a package that I really only made so that I can say that I have made a Python package (can you believe it? I made a Python package!). And also to learn more about sorting algoritms! If you're interested in this topic there are a few Youtube channels/playlists I can recommend:

[GeeksForGeeks](https://www.youtube.com/c/GeeksforGeeksVideos) has an awesome [playlist](https://www.youtube.com/playlist?list=PLqM7alHXFySHrGIxeBOo4-mKO4H8j2knW) detailing all kinds of sorting algoritms.

[Michael Sambol](https://www.youtube.com/c/MichaelSambol) also has a really cool [series](https://www.youtube.com/playlist?list=PL9xmBV_5YoZOZSbGAXAPIq1BeUf4j20pl) detailing sorting algorithms in a short amount of time.

It has been really fun learning about all these algorithms and I encourage you to try and implement some for yourself!
