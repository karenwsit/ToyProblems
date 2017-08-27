// Quick Sort
// Worstcase Runtime: O(n^2) when every pivot is either the smallest or largest integer
// Usual Runtime: O(n log(n)) divde and conquer
// Additional Spacetime Complexity: None; done in place

function quickSort(arr, start, end) {
  if (start >= end) {
    return
  }
  var pIndex = partition(arr, start, end)
  quickSort(arr, start, pIndex-1)
  quickSort(arr, pIndex+1, end)
  return arr
}

function partition(arr, start, end) {
  var pivotVal = arr[end]
  var pIndex = start

  for (var i = start; i < end; ++i) {
    if (arr[i] < pivotVal) {
      swap(arr, i, pIndex )
      pIndex = pIndex + 1
    }
  }
  swap(arr, end, pIndex)
  return pIndex
}

function swap(arr, i, j) {
  var temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}

console.log(quickSort([11,8,14,3,6,2,7],0,6));
//[2, 3, 6, 7, 8, 11, 14]
console.log(quickSort([11,8,14,3,6,2,1, 7],0,7));
//[1, 2, 3, 6, 7, 8, 11, 14]
console.log(quickSort([16,11,9,7,6,5,3, 2],0,7));
