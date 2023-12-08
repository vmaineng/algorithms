function duckGoose(players, goose) {
    //an array of letter to represent players, an integer to represent how many times til you say goose
    //return the player goose lands
    //[a,b,c,d,e], 4 => 'd'

    //iterate through the array
    //if the value = goose
    //return the player.name

    for (let i = 0; i < players.length; i++) {
        if (i === (goose - 1) % players.length) {
            return players[i].name
        }
    }

// return players[(goose - 1) % players.length].name
}

let playersArray = ['a','b','c','d']
 let index = 4;
// const adjustedIdx = (index - 1) % playersArray.length;
// console.log(adjustedIdx)

console.log(duckGoose(playersArray, index))

//since it is 1-based indexing, need to adjust back to 0-based indexing in JS
//by writing (goose - 1);
//(goose - 1) % players.length = ensure the adjusted index stays within the valid range
//ex: if index is 5, it will wrap around in the players array
