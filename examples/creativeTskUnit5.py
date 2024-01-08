#This python only works in the cs academy script editor
#IT was my unit 5 creative task(given as an example of code written at 3am in the last 2 days)

import time
import random

#colors
white = "white"
lightBackround = "lightgrey"
crimson = "crimson"
black = "black"

gameLabel = Label("Undertrol",195,55,size=50, italic=True, bold=True)

    
#variables
app.PLAYER_CAN_MOVE = False
app.FIRST_DIALOUGE_SCENE = False
app.CONTINUE_START_DIALOUGE = False
app.canPlaySound = False

#menu screen
shadowBox = Rect(152,202, 90,40,visible=False)
playBox = Rect(150,200, 90,40, border=black, fill=white)
playLabel = Label("Play", playBox.centerX, playBox.centerY, italic=True, size=20)
Playbutton = Group(playBox, playLabel)

settingShadow = Rect(50+2,300+2,90,40, visible=False)
settingsBox = Rect(50,300,90,40,border=black,fill=white)
settingsLabel = Label("Settings",settingsBox.centerX, settingsBox.centerY, italic=True, size=20 )
settingsButton = Group(settingsBox, settingsLabel)

tutorialShadow = Rect(250+2,300+2,90,40, visible=False)
tutorialBox = Rect(250,300,90,40,border=black,fill=white)
tutorialLabel = Label("Tutorial", tutorialBox.centerX, tutorialBox.centerY, italic=True,size=20)
tutorialButton = Group(tutorialBox, tutorialLabel)

app.main_menu_visible = True

backBtn = Polygon(25,5,10,15,25,25)
backLabel = Label("Back", 45, 14)
back_to_game = Group(backBtn, backLabel, visible=False)
main_Menu = Group(Playbutton, settingsButton, tutorialButton)

def group_shadow(group, x,y,shadow, label):
    if group.hits(x,y):
        shadow.visible = True
        label.opacity =80
    else:
        shadow.visible = False
        label.opacity = 100
        
def remove_shadows_label(reverse=False):
    if not reverse:
        gameLabel.visible = False
        shadowBox.visible = False
        settingShadow.visible = False
        tutorialShadow.visible = False
    else:
        gameLabel.visible = True
        shadowBox.visible = True
        settingShadow.visible = True
        tutorialShadow.visible = True

app.checkSoundBox = None
app.checkMark = None
def handleSettings():
    back_to_game.visible = True
    remove_shadows_label()
    app.main_menu_visible = False
    
    app.checkSoundBox = Rect(62,65,20,20,fill=None,border="grey")
    app.checkMark = Group(Line(68,72,73,77), Line(73,77,82,65))
    settingComponents = Group(
        Rect(50,50,300,300,fill=None,border="black"),
        Label("sound",125,75,size=20),
        app.checkSoundBox,
        app.checkMark)
    if app.canPlaySound:
        app.checkMark.visible = True
    else:
        app.checkMark.visible = False
    return settingComponents

tutorialGroup = Group(
    Label("Tutorial", 200, 65, size=40, bold=True),
    Label("Use arrow keys to select GUI", 200,112), 
    Label("Use enter to select option in GUI.", 200,132),
    Label("Use \"a\" and \"d\" for movement before fight.", 200, 152),
    Label("Use arrow keys for in fight movement.", 200, 172)
)
tutorialGroup.visible = False
def handleTutorialBtn():
    print("tutorial")
    tutorialGroup.visible = True
    back_to_game.visible = True
    remove_shadows_label()
    app.main_menu_visible = False

def onMouseMove(mouseX,mouseY):
    #menu screen
    if app.main_menu_visible:
        group_shadow(Playbutton,mouseX,mouseY, shadowBox, playLabel)
        group_shadow(settingsButton,mouseX,mouseY, settingShadow, settingsLabel)
        group_shadow(tutorialButton,mouseX,mouseY, tutorialShadow, tutorialLabel)
        
    elif back_to_game.visible:
        if back_to_game.hits(mouseX,mouseY):
            back_to_game.opacity = 80
        else:
            back_to_game.opacity = 100
app.settingsGroup = None
def onMousePress(mouseX, mouseY):
    #menu screen
    if not main_Menu.visible:
        if app.checkSoundBox:
            if app.checkSoundBox.contains(mouseX,mouseY):
                if app.checkMark.visible: 
                    app.canPlaySound = False
                    app.checkMark.visible = False
                else:
                    app.canPlaySound = True
                    app.checkMark.visible = True
                
    if app.main_menu_visible:
        if Playbutton.hits(mouseX,mouseY):
            main_Menu.visible = False #main menu
            menu.visible = True #name screen
        elif settingsButton.hits(mouseX,mouseY):
            main_Menu.visible = False
            app.settingsGroup = handleSettings()
        elif tutorialShadow.hits(mouseX,mouseY):
            main_Menu.visible = False
            handleTutorialBtn()
    elif back_to_game.visible:
        if back_to_game.hits(mouseX,mouseY):
            main_Menu.visible = True
            app.main_menu_visible = True
            remove_shadows_label(True)
            back_to_game.visible = False
            if app.settingsGroup:
                app.settingsGroup.visible = False
            tutorialGroup.visible = False
            
            
#main name screen
game_name = "Name Select!" 
menu_background = Rect(0,0,400,400, fill=lightBackround)
input_box = Rect(100,200,200,30, fill=white)
main_text = Label("Welcome, enter your name!", 200, 135, size=20)
game_name_text = Label(game_name, 200,45, size=40)
Label_Overlay = Label("",120,215)
menu = Group(menu_background, input_box, Label_Overlay, main_text, game_name_text)
max_length_label = Label("MAX LENGTH REACHED.", 200,245, fill=crimson, visible=False)
zeroCharacter_name = Label("Name cannot be 0 characters long!", 200,245, fill=crimson, visible=False)

menu.visible = False


# player sprite(Frisk) refrence: https://static.wikia.nocookie.net/new-undertale-fanon-au/images/1/1e/Undertale_frisk_Sprite.png/revision/latest?cb=20220205040720
playerBrown = 'saddleBrown'
playerYellow = 'gold'
playerBlue = 'lightBlue'
playerPink = 'hotPink'

