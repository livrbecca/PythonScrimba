function reverseNum(num) {
  const num1 = String(num).split("");
  num1.sort().reverse();
  const backToNum = num1.join("");
  return backToNum;
}

console.log(reverseNum(11051998));

function reverseAgain(num) {
  result = String(num).split("").sort().reverse().join("");
  return result;
}

console.log(reverseAgain(11051998));
