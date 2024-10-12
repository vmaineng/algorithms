function tournamentWinner(competitions, results) {
  //receive an array of array of [hometeam, awayteam], and results []
  //return return the winner of tournament

  //iterate through the competitions,
  //keep track of the results of hometeam or away team
  //check the value in the frequency counter
  //increment points for hometeam if it's 1 in results, else awayTeam gets the point
  //return the the best team who has the max scores

  let scores = {};
  let winner = "";
  scores[winner] = 0;

  for (let i = 0; i < competitions.length; i++) {
    const [homeTeam, awayTeam] = competitions[i];
    //console.log(homeTeam, awayTeam);
    if ((results[i] = 0)) {
      scores[homeTeam] += 1;
    } else {
      scores[awayTeam] += 1;
    }
    //console.log(scores[homeTeam], scores[awayTeam]);
    if (scores[homeTeam] > scores[awayTeam]) {
      winner = homeTeam;
    } else {
      winner = awayTeam;
    }
  }
  return winner;
}

// Do not edit the line below.
exports.tournamentWinner = tournamentWinner;

console.log(
  tournamentWinner(
    [
      ["HTML", "C#"],
      ["C#", "Python"],
      ["Python", "HTML"],
    ],
    [0, 0, 1]
  )
);
