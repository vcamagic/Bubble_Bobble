from Tournament import Tournament
import sys
from multiprocessing import Process
from multiprocessing import Queue
from PyQt5.QtWidgets import QApplication

class TournamentSrednja(Tournament):
    w = ""

    def __init__(self, queue: Queue, num, player1_input, player2_input):
        self.queue = queue
        super().__init__(queue, num, player1_input, player2_input)

    def readWinner(self):
        f = open('winner.txt', 'r')
        self.w = f.read()
        return self.w

    def checkEnd(self):
        self.queue.put(self.readWinner())
        self.queue.close()


def start_tournament(player1_input, player2_input, player3_input, player4_input):

    q = Queue()
    winner1_id = _start_game_process(q, player1_input, player2_input)
    print("Game 1 winner: ", winner1_id)

    winner2_id = _start_game_process(q, player3_input, player4_input)
    print("Game 2 winner: ", winner2_id)

    tournament_winner_id = _start_game_process(q, winner1_id, winner2_id)
    print(f"Tournament winner is: {tournament_winner_id}")


def _start_game_process(q, player1_input, player2_input) -> str:
    process = Process(target=_start_game, args=(q,player1_input,player1_input))
    process.start()

    winner_id = q.get()
    process.terminate()
    return winner_id


def _start_game(queue: Queue, player1_id,  player2_id):
    app = QApplication(sys.argv)
    game = Tournament(queue=queue, brojIgraca=2, name1=player1_id, name2=player2_id)
    game.inicijalizujSve()
    sys.exit(app.exec_())
