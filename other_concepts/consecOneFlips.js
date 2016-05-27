/**
 *  3. Given an array of binary values (0 and 1) and N number of flips (convert a 0 to a 1), 
 *     determine the maximum number of consecutive 1's that can be made.
 *
 *  Input: An Array of 1's and 0's, and an Integer N denoting the number of flips
 *  Output: Integer
 *
 *  Example: bitFlip([0,1,1,1,0,1,0,1,0,0], 2)
 *  Result: 7
 **/


 var consecOneFlips = function(arr, n){
    var max = 0;
    var streak = 0;
    var start = 0;
    for (var i = 0; i < arr.length; i++){
        if (!arr[i]){ // check if it is a 0
            if(n>0){
                n--;
            } else {
                streak--;
                while(arr[start]){ //check if it is a 1
                    start++;
                    streak--;
                }
                start++;
            }
        }
    streak++;
    max = Math.max(max, streak);
    return max;

    }
 };