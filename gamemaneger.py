
class GameManager:

    def check_progress_con(self,player,scoreboard,cars):
        if player.ycor() >= 310:
            player.goto(player.return_start_pos())
            player.increase_speed()
            scoreboard.increase_level()
            for car in cars:
                car.increase_speed()

    def reset_game(self,player,cars,scoreboard):
        player.reset_player()
        for car in cars:
            car.reset()
        cars.clear()
        scoreboard.reset_score_board()


