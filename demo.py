import time
from progbar import ProgressBar

progbar_length = 10 # Length of ProgressBar
num_progbar = 6 # Number of ProgressBars

# List containing the ProgressBar objects of different supported colors
bars = [ProgressBar(progbar_length),ProgressBar(progbar_length,"purple"),ProgressBar(progbar_length,"green"),
        ProgressBar(progbar_length,"red"),ProgressBar(progbar_length,"yellow"),ProgressBar(progbar_length,"cyan")]

# This is a ProgressBar with an unsupported color "blue" to demonstrate what'll happen
error_bar = ProgressBar(progbar_length,"blue")

for i in range(0,num_progbar):
    print("ProgressBar {}".format(i+1))
    for _ in range(0,progbar_length+1):
        print("\r{}".format(bars[i].bar),end="")
        bars[i].update()
        time.sleep(0.25)
    print()

print("ErrorBar")
for _ in range(0,progbar_length+1):
    print("\r{}".format(error_bar.bar),end="")
    error_bar.update()
    time.sleep(0.25)
print()
