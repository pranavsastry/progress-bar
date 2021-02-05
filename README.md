# progress-bar

<p float=left>
  <img src="prog-bar-dark.png" alt="logo" width="200" />
  <img src="prog-bar-light.png" alt="logo" width="200" />
</p>

# Download progbar<br>
<a href="https://raw.githubusercontent.com/pranavsastry/progress-bar/main/progbar.py">**Download**</a><br>

# Demo<br>
![demo](progbar_demo.gif)<br/>

# Supported Colors<br>
{"red", "cyan", "yellow", "green", "purple"}<br>
![colors](prog-bar-colors.png)<br/>

# Running the Demo<br>
**1. Download progbar.py and make sure your working directory and the path in which progbar.py is downloaded, matches <br>
2. Download demo.py into the same directory <br>
3. Run demo.py <br>**

# Code Snippets <br>
```
>>> from progbar import ProgressBar
>>> bar = ProgressBar(15)
>>> print(bar.bar)
░░░░░░░░░░░░░░░
>>> bar.update_till(5)
>>> print(bar.bar)
▓▓▓▓▓░░░░░░░░░░
>>> bar.update()
>>> print(bar.bar)
▓▓▓▓▓▓░░░░░░░░░
>>> bar.reset()
>>> print(bar.bar)
░░░░░░░░░░░░░░░
>>> 
```
