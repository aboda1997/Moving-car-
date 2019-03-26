from OpenGL.GL  import *
from  OpenGL.GLUT import *
from  OpenGL.GLU import *

def drawxyz():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex(0,0,0)
    glVertex(10, 0, 0)
    glVertex(0, 0, 0)
    glVertex(0, 10, 0)
    # glVertex(0, 0, 0)
    # glVertex(0, 10, 0)
    # glVertex(0, 0, 1)
    glVertex(0, 0, 0)
    glVertex(0, 0, 10)

    glEnd()

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity() # put identity matrix  in it
    gluPerspective(60,1,1,30)
    gluLookAt(8,9,10,
              0,0,0,
              0,1,0)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)



angle = 0
x = 0
forward =  True


def draw():
    glClearColor(0,1,1,0)
    global  angle
    global  x
    global  forward
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0, 1, 0)
    glTranslate(0, 0, 12)
    glScale(16, 0, 10)
    glutSolidCube(2)
    glLoadIdentity()

    glTranslate(0, 0, -10)
    glScale(20, 0, 10)
    glutSolidCube(2)
    glLoadIdentity()



    glColor3f(1,1,1)
    glScale(20,0,.5)
    glutSolidCube(2)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(0,0,2)
    glScale(15, 0, .5)
    glutSolidCube(2)
    glLoadIdentity()

    glColor3f(0, 0, 0)
    glTranslate(0,0,1)

    glScale(1, 0, .2)
    glutSolidCube(2)
    glLoadIdentity()

    glColor3f(0, 0, 0)
    glTranslate(3, 0, 1)

    glScale(1, 0, .2)
    glutSolidCube(2)
    glLoadIdentity()

    glColor3f(0, 0, 0)
    glTranslate(6, 0, 1)

    glScale(1, 0, .2)
    glutSolidCube(2)
    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(-3, 0, 1)

    glScale(1, 0, .2)
    glutSolidCube(2)
    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(-6, 0, 1)

    glScale(1, 0, .2)
    glutSolidCube(2)
    glLoadIdentity()

    glColor3f(0, 0, 0)
    glTranslate(-9, 0, 1)

    glScale(1, 0, .2)
    glutSolidCube(2)
    glLoadIdentity()

    glColor3f(1, 0, 0)




    #drawxyz()
    glTranslate(x,0,0)
    glScale(1 ,.25,.5)
    glutWireCube(5)
    glLoadIdentity()
    glTranslate(x,0,0)

    glTranslate(0 , 5*.25 , 0)
    # glRotate(angle,0,0,1)

    glScale(.5,.25 , .5)
    glutWireCube(5)
    glColor3f(0, 0,1 )
    glLoadIdentity()


    glTranslate(x+.5 * 5, -.5 * .25 * 5, .5 * 5 * .5)
    glRotate(angle,0,0,1)

    glutWireTorus(.125, .5, 10, 10)

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x+.5 * 5, -.5 * .25 * 5, -.5 * 5 * .5)
    glRotate(angle,0,0,1)

    glutWireTorus(.125, .5, 10, 10)

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x-.5 * 5, - .5 * .25 * 5, -.5 * 5 * .5)
    glRotate(angle,0,0,1)

    glutWireTorus(.125, .5, 10, 10)

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x-.5 * 5, - .5 * .25 * 5, .5 * 5 * .5)
    glRotate(angle,0,0,1)

    glutWireTorus(.125, .5, 10, 10)



    glutSwapBuffers()
    if forward:
        angle -= .5
        x += .01
        if x >5:
            forward = False
    else:
        angle += .5
        x -= .01
        if x < -5:
            forward = True












glutInit() # intialize
glutInitDisplayMode(GLUT_DOUBLE  | GLUT_RGB)  #GLUT_SINGLE
glutInitWindowSize(500,500) # W * H  in pixel
glutCreateWindow(b"Moving Car ") # title of program   b for asci code
glutDisplayFunc(draw ) # input for code to build model
glutIdleFunc(draw)
myInit()
glutMainLoop( ) # no stop for program  enter for loop