#arms
arm1 = Group(
    Rect(94,156,5,55,fill=playerBrown),
    Rect(85,186,10,4,fill=playerBrown),
    Rect(92,149,8,7,fill=playerBlue), #playerBlue small
    Rect(85,156,9,20, fill=playerBlue),
    Rect(92,143,22,6,fill=playerBrown),
    Rect(100,145,6,11,fill=playerBrown),
    Rect(85,150,7,6,fill=playerBrown) ,#playerBrown
    Rect(79,156,6,34,fill=playerBrown), #playerBrown long
    Rect(85,176,9,10, fill=playerYellow), #hand 1 - playerYellow
    Rect(84,171,11,5,fill=playerBrown)
    )
arm2 = Group(
    Rect(261,156,5,55,fill=playerBrown),
    Rect(265,186,10,4,fill=playerBrown),
    Rect(260,149,8,7,fill=playerBlue), #playerBlue small
    Rect(266,156,9,20, fill=playerBlue),
    Rect(246,143,22,6,fill=playerBrown),
    Rect(254,145,6,11,fill=playerBrown),
    Rect(268,150,7,6,fill=playerBrown) ,#playerBrown
    Rect(275,156,6,34,fill=playerBrown), #playerBrown long
    Rect(266,176,9,10, fill=playerYellow), #hand 2 - playerYellow
    Rect(265,171,11,5,fill=playerBrown)
)

#rotates arm
arm2.centerX = 172
arm2.centerY = 177
arm2.rotateAngle = 0
arms = Group(arm1,arm2)


#legs
playerLeftLeg = Polygon(125, 208, 108,208,108,218,100,218,100,225,127,225,127,208, fill=playerBrown)
playerRightLeg = Polygon(137, 208, 161, 208, 161, 218, 169, 218, 169, 225, 136, 225, 136, 208, fill=playerBrown)

legs = Group(playerLeftLeg,playerRightLeg)

#torso
torso = Group(
    Rect(163,156,7,7,fill=playerBrown), #small block near arm
    Rect(99,156,65,35,fill=playerBlue),
    Rect(99,191,22,14,fill=playerBlue),
    Rect(141,191,28,14,fill=playerBlue),
    Rect(163,163,6,40,fill=playerBlue), #playerBlue long strip
    Rect(114,142,7,7,fill=playerBlue),
    Rect(106,149,56,8,fill=playerBlue),
    
    Rect(121,142,27,7,fill=playerBrown), #playerBrown neck area
    Rect(148,142,7,7,fill=playerBlue),
    
    Line(99,160,164,160,lineWidth=6,fill=playerPink),
    Line(99,174,169,174,lineWidth=6, fill=playerPink),
    #lower torso
    Rect(99,205,28,6,fill=playerBrown),
    Rect(121,191,6,15,fill=playerBrown),
    Rect(127,191,9,6,fill=playerBrown),
    Rect(136,191,6,20,fill=playerBrown),
    Rect(141,205,30,6,fill=playerBrown),
    Rect(114,136,48,7,fill=playerBrown) #neck type
    )

eye1 = Rect(141,86,15,7,fill=playerBrown)
eye2 = Rect(99,86,15,7,fill=playerBrown)
eyes = Group(eye1,eye2)
head = Group(
    #head bg
    Rect(84,50,100,70,fill=playerYellow),
    Rect(126,118,20,18,fill=playerYellow),
    
    #head
    Rect(120,100,15,7,fill=playerBrown), #mouth
    #eyes
    eyes,
    
    Rect(121,121,7,15,fill=playerBrown),
    Rect(141,121,8,15,fill=playerBrown),
    
    Rect(148,114,28,13,fill=playerBrown),
    Rect(155,107,41,8,fill=playerBrown),
    Rect(176,114,20,6,fill=playerBrown),
    Rect(184,119,7,9,fill=playerBrown),
    Rect(169,126,6,9,fill=playerBrown),
    Rect(183,72,13,36,fill=playerBrown),
    Rect(176,93,8,15,fill=playerBrown),
    Rect(169,100,8,10,fill=playerBrown),
    Rect(86,38,89,20,fill=playerBrown),
    Rect(93,31,75,8,fill=playerBrown),
    Rect(100,23,62,10,fill=playerBrown),
    Rect(174,45,10,36,fill=playerBrown),
    Rect(183,52,6,21,fill=playerBrown),
    Rect(79,45,13,48,fill=playerBrown),
    Rect(91,57,9,9,fill=playerBrown),
    Rect(72,60,13,61,fill=playerBrown),
    Rect(65,80,10,41,fill=playerBrown),
    Rect(72,120,7,8,fill=playerBrown),
    Rect(107,56,27,9,fill=playerBrown),
    Rect(84,107,8,14,fill=playerBrown),
    Rect(85,120,43,8,fill=playerBrown),
    Rect(91,114,16,7,fill=playerBrown),
    Rect(141,57,14,15,fill=playerBrown),
    Rect(154,57,21,8,fill=playerBrown),
    Rect(162,64,15,8,fill=playerBrown),
    Rect(169,71,7,15,fill=playerBrown)
    )

playerFrisk = Group(arms, legs,torso,head)
playerFrisk.visible = False
playerFrisk.soulsText = Label("Souls",350,20,visible=False)
playerFrisk.souls = Label(0,350,35) #set to zero for now - set to animating grad as loop
playerFrisk.souls.visible = False

#add player hitbox for collision detection
hitbox = Group(Rect(playerFrisk.left, playerFrisk.top, playerFrisk.width, playerFrisk.height, fill=None)) #hit box(scaleable)
hitbox.opacity = 0
playerFrisk.add(hitbox)


g_letter = Group(
    Line(62,378,66,378,lineWidth=4,fill="orange"),
    Line(64.5,378,64.5,389,lineWidth=4,fill="orange"),
    Line(64.5,387,58,387,lineWidth=4,fill="orange"),
    Line(59,387,59,369,lineWidth=4,fill="orange")
)
g_letter.centerX -= 1

