class ProgressBar:
    """
        CLASS ProgressBar: Main class which generates a progress bar

        METHODS:
            __init__ : Constructor for ProgressBar which initialises a new empty ProgressBar
                attrs: bar_length - Total length of the ProgressBar
            update : Updates the ProgressBar by one unit towards completion
                attrs: None
            update_to: Updates the ProgressBar to the desired length
                attrs: len_done - Length of the ProgressBar to be completed
            reset: Resets the ProgressBar
                attrs: None

    """
    complete = b'\xe2\x96\x93'.decode('utf-8') # Unicode character used to indicate completed decoded to Python string
    empty = b'\xe2\x96\x91'.decode('utf-8') # Unicode character to indicate not completed decoded to Python string

    def __init__(self,bar_length):
        self.bar_length = bar_length # Length of the ProgressBar
        self.bar = "" # ProgressBar string
        self.done = 0 # Length already completed
        for i in range(0,bar_length):
            self.bar += ProgressBar.empty

    def update(self):
        updated = self.bar[0:self.done] + ProgressBar.complete
        self.done += 1
        updated += self.bar[self.done:]
        self.bar = updated

    def update_to(self,len_done):
        updated = ""
        for i in range(0,len_done):
            updated += ProgressBar.complete
        self.done += len_done
        updated += self.bar[len_done:]
        self.bar = updated

    def reset(self):
        self.done = 0
        self.bar = ""
        for i in range(0,self.bar_length):
            self.bar += ProgressBar.empty
