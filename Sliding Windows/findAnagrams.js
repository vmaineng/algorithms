var findAnagrams = function(s, p) {
    //return [] with start indices pushed in
    //

//p's length cannot be greater than s's length
    if (p.length > s.length) return []
    
    const output = []
    const hash = {}

//iterate through p's string
    for (let i = 0; i < p.length;i++) {
        //store the values in the object
        hash[p[i]] = (hash[p[i]] ?? 0) + 1; //values for each key
        // console.log(hash[p[i]])
        // console.log(Object.keys(hash))
    }

    let l = 0;
    let r = 0; 

    while (r < s.length) {
        if (hash[s[r]] > 0) {
            // console.log( hash[s[r]]) //hash[s[r] - value
            // console.log(hash)
            hash[s[r]]--
        //if length is equal to the same string, then we can make an anagram, and push the index of l in to it
        if (r - l + 1 === p.length) output.push(l);
        r++
    } else {
        //if value of s[l] does not equal undefined, keep adding and move the left window up
        if (hash[s[l]] !== undefined) hash[s[l]]++;
        l++

        //if left index is greater than right;
        //reassign the window?
        if (l > r) r = l;
        console.log(l, r)
    }
    }

    return output;

};

console.log(findAnagrams("cbaebabacd", "abc"))