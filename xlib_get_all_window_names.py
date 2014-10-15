import Xlib 
import Xlib.display 

display = Xlib.display.Display() 
screen = display.screen() 
root = screen.root 
tree = root.query_tree() 
wins = tree.children 

for win in wins: 
    print win