FightRectangle = Rect(20, 360,69,35, fill=None, border="orange")
FightSword = Group(
    Line(33,368,30,380,fill="orange",lineWidth=3),
    Line(26,380,33,382,fill="orange"),
    Line(29,382,27,388,fill="orange"),
    Polygon(31, 369, 34, 365, 35, 368,fill="orange")
)

FightRectGroup = Group(
    FightRectangle,
    g_letter,
    Line(48,369,39,369,lineWidth=4,fill="orange"),
    Line(41,369,41,389,lineWidth=4,fill="orange"),
    Line(40,378,47,378,lineWidth=4,fill="orange"),
    Line(49,369,56,369,lineWidth=4,fill="orange"),
    Line(52,369,52,385,lineWidth=4,fill="orange"),
    Line(49,387,56,387,lineWidth=4,fill="orange"),
    Line(58,369,66,369,lineWidth=4,fill="orange"),
    Line(65,369,65,374,lineWidth=4,fill="orange"),
    Line(68,389,68,367,lineWidth=4,fill="orange"),
    Line(68,378,74,378,lineWidth=4,fill="orange"),
    Line(74,389,74,367,lineWidth=4,fill="orange"),
    Line(81,389,81,368,lineWidth=4,fill="orange"), #t letter
    Line(76,369,86,369,lineWidth=4,fill="orange"),
)

ActSound = Group(
    Line(124,375,124,383,fill="orange",lineWidth=1),
    Line(126,373,127,377,fill="orange",lineWidth=1),
    Line(127,377,127,382,fill="orange",lineWidth=1),
    Line(127,382,126,384,fill="orange",lineWidth=1),
    Line(128,372,130,377,fill="orange",lineWidth=1),
    Line(130,377,130,383,fill="orange",lineWidth=1),
    Line(130,383,128,385,fill="orange",lineWidth=1)
)

ActRectangleFill = Rect(117, 360,69,35, fill=None, border="orange")
ActRect = Group(
    ActRectangleFill,
    Line(139,368,139,389,lineWidth=4,fill="orange"),
    Line(148,368,148,389,lineWidth=4,fill="orange"),
    Line(139,369,148,369,lineWidth=4,fill="orange"),
    Line(139,378,148,378,lineWidth=4,fill="orange"),
    Line(155,368,155,389,lineWidth=4,fill="orange"),
    Line(155,369,165,369,lineWidth=4,fill="orange"),
    Line(163,369,163,375,lineWidth=4,fill="orange"),
    Line(155,387,165,387,lineWidth=4,fill="orange"),
    Line(163,387,163,379,lineWidth=4,fill="orange"),
    Line(174,389,174,369,lineWidth=4,fill="orange"),
    Line(167,369,180,369,lineWidth=4,fill="orange")
)

itemActionPolygon = Polygon(223,380,229,382,231,388,229,389,225,389,223,388,fill="orange")
itemActionPolygon.width = 10
itemActionPolygon.height = 10
itemActionPolygon.centerY -= 2
ItemAction = Group(
    itemActionPolygon,
    Line(223,371,225,377,fill="orange"),
    Line(225,377,229,372,fill="orange"),
    Line(225,379,225,372,fill="orange")
    )

ItemSubRect = Rect(217, 360,69,35, fill=None, border="orange")
ItemRect = Group(
    ItemSubRect,
    Line(239,370,239,387,lineWidth=4,fill="orange"),
    Line(234,369,244,369,lineWidth=4,fill="orange"),
    Line(235,387,244,387,lineWidth=4,fill="orange"),
    Line(250,369,250,388,lineWidth=4,fill="orange"),
    Line(246,369,254,369,lineWidth=4,fill="orange"),
    Line(258,368,258,389,lineWidth=4,fill="orange"),
    Line(258,387,265,387,lineWidth=4,fill="orange"),
    Line(258,369,265,369,lineWidth=4,fill="orange"),
    Line(269,369,269,389,lineWidth=4,fill="orange"),
    Line(269,368,274,374,lineWidth=4,fill="orange"),
    Line(274,374,276,368,lineWidth=4,fill="orange"),
    Line(277,368,277,389,lineWidth=4,fill="orange"),
    Line(258,377,264,377,lineWidth=4,fill="orange")
)

MercyAction = Group(
    Line(320,370,328,386,fill="orange",lineWidth=1),
    Line(325,370,318,386,fill="orange",lineWidth=1)
    )

MercySubRect = Rect(313,360,69,35, fill=None, border="orange")
MercyRect = Group(
    MercySubRect,
    Line(332,367,332,389,lineWidth=4,fill="orange"),
    Line(339,367,339,389,lineWidth=4,fill="orange"),
    Line(332,367,336,375,lineWidth=4,fill="orange"),
    Line(336,375,339,367,lineWidth=4,fill="orange"),
    Line(345,368,345,388,lineWidth=4,fill="orange"),
    Line(345,369,350,369,lineWidth=4,fill="orange"),
    Line(345,377,350,377,lineWidth=4,fill="orange"),
    Line(345,387,350,387,lineWidth=4,fill="orange"),
    Line(354,389,354,367,lineWidth=4,fill="orange"),
    Line(354,369,360,369,lineWidth=4,fill="orange"),
    Line(359,368,359,377,lineWidth=4,fill="orange"),
    Line(359,377,355,377,lineWidth=4,fill="orange"),
    Line(355,377,359,385,lineWidth=4,fill="orange"),
    Line(359,384,359,389,lineWidth=4,fill="orange"),
    Line(364,369,368,369,lineWidth=4,fill="orange"),
    Line(364,369,364,388,lineWidth=4,fill="orange"),
    Line(364,387,368,387,lineWidth=4,fill="orange"),
    Line(368,387,368,380,lineWidth=2,fill="orange"),
    Line(368,369,368,375,lineWidth=2,fill="orange"),
    Line(372,367,372,376,lineWidth=4,fill="orange"),
    Line(372,375,375,380,lineWidth=4,fill="orange"),
    Line(374,379,374,389,lineWidth=4,fill="orange"),
    Line(377,367,377,376,lineWidth=4,fill="orange"),
    Line(376,375,375,379,lineWidth=4,fill="orange")
)

