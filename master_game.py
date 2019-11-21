import sys
from enum import Enum
from GIFImage import GIFImage
from Pet import Pet 
from Pet import PetType
from Buttonify import Buttonify
from RectButton import RectButton
from Meditate import Meditate
import pygame as pg
from RectButton import RectButton
import os
import shutil
import datetime

class Screen(Enum):
    STARTING = 0
    CREDITS = 1
    SELECTION = 2
    EGG = 3
    Q_A = 4
    Q_A1 = 5
    Q_A2 = 6
    Q_A3 = 7
    Q_A4 = 8
    HATCH = 9
    HOME = 100
    FOOD = 101
    WATER = 102
    SLEEP = 103
    FUN = 104
    MEDITATION = 105

    def __lt__(this, other):
        if this.__class__ is other.__class__:
            return this.value < other.value
        return NotImplemented

    def __gt__(this, other):
        if this.__class__ is other.__class__:
            return this.value > other.value
        return NotImplemented


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # More colours should be added here
ORANGE = (255, 128, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (127, 0, 255)
WIDTH = 800
HEIGHT = 480

FOOD_CHANGE_RATE = -100 / (12 * 60 * 60 * 12) # 100% per (12 f/s * 60s/m * 60 m/h * 12 h to empty)
WATER_CHANGE_RATE = -100 / (12 * 60 * 60 * 6) # 100% per (12 f/s * 60s/m * 60 m/h * 6 h to empty)
SLEEP_CHANGE_RATE = -100 / (12 * 60 * 60 * 16) # 100% per (12 f/s * 60s/m * 60 m/h * 16 h to empty)
STRESS_CHANGE_RATE = 100 / (12 * 60 * 60 * 24) # 100% per (12 f/s * 60s/m * 60 m/h * 24 h to full)

pg.init()
pg.font.init()
init_time = datetime.datetime.now()
titleFont = pg.font.Font("VT323-Regular.ttf", 180)
textFont = pg.font.Font("VT323-Regular.ttf", 60)
smallFont = pg.font.Font("VT323-Regular.ttf", 40)

screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)


