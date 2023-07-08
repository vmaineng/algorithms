function isValidWalk(walk) {
  //insert brilliant code here

  //if length is greater than 10, too long to walk = return false
  //isol
  //if go north, add 1
  //if go south, subtract 1
  //if go west, subtract 1
  //if go east, add 1

  //if (walk.length > 10) return false;

  let ns = 0;
  let ew = 0;

  if (walk.length === 10) {
    for (let i of walk) {
      if (i === "n") ns += 1;
      if (i === "s") ns -= 1;
      if (i === "e") ew += 1;
      if (i === "w") ew -= 1;
    }
  } else return false
  return ns === 0 && ew === 0;
}


console.log(isValidWalk(['n','s','n','s','n','s','n','s','n','e']))