backgroundLines = Group(
    Line(199,8,199,204,fill="green"),
    Line(10,8,390,8,fill="green"),
    Line(10,106,390,106,fill="green"),
    Line(10,106,390,106,fill="green"),
    Line(10,203,390,203,fill="green"),
    Line(10,8,10,203,fill="green"),
    Line(390,8,390,203,fill="green"),
    Line(263,8,263,203,fill="green"),
    Line(328,8,328,203,fill="green"),
    Line(136,8,136,203,fill="green"),
    Line(72,8,72,203,fill="green")
)



healthRect = Rect(172,331,20,20,fill="yellow")

nameLabel = Label("",90,341,fill="white",size=20,bold=True, italic=True)

healthLabel = Label("HP",160,341,fill="white",size=10,bold=True)

slashLabel = Label("/", 224,340,fill="white",size=20,bold=True,rotateAngle=25)


fightDialogRect = Rect(20,208,360,117,fill=None,border="white",borderWidth = 3)

playerFrisk.maxHealthLabel = Label(20,245,341,fill="white",bold=True,size=15)

playerFrisk.currentHealthLabel = Label(20,205,341,fill="white",bold=True,size=15)

fightGui = Group(healthRect,nameLabel,healthLabel,slashLabel,fightDialogRect, playerFrisk.currentHealthLabel, playerFrisk.maxHealthLabel )

fightBackground = Group(FightRectGroup,FightSword,ActSound,ActRect,ItemAction,ItemRect,MercyAction,MercyRect,backgroundLines)

fightGui.visible = False
fightBackground.visible = False

battleImage = Image("cmu://735068/26905876/Screenshot+2023-12-01+at+11.38.20+PM.png", 25,215,visible=False)
#enemy sprites

dummy = Group(
    Polygon(142, 170, 218, 121, 251, 113, 259, 118, 264, 135, 270, 147, 269, 163, 266, 175, 260, 180, 259, 188, 259, 201, 264, 210, 266, 224, 270, 241, 271, 251, 273, 258, 274, 269, 272, 281, 260, 289, 248, 292, 230, 293, 212, 291, 205, 275, 213, 252, 217, 234, 216, 225, 210, 201, 207, 191, 204, 185),
    Circle(207,148,5,fill="white"),
    Rect(213,315,60,20),
    Line(243,291,243,316,lineWidth=5,fill="white")
)
dummy.visible = False
dummy.centerX = 260
dummy.centerY = playerFrisk.centerY - 10
dummy.health = 50

app.run_dialogue = False #default is false
# is called on playbtn click
def start_game():
    app.main_menu_visible = False
    remove_shadows_label()
    menu.visible = False
    playerFrisk.visible = True
    app.run_dialogue = True
    nameLabel.value = app.name.upper()
    
    if app.run_dialogue:
        app.fallen_down_sound = Sound("cmu://735068/26602777/Undertale+OST_+085+-+Fallen+Down+(Reprise).mp3")
        if app.canPlaySound:
            app.fallen_down_sound.play()
        load_shapes()



def hideAllCanvasElements():
    #ANONYMOUS FUNCTION(lambda) TO CLEAR ALL ELEMENTS ON THE SCREEN
    getAllElements = lambda i: setattr(i, 'visible', False) #lambda to set all elements to not visible
    list(map(getAllElements, app.group.children))
    #hides using map function and list for no visiblity of app children

def encounterBoxVisible():
    app.playerCanMove = False
    popUpCircle = Circle(playerFrisk.centerX+20,playerFrisk.centerY-15,10,fill="white")
    exclaimLabel = Label("!", popUpCircle.centerX, popUpCircle.centerY, fill="black", bold=True)
    encounterBox = Group(
        #og val 70,326,10
        popUpCircle,
        Line(popUpCircle.centerX,popUpCircle.centerY,popUpCircle.centerX - 13,popUpCircle.centerY + 1,fill="white"),
        Line(popUpCircle.centerX - 13,popUpCircle.centerY + 1,popUpCircle.centerX,popUpCircle.centerY - 3,fill="white"),
        Line(popUpCircle.centerX - 9,popUpCircle.centerY - 1,popUpCircle.centerX + 1,popUpCircle.centerY - 6,fill="white"),
        exclaimLabel
    )
    encounterBox.visible = True

def animateHeart():
    halfheart, half_heart_2 = Oval(playerFrisk.centerX-3,playerFrisk.centerY,13,8, fill="red"), Oval(playerFrisk.centerX+3,playerFrisk.centerY,13,8, fill="red")
    heart = Group(halfheart,half_heart_2)
    halfheart.rotateAngle = 35
    half_heart_2.rotateAngle = -35
    sleep(0.08)
    halfheart.visible = False
    half_heart_2.visible = False
    sleep(0.08)
    halfheart.visible = True
    half_heart_2.visible = True
    sleep(0.08)
    halfheart.visible = False
    half_heart_2.visible = False
    sleep(0.08)
    halfheart.visible = True
    half_heart_2.visible = True
    playerFrisk.heart1 = halfheart
    playerFrisk.heart2 = half_heart_2
    while halfheart.centerX > 50:
        heart.centerX -= 20
        heart.centerY += 64
        sleep(0.0002)
    heart.centerX = 30
    return halfheart.centerX ,halfheart.centerY
    
playerFrisk.GUISelect = False

def makeGuiVisible(mainRectangle, secondRect, action, color, actionVisible=True): #default is true for action visible
    mainRectangle.fill = color
    secondRect.fill = None
    secondRect.border = color
    if actionVisible:
        action.visible = True
    else:
        action.visible = False
        playerFrisk.fullHeart.centerX = action.centerX
        playerFrisk.fullHeart.centerY = action.centerY

def displayFightBoxes(centerValues):
    fightGui.visible = True
    fightBackground.visible = True
    playerFrisk.GUISelect = "Fight"
    print(f"Heart:{centerValues}")
    

