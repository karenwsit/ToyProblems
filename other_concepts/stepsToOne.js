/**
 *  Minimum Steps to One
 *
 *     Given a positive integer, you can perform any combination of these 3 steps:
 *      1.) Subtract 1 from it.
 *      2.) If its divisible by 2, divide by 2. 
 *      3.) If its divisible by 3, divide by 3.
 *
 *     Find the minimum number of steps that it takes get from N to 1
 * 
 *  Input: Positive Integer N
 *  Output:Integer
 **/

 function stepsToOne(n){
    var steps = [0,0];
    var min;
    for (var i = 2; i <= n; i++){
        min = steps[i-1];
        if (i%2 === 0){
            min = Math.min(steps[i/2], min);
        }
        if (i%3 === 0){
            min = Math.min(steps[i/3], min);
        }
        steps.push(min+1);
    }
    return steps[n];
 }

console.log(stepsToOne(20));
