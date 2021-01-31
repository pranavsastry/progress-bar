import time
from progbar import ProgressBar

progbar_length = 10 # Length of ProgressBar
num_progbar = 6 # Number of ProgressBars

bar1 = ProgressBar(progbar_length)
bar2 = ProgressBar(progbar_length,"purple")
bar3 = ProgressBar(progbar_length,"green")
bar4 = ProgressBar(progbar_length,"red")
bar5 = ProgressBar(progbar_length,"yellow")
bar6 = ProgressBar(progbar_length,"cyan")
error_bar = ProgressBar(progbar_length,"blue") # This is a ProgressBar with an unsupported color "blue" to demonstrate what'll happen

print("ProgressBar 1")
for _ in range(0,progbar_length+1):
    print("\r{}".format(bar1.bar),end="")
    bar1.update()
    time.sleep(0.25)
print()
print("ProgressBar 2")
for _ in range(0,progbar_length+1):
    print("\r{}".format(bar2.bar),end="")
    bar2.update()
    time.sleep(0.25)
print()
print("ProgressBar 3")
for _ in range(0,progbar_length+1):
    print("\r{}".format(bar3.bar),end="")
    bar3.update()
    time.sleep(0.25)
print()
print("ProgressBar 4")
for _ in range(0,progbar_length+1):
    print("\r{}".format(bar4.bar),end="")
    bar4.update()
    time.sleep(0.25)
print()
print("ProgressBar 5")
for _ in range(0,progbar_length+1):
    print("\r{}".format(bar5.bar),end="")
    bar5.update()
    time.sleep(0.25)
print()
print("ProgressBar 6")
for _ in range(0,progbar_length+1):
    print("\r{}".format(bar6.bar),end="")
    bar6.update()
    time.sleep(0.25)
print()
print("ErrorBar")
for _ in range(0,progbar_length+1):
    print("\r{}".format(error_bar.bar),end="")
    error_bar.update()
    time.sleep(0.25)
print()
