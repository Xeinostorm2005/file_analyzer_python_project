## Sources
- Found a useful guide to change the colors of a text in the terminal
https://stackoverflow.com/questions/74589665/how-to-print-rgb-colour-to-the-terminal
```
\033[38;2;146;255;12mHello!\033[0m
^     ^ ^  ^   ^   ^   ^     ^   ^ 
|     | |  R   G   B   |     |   |
|     | |  |           |     |   \ Reset the colour to default
|     | |  |           |     | 
|     | |  |           |     \ Escape character
|     | |  |           |
|     | |  \ R;G;B     \ Text to print
|     | |
|     | \ Indicate the following sequence is RGB
|     |
|     \ Code to instruct the setting of an 8 or 24-bit foreground (text) colour
|
\ Escape character
```
- Used this website to convert colors to RGB Color codes
- https://www.rapidtables.com/web/color/RGB_Color.html

- Learned a new built-in function called Enumerate().
- https://docs.python.org/3.14/library/functions.html#enumerate

- Write data in JSON file
- https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file

- Matplotlib guide
- https://matplotlib.org/stable/users/explain/quick_start.html#a-simple-example
  
- Website that converts typescript to python (Who doesn't love that?)
- https://www.codeconvert.ai/typescript-to-python-converter

- How to rotate x-axel labels for each key
- https://matplotlib.org/stable/gallery/ticks/ticklabels_rotation.html