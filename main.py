from display import *
from draw import *
from parser import *
from matrix import *
import sys

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = [new_matrix()]
ident(transform[0])

if len(sys.argv) == 2:
    f = open(sys.argv[1])

parse_file( f, edges, transform, screen, color )
f.close()