def checkFightSelect():
    if playerFrisk.GUISelect == "Fight":
        #make fight falsey
        makeGuiVisible(FightRectGroup, FightRectangle, FightSword, "yellow", False)
        #make act rect visible
        makeGuiVisible(ActRect, ActRectangleFill, ActSound, "orange")
        #make item rect visible
        makeGuiVisible(ItemRect, ItemSubRect, ItemAction, "orange")
        #make mercy rect visible
        makeGuiVisible(MercyRect, MercySubRect, MercyAction, "orange")
    elif playerFrisk.GUISelect == "Act":
        #do act rect falsey
        makeGuiVisible(ActRect, ActRectangleFill, ActSound, "yellow", False)
        #make fight rect visible
        makeGuiVisible(FightRectGroup, FightRectangle, FightSword, "orange")
        #make item rect visible
        makeGuiVisible(ItemRect, ItemSubRect, ItemAction, "orange")
        #make mercy rect visible
        makeGuiVisible(MercyRect, MercySubRect, MercyAction, "orange")
    elif playerFrisk.GUISelect == "Item":
        #make item falsey
        makeGuiVisible(ItemRect, ItemSubRect, ItemAction, "yellow", False)
        #make act rect visible
        makeGuiVisible(ActRect, ActRectangleFill, ActSound, "orange")
        #make fight rect visible
        makeGuiVisible(FightRectGroup, FightRectangle, FightSword, "orange")
        #make mercy rect visible
        makeGuiVisible(MercyRect, MercySubRect, MercyAction, "orange")
    elif playerFrisk.GUISelect == "Mercy":
        #make mercy rect falsey
        makeGuiVisible(MercyRect, MercySubRect, MercyAction, "yellow", False)
        #make act rect visible
        makeGuiVisible(ActRect, ActRectangleFill, ActSound, "orange")
        #make item rect visible
        makeGuiVisible(ItemRect, ItemSubRect, ItemAction, "orange")
        #make fight rect visible
        makeGuiVisible(FightRectGroup, FightRectangle, FightSword, "orange")

def loopOverString(string,label,leftValue, delay):
    for char in string:
        label.value += char
        label.left = leftValue
        sleep(delay) #delay in ms
app.FightLabel = None
def displayDefaultText(enemyType):
    if enemyType.lower() == "dummy":
      desiredString = "* Dummy approaches!"
      app.fightLabel = Label(desiredString,108,226, fill="white", size=15,bold=True)
      app.fightLabel.toFront()

def loadEnemy(enemyType):
    if enemyType.lower() == "dummy":
        dummy.centerX = 165 - 20
        dummy.centerY = 153 + 5
        dummy.children[0].fill = "lightgrey"
        dummy.children[2].fill = "lightgrey"
        dummy.visible = True
        dummy.width = 75
        dummy.height = 95
        
def resetGui():
    displayDefaultText("Dummy")
    fightDialogRect.left = 20
    fightDialogRect.top = 208
    fightDialogRect.width = 360
    fightDialogRect.height = 117
def gameWin():
    hideAllCanvasElements()
    Rect(0,0,400,400,fill=white)
    playerFrisk.visible = True
    playerFrisk.toFront()
    playerFrisk.opacity = 0
    while playerFrisk.opacity < 100:
        playerFrisk.opacity += 5
        sleep(0.005)
    Label("Dummy defeated!", 200,300, bold=True,size=20)
    app.stop()

app.thirdKnife = False
app.firstKnife = False
app.timer = 0
app.secondKnife = False
def dummyAttacks(attackChoice):
    app.stepsPerSecond = 30
    if knife.hitsShape(playerFrisk.fullHeart):
        damage = random.randint(1, 8)
        if not damage:
            damage = random_number(10,400,2000)
        playerFrisk.currentHealthLabel.value -= damage
        if playerFrisk.currentHealthLabel.value > 0:
            healthRect.width = healthRect.width  - damage
        else:
            hideAllCanvasElements()
            Label("YOU DIED", 200,200,bold=True,fill=white)
            app.stop()
        if playerFrisk.currentHealthLabel.value <= 0 and playerFrisk.souls.value == 2:
            playerFrisk.souls.value -= 1
            playerFrisk.currentHealthLabel.value = 20
            healthRect.width = 20
        if playerFrisk.currentHealthLabel.value <= 0 and playerFrisk.souls.value == 1:
            hideAllCanvasElements()
            Label("YOU DIED", 200,200,bold=True,fill=white)
            app.stop()
    if attackChoice == 1:
        if knife.visible or knife.centerX == 2000:
            if not knife.centerY > 260 and not app.firstKnife:
                knife.centerX += 2
                knife.centerY += 4
            else:
                app.firstKnife = True
                app.timer += 1
                if app.timer < 25:
                    knife.centerX = 200
                    knife.rotateAngle = 0
                    sleep(0.02)
                    knife.centerX = 226
                    sleep(0.02)
                    knife.centerX = 164
                    sleep(0.02)
                else:
                    if app.timer < 65:
                        knife.centerX = 165
                        knife.centerY = 265
                        sleep(0.02)
                        knife.centerX = 190
                        sleep(0.02)
                        knife.centerX = 200
                        sleep(0.02)
                    else:
                        if not app.secondKnife:
                            knife.centerX = 283
                            knife.centerY = 42
                            knife.rotateAngle = 300
                            app.secondKnife = True
                        if not knife.centerY > 260:
                            knife.centerX -= 2
                            knife.centerY += 4
                        else:
                            for i in range(1,5):
                                knife.centerX = 200
                                knife.centerY = 200
                                sleep(0.002)
                                knife.centerX = 162
                                knife.centerX = 204
                                sleep(0.002)
                                knife.centerX = 190
                                knife.centerY = 200
                            if not app.thirdKnife:
                                knife.centerX = 315
                                knife.centerY = 275
                                knife.rotateAngle = 0
                                app.thirdKnife = True
                            if app.thirdKnife:
                                while knife.centerX > 155:
                                    knife.centerX -= 4
                            knife.centerX = 200
                            knife.centerY = 200
                            sleep(0.1)
                            knife.centerX = 165
                            knife.centerY = 165
                            sleep(0.1)
                            knife.centerX = 190
                            knife.centerY = 165
                            sleep(1)
                            knife.visible = False
                            #so its offscreen and does not kill plr
                            knife.centerX = 2000
                            sleep(1)
                            dummySpeech = Oval(225, 105, 80, 60,fill="White")
                            labelToo = Label("AHH! I can't win..", dummySpeech.centerX, dummySpeech.centerY, italic=True, size=8)
                            while dummy.opacity > 0:
                                dummy.opacity -= 2
                                labelToo.opacity -= 2
                                dummySpeech.opacity -= 2
                                sleep(0.002)
                            gameWin()
                        
                            
                            
                        

