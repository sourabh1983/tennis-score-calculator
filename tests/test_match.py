import pytest

from tennis.match import Match


@pytest.mark.parametrize(
    'initial_score, score_after_winning',
    [
        ({'set': 0, 'game': 0}, {'set': 0, 'game': 1}),
        ({'set': 0, 'game': 4}, {'set': 1, 'game': 0}),
        ({'set': 1, 'game': 4}, {'set': 2, 'game': 0}),
    ]
)
def test_point_won_by(initial_score, score_after_winning):
    match = Match('player1', 'player2', player_one_score=initial_score)
    match.point_won_by('player1')
    assert match.player_one_score == score_after_winning


@pytest.mark.parametrize(
    'player1_score, player2_score, deuce',
    [
        ({'set': 0, 'game': 3}, {'set': 0, 'game': 3}, True),
        ({'set': 0, 'game': 4}, {'set': 1, 'game': 4}, True),
        ({'set': 0, 'game': 2}, {'set': 1, 'game': 4}, False),
    ]
)
def test_deuce(player1_score, player2_score, deuce):
    match = Match(
        'player1',
        'player2',
        player_one_score=player1_score,
        player_two_score=player2_score
    )
    assert match.deuce() is deuce


@pytest.mark.parametrize(
    'player1_score, player2_score, advantage',
    [
        ({'set': 0, 'game': 3}, {'set': 0, 'game': 4}, True),
        ({'set': 0, 'game': 4}, {'set': 1, 'game': 3}, True),
        ({'set': 0, 'game': 3}, {'set': 1, 'game': 1}, False),
    ]
)
def test_advantage(player1_score, player2_score, advantage):
    match = Match(
        'player1',
        'player2',
        player_one_score=player1_score,
        player_two_score=player2_score
    )
    assert match.advantage() is advantage


@pytest.mark.parametrize(
    'player1_score, player2_score, winner',
    [
        ({'set': 0, 'game': 4}, {'set': 0, 'game': 2}, True),
        ({'set': 0, 'game': 4}, {'set': 1, 'game': 1}, True),
        ({'set': 0, 'game': 4}, {'set': 1, 'game': 3}, False),
    ]
)
def test_winner(player1_score, player2_score, winner):
    match = Match(
        'player1',
        'player2',
        player_one_score=player1_score,
        player_two_score=player2_score
    )
    assert match.winner() is winner


@pytest.mark.parametrize(
    'player1_score, player2_score, high_score_player',
    [
        ({'set': 0, 'game': 4}, {'set': 0, 'game': 2}, 'player1'),
        ({'set': 0, 'game': 4}, {'set': 1, 'game': 1}, 'player1'),
        ({'set': 0, 'game': 1}, {'set': 1, 'game': 2}, 'player2'),
    ]
)
def test_get_player_having_highest_score(
    player1_score,
    player2_score,
    high_score_player
):
    match = Match(
        'player1',
        'player2',
        player_one_score=player1_score,
        player_two_score=player2_score
    )
    assert match.get_player_having_highest_score() == high_score_player


@pytest.mark.parametrize(
    'player1_score, player2_score, game_score',
    [
        ({'set': 0, 'game': 4}, {'set': 0, 'game': 2}, '40 - 15'),
        ({'set': 0, 'game': 4}, {'set': 1, 'game': 1}, '40 - 10'),
        ({'set': 0, 'game': 0}, {'set': 1, 'game': 3}, '0 - 30'),
    ]
)
def test_get_game_score(player1_score, player2_score, game_score):
    match = Match(
        'player1',
        'player2',
        player_one_score=player1_score,
        player_two_score=player2_score
    )
    match.get_game_score() == game_score


@pytest.mark.parametrize(
    'player1_score, player2_score, set_score',
    [
        ({'set': 0, 'game': 4}, {'set': 0, 'game': 2}, '0 - 0'),
        ({'set': 0, 'game': 4}, {'set': 1, 'game': 1}, '0 - 1'),
        ({'set': 1, 'game': 0}, {'set': 1, 'game': 3}, '1 - 1'),
    ]
)
def test_get_set_score(player1_score, player2_score, set_score):
    match = Match(
        'player1',
        'player2',
        player_one_score=player1_score,
        player_two_score=player2_score
    )
    match.get_game_score() == set_score
