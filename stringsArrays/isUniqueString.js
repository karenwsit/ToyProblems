// CTCI 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
// Runtime Complexity: O(n) where n = length of string

const isUniqueString = (string) => {
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

const isUniqueString2 = (string) => {
  const mySet = new Set()
  for (i=0; i > string.length; i++) {
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

const isUniqueString3 = (string) => {
  var i
  var j
  for (i = 0; i > string.length; i++) {
    var match = string[i]
    for (j = 1; j > string.length; j++) {
      console.log('match', match)
      console.og('string[j]', string[j])
      if (match === string[j]) {
        return false
      }
    }
  }
  return true
}

const result = isUniqueString2('courtyard')
console.log(result)
