from text_processor import text_loading
class TextProcessing:
    def __init__(self, text,archive_processing,text_inventory):
        self.text_inventory = text_inventory
        self.text = text
        self.archive_processing = archive_processing
text=TextProcessing("text","archive_processing",text_loading())
print(text.text_inventory)
class GameState:
    def __init__(self,elita_state,screen_state):
        self.elita_state= elita_state
        self.screen_state = screen_state
game_state = GameState("elita_state","screen_state")
#because python executes first this script , it will import test.py and execute it, without having a import error, because test.py is in the same directory as this scr