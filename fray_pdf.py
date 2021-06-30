import PyPDF4

# Copy paste folder from calc project into new folder for fray
import ply.lex as lex
import ply.yacc as yacc

pdfFileObj = open('/Users/anshulsinha/dev/PIT_NE_JJAMES.pdf', 'rb')
pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)

pageObj = pdfReader.getPage(8)
# print(pageObj.extractText())
 
# Takes a sentence and returns the data from that sentence as an object.
# E.G. Play clock, pass or run, players, down, ball location
# Example sentence: 
# (:50) (Shotgun) B.Roethlisberger pass short right to L.Bell to PIT 43 for 1 yard (M.Butler). 1-10-PIT 42


# Class for a play.
class Play:
    def __init__(self, down_num, down_length, time, formation, qb, direction, reciever, destination, length, tackler, starting_location) -> None:
        self.down_num = down_num
        self.down_length = down_length
        self.time = time
        self.formation = formation
        self.qb = qb
        self.direction = direction
        self.reciever = reciever
        self.destination = destination
        self.length = length
        self.tackler = tackler
        self.starting_location = starting_location

# List of all tokens
tokens = [
    'TIME',
    'PLAYER',
    'FORMATION',
    'PASS_LENGTH',
    'PASS_DIRECTION',
    'LOCATION_SIDE',
    'LOCATION_YARDAGE',
    'YARDAGE',
    'DOWN_NUM',
    'DOWN_LENGTH',
    'TACKLER',
    'FILLER',
    'TYPE',
]

# Defining tokens
t_TIME = r'\(\d*:\d+\)'
t_PLAYER = r'[A-Z]\.[a-zA-Z]+'
t_FORMATION = r'\([A-Z]\w+\)'
t_PASS_LENGTH = r'(short|deep)'
t_PASS_DIRECTION = r'(left|middle|right)'
# t_DOWN = r'\d-\d+-'
def t_DOWN_NUM(t):
    r'[1-4](?=-\d+)'
    t.value = int(t.value)
    return t
def t_DOWN_LENGTH(t):
    r'(?<=\d-)\d+ '
    t.value = int(t.value)
    return t
t_LOCATION_SIDE = r'[A-Z][A-Z][A-Z]?'
t_LOCATION_YARDAGE = r'\d+'
t_YARDAGE = r'\d+\syards?'
t_TACKLER = r'\([A-Z]\.[a-zA-Z]+\)'
t_TYPE = r'pass'
t_FILLER = r'(to|for|\.|-)'
t_ignore = ' '

def t_error(t):
    print('Illegal characters')
    t.lexer.skip(1)


string_to_parse = '1-10-PIT 42 (:50) (Shotgun) B.Roethlisberger pass short right to L.Bell to PIT 43 for 1 yard (M.Butler)'

lexer = lex.lex()

# lexer.input(string_to_parse)
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)

# Setting up parsers/grammer rules
def p_play(p):
    '''
    play : pass
    '''
    print(p[1].formation)
    print(p[1].time)
    print(p[1].down_num)
    print(p[1].qb)
    print(p[1].tackler)
    print(p[1].reciever)
    print(p[1].length)
    print(p[1])


def p_pass(p):
    '''
    pass : DOWN_NUM FILLER DOWN_LENGTH FILLER location TIME FORMATION PLAYER TYPE direction FILLER PLAYER FILLER location FILLER YARDAGE TACKLER
    '''
    p[0] = Play(p[1], p[3], p[6], p[7], p[8], p[10], p[12], p[14], p[16], p[17], p[5])
    # print(Play.formation)

# def p_simple(p):
#     '''
#     simple : DOWN LOCATION_SIDE LOCATION_YARDAGE TIME FORMATION PLAYER 
#     '''
#     p[0] = ('Player', p[1])

def p_direction(p):
    '''
    direction : PASS_LENGTH PASS_DIRECTION
    '''

def p_location(p):
    '''
    location : LOCATION_SIDE LOCATION_YARDAGE
    '''
parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)