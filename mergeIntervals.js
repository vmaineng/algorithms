const merge = (intervals) => {
    
//sort the index array by starting index
//then compare end of first interval to beginning of second interval start
//add it to the output is <= the second interval, then merge it in


let newInterval = []

//sort by first index, in-place
intervals.sort((a,b) => a[0] - b[0])

let temp = intervals[0]
for (let i = 0; i < intervals.length; i++) {
    if ( intervals[i][0] <= temp[1]) {
        console.log( intervals[i][0], temp[1])

    }
}


}

console.log(merge([[1,3],[2,6],[8,10],[15,18]]))