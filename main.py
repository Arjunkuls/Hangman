import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

RADIUS = 20
GAP = 15
letters=[]
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13)/2)
starty = 400
A = 65

for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x,y, chr(A + i)])

Letter_Font = pygame.font.SysFont("comicsans", 40)
Word_Font = pygame.font.SysFont("comicsans", 60)

images = []
for i in range(7):
    imgload = pygame.image.load("hangman" + str(i) + ".png")
    images.append(imgload)

hstatus = 0
words = ["abandon", "ability", "able", "about", "above", "abroad", "absolute", "academic", "accept", "access", "accident", "accommodation", "accompany", "account", "achievement", "acknowledge", "awesome", "cool", "clever", "genius", "hangman", "game", "play", "fun", "enjoy", "entertain", "sky", "helicopter", "plane", "jet", "immortal", "invinvible"]
wordsmall = random.choice(words)
word = wordsmall.upper() 
guessed = []

FPS = 60

clock = pygame.time.Clock()

run = True

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

won = True

def draw():
    win.fill(WHITE)

    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        elif letter.lower() in "aeiou":
            display_word += "- "
        else:
            display_word += "_ "

        theword = Word_Font.render(display_word, 1, BLACK)
        win.blit(theword, (400, 200))


    for letter in letters:
        x,y,alphabet = letter
        pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
        text = Letter_Font.render(alphabet, 1, BLACK)
        win.blit(text, (x - (text.get_width()/2), y - (text.get_height()/2)))

    win.blit(images[hstatus], (150, 100))
    pygame.display.update()

while run:
    clock.tick(FPS)

    draw()    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for letter in letters:
                x,y,ltr = letter
                dis = math.sqrt(((x-mx)**2) + ((y-my)**2))
                if dis<=RADIUS:
                    print(ltr)
                    guessed.append(ltr)
                    if ltr not in word:
                        hstatus+=1
                    letters.pop(letters.index(letter))

    won = True    
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        pygame.time.delay(1000)
        win.fill(WHITE)
        t = Word_Font.render("WE HAVE A WINNER!!", 1, BLACK)
        win.blit(t, ((WIDTH/2 - t.get_width()/2),(HEIGHT/2 - t.get_height()/2)))
        pygame.display.update()
        pygame.time.delay(3000)
        break

    if hstatus == 6:
        pygame.time.delay(1000)
        win.fill(WHITE)
        t = Word_Font.render("WE HAVE A LOSER!!,", 1, BLACK)
        t2 = Word_Font.render("The correct answer was: " + word, 1, BLACK)
        win.blit(t, ((WIDTH/2 - t.get_width()/2),(HEIGHT/2 - t.get_height()/2)))
        win.blit(t2, ((WIDTH/2 - t2.get_width()/2),(HEIGHT/2 - t2.get_height()/2) + (t2.get_height()+20)))

        pygame.display.update()
        pygame.time.delay(3000)
        break

pygame.quit()