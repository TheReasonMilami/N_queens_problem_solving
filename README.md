# N_queens_problem_solving
- Program to solve N queens problem and present with pygame.

- This sample run with 8 queens and 8x8 board.

## Board color
- Color declaration from `line 10 to 13` with 4 color in RGB
- Change board color in `line 24`
```php 
color = blue if (row + col) % 2 == 0 else yellow  
```
change `blue` and `yellow` with anyone you want.

## Queens presentation
- Change file link in `" "` at `line 28` to change image of queen. 
- if you want present Queens with shape (rectange, trialge, ....), use: 
```php
pygame.draw.circle()
```
> Remember scale image! Code to do that at `line 29`
***
***If you want change program icon at top left corner when display with pygame. Do it at `line 17 and 18`, change present link with your image link, or shape with `pygame.draw`***

## THANKS FOR READING. IF YOU LIKE, GIVE ME 1 STAR <3

