function describeAsYum(fruit) {
  return `${fruit} are yum`;
}

function describeAllAsYum(fruitArr) {
  return fruitArr.map(describeAsYum);
}

console.log(describeAllAsYum(["apple", "mango", "pomegranate"]));