app.armLoopVar = False
app.black_transition_finished = False
app.runOnce = False
app.stepsPerSecond = 10
def onStep():
    if app.backgroundRect and app.backgroundRect.opacity > 0:
        app.backgroundRect.opacity -= 10
        if app.run_dialogue:
            if not app.armLoopVar:
                arms.centerY += 1
                app.armLoopVar = True
            else:
                arms.centerY -= 1
                app.armLoopVar = False
        sleep(1)
    elif app.backgroundRect and app.backgroundRect.opacity <= 0: #notice how else is not used? 
    #this is because it checks anyways, even if app.background rect is a NoneType(not made yet)
        if not app.FIRST_DIALOUGE_SCENE: #so it runs once
            showStartDialogue()
        if app.soul:
            animate_soul() #does not leave it buffering in stack trace with this if(performance)
        else:   
            if app.playerTouchedWallCounter > 0: #put if waiting til player touches wall
                continueStartDialogue()
    if not app.runOnce:
        if app.PLAYER_CAN_MOVE:
            if dummy.visible:
                if playerFrisk.hitsShape(dummy):
                    encounterBoxVisible()
                    sleep(1)
                    app.background = "black"
                    hideAllCanvasElements()
                    displayFightBoxes(animateHeart())
                    displayDefaultText("Dummy")
                    loadEnemy("Dummy")
                    playerFrisk.fullHeart = Group(playerFrisk.heart1, playerFrisk.heart2)
                    app.runOnce = True
    if app.enemyTurn:
        dummyAttacks(1)
    if playerFrisk.GUISelect:
        if not app.enemyTurn:
            if not app.inFightMode and app.canSwitch and not app.inMercyMode:
                checkFightSelect()
            else:
                if app.moveableRect:
                    #if fight is active!
                    if app.moveableRect.centerX > 375:
                        app.moveableRect.visible = False
                        print("Miss")
                        battleImage.visible = False
                    else:      
                        app.moveableRect.centerX += 10
            



app.soul = None
def animate_soul():
    #in python you can access first item of a tuple with [0] index
    if app.soul[0].hitsShape(playerFrisk):
        app.soul[0].visible = False
        if app.soul[1].hitsShape(playerFrisk):
            app.soul[1].visible = False
            app.soul = None #make it falsy to stop loop in Onstep
            playerFrisk.souls.value = 2
            playerFrisk.souls.visible = True
        else:
            app.soul[1].centerX -= 20
    else:
        app.soul[0].centerX -= 20


displayLabel = Label("", 56,298, fill="white") #f string is basically easier string concatenation here
secondLineLabel = Label("",56,316,fill="white")
DialogBox = Group(
        Rect(30,280,350,100,border="white",fill="black"),
        displayLabel,
        secondLineLabel, visible=False
)
app.labelLeftValue = None
def showStartDialogue():
    app.PLAYER_CAN_MOVE = True
    app.FIRST_DIALOUGE_SCENE = True
    app.labelLeftValue = 43
    labelLeftValue = app.labelLeftValue 
    DialogBox.visible = True
    labelString = f"Welcome, {app.name}."
    #gets iterable as str and loops with for i in var:
    loopOverString(labelString,displayLabel, labelLeftValue, 0.05)
    # add delay
    sleep(1)
    displayLabel.value = ""
    labelString = "You've been brought here for a reason, you know."
    loopOverString(labelString,displayLabel, labelLeftValue, 0.05)
    sleep(1)
    displayLabel.value = ""
    labelString = "This is the start of your journey, your journey in the"
    loopOverString(labelString,displayLabel, labelLeftValue, 0.05)
    labelString = "underground. "
    loopOverString(labelString,secondLineLabel, labelLeftValue, 0.05)
    labelString = "Try to move to the walls with \"a\" and \"d\"."
    loopOverString(labelString,secondLineLabel, labelLeftValue, 0.05)
    app.soul = Circle(400,200,5, fill="yellow"), Circle(410,200,3,fill="orange")
app.testLimit = 0
app.counterGradient = 0


def continueStartDialogue():
    if not app.CONTINUE_START_DIALOUGE:
        app.CONTINUE_START_DIALOUGE = True
        app.finishedGraidentStartAnimation = False
        labelLeftValue = app.labelLeftValue 
        displayLabel.value = ""
        secondLineLabel.value = ""
        labelString = "Great! See the new number in the top right?"
        loopOverString(labelString,displayLabel, labelLeftValue, 0.05)
    #below gonna run in the actual onStep.
    if app.testLimit < 50:
        if app.counterGradient % 3 == 0: #if app counter is == 0
            playerFrisk.souls.fill = gradient("red", "orange", "yellow",start="left")
            
        elif app.counterGradient  % 3 == 1: #if app counter is == 1 after % 3
            playerFrisk.souls.fill = gradient("red", "orange", "yellow",start="center")
        else:
            playerFrisk.souls.fill = gradient("red", "orange", "yellow",start="right")
    
        app.counterGradient += 1
        app.testLimit += 1
    else:
        if not app.finishedGraidentStartAnimation:
            playerFrisk.souls.fill = "black"
            app.finishedGraidentStartAnimation = True
            displayLabel.value = ""
            secondLineLabel.value = ""
            labelString = "That's your souls, or amount of lives you have."
            loopOverString(labelString,displayLabel, app.labelLeftValue, 0.05)
            sleep(2)
            playerFrisk.soulsText.visible = True
            dummy.visible = True
            playerFrisk.centerX = 50
            displayLabel.value = ""
            secondLineLabel.value = ""
            labelString = "Now, let's try fighting an enemy! Go over to the dummy."
            loopOverString(labelString,displayLabel, app.labelLeftValue, 0.05)
    
   
    
    
    
