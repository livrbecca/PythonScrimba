/**
 * Create the highest possible integer by taking the input, sorting it and reversing it
 * @param {number} num - the inputted integer
 * @returns {number} backToNum - the highest integer
 */
function reverseNum(num) {
  const num1 = String(num).split("");
  num1.sort().reverse();
  const backToNum = Number(num1.join(""));
  return backToNum;
}

console.log(reverseNum(11051998));

// function reverseAgain(num) {
//   result = String(num).split("").sort().reverse().join("");
//   return result;
// }

// console.log(reverseAgain(11051998));
