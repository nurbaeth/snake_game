import curses
import random

def setup_window():
    screen = curses.initscr()
    curses.curs_set(0)
    height, width = screen.getmaxyx()
    window = curses.newwin(height, width, 0, 0)
    window.keypad(1)
    window.timeout(100)
    return window, height, width

def main():
    window, height, width = setup_window()
    
    snake = [[height // 2, width // 4]]
    food = [height // 2, width // 2]
    window.addch(food[0], food[1], '*')
    
    key = curses.KEY_RIGHT
    directions = {curses.KEY_RIGHT: (0, 1), curses.KEY_LEFT: (0, -1),
                  curses.KEY_DOWN: (1, 0), curses.KEY_UP: (-1, 0)}
    
    while True:
        next_key = window.getch()
        key = key if next_key == -1 else next_key
        
        new_head = [snake[0][0] + directions[key][0],
                    snake[0][1] + directions[key][1]]
        
        if new_head in snake or new_head[0] in [0, height] or new_head[1] in [0, width]:
            break
        
        snake.insert(0, new_head)
        
        if new_head == food:
            food = None
            while food is None:
                nf = [random.randint(1, height - 1), random.randint(1, width - 1)]
                food = nf if nf not in snake else None
            window.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')
        
        window.addch(snake[0][0], snake[0][1], '#')
    
    curses.endwin()

if __name__ == "__main__":
    main()
