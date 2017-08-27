// CTCI 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.

// Runtime Complexity: O(n) where n = length of string
// Additional Space Complexity: O(n)

const isUniqueStringHash = (string) => {
  const hashTable = {}
  for (const char of string) {
    if (hashTable.hasOwnProperty(char)) {
      return false
    } else {
      hashTable[char] = true
    }
  }
  return true
}

const isUniqueStringSet = (string) => {
  const mySet = new Set()
  for (i=0; i < string.length; ++i) {
    console.log(string[i])
    if (mySet.has(string[i])) {
      return false
    } else {
      mySet.add(string[i])
    }
  }
  return true
}

// What if you cannot use additional data structures?

// Runtime: O(n^2)
// Additional Space Complexity: 1

const isUniqueStringLoop = (string) => {
  var i
  var j
  for (i = 0; i < string.length; ++i) {
    var match = string[i]
    for (j = 1; j < string.length; ++j) {
      if (match === string[j]) {
        return false
      }
    }
  }
  return true
}

// Runtime: O(n log n)
// Additional Space: 1

const isUniqueStringSort = (string) => {
  string.sort() //quicksort
  for (const i = 0; i < string.length; ++i) {
    if (string[i] === string[i+1] ) {
      return false
    }
  }
  return true
}
