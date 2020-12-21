from src.gameloop import *

game = GameLoop()
game.start()

game.runtime.db_connection.close()