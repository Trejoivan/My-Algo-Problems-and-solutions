



const array1 = [1, 2, 3];

const arry2 = [2, 3]

const result = []

for (let i = 0; i < array1.length; i++) {
  if (!arry2.includes(array1[i])) {
    result.push(array1[i])
  }
}

console.log(result);
// expected output: true
