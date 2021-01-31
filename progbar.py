class ProgressBar:
    """
        CLASS ProgressBar: Main class which generates a progress bar

        METHODS:
            __init__ : Constructor for ProgressBar which initialises a new empty ProgressBar
                attrs: bar_length(Integer) - Total length of the ProgressBar
                       bar_color(String) - Set ProgressBar color. Default value = None. Choose from {"red","green","yellow","cyan","purple"}
            update : Updates the ProgressBar by one unit towards completion
                attrs: None
            update_to: Updates the ProgressBar to the desired length
                attrs: len_done(Integer) - Length of the ProgressBar to be completed
            reset: Resets the ProgressBar
                attrs: None

    """
    complete = b'\xe2\x96\x93'.decode('utf-8') # Unicode character used to indicate completed decoded to Python string
    empty = b'\xe2\x96\x91'.decode('utf-8') # Unicode character to indicate not completed decoded to Python string

    colors = {"purple":"\033[95m",
    "yellow":"\033[93m",
    "cyan":"\033[96m",
    "green":"\033[92m",
    "red":"\033[91m",
    "ENDC":"\033[0m"} # Dictionary containing ANSI Color Codes for Colored ProgressBar

    def __init__(self,bar_length,bar_color=None):
        self.bar_length = bar_length # Length of the ProgressBar
        self.orig = "" # ProgressBar string
        self.done = 0 # Length already completed
        self.bar_color = bar_color
        for i in range(0,bar_length):
            self.orig += ProgressBar.empty
        if(self.bar_color is None):
            self.bar = self.orig
        else:
            try:
                self.bar = "{}{}{}".format(ProgressBar.colors[self.bar_color],self.orig,ProgressBar.colors["ENDC"])
            except:
                self.bar_color = None
                print("{}WARNING{}: ".format(ProgressBar.colors["red"],ProgressBar.colors["ENDC"]),end="")
                print("Specified bar-color is not supported! Using the default color!")
                self.bar = self.orig

    def update(self):
        updated = self.orig[0:self.done] + ProgressBar.complete
        self.done += 1
        updated += self.orig[self.done:]
        self.orig = updated
        if(self.bar_color is None):
            self.bar = updated
        else:
            self.bar = "{}{}{}".format(ProgressBar.colors[self.bar_color],self.orig,ProgressBar.colors["ENDC"])

    def update_to(self,len_done):
        updated = ""
        for i in range(0,len_done):
            updated += ProgressBar.complete
        self.done += len_done
        updated += self.orig[len_done:]
        self.orig = updated
        if(self.bar_color is None):
            self.bar = updated
        else:
            self.bar = "{}{}{}".format(ProgressBar.colors[self.bar_color],self.orig,ProgressBar.colors["ENDC"])

    def reset(self):
        self.done = 0
        self.orig = ""
        for i in range(0,self.bar_length):
            self.orig += ProgressBar.empty
        if(self.bar_color is None):
            self.bar = self.orig
        else:
            self.bar = "{}{}{}".format(ProgressBar.colors[self.bar_color],self.orig,ProgressBar.colors["ENDC"])
