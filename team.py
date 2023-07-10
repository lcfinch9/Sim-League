import random

#### ---- SIMULATE WINNER ---- ####

def simulate_winner(t1_wins, t1_losses, t2_wins, t2_losses):
    rand_num = random.randint(0, 100)
    t1_win_percent = t1_wins / (t1_losses + t1_wins)
    t2_win_percent = t2_wins / (t2_losses + t2_wins)
    t1_win_chance = int(t1_win_percent * 100 / (t1_win_percent + t2_win_percent))

    ## -- Check if team 1 wins -- ##
    
    if rand_num < t1_win_chance:
        return True
    else:
        return False

#### ---- TEAM CLASS ---- ####

class Team:

    ## -- Init method -- ##

    def __init__(self, name, wins, losses):
        self.name = name
        self._total_wins = wins
        self._total_losses = losses
        self._season_wins = 0
        self._season_losses = 0

    ## -- Compete against team method -- ##

    def compete(self, other_team):
        print(self.name.upper(), "VS", other_team.name.upper(), end="")

        ## -- Check winner -- ##

        winner = simulate_winner(self._total_wins, self._total_losses, other_team._total_wins, other_team._total_losses)


        ## -- Display game results -- ##

        if winner:
            self._total_wins += 1
            self._season_wins += 1
            other_team._total_losses += 1
            other_team._season_losses += 1
            print(": " + self.name + " win!")
        else:
            self._total_losses += 1
            self._season_losses += 1
            other_team._total_wins += 1
            other_team._season_wins += 1
            print(": " + other_team.name + " win!")

    ## -- Display season results -- ##

    def display_season(self):
        print(self.name.upper() + "\n\tWINS: " + str(self._season_wins) + " LOSSES: " + str(self._season_losses))
