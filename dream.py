# Global variables
IN 				= "in"
EAST 			= "e"
WEST 			= "w"
NORTH 			= "n"
SOUTH 			= "s"
LOOK 			= "look"
PUSH 			= "push"
PULL 			= "pull"
TAKE			= "take"
SWIM 			= "swim"
WAIT 			= "wait"
HOLD 			= "hold"
NORTH_EAST		= "ne"
NORTH_WEST		= "nw"
SOUTH_EAST   	= "se"
SOUTH_WEST 		= "sw"
HELP 			= "help"


PROMPT 			= "\n$:> "
ERROR 			= "Maybe that's not the best thing to right now..." + PROMPT

INTRO 			= "You wake up on you birthday and you find yourself in a strang new land. As you look around, you cannot see anything around due to the lack of light. But you see a small glimmer of light coming from a short distance. As you go towards the light, you realize that it is door left ajar by someone." + PROMPT

NSROOM_INTRO 	= "As you enter the room, you see that this is an aftermath of an amazing party. You see HAPPY BIRTHDAY plastered all over the walls. As you look back you see a sign plastered on the door you just came in through." + PROMPT 

NSROOM_LOOK1	= "You read the sign saying SOUTH EXIT. You see that the room is actually a long corridor extending down north." + PROMPT

NSROOM_NORTH	= "As you move along north, you hear a party still going on with amazing Salman movie songs playing all along. At this very moment, you hear the following song: https://www.youtube.com/watch?v=yTv0PiRCPjg. You feel all excited and rush along the path."  + PROMPT 

NSROOM_LOOK2	= "As you see around, you see a dead end. Eventhough you can hear the party as clear as you were right there, you cannot seem to find a way into it. But all your groping around pays off. You see a small red button on the floor."  + PROMPT 

NSROOM_PUSH 	= "As you push the botton, the floor gives away. You fall down through an endless abyss and seemingly never hitting the bottom. You eventually pass out with sheer anticipation. \n" 

LROOM_INTRO		= "You finally wake up, not knowing how long you have passed out. You feel the soft ground around you, half wondering how you survided the fall. But before you can fully comprehend where you are and what is happening to you, a load roar pierces the silence around you and you hear it approaching you." + PROMPT

LROOM_LOOK1		= "As you look around, you see a small compass and a miners helmet (a helmet with working torch attached to it) around you." + PROMPT

LROOM_TAKE 		= "You pick the compass and the helmet. As you put on the helmet that torch lights up. But the light is a bit flaky. You think that the battery is low and you need to get to a safe place quickly, before the light runs out. As you look around, you see a small track running north west." + PROMPT

LROOM_NW1		= "You scamper along the battered path. You hear the roar growing louder by the minute. You hit a dead end. But you see a stream flowing right across the path going south west. That might be the only way to proceed now." + PROMPT

LROOM_SWIM    	= "As you swim along, you see that the stream picks up pace and at a distance turns into a huge water fall. You spot a dense overgrowth of trees to your left." + PROMPT

LROOM_HOLD_ON	= "You hold on to the tree over growth and finally move ashore. You see a clearing of trees along the tree overgrowth in the south east direction. You also notice a leopard eyeing you from the tree you used to get ashore." + PROMPT

LROOM_SE 		= "You run at the top of your speed. The leopard jumps right at you. You keep running. Now you hear the loud roar that was chasing you earlier. Out of options, you continue running towards the roar this time. \n \nYou hit the end of the road. You hear the roar growing louder. You can also see the leopard approaching you." + PROMPT

LROOM_WAIT 		= "As you lay in wait, you feel a very strong sensation giving you goosebumps pass right through you." + PROMPT

LROOM_LOOK2		= "As you recover from the experience, you see the leopard scampering away in absolute fear. You see that there a clearing that formed in the north east direction. You see a long tunnel ahead." + PROMPT

LROOM_NE 		= "As you enter the tunnel you feel the damp, stale air through your hair. As you keep walking through the tunnel, the battery on your helmet dies and the light goes out. But you continue moving groping your way through the tunnel. In this darkness you are surrounded by a swarm of fireflies giving you enough light and warmth in the tunnel. You suddenly feel that someone is watching over you and confidentl keep moving forward where you hit the end of the tunnel but find a large lever on the wall." + PROMPT

LROOM_PULL 		= "As you pull the level, the tunnel opens on both your right and left. There are tracks running across the left-right path. You hear something approaching from your right. As you wait momentarily, you see a large boulder approaching you from the right. Yous only option to survive might be to rush north west." + PROMPT

LROOM_NW2 		= "As you keep running, the boulder eventually stops. But you seem to have hit yet another dead end. But you see a small clearing to your south west." + PROMPT

LROOM_WELCOME	= "As you move along the clearing, you hear familiar voices and the same songs you heard while you started your journey. You hear the following song blaring though the speakers: https://www.youtube.com/watch?v=xx82pTgJ2_Y and a large sign saying HAPPY BIRTHDAY!. You see an open door." + PROMPT

FINALE 			= "As you complete your adventure, you see that you are at the head of a U-shaped table. You see that all your friends and family have been waiting for you. A familiar friend (you know who) walks up to you and says: 'Wish you a very happy birthday. You are now officially 23!. By the way, did you get the message?\n*** THE END ***"

def process(description_text, accepted_response):
	response = str(input(description_text).lower())
	while response != accepted_response:
		if response == HELP:
			help()
			response = str(input(PROMPT))
		else:
			response = str(input(ERROR))


def help():
	print ("""Hello. Welcome to help. This is a comprehensive listing of all the commands you can enter.
	help	: gives a list of commands that you can input.
	e 	: go east
	ne 	: go north east
	n 	: go north
	nw 	: go north west
	w 	: go west
	sw 	: go south west
	s 	: go south
	se 	: go south east
	in 	: go inside
	swim 	: swim streams if needed
	look	: look around
	wait	: wait at current location
	hold 	: hold on to something
	push	: push something
	pull 	: pull something
	take 	: take something
	""")
def intro():
	"""
	This is the introductory function that is called when the program is initiated
	"""
	process(INTRO, IN)

def nsroom():
	"""
	This is the first room in the game
	""" 
	process(NSROOM_INTRO, LOOK)
	process(NSROOM_LOOK1, NORTH)
	process(NSROOM_NORTH, LOOK)
	process(NSROOM_LOOK2, PUSH)

	print(NSROOM_PUSH)

def love_room():
	"""
	This in the second room in the game. 
	"""
	process(LROOM_INTRO, LOOK)
	process(LROOM_LOOK1, TAKE)
	process(LROOM_TAKE, NORTH_WEST)
	process(LROOM_NW1, SWIM)
	process(LROOM_SWIM, HOLD)
	process(LROOM_HOLD_ON, SOUTH_EAST)
	process(LROOM_SE, WAIT)
	process(LROOM_WAIT, LOOK)
	process(LROOM_LOOK2, NORTH_EAST)
	process(LROOM_NE, PULL)
	process(LROOM_PULL, NORTH_WEST)
	process(LROOM_NW2, SOUTH_WEST)
	process(LROOM_WELCOME, IN)

def finale():
	print (FINALE)

def __init__():
	intro()
	nsroom()
	love_room()
	finale()


__init__()
