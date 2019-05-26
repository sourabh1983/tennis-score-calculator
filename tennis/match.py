score_mapper = {0: 0, 1: 15, 2: 30, 3: 40}


class Match:

    def __init__(
            self,
            player_one_name,
            player_two_name,
            player_one_score={'set': 0, 'game': 0},
            player_two_score={'set': 0, 'game': 0}
    ):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.player_one_score = player_one_score
        self.player_two_score = player_two_score

    def point_won_by(self, player_name):
        pass

    def update_set_score(self):
        pass

    def score(self):
        pass

    def get_game_score(self):
        return '1 - 1'

    def get_set_score(self):
        return '2 - 2'

    def deuce(self):
        return True

    def advantage(self):
        return False

    def winner(self):
        return False

    def get_player_having_highest_score(self):
        return self.player_one_name

