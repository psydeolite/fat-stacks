from display import *
from matrix import *
from draw import *

ARG_COMMANDS = [ 'line', 'scale', 'translate', 'xrotate', 'yrotate', 'zrotate', 'circle', 'bezier', 'hermite', 'sphere', 'box', 'torus']

def parse_file( f, points, transform, screen, color ):

    commands = f.readlines()
    #screen = new_screen()
    c = 0
    while c  <  len(commands):
        cmd = commands[c].strip()
        if cmd in ARG_COMMANDS:
            c+= 1
            args = commands[c].strip().split(' ')
            i = 0
            while i < len( args ):
                args[i] = float( args[i] )
                i+= 1

            if cmd == 'line':
                add_edge( points, args[0], args[1], args[2], args[3], args[4], args[5] )
                matrix_mult(transform[-1], points)
                #print points
                draw_lines(points, screen, color)
                points=[]
                #print points
                
            elif cmd == 'circle':
                add_circle( points, args[0], args[1], 0, args[2], .01 )
                matrix_mult(transform[-1], points)
                draw_lines(points, screen, color)
                points=[]
            
            elif cmd == 'bezier':
                add_curve( points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'bezier' )
                matrix_mult(transform[-1], points)
                draw_lines(points, screen, color)
                points=[]
            
            elif cmd == 'hermite':
                add_curve( points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'hermite' )
                matrix_mult(transform[-1], points)
                draw_lines(points, screen, color)
                points=[]

            elif cmd == 'sphere':
                add_sphere( points, args[0], args[1], 0, args[2], 5 )
                matrix_mult(transform[-1], points)
                draw_polygons(points, screen, color)
                points=[]
                
            elif cmd == 'torus':
                add_torus( points, args[0], args[1], 0, args[2], args[3], 5 )
                matrix_mult(transform[-1], points)
                draw_polygons(points, screen, color)
                points=[]
                
            elif cmd == 'box':
                add_box( points, args[0], args[1], args[2], args[3], args[4], args[5] )
                #print transform
                matrix_mult(transform[-1], points)
                #print transform[-1]
                draw_polygons(points, screen, color)
                points=[]

            elif cmd == 'scale':
                s = make_scale( args[0], args[1], args[2] )
                #matrix_mult( s, transform[-1] )
                matrix_mult(transform[-1], s)
                transform[-1]=s
                
            elif cmd == 'translate':
                t = make_translate( args[0], args[1], args[2] )
                #matrix_mult( t, transform[-1] )
                matrix_mult(transform[-1], t)
                transform[-1]=t
                
            else:
                angle = args[0] * ( math.pi / 180 )
                if cmd == 'xrotate':
                    r = make_rotX( angle )
                elif cmd == 'yrotate':
                    r = make_rotY( angle )
                elif cmd == 'zrotate':
                    r = make_rotZ( angle )
                #matrix_mult( r, transform[-1] )
                matrix_mult(transform[-1], r)
                transform[-1]=r
                
        elif cmd=='push':
            '''
            top=transform[-1]
            print 'pre'
            print transform
            transform.append(top)
            print 'post'
            print transform
            print ''
            '''
            print 'pre'
            print transform
            mpush(transform)
            print 'post'
            print transform
            print ''

        elif cmd=='pop':
            print 'pop'
            transform.pop()
            print transform
            print ''

        elif cmd == 'ident':
            ident( transform )
            
        elif cmd == 'apply':
            matrix_mult( transform, points )

        elif cmd == 'clear':
            points = []

        elif cmd in ['display', 'save' ]:
            #screen = new_screen()
            #draw_polygons( points, screen, color )
            #draw_lines( points, screen, color )
            
            if cmd == 'display':
                display( screen )

            elif cmd == 'save':
                c+= 1
                save_extension( screen, commands[c].strip() )
        elif cmd == 'quit':
            return    
        elif cmd[0] != '#':
            print 'Invalid command: ' + cmd
        c+= 1
