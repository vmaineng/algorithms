function map(array, callback) {
  const result = [];
  for (i = 0; i < array.length; i++) {
    const newEle = callback(array[i], i, array);
    result.push(newEle);
  }
  return result;
}
const result = map([1, 2, 3, 4], (x) => x ** 2);
console.log(result);
