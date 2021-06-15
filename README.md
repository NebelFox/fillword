# fillword
A simple fillword game, made with pygame. 

## Goal
You need to find snake-like words in the grid.
If you spot one - drag your mouse cursor from the beginning to the end while holding LBM.
If a word lies exactly on drawn path - corresponding ceils will be cleared for better visibility.
The game ends when all words are found.

## How to play
Just run the main.py. You should see a new window with grid, filled with letters.

## Configuration
Currently, configuration is allowed only inside the code within calls to words generator.
You can adjust the size of the grid at main.py::13 line.
Also, you can adjust min and max length of generated words,
as well as total length of all words in the wm.generate () at main.py::38 line.
