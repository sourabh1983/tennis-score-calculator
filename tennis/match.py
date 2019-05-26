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
        if player_name == self.player_one_name:
            self.player_one_score['game'] = self.player_one_score['game'] + 1
        elif player_name == self.player_two_name:
            self.player_two_score['game'] = self.player_two_score['game'] + 1

        if self.winner():
            self.update_set_score()

    def update_set_score(self):
        if self.player_one_name == self.get_player_having_highest_score():
            self.player_one_score['set'] = self.player_one_score['set'] + 1
        else:
            self.player_two_score['set'] = self.player_two_score['set'] + 1
        self.player_one_score['game'] = 0
        self.player_two_score['game'] = 0

    def score(self):
        if self.deuce():
            print(f'{self.get_set_score()}, Deuce')
            return

        if self.advantage():
            score = f'Advantage - {self.get_player_having_highest_score()}'
            print(f'{self.get_set_score()}, {score}')
            return

        print(f'{self.get_set_score()}, {self.get_game_score()}')

    def get_game_score(self):
        player_one_game_score = score_mapper.get(self.player_one_score['game'])
        player_two_game_score = score_mapper.get(self.player_two_score['game'])
        return f'{player_one_game_score} - {player_two_game_score}'

    def get_set_score(self):
        return \
            f'{self.player_one_score["set"]} - {self.player_two_score["set"]}'

    def deuce(self):
        return self.player_one_score['game'] >= 3 and \
         self.player_two_score['game'] == self.player_one_score['game']

    def advantage(self):
        if self.player_one_score['game'] >= 4 and \
           self.player_one_score['game'] == self.player_two_score['game'] + 1:
            return True
        if self.player_two_score['game'] >= 4 and \
           self.player_two_score['game'] == self.player_one_score['game'] + 1:
            return True
        return False

    def winner(self):
        if self.player_two_score['game'] >= 4 and \
           self.player_two_score['game'] >= self.player_one_score['game'] + 2:
            return True
        if self.player_one_score['game'] >= 4 and \
           self.player_one_score['game'] >= self.player_two_score['game'] + 2:
            return True
        return False

    def get_player_having_highest_score(self):
        if self.player_one_score['game'] > self.player_two_score['game']:
            return self.player_one_name
        else:
            return self.player_two_name