app.backgroundRect = None
def load_shapes(): 
    test = Rect(0,0,400,400,fill="lightgrey")
    line = Line(0,226,400,226,lineWidth=3)
    test.toBack() #send to behind plr
    app.backgroundRect = Rect(0,0,400,400,fill=black)
    
    
    
#!using app globals make this harder to refactor, and pollute global namespace
app.hash = None #create hash var
def create_hash(string):
    desired_hash = hash(string) #create the hash of the string
    print("Hash:",desired_hash)
    app.hash = desired_hash
    #start game
    start_game()

# default parameters, but yuou can change them!
def random_number(a_val=340, m_val=2**31 - 1, c_val=1000):
    #generate the pesudo random number - using LCG
    #i would have done it using random but not refactoring now
    if app.hash:
        seed = app.hash
        a_value = a_val  # multipler
        c_value = c_val # increment
        m_value = m_val # modulus -set upper limit here.(using merresne's primes for default)
        #create equation
        random_number = (a_value*seed+c_value) % m_value
        print(random_number)
        return random_number


app.name = None #player does not have a name yet
def label_overlay(shape, keys):
    #can't import string.puncuation - so i have the string value set here.
    punc_string = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~\"\'1234567890"""
    if keys.lower() == "enter": # save the name if key is enter
        if len(shape.value) > 0:
            app.name = shape.value.lower() #save lower version.
            create_hash(app.name)
            zeroCharacter_name.visible = False
            max_length_label.visible = False
        else:
            zeroCharacter_name.visible = True
    elif keys in punc_string:
        print("no")
        pass
    elif keys == "space":
        pass
    elif not keys.lower() == "backspace":
        if len(shape.value) < 12:
            shape.value += keys
            shape.left = 115
            zeroCharacter_name.visible = False
        else:
            max_length_label.visible = True
    else:
        #i could use try except, but using if statement is better
        #cause we didn't learn exceptions 
        #if key is backspace..
        if len(shape.value) > 0:
            shape.value = shape.value[:-1] #removes last char
            shape.left = 115
       
        if len(shape.value) < 12:  
            max_length_label.visible = False


actLabel = Group(
    Label("Check",105,225, size=20,bold=True, fill=white),
    Label("Stare", 105, 260,size=20,bold=True,fill=white),
    Label("Paper", 230, 225,size=20,bold=True, fill=white)
    )
actLabel.visible = False
actLabel.selectedValue = None

itemLabel = Group(
    Label("Soup",105,225, size=20,bold=True, fill=white),
    Label("Apple", 105, 260,size=20,bold=True,fill=white),
    Label("Paper", 230, 225,size=20,bold=True, fill=white)
    )
itemLabel.visible = False

knife = Group(
Polygon(40, 45, 93, 21, 93, 45,fill="white"),
Polygon(93, 45, 126, 45, 126, 35, 93, 35,fill="grey")
)
knife.visible = False

def mercyScene():
    correctPath = Label("This is the correct path..", 200,200,fill=white)
    sleep(2)
    labelString = "you passed the test!"
    desiredLabel = Label("", 200,240,fill=white)
    loopOverString(labelString,desiredLabel, correctPath.left, 0.05)
    sleep(1)
    desiredLabel.value = ""
    labelString = "That's it, the game's over.."
    correctPath.visible = False
    loopOverString(labelString,desiredLabel, correctPath.left, 0.05)
    sleep(3)
    playerFrisk.visible = True
    playerFrisk.opacity = 80
    playerFrisk.centerX = 200
    playerFrisk.centerY = 200
    desiredLabel.visible = False
    Label("End",200,200,size=40,italic=True,fill=white)
    app.stop()

def enemyTurn():
    fightDialogRect.width = 100
    fightDialogRect.centerX = 200
    playerFrisk.fullHeart.centerX = fightDialogRect.centerX
    playerFrisk.fullHeart.centerY = fightDialogRect.centerY
    app.enemyTurn = True
    knife.visible = True
    knife.rotateAngle = 600
    

