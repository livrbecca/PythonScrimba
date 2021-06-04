function reverseArrayOfNumbers(arr) {
  let reversedArray = [];

  for (let i = arr.length - 1; i >= 0; i--) {
    let num = arr[i]; // arr[3], arr[2], then arr[1], then arr[0]
    reversedArray.push(num);
  }
  return reversedArray;
}

console.log(reverseArrayOfNumbers([11, 5, 19, 98]));

// define the function, set a parameter for the array / list of numbers to later be passed in as an argument once you call the function

// create an empty array, this is where you'll store the reversed result at the end

// create a for loop - summary, -1 because index's start from 0 not 1!
// for (let i = arr.length - 1; )
// i will be equal to the length of the array, -1
// [11, 5, 19, 98], the length is 4
// i = 3. - remember that length and index are different
// so: for (let i = arr.length - 1) which gives us the index, and indexes start at 0
// a length of 4 , will actually look like 0 1 2 3 as an index

//  for (~; i >= 0; i--)
// second part of the for loop: if 1 is GREATER THAN OR EQUAL TO 0
// then continue and perform the body of the loop!
// so if our starting length is 3, i = 3, 3 is bigger than 0, continue the loop
// once complete, subtract 1 from i and repeat until i is no longer greater than or equal to zero

// on iteration, num becomes an element in the array, determined by arr[i]
// so if using [11, 5, 19, 98], and on first iteration i is 3,
// num will be: num = arr[3], so 98! as 98 is at index 3

// ITERATIONS: [11, 5, 19, 98]
// one: i = 3, true, num = arr[3], 98 gets pushed to empty array, i - 1
// two: i = 2, true, num = arr[2], 19 gets pushed to empty array, i - 1
// three: i = 1, true, num = arr[1], 5 gets pushed to empty array, i - 1
// four: i = 0, true, num = arr[0], 11 gets pushed to empty array, i - 1
// five: i = -1, false, loop terminated.
// reversed array = [98, 19, 5, 11]
