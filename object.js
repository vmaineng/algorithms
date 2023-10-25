const age = [11, 22, 43, 55, 2342, 879, 11, 42];

let alienAges = {};

for (let i = 0; i < age.length; i++) {
  let individualAge = age[i] //created a variable to store the value at position of i
  if (alienAges[individualAge]) { //if the key does exist in the object yet
    alienAges[individualAge] += 1 //assigning the value to match the key
  } else {
    alienAges[individualAge] = 1 // If the key doesn't exist, initialize it with 1
  }
}

//console.log(alienAges[11]) //2

alienAges[14] = 1; //adding in a new age



console.log(alienAges)