app.canSwitch = True
app.enemyTurn = False
app.inFightMode = False
app.inActMode = False
app.inMercyMode = False
app.moveableRect = None
eyes.lastKeyPressed = None
def onKeyPress(key):
    if not app.name and menu.visible: #if we don't have the name yet..
        label_overlay(Label_Overlay, key)
    if playerFrisk.GUISelect:
        if not app.inFightMode and app.canSwitch and not app.inMercyMode:
            if key == "right":
                if playerFrisk.GUISelect == "Fight":
                    playerFrisk.GUISelect = "Act"
                elif playerFrisk.GUISelect == "Act":
                    playerFrisk.GUISelect = "Item"
                elif playerFrisk.GUISelect == "Item":
                    playerFrisk.GUISelect = "Mercy"
            if key == "left":
                if playerFrisk.GUISelect == "Mercy":
                    playerFrisk.GUISelect = "Item"
                elif playerFrisk.GUISelect == "Item":
                    playerFrisk.GUISelect = "Act"
                elif playerFrisk.GUISelect == "Act":
                    playerFrisk.GUISelect = "Fight"
        if key == "enter":
            if not app.enemyTurn:
                app.fightLabel.visible = False
                print(playerFrisk.GUISelect)
                if not app.inFightMode:
                    if playerFrisk.GUISelect == "Fight":
                        battleImage.visible = True
                        battleImage.width = fightDialogRect.width - 10
                        battleImage.height = fightDialogRect.height - 10
                        app.inFightMode = True
                        app.moveableRect = Rect(battleImage.left,battleImage.top - 3,fightDialogRect.width - fightDialogRect.width/1.03,fightDialogRect.height - 8, fill="white",border="black", borderWidth = 1)
                    if not app.inActMode:
                        if playerFrisk.GUISelect == "Act":
                            print("Act selected")
                            actLabel.visible = True
                            actLabel.selectedValue = actLabel.children[0].value
                            playerFrisk.fullHeart.centerX = actLabel.children[0].centerX - 45
                            playerFrisk.fullHeart.centerY = actLabel.children[0].centerY
                            app.canSwitch = False
                            app.inActMode = True
                    else:
                        print(actLabel.selectedValue)
                        playerFrisk.fullHeart.centerX  = ActSound.centerX
                        playerFrisk.fullHeart.centerY = ActSound.centerY
                        if actLabel.selectedValue == "Check":
                            actLabel.visible = False
                            dummyLabelName = Label("Dummy",80,225,fill=white,bold=True)
                            hpLabel = Label("HP: 40", 160,225,fill=white,bold=True)
                            damageLabel = Label("Does 5-10 damage",80, 260,fill=white,bold=True)
                            damageLabel.left = dummyLabelName.left
                            sleep(3)
                            hpLabel.visible = False
                            damageLabel.visible = False
                            dummyLabelName.visible = False
                            enemyTurn()
                        elif actLabel.selectedValue == "Stare":
                            actLabel.visible = False
                            dummyStareLabel = Label("You stare at the dummy",120,225,fill=white,bold=True)
                            stareBackLabel = Label("It stares back.", 120,260,fill=white,bold=True)
                            conversationLabel = Label("What a meaningful conversation!",120, 300,fill=white,bold=True)
                            stareBackLabel.left = dummyStareLabel.left
                            sleep(3)
                            dummyStareLabel.visible = False
                            stareBackLabel.visible = False
                            conversationLabel.visible = False
                            enemyTurn()
                        elif actLabel.selectedValue == "Paper":
                            actLabel.visible = False
                            showLabel = Label("You show the dummy a blank piece of paper.",80,225,fill=white,bold=True)
                            notRespondLabel = Label("It does not respond..", 80,260,fill=white,bold=True)
                            notRespondLabel.left = showLabel.left
                            sleep(3)
                            showLabel.visible = False
                            notRespondLabel.visible = False
                            enemyTurn()
                    if not app.inMercyMode:
                        if playerFrisk.GUISelect == "Item":
                            print("Item selected")
                            noItemsLabel = Label("No items..", 80, 225,fill=white,bold=True,size=20)
                            sleep(3)
                            noItemsLabel.visible = False
                            enemyTurn()
                        elif playerFrisk.GUISelect == "Mercy":
                            print("Mercy selected")
                            MercyLabel = Label("Mercy?", 100,225,fill=white,bold=True,size=20)
                            playerFrisk.fullHeart.centerX  = MercyLabel.centerX - 55
                            playerFrisk.fullHeart.centerY = MercyLabel.centerY
                            app.inMercyMode = True
                    else:
                        hideAllCanvasElements()
                        mercyScene()
                else:
                    if playerFrisk.GUISelect == "Fight":
                        print(app.moveableRect.centerX)
                        if app.moveableRect.centerX > 140 and app.moveableRect.centerX < 260:
                            damage = random.randint(5,20)
                        else:
                            damage = random.randint(3,10)
                        if not damage:
                            random_number(1000,400,50023)
                        battleImage.visible = False
                        app.moveableRect.visible = False
                        damageLabel = Label("-"+str(damage),278,172,fill="red")
                        dummy.health -= damage
                        sleep(1)
                        damageLabel.visible = False
                    enemyTurn()
        if key == "up":
            if actLabel.visible:
                if actLabel.selectedValue == actLabel.children[0].value:
                    pass
                #if label is 2nd value.., it goes up to first value
                elif actLabel.selectedValue == actLabel.children[1].value:
                    actLabel.selectedValue = actLabel.children[0].value
                    playerFrisk.fullHeart.centerX = actLabel.children[0].centerX - 45
                    playerFrisk.fullHeart.centerY = actLabel.children[0].centerY
                #if label is 3rd value goes to 2nd
                elif actLabel.selectedValue == actLabel.children[2].value:
                    actLabel.selectedValue = actLabel.children[1].value
                    playerFrisk.fullHeart.centerX = actLabel.children[1].centerX - 45
                    playerFrisk.fullHeart.centerY = actLabel.children[1].centerY
        elif key == "down":
            if actLabel.visible:
                if actLabel.selectedValue == actLabel.children[0].value:
                    actLabel.selectedValue = actLabel.children[1].value
                    playerFrisk.fullHeart.centerX = actLabel.children[1].centerX - 45
                    playerFrisk.fullHeart.centerY = actLabel.children[1].centerY
                #if label is 2nd value.., it goes up to 3rd value
                elif actLabel.selectedValue == actLabel.children[1].value:
                    actLabel.selectedValue = actLabel.children[2].value
                    playerFrisk.fullHeart.centerX = actLabel.children[2].centerX - 45
                    playerFrisk.fullHeart.centerY = actLabel.children[2].centerY
                #if label is 3rd value goes to 2nd
                elif actLabel.selectedValue == actLabel.children[2].value:
                    pass

app.playerTouchedWallCounter = 0
def onKeyHold(keys):
    if app.PLAYER_CAN_MOVE:
        if app.FIRST_DIALOUGE_SCENE:
            if playerFrisk.centerX > 400 or playerFrisk.centerX < 0:
               playerFrisk.centerX = 200 #stops the player from going past 400 or 0
               app.playerTouchedWallCounter += 1
            else:
                if playerFrisk.souls.visible:
                    if "d" in keys:
                        playerFrisk.centerX += 5
                        eyes.centerX = playerFrisk.centerX + 5 #make eyes move
                    elif "a" in keys:
                        playerFrisk.centerX -= 5
                        eyes.centerX = playerFrisk.centerX - 5 
    if app.enemyTurn:
        if "left" in keys:
            if playerFrisk.fullHeart.centerX > 160:
                playerFrisk.fullHeart.centerX -= 8
        if "right" in keys:
            if playerFrisk.fullHeart.centerX < 240:
                playerFrisk.fullHeart.centerX += 8
        if "up" in keys:
            if playerFrisk.fullHeart.centerY > 220:
                playerFrisk.fullHeart.centerY -= 8
        if "down" in keys:
            if playerFrisk.fullHeart.centerY < 316 - 3:
                playerFrisk.fullHeart.centerY += 8
