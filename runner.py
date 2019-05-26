'''
Implementation Notes:
Only worry about 1 set
Don't worry about validation, assume the client passes in correct data
use Java, Javascript, TypeScript, Ruby, Kotlin, Python, Swift, or Groovy
try not to spend more than 2 hours maximum.
don't build guis etc, we're more interested in your
approach to solving the given task, not how shiny it looks
don't worry about making a command line interface to the application
don't use any frameworks (rails, spring etc), or any external jars/gems
'''

from tennis.match import Match


def match_runner():
    match = Match("player 1", "player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 2")
    # this will return "0-0, 15-15"
    match.score()

    match.point_won_by("player 1")
    match.point_won_by("player 1")
    # this will return "0-0, 40-15"
    match.score()

    match.point_won_by("player 2")
    match.point_won_by("player 2")
    # this will return "0-0, Deuce"
    match.score()

    match.point_won_by("player 1")
    # this will return "0-0, Advantage player 1"
    match.score()

    match.point_won_by("player 1")
    # this will return "1-0"
    match.score()


match_runner()
