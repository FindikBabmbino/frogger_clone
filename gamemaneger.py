
class GameManager:

    def __init__(self):
        self.game_is_on = True

    def check_progress_con(self,player,scoreboard,cars):
        if player.ycor() >= 310:
            player.goto(player.return_start_pos())
            player.increase_speed()
            scoreboard.increase_level()
            for car in cars:
                car.increase_speed()

    def game_over(self,scoreboard):
        scoreboard.write_game_over()
        self.game_is_on = False

    def return_game_is_on(self):
        return self.game_is_on
