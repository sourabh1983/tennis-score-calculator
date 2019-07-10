# Tennis Score

The scoring system for tennis works like this.

A match has one set and a set has many games

A game is won by the first player to have won at least 4 points in total and at least 2 points more than the opponent.

The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as 0, 15, 30, 40, respectively
If at least 3 points have been scored by each player, and the scores are equal, the score is "deuce".

If at least 3 points have been scored by each side and a player has one more point than his opponent, the score of the game is "advantage" for the player in the lead.

There are many games to a set in tennis

A player wins a set by winning at least 6 games and at least 2 games more than the opponent.

If one player has won six games and the opponent five, an additional game is played. If the leading player wins that game, the player wins the set 7–5. If the trailing player wins the game, a tie-break is played.

Add a score method that will return the current set score followed by the current game score

Add a pointWonBy method that indicates who won the point

### Prerequisites

You need to have tox installed in order to run this program and tests

```
pip install tox
```

## Running tennis score application
```
tox -e tennis
```

## Running unit tests
```
tox
```

## Example output:
```
The interface should look something like this in Java:


  Match match = new Match("player 1", "player 2");
  match.pointWonBy("player 1");
  match.pointWonBy("player 2");
  // this will return "0-0, 15-15"
  match.score();

  match.pointWonBy("player 1");
  match.pointWonBy("player 1");
  // this will return "0-0, 40-15"
  match.score();
  
  match.pointWonBy("player 2");
  match.pointWonBy("player 2");
  // this will return "0-0, Deuce"
  match.score();
  
  match.pointWonBy("player 1");
  // this will return "0-0, Advantage player 1"
  match.score();
  
  match.pointWonBy("player 1");
  // this will return "1-0"
  match.score();
```

## Constraints
* No guis etc
* No command line interface to the application
* Only 1 set
* No validation, assume the client passes in correct data

## Running the tests

run `tox` to execute unit tests

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Sourabh Kumar**

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
