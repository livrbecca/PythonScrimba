// [{ n: 10, subtract: 1 }, { n: 10, subtract: 2 }, { n: 100, subtract: 99 }]

function doSubtraction(obj) {
  return obj.n - obj.subtract;
}

function subtract(objArr) {
  return objArr.map(doSubtraction);
}

console.log(
  subtract([
    { n: 10, subtract: 1 },
    { n: 10, subtract: 2 },
    { n: 100, subtract: 99 },
  ])
);
