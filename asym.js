array = [1, 2, 3, 4,5, 6, 7,8 9, 10]

for (let i = 0;i <array) {

  //do this 1x ; visited 10n
}
for (let i = 0;i <array) {

  //do this 2x //visited 10n
}
for (let i = 0;i <array) {

  //do this 3x //visited 10n
}


//time = O(30n) => O(n)

array = [1, 2, 3, 4,5, 6, 7,8 9, 10, 1, 2, 3, 4,5, 6, 7,8 9, 10]


for (let i = 0;i <array) {

  //do this 1x ; visited 20n
}

for (let i = 0;i <array) {

  //do this 2x //visited 20n
}
for (let i = 0;i <array) {

  //do this 3x //visited 20n
}

//time = O(60n) => O(n)

//how fast did your code run based on your input

//how much space you used based on your input size