def update_save(currPet):
    savefile = open("save/saveFile.txt", "w+")
    savefile.write(str((currPet.petType)) + "\n")
    savefile.write(currPet.name + "\n")
    savefile.write(str(currPet.food) + "\n")
    savefile.write(str(currPet.water) + "\n")
    savefile.write(str(currPet.sleep) + "\n")
    savefile.write(str(currPet.stress) + "\n")
    savefile.write(str(datetime.datetime.now().strftime("%Y-%B-%d %I:%M:%S.%f")) + "\n")
    savefile.close()

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(29, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
 
# Our function on what to do when the button is pressed  
def Shutdown(channel):  
    os.system("sudo shutdown -h now") 
  
GPIO.add_event_detect(29, GPIO.FALLING, callback = Shutdown, bouncetime = 5000)  

def main():    
    savefile = open("save/saveFile.txt", "a+")

    FRAMERATE = 12

    titleBG = GIFImage("graphicAssets/BgTitle3")
    homeBG = GIFImage("graphicAssets/BgTitle5")
    homeBG.resize(800, 480)
    qaBG = GIFImage("graphicAssets/BgTitle4")
    qaBG.resize(800, 480)
    sleepBG = GIFImage("graphicAssets/SleepBG")
    sleepBG.resize(800, 480)

    eggUnhatched = GIFImage("graphicAssets/EggUnhatched",
                            WIDTH/4 + 80, HEIGHT/2 - 170, 15)
    eggUnhatched.resize(250, 250)

    startButton = Buttonify("graphicAssets/startButton.png", screen)
    startButton.resize(300, 100)
    startButton.setCoords(100, 300)

    newGameButton = Buttonify("graphicAssets/NewGame.png", screen)
    newGameButton.resize(320, 110)
    newGameButton.setCoords(75, 180)

    continueGameButton = Buttonify("graphicAssets/LoadGame.png", screen)
    continueGameButton.resize(300, 100)
    continueGameButton.setCoords(425, 175)

    qa1LeftButton = RectButton(
        WIDTH / 4 - 145, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa1MiddleButton = RectButton(
        WIDTH / 4 + 98, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa1RightButton = RectButton(
        WIDTH / 4 + 340, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)

    qa2LeftButton = RectButton(
        WIDTH / 4 - 145, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa2MiddleButton = RectButton(
        WIDTH / 4 + 98, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa2RightButton = RectButton(
        WIDTH / 4 + 340, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)

    qa3LeftButton = RectButton(
        WIDTH / 4 - 145, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa3MiddleButton = RectButton(
        WIDTH / 4 + 98, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa3RightButton = RectButton(
        WIDTH / 4 + 340, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)

    qa4LeftButton = RectButton(
        WIDTH / 4 - 145, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa4MiddleButton = RectButton(
        WIDTH / 4 + 98, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa4RightButton = RectButton(
        WIDTH / 4 + 340, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)

    HomeFoodButton = RectButton(
        7 * WIDTH / 8, HEIGHT / 16 + 10, 90, 90, screen, BLACK, 180)
    HomeWaterButton = RectButton(
        7 * WIDTH / 8, HEIGHT / 16 + 110, 90, 90, screen, BLACK, 180)
    HomeSleepButton = RectButton(
        7 * WIDTH / 8, HEIGHT / 16 + 210, 90, 90, screen, BLACK, 180)
    HomeStressButton = RectButton(
        7 * WIDTH / 8, HEIGHT / 16 + 310, 90, 90, screen, BLACK, 180)

    sleepAffirmationsButton = RectButton(10, 60, 215, 50, screen, BLACK, 100)
    sleepBackButton = RectButton(10, 10, 215, 50, screen, BLACK, 100)
    sleepLogButton = RectButton(80, 10, 215, 50, screen, BLACK, 100)
    sleepMeditateButton = RectButton(100, 100, 215, 50, screen, BLACK, 100)
    sleepBreatheButton = RectButton(200, 200, 215, 50, screen, BLACK, 100)

    creditsButton = RectButton(300, 350, 215, 50, screen, BLACK, 100)

    creditToTitleButton = RectButton(20, 20, 215, 50, screen, BLACK, 100)

    randomButton = RectButton(20, 20, 215, 50, screen, BLACK, 100)

    exitButton = RectButton(20, HEIGHT - 70, 215, 50, screen, BLACK, 100)

    currGameState = Screen.STARTING
    currPet = Pet.init_gifImage(PetType.BALAGIF, "bala")
    currPet.setCoords(WIDTH / 2, 3 * HEIGHT / 4)
    currPet.setMoveCycleCount(45)

    meditate = Meditate(screen)

    petSum = 0
    
    while True:

        clock = pg.time.Clock()

        ev = pg.event.get()
        screen.fill(WHITE)

        if currGameState.value > Screen.HATCH.value:
            currPet.food += FOOD_CHANGE_RATE
            currPet.water += WATER_CHANGE_RATE
            currPet.sleep += SLEEP_CHANGE_RATE
            currPet.stress += STRESS_CHANGE_RATE

            currPet.food = 0 if currPet.food < 0 else 100 if currPet.food > 100 else currPet.food
            currPet.water = 0 if currPet.water < 0 else 100 if currPet.water > 100 else currPet.water
            currPet.sleep = 0 if currPet.sleep < 0 else 100 if currPet.sleep > 100 else currPet.sleep
            currPet.stress = 0 if currPet.stress < 0 else 100 if currPet.stress > 100 else currPet.stress

        if currGameState == Screen.STARTING:

            titleBG.animate(screen)

            title = titleFont.render('JikoAi', True, WHITE) 
            screen.blit(title, (WIDTH / 4 - 15, HEIGHT / 2 - 125))

            subtitle = textFont.render('Click to begin!', True, WHITE)
            screen.blit(subtitle, (WIDTH / 4 + 25, HEIGHT / 2 + 32))

            creditsButton.draw()
            creditsButton.draw_text("Credits")

        elif currGameState == Screen.SELECTION:

            titleBG.animate(screen)

            newGameButton.draw()
            continueGameButton.draw()

        elif currGameState == Screen.HOME:

            homeBG.animate(screen)

            innerFoodBar = pg.Rect(40, 40, 200, 25)
            innerWaterBar = pg.Rect(40, 80, 200, 25)
            innerSleepBar = pg.Rect(40, 120, 200, 25)
            innerStressBar = pg.Rect(40, 160, 200, 25)
            currPet.drawStatBar(screen, innerFoodBar, ORANGE, currPet.food)
            currPet.drawStatBar(screen, innerWaterBar, BLUE, currPet.water)
            currPet.drawStatBar(screen, innerSleepBar, PURPLE, currPet.sleep)
            currPet.drawStatBar(screen, innerStressBar, RED, currPet.stress)
            currPet.draw(screen)

            HomeFoodButton.draw()
            HomeFoodButton.draw_text("food")
            HomeWaterButton.draw()
            HomeWaterButton.draw_text("water")
            HomeSleepButton.draw()
            HomeSleepButton.draw_text("sleep")
            HomeStressButton.draw()
            HomeStressButton.draw_text("play")

            exitButton.draw()
            exitButton.draw_text("EXIT")

            randomButton.draw()
            randomButton.draw_text("RANDOM")
        elif currGameState == Screen.EGG:
            print("FILLER")
        elif currGameState == Screen.FOOD:

            print("FILLER")
        elif currGameState == Screen.HATCH:
            if petSum <= 6:
                currPet = Pet.init_gifImage(PetType.BALAGIF, "bala")
            elif petSum <= 9:
                currPet = Pet.init_gifImage(PetType.MAMAUGIF, "mamau")
            else:
                currPet = Pet.init_gifImage(PetType.TORAGIF, "tora")
            savefile.write(str(currPet.petType.value) + "\n")
            #TODO: make an animation
            currGameState = Screen.HOME
        elif currGameState == Screen.Q_A:

            homeBG.animate(screen)
            eggUnhatched.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 80, HEIGHT / 2 + 70))

            eggSubtitle = textFont.render('Who will your pet be?', True, WHITE)
            screen.blit(eggSubtitle, (WIDTH / 4 - 30, HEIGHT / 2 + 77))

            if pg.mouse.get_pressed()[0] and currGameState == Screen.Q_A:
                currGameState = Screen.Q_A1

        elif currGameState == Screen.Q_A1:

            qaBG.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 90, HEIGHT / 2 - 160))

            qTitle = textFont.render('Some questions first!', True, WHITE)
            screen.blit(qTitle, (WIDTH / 4 - 30, HEIGHT / 2 - 157))

            q1Text = textFont.render(
                'Do you often feel stressed?', True, WHITE)

            bgRect1 = pg.Surface((700, 75))
            bgRect1.set_alpha(100)
            bgRect1.fill(BLACK)

            screen.blit(bgRect1, (WIDTH / 4 - 145, HEIGHT / 2 - 35))
            screen.blit(q1Text, (WIDTH / 4 - 110, HEIGHT / 2 - 30))

            bgRect2 = pg.Surface((215, 50))
            bgRect2.set_alpha(100)
            bgRect2.fill(BLACK)

            qa1LeftButton.draw()
            qa1LeftButton.draw_text("Not often")

            qa1MiddleButton.draw()
            qa1MiddleButton.draw_text("Sometimes")

            qa1RightButton.draw()
            qa1RightButton.draw_text("Often")

        elif currGameState == Screen.Q_A2:

            qaBG.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 90, HEIGHT / 2 - 160))

            qTitle = textFont.render('Some questions first!', True, WHITE)
            screen.blit(qTitle, (WIDTH / 4 - 30, HEIGHT / 2 - 157))

            q1Text = textFont.render('I feel good about myself.', True, WHITE)

            bgRect1 = pg.Surface((700, 75))
            bgRect1.set_alpha(100)
            bgRect1.fill(BLACK)

            screen.blit(bgRect1, (WIDTH / 4 - 145, HEIGHT / 2 - 35))
            screen.blit(q1Text, (WIDTH / 4 - 110, HEIGHT / 2 - 30))

            bgRect2 = pg.Surface((215, 50))
            bgRect2.set_alpha(100)
            bgRect2.fill(BLACK)

            qa2LeftButton.draw()
            qa2LeftButton.draw_text("Disagree")

            qa2MiddleButton.draw()
            qa2MiddleButton.draw_text("Not sure")

            qa2RightButton.draw()
            qa2RightButton.draw_text("Agree")

        elif currGameState == Screen.Q_A3:

            qaBG.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 90, HEIGHT / 2 - 160))

            qTitle = textFont.render('Some questions first!', True, WHITE)
            screen.blit(qTitle, (WIDTH / 4 - 30, HEIGHT / 2 - 157))

            q1Text = textFont.render(
                'I have things under control.', True, WHITE)

            bgRect1 = pg.Surface((700, 75))
            bgRect1.set_alpha(100)
            bgRect1.fill(BLACK)

            screen.blit(bgRect1, (WIDTH / 4 - 145, HEIGHT / 2 - 35))
            screen.blit(q1Text, (WIDTH / 4 - 110, HEIGHT / 2 - 30))

            bgRect2 = pg.Surface((215, 50))
            bgRect2.set_alpha(100)
            bgRect2.fill(BLACK)

            qa3LeftButton.draw()
            qa3LeftButton.draw_text("Disagree")

            qa3MiddleButton.draw()
            qa3MiddleButton.draw_text("Not sure")

            qa3RightButton.draw()
            qa3RightButton.draw_text("Agree")

        elif currGameState == Screen.Q_A4:

            qaBG.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 90, HEIGHT / 2 - 160))

            qTitle = textFont.render('Some questions first!', True, WHITE)
            screen.blit(qTitle, (WIDTH / 4 - 30, HEIGHT / 2 - 157))

            q1Text = textFont.render(
                'I take good care of myself.', True, WHITE)

            bgRect1 = pg.Surface((700, 75))
            bgRect1.set_alpha(100)
            bgRect1.fill(BLACK)

            screen.blit(bgRect1, (WIDTH / 4 - 145, HEIGHT / 2 - 35))
            screen.blit(q1Text, (WIDTH / 4 - 110, HEIGHT / 2 - 30))

            bgRect2 = pg.Surface((215, 50))
            bgRect2.set_alpha(100)
            bgRect2.fill(BLACK)

            qa4LeftButton.draw()
            qa4LeftButton.draw_text("Disagree")

            qa4MiddleButton.draw()
            qa4MiddleButton.draw_text("Not sure")

            qa4RightButton.draw()
            qa4RightButton.draw_text("Agree")

        elif currGameState == Screen.WATER:
            print("FILLER")
        elif currGameState == Screen.FUN:
            print("FILLER")
        elif currGameState == Screen.SLEEP:
            sleepBG.animate(screen)
            #affirmations
            sleepAffirmationsButton.draw()
            sleepAffirmationsButton.draw_text("Affirmations")
            #meditate
            #sleep
            #breathe
            #back
            sleepBackButton.draw()
            sleepBackButton.draw_text("Back")
        elif currGameState == Screen.MEDITATION:
            sleepBG.animate(screen)
            meditate.setOn()
        elif currGameState == Screen.CREDITS:
            titleBG.animate(screen)
            creditToTitleButton.draw()
            creditToTitleButton.draw_text("Back")

        pg.display.update()

        clock.tick(FRAMERATE)

        for event in ev:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if currGameState.value > Screen.HATCH.value:
                    savefile.close()
                    update_save(currPet) 
                    savefile = open("save/saveFile.txt", 'a+')
                    print ("saving")
                mouse = pg.mouse.get_pos()
                if creditsButton.getImageRect().collidepoint(mouse) and currGameState == Screen.STARTING:
                    currGameState = Screen.CREDITS
                elif currGameState == Screen.STARTING:
                    currGameState = Screen.SELECTION
                elif newGameButton.getImageRect().collidepoint(mouse) and currGameState == Screen.SELECTION:
                    open("save/saveFile.txt", 'w').close()
                    currGameState = Screen.Q_A
                elif continueGameButton.getImageRect().collidepoint(mouse) and currGameState == Screen.SELECTION:
                    lines = open("save/saveFile.txt", "r").read().splitlines()
                    if len(lines) > 5:
                        savePetType = lines[0]
                        if savePetType.__contains__("GIF"):
                            currPet = Pet.init_gifImage(lines[0], lines[1])
                        else:
                            currPet = Pet(lines[0], lines[1])
                        currPet.food = float(lines[2])
                        currPet.water = float(lines[3])
                        currPet.sleep = float(lines[4])
                        currPet.stress = float(lines[5])
                        dtime = (init_time - datetime.datetime.strptime(lines[6], "%Y-%B-%d %I:%M:%S.%f")).seconds
                        currPet.food += FOOD_CHANGE_RATE * dtime * FRAMERATE
                        currPet.water += WATER_CHANGE_RATE * dtime * FRAMERATE
                        currPet.sleep += SLEEP_CHANGE_RATE * dtime * FRAMERATE
                        currPet.stress += STRESS_CHANGE_RATE * dtime * FRAMERATE
                        currGameState = Screen.HOME
                    else:
                        print("Save game not found")
                        open("save/saveFile.txt", 'w').close()
                        currGameState = Screen.Q_A
                elif qa1LeftButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A1:
                    petSum += 1
                    currGameState = Screen.Q_A2
                elif qa1MiddleButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A1:
                    petSum += 2
                    currGameState = Screen.Q_A2
                elif qa1RightButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A1:
                    petSum += 3
                    currGameState = Screen.Q_A2
                elif qa2LeftButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A2:
                    petSum += 1
                    currGameState = Screen.Q_A3
                elif qa2MiddleButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A2:
                    petSum += 2
                    currGameState = Screen.Q_A3
                elif qa2RightButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A2:
                    petSum += 3
                    currGameState = Screen.Q_A3
                elif qa3LeftButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A3:
                    petSum += 1
                    currGameState = Screen.Q_A4
                elif qa3MiddleButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A3:
                    petSum += 2
                    currGameState = Screen.Q_A4
                elif qa3RightButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A3:
                    petSum += 3
                    currGameState = Screen.Q_A4
                elif qa4LeftButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A4:
                    petSum += 1
                    currGameState = Screen.HATCH
                elif qa4MiddleButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A4:
                    petSum += 2
                    currGameState = Screen.HATCH
                elif qa4RightButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A4:
                    petSum += 3
                    currGameState = Screen.HATCH
                elif currGameState == Screen.HATCH:
                    currGameState = Screen.HOME
                elif creditToTitleButton.getImageRect().collidepoint(mouse) and currGameState == Screen.CREDITS:
                    currGameState = Screen.STARTING
                elif sleepAffirmationsButton.getImageRect().collidepoint(mouse) and currGameState == Screen.SLEEP:
                    currGameState = Screen.MEDITATION
                elif currGameState == Screen.HOME:
                    if HomeFoodButton.getImageRect().collidepoint(mouse):
                        currGameState = Screen.FOOD
                    elif HomeWaterButton.getImageRect().collidepoint(mouse):
                        currGameState = Screen.WATER
                    elif HomeSleepButton.getImageRect().collidepoint(mouse):
                        currGameState = Screen.SLEEP
                    elif HomeStressButton.getImageRect().collidepoint(mouse):
                        currGameState = Screen.FUN
                    elif exitButton.getImageRect().collidepoint(mouse):
                        update_save(currPet)
                        pg.quit()
                        if sys.platform.startswith('linux'):
                            os.system("sudo shutdown -h now")  
                        sys.exit()


main()
