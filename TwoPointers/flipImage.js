const flipImage = (image) => {
    //flips horizontally = reverse
for (let i = 0; i < image[0].length; i++) {
    let l = 0; 
    let r = image[i].length - 1;
    while (l < r) {
        let temp = image[i][l] //i = row; l = column
        image[i][l] = image[i][r]
        image[i][r] = temp
        l++;
        r--
    }
    // console.log(i, r, image[i])
}

for (let i = 0; i < image[0].length; i++) {
    for (let j = 0; j < image[0].length; j++) {
        if(image[i][j] === 0) {
            image[i][j] = 1
        } else {
            image[i][j] = 0
        }
    }
}
return image
}



console.log(flipImage([[1,1,0],[1,0,1],[0,0,0]]))