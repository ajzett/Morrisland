from sys import pathfrom sys import path
path.append('./Gilbo-API/')
path.append('./Gilbo-API/deps/')
import Gilbo as G
import os
from sys import stdout


end_map = 0
current_til = 0
#
# Story Variables #
#
####
al_talked_mor = False
al_talked_ten = False
al_talked_nat = False
al_talked_dre = False
al_talked_dro = False
al_treas = False
####
shelf = 0
in_hall = 0
have_wep = 0
help = 0
class_type = 0
honesty = 0
curiosity = False
book = False
box = False
TvsN = False
#Standing with characters
Droxone_s = 0
Nathik_s = 0
Tenaxx_s = 0
Morena_s = 0
Dredall_s = 0




#
# !PUT ALL ITEMS HERE! #
#

# Consumables(ie. arrows, mana, etc...)
mana = G.item("Mana", "Used to fuel spells", 10)

arrow = G.item("Arrow", "A common arrow, can be found almost anywhere", .1)
cursed_arrow = G.item("A cursed arrow", "", 10)
snipers_arrow = G.item("Will always hit and crit", "", 10)
black_arrow = G.item("Negates all armor", "", 10)
life_drain_arrow = G.item("Drains the health of anything hit with it", "", 10)
rope_arrow = G.item("Launches a rope a long distance", "", 5)

bolt = G.item("A plain crossbow bolt", "", 1)

dart = G.item("", "", 1)

# Legendary Items
nathiks_soul_box = G.item("Green glowing box", "A box that Nathik can store souls in.", 1000)
philosophers_stone = G.equippable("A stone that can give you eternal life", "", 2000, hp=100)
shanams_ring = G.equippable("A ring that lets your summon a massive creature to fight for you", "", 2000, hp=100, stren=10)
bruldrins_stone = G.item("Makes the owner a God of Death", "", 3000)


#
# End of items
#


#
# End of NPCs
#

#
# Attacks
#
daggar_stab = G.attack("Daggar", "You stab something with a small knife", 3)
sword_slash = G.attack("", "You slash at your opponent", 5)
sword_thrust = G.attack("", "You run your opponent through", 10)
rapier_slash = G.attack("", "You slash", 4)
rapier_thrust = G.attack("", "You stab", 8)
wood_bludgeon = G.attack("", "You hit them really hard", 4)
brass_punch = G.attack("", "You punch them in the face", 6)
far_shot = G.ammo_attack("", "You shoot something really far away", 6, arrow, 1, acc=80)
near_shot = G.ammo_attack("", "You shoot something near you", 4, arrow, 1, acc=90)
face_shot = G.ammo_attack("", "You shoot someone right in front of you", 8, arrow, 1)
bolt_shot = G.ammo_attack("", "You shoot a crossbow", 10, bolt, 1, acc=90)
axe_cleave = G.attack("", "You hit with an axe", 5)
pike_stab = G.attack("", "You stab something with a pike", 3)
mace_hit = G.attack("", "You hit them with your mace", 5)
throw_spear = G.ammo_attack("", "You through your spear", 6, arrow, 1, acc=60)
spear_stab = G.attack("", "You stab with the spear", 2)
flail_hit = G.attack("", "You hit with your flail", 5)
war_hammer_hit = G.attack("", "You hit with a hammer", 4)
blowgun_shot = G.ammo_attack("", "You hit with a dart", 1, dart, 1)
push = G.attack("", "You push with your shield", 3)
#Dragon Attacks
poison = G.attack("poison", "", 10)
fire = G.attack("fire", "", 15)
claws = G.attack("claws", "", 15)

#Magic Attacks
fire_needle = G.ammo_attack("", "You send a needle of fire at your opponent", 4, mana, 1)
icicle = G.ammo_attack("", "You send a spike of ice at your opponent", 6, mana, 2)
eletricute = G.ammo_attack("", "", 7, mana, 2, acc=85)
blind = G.ammo_attack("", "", 2, mana, 1, acc=70)
fire_ball = G.ammo_attack("", "", 15, mana, 3)
possession = G.ammo_attack("", "", 30, mana, 6, acc=70)
sophocate = G.ammo_attack("", "", 20, mana, 4, acc=60)

# Big attacks
rot_attack = G.attack(2, 50, "You rot the flesh around the wound", 1)
zombiefy = G.attack(4, 80, "You turn your opponent into a zombie", 1)
dragon_fire = G.attack(5, 70, "You shoot dragon fire", 1)
possession = G.attack(1, 80, "You call up a spirit that kills your opponent", 1)





#
# Weapons
#

#basic attacks
daggar_linked = [daggar_stab]
daggar = G.weapon("Daggar", "", 1, 2, daggar_linked)
sword_linked = [sword_slash, sword_thrust]
sword = G.weapon("Sword", "", 10, 3, sword_linked)
rapier_linked = [rapier_slash, rapier_thrust]
rapier = G.weapon("Rapier", "", 7, 3, rapier_linked)
quartterstaff_linked = [wood_bludgeon]
quarterstaff = G.weapon("Quarterstaff", "", 1, 2, quartterstaff_linked)
brass_linked = [brass_punch]
brass_knuckles = G.weapon("Brass Knuckles", "", 2, 2, brass_linked)
long_bow_linked = [far_shot, near_shot]
long_bow = G.weapon("Long Bow", "", 3, 3, long_bow_linked)
short_bow_linked = [near_shot, face_shot]
short_bow = G.weapon("Short Bow", "", 3, 2, short_bow_linked)
cross_bow_linked = [bolt_shot]
cross_bow = G.weapon("Cross Bow", "", 4, 3, cross_bow_linked)
axe_linked = [wood_bludgeon, axe_cleave]
axe = G.weapon("Axe", "", 5, 3, axe_linked)
pike_linked = [pike_stab]
pike = G.weapon("Pike", "", 1, 2, pike_linked)
mace_linked = [mace_hit]
mace = G.weapon("Mace", "", 5, 3, mace_linked)
spear_linked = [throw_spear, spear_stab]
spear = G.weapon("Spear", "", 1, 2, spear_linked)
warhammer_linked = [war_hammer_hit]
warhammer = G.weapon("Warhammer", "", 3, 3, warhammer_linked)
blowgun_linked = [blowgun_shot]
blowgun = G.weapon("Blowgun", "", 1, 1, blowgun_linked)
club_linked = [wood_bludgeon]
club = G.weapon("Club", "", 1, 2, club_linked)
s_and_s_linked = [push, sword_slash, sword_thrust, wood_bludgeon]
shield_sword = G.weapon("Sword and Shield", "", 12, 3, s_and_s_linked, armr=3)
oak_wand_linked = [fire_needle, icicle, eletricute, blind]
oak_wand = G.weapon("Wand", "", 20, 4, oak_wand_linked)
morenas_wand_linked = [fire_ball, possession, sophocate]
morenas_wand = G.weapon("Morena's Wand", "", 50, 4, morenas_wand_linked)
dragons_blood_linked = [sword_slash, sword_thrust, dragon_fire]
dragons_blood = G.weapon("Dragon's Blood", "", 100, 8, dragons_blood_linked)
dragon_linked = [poison, fire, claws]
dragon_weapon = G.weapon("The Dragon", "", 1000, 10, dragon_linked)

#
# Armor
#
basic_armor = G.armor("Leather Armor", "", 4, armr=3)
steel_armor = G.armor("Steel Armor", "", 15, armr=6)
ench_basic_armor = G.armor("Enchanted Leather Armor", "", 10, armr=5, agil=2)
ench_steel_armor = G.armor("Enchanted Steel Armor", "", 25, armr=10, stren=4)
mythril_armor = G.armor("Mythril Armor", "", 75, armr=25, pwr=1, agil=3, stren=5)
sheild_charm = G.armor("Shield Bracelet", "", 60, armr=26)

#
# Potions
#
minor_health = G.stat_item("Minor Health Potion", "", 10, 1, hp=10)
health_potion = G.stat_item("Health Potion", "", 15, 1, hp=15)
major_health = G.stat_item("Major Health Potion", "", 20, 1, hp=20)
iron_skin_potion = G.stat_item("Iron Skin Potion", "", 10, 5, armr=5)
strength_potion = G.stat_item("Stength Potion", "", 10, 5, stren=5)
grace_potion = G.stat_item("Grace Potion", "", 20, 5, agil=3, pwr=1, armr=1)
giant_potion = G.stat_item("Giant Potion", "", 20, 5, stren=5, hp=20, pwr=1, agil=-2, armr=4)
durable_potion = G.stat_item("Durable Potion", "", 10, 5, hp=20, armr=6)




weapon_choice = [daggar, sword, rapier, quarterstaff, brass_knuckles, \
    long_bow, short_bow, cross_bow, axe, pike, mace, spear, warhammer, blowgun, \
    club, shield_sword, oak_wand]

steve_stats = G.battler_stats(100, 5, 0, 5, 1)
arms_master_stats = G.battler_stats(100, 4, 0, 4, 1)
steve_stuff = []
steve_using = []
steve_inv = G.player_collection(10, steve_stuff, steve_using)
arms_m_stuff = [shield_sword, daggar, basic_armor, minor_health]
arms_m_using = []
arms_m_inv = G.battler_collection(50, arms_m_stuff, arms_m_using)
arms_m_inv.equip(basic_armor)



arms_master = G.battler("Greg", G.loc_man, 2, 3, arms_m_inv, arms_master_stats)

end_map = 0




#Maps!
class appartment(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start(self):
        G.write("7:10am")

        G.write("Monday, March 4th.")
        G.write("Your apartment.")
        phone.say("hello")
        G.write("Your cat knocks your phone on the floor")
        G.write("Wait... You don't own a cat. You're not that sad!")
        G.write("Yet...")
        cat.say("meowl")

        G.write("The cat jumps down onto the floor and goes into the other room. You hear the TV turn on.")

    def send_data(self, til, plyr=False):
        print(til)

        if til == (1,3):
            if plyr is True:
                global end_map
                end_map = end_map + 1
                G.write("Do you follow the cat?")
                morning = int(input("1: yes, 2: no"))
                if morning is 1:
                    os.system('cls')
                    G.write("You follow the cat into the other room. The news is on the TV.")
                    news_reader.say("news3")
                    G.write("A picture of your street shows up on the news.")
                    G.write("You might not want to go to work early.")
                    G.write("How did the cat turn on the TV?")
                    G.write("It's staring at you.")
                    cat.say("meow")
                    os.system("PAUSE")
                    os.system('cls')
                    G.write("As you walk out of your door you see a lot of cops on the other side of the street.")
                    G.write("The knifeman you saw on TV is in the back of one of the patrol cars.")
                    os.system("PAUSE")
                    os.system('cls')
                    G.write("You get to work without a problem")
                    steves_boss.say("greating")
                    G.write("*Gulp*")
                    G.write("You quickly get down to work.")
                    co_worker.say("greating")
                    G.write("Steve: I don't know.")
                    co_worker.say("fired")
                    G.write("Steve: I'm sure you could find someone. I won't be able to make rent if I'm fired.")
                    co_worker.say("weekend")
                    G.write("1: Of course we're on! Why would I cancel?")
                    G.write("2: If I get laid off I'll be job hunting.")
                    choice = int(input(""))
                    if choice is 1:
                        G.write("Lary: Great! Beers on me if you get fired.")
                        honesty = honesty - 1
                    else:
                        G.write("Lary: That's probably for the best.")
                        honesty = honesty + 1
                    os.system("PAUSE")
                    os.system('cls')
                    G.write("You get lunch in the middle of the day.")
                    G.write("Someone else is in the lunch room.")
                    cat.say("meowq")
                    G.write("Steve: Why are you still here!?")
                    os.system("PAUSE")
                    os.system('cls')
                    G.write("At the end of the day you go to the Boss's office")
                    steves_boss.say("fired")
                    G.write("You leave the room and start packing up.")
                    G.write("The cat is sitting on your desk.")
                    cat.say("purr")
                    os.system("PAUSE")
                    os.system('cls')
                    G.write("You leave the office building with a medium box of stuff.")
                    G.write("You look back up at your old office building.")
                    G.write("The cat is sitting on a ledge, staring at you.")
                    pes_emily.say("move")
                    G.write("Steve: Sorry")
                    G.write("What is with that cat? We does it keep following you?")
                    cat.say("meowl")
                    G.write("While staring at the cat, you hear brakes scretching")
                    pes_emily.say("look_out")
                    G.write("You hear a crunch and everything goes black.")
                    global curiosity
                    curiosity = True

                else:
                    os.system('cls')
                    G.write("You ignore the cat and get ready to go to work.")

                    news_reader.say("news1")
                    news_reader.say("news2")
                    G.write("You hope you don't get laid off. This world is horrible.")
                    cat.say("meowl")
                    G.write("You should get to work early.")
                    os.system("PAUSE")
                    os.system('cls')
                    G.write("You walk out onto the street.")
                    G.write("You hear sirens.")
                    G.write("That's not important. You take your usual route to work.")
                    G.write("But if you cut through this ally it will be faster.")
                    choice = int(input("1:Usual route, 2:Ally"))
                    os.system('cls')
                    if choice is 2:
                        G.write("You here someone walking behind you.")
                        knifeman.say("cops")
                        G.write("Before you can respond to the man he thrusts his hand toward your stomach.")
                        G.write("Did he punch you?")
                        G.write("You look down.")
                        G.write("There's a knife sticking out of your gut.")
                        G.write("The last thing you see is the cat.")
                        cat.say("purr")
                        os.system("PAUSE")
                        os.system('cls')
                    else:
                        G.write("You take your normal route to work.")
                        cat.say("meowl")
                        G.write("You look behind you. The cat is following you!")
                        G.write("You ignore it.")
                        G.write("You stop as you wait to cross a road.")
                        G.write("Suddenly a hissing ball of fur hits you from behind.")
                        G.write("Steve: Get away you stupid cat!")
                        G.write("Pedestrian: LOOK OUT!")
                        G.write("You hear a crunch.")
                    os.system("PAUSE")

        return True

    def finished_map(self):
        G.write("All you can see is blackness.")
        G.write("A pinprick of light appears and grows bigger.")
        G.write("You walk toward it.")

appartment_map = appartment('appartment_n')

appartment_map.layout = G.np.array([[G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building], \
                                [G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Ice, G.Tiles.Building], \
                                [G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building]])




class fortress_chamber(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start(self):
        head_witch.say("first")
        head_necromancer.say("first")
        head_summoner.say('first')
        G.write("Steve: Whaaa?")
        G.write("Steve: Who are y...")
        G.write("You voice trails off as you look up at five old 'people'.")
        os.system("PAUSE")
        os.system('cls')
        G.write("A super old and croutched woman started crowing.")
        head_witch.say("insult_n")
        head_witch.say("insult_n2")
        head_necromancer.say("insult_w")
        G.write("The woman, Morena, slapped the talking corpse.")
        G.write("The two started squabbling even more.")
        os.system("PAUSE")
        os.system('cls')
        head_summoner.say("calm")
        G.write("The man who had just spoken was really tall.")
        G.write("You look down from his face to his body.")
        G.write("He has a horses body.")
        os.system("PAUSE")
        os.system('cls')
        head_wizard.say("hello")
        G.write("Steve: B-b-b-barn who?")
        head_wizard.say("confustion")
        head_wizard.say("blame")
        head_alchemist.say("sigh")
        head_wizard.say("hearinglose")
        head_alchemist.say("backtrack")

        G.write("Now the other two start squablling")


    def send_data(self, til, plyr=False):
        done = False
        print(til)

        if til == (3,5):
            if plyr is True:
                G.write("You walk to the door leading out of the room.")
            return True

        if til == (3,2):
            if plyr is True:
                G.write("That is the table you were on.")
            return True

        if til == (1,1):
            if plyr is True:
                G.write("Would you like to talk to Droxone?")
                talk = int(input("1:yes, 2:no"))
                if talk is 1 and done != True:
                    done = True
                    G.write("You get up off the table.")
                    G.write("You walk over to Droxone, who is by far the youngest of all the five.")
                    G.write("Steve: Hello?")
                    head_alchemist.say("get1")
                    G.write("Steve: I'll start with a simple question, where am I?")
                    G.write("The men, who can't be much older than you, looks very confused.")
                    head_alchemist.say("get2")
                    G.write("Steve: My name isn't Barnabas, it's Steve.")
                    G.write("Before he can say anything else someone calls everyone to attention.")
                    os.system("PAUSE")
                    global Droxone_s
                    Droxone_s = Droxone_s + 1
                    global end_map
                    end_map = end_map + 1
                else:
                    G.write("You don't talk to him yet.")
            return True

        if til == (3,1):
            if plyr is True:
                G.write("Would you like to talk to Tenaxx?")
                talk = int(input("1:yes, 2:no"))
                if talk is 1 and done != True:
                    done = True
                    G.write("The older guy seems like the most aprotchable of the five.")

                    G.write("The think his name is Tenaxx?")
                    G.write("Steve: Hello... sir.")
                    head_wizard.say("get1")
                    G.write("Steve: I'm sorry sir, but I don't think I am who you think I am.")
                    head_wizard.say("get2")
                    head_wizard.say("get3")
                    G.write("Tenaxx calls everyone over.")
                    os.system("PAUSE")
                    global Tenaxx_s
                    Tenaxx_s = Tenaxx_s + 1

                    end_map = end_map + 1
                else:
                    G.write("You don't talk to him yet.")
            return True

        if til == (2,2):
            if plyr is True:
                G.write("Would you like to talk to Dredall?")
                talk = int(input("1:yes, 2:no"))
                if talk is 1 and done != True:
                    done = True
                    G.write("You get off the table and cautiously aproutch the horse person. What are they called again?")
                    G.write("Really what are they called?")
                    head_summoner.say("get1")
                    G.write("He's got to be at least nine feet tall.")
                    head_summoner.say("get2")
                    head_summoner.say("get3")
                    G.write("Steve: Uhhh.... What?")
                    head_summoner.say("get4")
                    G.write("Before you can say anything else, the old man calls everyone over.")
                    os.system("PAUSE")
                    global Dredall_s
                    Dredall_s = Dredall_s + 1
                    end_map = end_map + 1
                else:
                    G.write("You don't talk to him yet.")
            return True

        if til == (3,3):
            if plyr is True:
                G.write("Would you like to talk to Morena?")
                talk = int(input("1:yes, 2:no"))
                if talk is 1 and done != True:
                    done = True
                    G.write("You walk over to the old lady. You can just run if she starts screaming again.")
                    G.write("Steve: Hello Ma'am")
                    head_witch.say("get1")
                    G.write("Steve: I'm sorry, but I don't know who you think I am.")
                    G.write("The woman looks at you through squinted eyes.")
                    head_witch.say("get2")
                    head_witch.say("get3")
                    head_witch.say("get4")
                    G.write("Steve: A witch? Those are real?")
                    G.write("At this Morena laughs.")
                    head_witch.say("get5")
                    G.write("Before you can say anything the oldest men of the five calls everyone over.")
                    os.system("PAUSE")
                    global Morena_s
                    Morena_s = Morena_s + 1
                    end_map = end_map + 1
                else:
                    G.write("You don't talk to her yet.")
            return True

        if til == (5,4):
            if plyr is True:
                G.write("Would you like to talk to Nathik?")
                talk = int(input("1:yes, 2:no"))
                if talk is 1 and done != True:
                    done = True
                    G.write("For some reason, you walk over to the courpse, Nathik.")
                    G.write("Maybe it's because you liked his joke.")
                    G.write("Steve: Hello, sir?")
                    head_necromancer.say("get1")
                    G.write("Steve: Umm... Where am I and who do you think I am?")
                    G.write("This brings an actual expression of shock to Nathik's face.")
                    head_necromancer.say("get2")
                    head_necromancer.say("get3")
                    head_necromancer.say("get4")
                    G.write("You keep you mouth shut. Nathik seems to be brooding now. You slowly walk away.")
                    os.system("PAUSE")
                    global Nathik_s
                    Nathik_s = Nathik_s + 1
                    end_map = end_map + 1
                else:
                    G.write("You don't talk to him yet.")
        return True
    def finished_map(self):
        head_wizard.say("expo1")

        head_wizard.say("expo2")
        head_wizard.say("expo3")
        G.write("Steve: There was a creepy cat, and I had cerial for breakfast.")
        os.system("PAUSE")
        os.system('cls')
        G.write("They all blink at you.")
        head_alchemist.say("shock")
        head_summoner.say("solution")

        G.write("Dredall grabs you and you find your self on his back. You all walk out a side door and down a coridor.")


fortess_room = fortress_chamber('fortress')

fortess_room.layout = G.np.array([[G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall], \
                            [G.Tiles.Wall, G.Tiles.Ice, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                            [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                            [G.Tiles.Wall, G.Tiles.Ice, G.Tiles.Cave, G.Tiles.Ice, G.Tiles.Mountain, G.Tiles.Mountain], \
                            [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                            [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Wall], \
                            [G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall]])




class arena(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start(self):
        os.system('cls')
        head_summoner.say("train")

        G.write("Steve: Does it have to be a master? Why not a beginner?")
        G.write("Steve: Not that I don't know what I'm doing, which I totally do.")
        G.write("Steve: I may be rusty.")
        head_necromancer.say("rust")
        G.write("It occurs to you that these people might not know the same sayings as you.")
        os.system("PAUSE")
        os.system('cls')
        G.write("Dredall leads a grizled looking man in leather armor over to you.")
        head_summoner.say("spar")
        G.write("Steve: Right to the main fight? Don't we have, like, special items to gather or something?")
        head_wizard.say("already")
        G.write("Steve: Oh, yes... O-of course you have everything.")
        head_alchemist.say("yahn")

        G.write("Droxone just walks off and leaves everyone else.")

    def send_data(self, til, plyr=False):

        if til == (0,0) or til == (5,0) or til == (0,5) or til == (5,5):
            if plyr is True:
                G.write("Those are pillars. You just walked into a pillar.")
            return True

        if til == (0,1):
            if plyr is True:
                global have_wep
                have_wep = have_wep + 1
                for i in range(len(weapon_choice)):
                    stdout.write(str(i))
                    stdout.write(": ")
                    print(weapon_choice[i].name)

                wc = int(input("What will you choice?"))
                os.system('cls')
                steve_inv.add_item(weapon_choice[wc], 1)
                print(weapon_choice[wc].dscrpt)
                if weapon_choice[wc].name is "Warhammer":
                    head_summoner.say("warhammer")
                    global Dredall_s
                    Dredall_s = Dredall_s + 1

                elif weapon_choice[wc].name is "Wand":
                    head_witch.say("wand")

                    global help
                    help = int(input("1: yes, 2: no"))
                    if help is 1:
                        G.write("You don't know how this works. Some help sounds like a great idea.")
                        head_witch.say("(:")
                        global Morena_s
                        Morena_s = Morena_s + 1

                    else:
                        G.write("You aren't sure you trust her just yet.")
                        head_witch.say("wait")

                else:
                    head_summoner.say("wrong_weapon")

                if help is 1:

                    G.write("Before leaving, Morena walks over and says in a lowered voice,")
                    head_witch.say("come")

                G.write("The other four walk away in different dirrections with little more than a word.")
                os.system("PAUSE")
                os.system('clr')

            return True

        if til == (2,3):
            if plyr is True:
                if have_wep is 1:
                    global end_map
                    end_map = end_map + 1
                    G.write("You hear the Arms Master cough.")
                    arms_master_npc.say("first")
                    G.write("Oh, umm... I don't now how.")
                    arms_master_npc.say("confus")
                    G.write("You have to pass for this guy. You think about your answer.")
                    G.write("Steve: Something went amiss in this resurection. I seem to have lost all my memories.")
                    os.system("PAUSE")
                    os.system('cls')
                    G.write("A thoughtful expression comes over Gregs face.")
                    arms_master_npc.say("realize")
                    arms_master_npc.say("sad")
                    G.write("Steve: I don't even know where I am or what I'm supose to do.")
                    arms_master_npc.say("expl1")
                    arms_master_npc.say("expl2")
                    arms_master_npc.say("expl3")
                    os.system("PAUSE")
                    os.system('cls')
                    arms_master_npc.say("ask")
                    G.write("Steve: No.")
                    arms_master_npc.say("expl4")
                    arms_master_npc.say("expl5")
                    arms_master_npc.say("expl6")
                    arms_master_npc.say("expl7")
                    arms_master_npc.say("expl8")
                    os.system("PAUSE")
                    os.system('cls')
                    arms_master_npc.say("ask")
                    G.write("You could just lie? You could tell him it rings a bell.")
                else:
                    G.write("You don't have a wepaon yet. Go the the weapon wrack and get one.")
        return True


    def finished_map(self):
        G.write("Will you lie?")

        lie = int(input("1: yes, 2:no"))
        if lie is 1:
            G.write("Steve: All of that sounds very familiar. I still can't remember specifics though.")
            arms_master_npc.say("lieyes")
            global honesty
            honesty = honesty - 1
            arms_master_npc.say("lieyes2")


        else:
            G.write("Steve: I still don't know what you're talking about.")
            arms_master_npc.say("lieno")
            arms_master_npc.say("lieno2")
            honesty = honesty + 1

arena_map = arena('arena_map')

arena_map.layout = G.np.array([[G.Tiles.Building, G.Tiles.Ice, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Building], \
                            [G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass], \
                            [G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Ice, G.Tiles.Grass, G.Tiles.Grass], \
                            [G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass], \
                            [G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass], \
                            [G.Tiles.Building, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Grass, G.Tiles.Building]])



class hallway(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start(self):
        arms_master_npc.say("gowhere")

    def send_data(self, til, plyr=False):
        go = 0
        global current_til
        current_til = til
        if til == (0,0):
            if plyr is True:
                G.write("Would you like to go to your room?")
                G.write("Note: You will be taken to the next part of the story if you go to your room.")
                go = int(input("1:yes, 2:no"))
                if go is 1:
                    global end_map
                    end_map = end_map + 1
                else:
                    G.write("Maybe later.")
            return True

        if til == (0,2):
            if plyr is True:
                G.write("Would you like to go to The library?")
                go = int(input("1:yes, 2:no"))
                if go is 1:
                    end_map = end_map + 1
                else:
                    G.write("Maybe later.")
            return True

        if til == (0,4):
            if plyr is True:
                G.write("Would you like to go talk to Tenaxx?")
                go = int(input("1:yes, 2:no"))
                if go is 1:
                    end_map = end_map + 1
                else:
                    G.write("Maybe later.")
            return True

        if til == (0,6):
            if plyr is True:
                G.write("Would you like to talk to Dredall?")
                go = int(input("1:yes, 2:no"))
                if go is 1:
                    end_map = end_map + 1
                else:
                    G.write("Maybe later.")
            return True

        if til == (3,2):
            if plyr is True:
                G.write("Would you like to talk to Droxone?")
                go = int(input("1:yes, 2:no"))
                if go is 1:
                    end_map = end_map + 1
                else:
                    G.write("Maybe later.")
            return True

        if til == (3,4):
            if plyr is True:
                G.write("Would you like to talk to Nathik?")
                go = int(input("1:yes, 2:no"))
                if go is 1:
                    end_map = end_map + 1
                else:
                    G.write("Maybe later.")
            return True

        if til == (3,6):
            if plyr is True:#FIX ENTIRE SECTION!!!
                if curiosity is True:
                    end_map = end_map + 1
                else:
                    G.write("That way looks boring, and you don't want to go down there.")
        return True

    def finished_map(self):
        G.write("You leave the hall.")


hallway_map = hallway('hallway_map')

hallway_map.layout = G.np.array([[G.Tiles.Ice, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Mountain], \
                                [G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain], \
                                [G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain], \
                                [G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Mountain]])

class your_room(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start(self):
        G.write("You enter your room.")

    def send_data(self, til, plyr=False):
        if til == (1,2):
            if plyr == True:
                global end_map
                end_map = end_map + 1
                global book
                if book == True:
                    
                G.write("As you lay down of the bed you think maybe you'll wake up from this dream soon.")
                os.system("PAUSE")
        return True

    def finished_map(self):
        G.write("You wake up the next morning.")

your_room = your_room('your_room')

your_room.layout = G.np.array([[G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall], \
                                [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Dirt, G.Tiles.Mountain, G.Tiles.Wall], \
                                [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                [G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Wall, G.Tiles.Wall]])

class library(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start(self):
        G.write("Greg takes you to a section of the fortresses massive library. Morena is sitting in a well hidden side room.")
        G.write("Plants are hanging from the cieling. There are tanks with salamanders and frogs. Anything that you would think a witch would have is somehow crammed into this tiny room.")

    def send_data(self, til, plyr=False):
        if til == (1,8):
            if plyr is True:
                global al_talked_mor
                if al_talked_mor == False:
                    if help is 1:
                        head_witch.say("training")
                        G.write("Steve: What did you want to show me?")
                        head_witch.say("training2")
                        G.write("Out of somewhere Morena pulls out three items. A bottle full of blue liquid, a braclet covered in charms, and an engraved wand.")
                        head_witch.say("training3")
                        head_witch.say("training4")
                        G.write("Do you take the items?")

                        witch_items = int(input("1: yes, 2: no"))
                        if witch_items is 1:
                            G.write("Steve: Okay. I'll take them")
                            #steve.collection.add_item(sheild_charm, 1)
                            #steve.collection.add_item(giant_potion, 1)
                            #steve.collection.add_item(morenas_wand, 1)
                            head_witch.say("takeitems")
                            global Morena_s
                            Morena_s = Morena_s + 1

                        else:
                            G.write("Steve: I don't even know how to use these things. I can't take them.")
                            head_witch.say("regect")
                            Morena_s = Morena_s - 1
                        global honesty
                        honesty = honesty + 1

                    else:
                        head_witch.say("curio")
                        G.write("Steve: I just want to know what's going on.")
                        head_witch.say("curio2")
                        head_witch.say("curio3")

                    head_witch.say("endtalk")
                    Morena_s = Morena_s + 1
                    al_talked_mor = True
                else:
                    G.write("You already talked to her.")
                os.system("PAUSE")
            return True

        if til == (0,6) or til == (1,6) or til == (3,6) or til == (3,7) or til == (3,8) or til == (3,9):
            if plyr is True:
                G.write("That's a wall. You just walked into a wall.")
            return False

        if til == (2,1) or til == (2,2) or til == (2,3) or til == (2,4) or til == (4,1) or til == (4,2) or til == (4,3) or til == (4,4):
            if plyr is True:
                G.write("That's a bookshelf")
                shelf = shelf + 1
                if shelf > 2:
                    G.write("Why are you climbing the shelves?")
                    G.write("You find a book on top of the shelves. It looks interesting. You pick it up.")
                    global book
                    book = True
                elif shelf > 3:
                    G.write("STOP CLIMBING ON THE SHELVES!")
            return True

        if til == (5,7):
            if plyr is True:
                G.write("Would you like to leave?")
                leave = int(input("1:yes, 2:no"))
                if leave is 1:
                    global end_map
                    end_map = end_map + 1
                else:
                    G.write("Not yet.")
        return True


    def finished_map(self):
        G.write("You leave the Library")

library_room = library('library_room')

library_room.layout = G.np.array([[G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Wall, G.Tiles.Wall]])

class tenaxx_study(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start(self):
        G.write("While taking you to Tenaxx, Greg tells you that he is so old because he's a wizard. This place is so weird you don't even question it.")
        G.write("The Arms Master leaves you at the door to Tenaxx's study. You knock, and here a muffled invitation to enter.")

    def send_data(self, til, plyr=False):
        if til == (2,1):
            if plyr is True:
                global al_talked_ten
                if al_talked_ten is False:
                    al_talked_ten = True
                    head_wizard.say("studyhello")
                    G.write("Steve: Sparing was fine. I was wondering what the plan was exsactly for dealing with this world dragon?")
                    head_wizard.say("plan1")
                    head_wizard.say("plan2")
                    head_wizard.say("plan3")
                    head_wizard.say("plan4")
                    os.system("PAUSE")
                    os.system('cls')
                    G.write("Steve: Okay, how do you do that?")
                    head_wizard.say("roles")
                    G.write("Steve: Uhh... okay.")
                    G.write("You pretend to understand a word he's talking about.")
                    G.write("He doesn't seem to notice and is now rambling on using words you don't understand.")
                    G.write("You think he's talking about his powers, but you can't be sure.")
                    G.write("You look around. The study is full of interesting stuff that probably shouldn't be touched.")
                    os.system("PAUSE")
                    global Tenaxx_s
                    Tenaxx_s = Tenaxx_s + 1
                else:
                    G.write("You already talked to him")
            return True

        if til == (2,2):
            if plyr is True:
                G.write("You're standing on his desk.")
            return True

        if til == (1,4):
            if plyr is True:
                if curiosity is True:
                    global box
                    if box is False:
                        G.write("While the old wizard keeps rambling, you walk over to a shelf covered in odd things.")
                        G.write("You pick up an odd contraption that looks like a box made of filigree.")
                        G.write("Particles start swirling inside and glowing green. There is a little ingraved N on the metal.")
                        G.write("You pocket the box.")
                        os.system("PAUSE")
                        steve.collection.add_item(nathiks_soul_box)
                        box = True
                    else:
                        G.write("You've already gathered everything here.")
                else:
                    G.write("There's some stuff here, but none of it's interesting.")
            return True

        if til == (5,2):
            if plyr is True:
                G.write("Would yo like to leave?")
                leave = int(input("1:yes, 2:no"))
                if leave is 1:
                    global end_map
                    end_map = end_map + 1
                else:
                    G.write("Not yet.")
        return True

    def finished_map(self):
        G.write("You leave the room. Tenaxx doesn't notice. You can hear him still talking as you close the door.")


tenaxx_study = tenaxx_study('tenaxx_study')

tenaxx_study.layout = G.np.array([[G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Ice, G.Tiles.Dirt, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall]])

class dradall_study(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start(self):
        G.write("Centaur! That's what he's called! Greg seems to take it for granted that Centaurs are real.")
        G.write("The door to his study is really tall, but you suppose it has to be.")
        G.write("Greg leaves you at the door.")
        G.write("Before you can knock the door opens.")

    def send_data(self, til, plyr=False):
        if til == (4,2):
            if plyr is True:
                global al_talked_dre
                if al_talked_dre is False:
                    al_talked_dre = True
                    head_summoner.say("great")
                    G.write("Steve: I was wondering when I can go home?")
                    head_summoner.say("home")
                    G.write("Steve: I mean earth. My home is earth, and I want to go back to it?")
                    head_summoner.say("earth")
                    G.write("Steve: But I've never held a sword in my life. I didn't even get into fights at school. I'm useless.")
                    head_summoner.say("useless")
                    head_summoner.say("truth")
                    G.write("Steve: Have you ever gotten the right person?!")
                    head_summoner.say("defen")
                    head_summoner.say("goaway")
                    os.system("PAUSE")
                else:
                    G.write("You've already talked to him.")
            return True

        if til == (5,2):
            if plyr is True:
                G.write("Would you like to leave?")
                leave = int(input("1:yes, 2:no"))
                if leave is 1:
                    global end_map
                    end_map = end_map + 1
                else:
                    G.write("Not yet.")
        return True

    def finished_map(self):
        G.write("With that you're shoed out the door. You hear it lock behind you.")
        global Dredall_s
        Dredall_s = Dredall_s + 1


dradall_study = dradall_study('dradall_study')

dradall_study.layout = G.np.array([[G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Dirt, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall]])

class droxone_study(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start(self):
        G.write("Droxone seemed like the nicest one there. He's also your age. Greg admits that he's a little wierd, but you don't care anymore.")
        G.write("As soon as you stop in front of the door Greg indicated, you can hear ticking from inside.")
        G.write("A voice that sounds like it's coming through a really old radio eminates from a point behind the door.")
        G.write("Radio: Droxone will be with you in a moment. Please do not open the door for your own safety.")
        G.write("There's more crashing and banging from inside. Was that a small explosion?")
        os.system("PAUSE")
        os.system('cls')
        head_alchemist.say("radio")
        G.write("You open the door with a lot of caution. The room beyond is the biggest and most confusing mess you've ever seem.")
        G.write("The smell of burning chemicals permiates the air. You can see burn marks on the wall behind a metal table covered in gizmozes of all shapes.")
        G.write("Another table is covered in what looked like a chemistry set of steroids.")
        G.write("Smoke covers the ceiling. Some of the machines are whirring, some glowing, most are skaing and making noise.")
        G.write("Droxone is standing over at the third table covered in parts. It's exident what he was building blew up in him face.")

    def send_data(self, til, plyr=False):
        if til == (2,3):
            if plyr is True:
                global al_talked_dro
                if al_talked_dro is False:
                    al_talked_dro = True
                    head_alchemist.say("blewup")
                    G.write("Steve: I don't mind. It's your lab.")
                    head_alchemist.say("memoryloss")
                    G.write("Steve: I think you have the wrong person. I'm not Barnabas. My name is Steve.")
                    G.write("At that he turns and looks at you.")
                    head_alchemist.say("thought")
                    os.system("PAUSE")
                    os.system('cls')
                    G.write("Steve: What do you mean prep the body?")
                    head_alchemist.say("body")
                    head_alchemist.say("body2")
                    head_alchemist.say("body3")
                    head_alchemist.say("concern")
                    G.write("Everything is going black. Your ears are ringing.")
                    G.write("You pass out.")
                    os.system("PAUSE")
                    global Droxone_s
                    Droxone_s = Droxone_s + 1
                    global end_map
                    end_map = end_map + 1
                else:
                    G.write("You already talked to him.")
        return True

    def finished_map(self):
        G.write("You wake up on the floor")
        G.write("How did you get here?")
        G.write("Oh that's right")
        G.write("You're a magic android.")
        G.write("Droxone says you should go and sleep. You agree.")
        os.system("PAUSE")

droxone_study = droxone_study('droxone_study')

droxone_study.layout = G.np.array([[G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Dirt, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Dirt, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Dirt, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall]])

class nathik_study(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start(self):
        G.write("For some reason you want to talk to Nathik. The Arms Master looks vissably nervious.")
        G.write("He leads you to a place in the dungeon. You suppose that Nathik doesn't want to be around other people.")
        G.write("You nerviously knock on the door.")
        head_necromancer.say("what")
        G.write("Steve: It's me, the person you all brought here.")
        G.write("The door flies open and nearly hits you in the face.")

    def send_data(self, til, plyr=False):
        if til == (2,1):
            if plyr is True:
                global al_talked_nat
                if al_talked_nat is False:
                    al_talked_nat = True
                    head_necromancer.say("mad")
                    G.write("Apologize, or Ask?")

                    AorA = int(input("1: Apologize, 2: Ask"))
                    if AorA is 1:
                        G.write("Steve: I'm sorry for what I did. Whatever it was I probably thought it was best at the time. It might have been, or might not have been.")
                        head_necromancer.say("apol")
                        global Nathik_s
                        Nathik_s = Nathik_s + 1

                    else:
                        G.write("Steve: What did I ever do too you?")
                        head_necromancer.say("ask")
                        head_necromancer.say("ask2")
                        Nathik_s = Nathik_s - 1
                    os.system("PAUSE")
                else:
                    G.write("You already talked to him.")
            return True

        if til == (5,2):
            if plyr is True:
                G.write("Would you like to leave?")
                leave = int(input("1:yes, 2:no"))
                if leave is 1:
                    global end_map
                    end_map = end_map + 1
                else:
                    G.write("Not yet.")
        return True

    def finished_map(self):
        G.write("Nathik shuts the door in your face.")


nathik_study = nathik_study('nathik_study')

nathik_study.layout = G.np.array([[G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Ice, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Wall], \
                                    [G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Mountain, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall]])

class treasury(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start(self):
        G.write("After a moment of thought, Greg grins and leads you deep into the fortress.")
        G.write("You go down to many staircases to count. Your legs are burning by the time you reach your destination.")
        G.write("Steve: What is this place?")
        arms_master_npc.say("treasure")
        G.write("He takes out a key and opens a small steel door. The sound of metal on stone makes both of you wince.")
        arms_master_npc.say("coolstuff")
        os.system("PAUSE")
        os.system('cls')
        G.write("Pedestals line the room. Each one has an artifact on it. Giant gems, flashy flasks, astoinding armor, bounties abound.")
        G.write("Steve: Where did all this stuff come from?")
        arms_master_npc.say("coolstuff2")
        G.write("There are three things with your name on them, or Banabas's at least.")
        G.write("A blue-silver armor, a red sword, and a ring that seems to be made of pure emerald.")
        G.write("Greg insists that you take the items. Maybe they'll help you.")

    def send_data(self, til, plyr=False):
        if til == (1,1):
            if plyr is True:
                G.write("You pick up a ring.")
                #steve.collection.add_item(shanams_ring, 1)
            return True

        if til == (1,3):
            if plyr is True:
                G.write("You pick up a red sword.")
                #steve.collection.add_item(dragons_blood, 1)
            return True

        if til == (3,5):
            if plyr is True:
                G.write("You pick up a armor.")
                #steve.collection.add_item(mythirl_armor, 1)
            return True

        if til == (3,1):
            if plyr is True:
                G.write("A stone. It has Dredall's name on it. You leave it.")
            return True

        if til == (1,5):
            if plyr is True:
                G.write("A jar of frog eyes. Why is there a random jar of frog eyes here?")
            return True

        if til == (4,4):
            if plyr is True:
                G.write("Would you like to leave?")
                leave = int(input("1:yes, 2:no"))
                if leave is 1:
                    global end_map
                    end_map = end_map + 1
                else:
                    G.write("Not yet.")
        return True

    def finished_map(self):
        arms_master_npc.say("goback")
        G.write("He leads you back up to the hall.")

treasury = treasury('treasury')

treasury.layout = G.np.array([[G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain], \
                                [G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Mountain, G.Tiles.Dirt, G.Tiles.Mountain], \
                                [G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain], \
                                [G.Tiles.Mountain, G.Tiles.Dirt, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Mountain], \
                                [G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Mountain, G.Tiles.Ice, G.Tiles.Mountain, G.Tiles.Mountain]])

class great_hall(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start(self):
        G.write("The next morning someone comes and leads you too a dining hall.")
        G.write("Tenaxx comes over and greets you.")
        head_wizard.say("leave")
        head_wizard.say("leave2")
        G.write("Everone is somewhere in the room.")

    def send_data(self, til, plyr=False):
        if til == (2,1):
            if plyr == True:
                global box
                if box == True:
                    G.write("You find that the box you took from Tenaxx is in the chest.")
                    G.write("It has a N engraved on the side, it must be Nathik's. It looks like his style.")
                else:
                    G.write("Someone has packed all your stuff in a chest and left it by the door to the dining hall.")
                os.system("PAUSE")
            return True

        if til == (1,10):
            if plyr == True:
                if box == True:
                    G.write("You walk over to Nathik.")
                    G.write("Steve: Hey, Nathik. I found this and was wondering if it was yours.")
                    G.write("You offer the box.")
                    G.write("For a moment he stares at it.")
                    head_necromancer.say("box")
                    os.system("PAUSE")
                    global Dredall_s
                    Dredall_s = Dredall_s - 1
                    global Nathik_s
                    Nathik_s = Nathik_s + 2
                    box_truth = int(input("1: Tell the truth? 2: Lie?"))
                    if box_truth is 1:
                        G.write("Steve: I was in Tenaxx's study and it was there. I was looking over it and thought it might be yours.")
                        head_necromancer.say("box")
                        head_necromancer.say("boxt")
                        G.write("Nathik takes the box, and with a slight nod, storms off to find Tenaxx.")
                        global Tenaxx_s
                        Tenaxx_s = Tenaxx_s - 2
                        global honesty
                        honesty = honesty + 1
                        TvsN = True
                    else:
                        G.write("Steve: It was in the chambers I was given. I don't know how it got in there.")
                        head_necromancer.say("boxl")
                        head_necromancer.say("boxl2")
                        G.write("He turns on his heels and leaves.")
                        honesty = honesty - 1
                    box = False
                    os.system("PAUSE")
                else:
                    G.write("Nathik glares at you until you go away.")
            return True

        if til == (3,1):
            if plyr == True:
                G.write("Tenaxx tells you to hurry up.")
            return True

        if til == (4,7):
            if plyr == True:
                G.write("Droxone seems to be fixing something and ignoring the food. It looks like the item blew up.")
            return True

        if til == (4,10):
            if plyr == True:
                G.write("Dredall is in some arguement with Morena and just waves you off.")
            return True

        if til == (6,8):
            if plyr == True:
                G.write("Morena is in an argument with Dredall.")
                G.write("A cat jumps up on the table. It really looks familiar.")
            return True

        if til == (3,0) or til == (4,0):
            if plyr == True:
                G.write("Would you like to leave?")
                leave = int(input("1:yes, 2:no"))
                if leave is 1:
                    global end_map
                    end_map = end_map + 1
                else:
                    G.write("Not yet.")
        return True


    def finished_map(self):
        G.write("You have breakfast, and then are quickly shoed out into a carage.")

great_hall = great_hall('great_hall')

great_hall.layout = G.np.array([[G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, \
                                G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall], \
                                [G.Tiles.Wall, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, \
                                G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Ice, G.Tiles.Cave, G.Tiles.Wall], \
                                [G.Tiles.Wall, G.Tiles.Ice, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Cave, \
                                G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Cave, G.Tiles.Wall], \
                                [G.Tiles.Cave, G.Tiles.Ice, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, \
                                G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Wall], \
                                [G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, \
                                G.Tiles.Ice, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Ice, G.Tiles.Cave, G.Tiles.Wall], \
                                [G.Tiles.Wall, G.Tiles.Cave, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Cave, \
                                G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Cave, G.Tiles.Wall], \
                                [G.Tiles.Wall, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, \
                                G.Tiles.Cave, G.Tiles.Ice, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Wall], \
                                [G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, \
                                G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall]])

class ship(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start():
        G.write("2 Weeks Later")
        G.write("The Northern Clyps Ocean")
        G.write("East of the Island Ashor")
        G.write("3 Days Out From the Hunirst Chain")
        G.write("You've been sea sick for the past 2 weeks. You've also been sick with nerves for the past two weeks.")

    def send_data(til, plyr=False):
        if til == (4,5):
            if plyr == True:
                G.write("Would you like to leave?")
                leave = int(input("1:yes, 2:no"))
                if leave is 1:
                    global end_map
                    end_map = end_map + 1
            return True

        if til == (0,4) or til == (0,6) or til == (1,3) or til == (1,7) \
            or til == (3,1) or til == (3,9) or til == (4,1) or til == (4,9) \
            or til == (5,0) or til == (6,0) or til == (7,0) or til == (8,0) \
            or til == (9,0) or til == (10,0) or til == (5,10) or til == (6,10) \
            or til == (7,10) or til == (8,10) or til == (9,10) or til == (10,10) \
            or til == (11,0) or til == (11,10) or til == (12,0) or til == (12,10) \
            or til == (13,0) or til == (13,10) or til == (14,0) or til == (14,10) \
            or til == (15,0) or til == (15,10) or til == (2,8) or til == (2,2) \
            or til == (16,1) or til == (16,9) or til == (17,1) or til == (17,9) \
            or til == (18,2) or til == (18,8) or til == (19,3) or til == (19,7) \
            or til == (20,4) or til == (20,6):
            G.write("Don't jump of the ship. You can't jump off the ship.")
            if plyr == True:
                G.write("Don't jump of the ship. You can't jump off the ship.")
            return False

        if til == (10,5):
            G.write("That's the main mast. You try and climb the mast, but just look really dumb.")
            if plyr is True:
                G.write("That's the main mast. You can't climb the main mast.")
            return False

        if til == (7,8):
            if plyr is True:
                G.write("Droxone has been trying to make you feel better.")
                head_alchemist.say("island")
                if honesty > 0:
                    G.write("You're an honest person. You tell the truth.")
                    G.write("Steve: I still have no idea what I'm doing. I don't remember any of this.")
                    head_alchemist.say("islandh")
                    G.write("Droxone seems to be a little uncomfortable whenever he looks at you.")
                else:
                    G.write("You're not that honest, so you lie.")
                    G.write("Steve: I think I remember some of this. It's all still a blur.")
                    head_alchemist.say("islandl")
                head_alchemist.say("island2")
                os.system("PAUSE")
            return True

        if til == (15,4):
            if plyr is True:
                G.write("Go away")
                global TvsN
                if TvsN is True:
                    G.write("You hear shouting.")
                    G.write("Nathik and Tenaxx seem to be having some sort of arguement.")
                    G.write("You walk closer to listen.")
                    G.write("Nathik: Is it not enough that you killed me? Is it not enough that you always make it clear I'm unwelcome?")
                    G.write("Nathik: Must you steal from me too?")
                    G.write("He brandishes the box you gave him back.")
                    G.write("Tenaxx: I don't know what you're talking about. That isn't yours.")
                    G.write("Nathik: It actually has my name on it! Right there! That is my name!")
                    G.write("Tenaxx: That's fake. That box is mine.")
                    G.write("Nathik: How would you even make a soul box? I'm the only one who knows how and I never told you.")
                    G.write("Tenaxx: There are other ways to do things other than necromancy.")
                    G.write("Nathik looks at Tenaxx with a flat expression.")
                    G.write("Nathik: Whose soul is in this? Because the last one I put in here before you stole it was someone who died of the blight.")
                    G.write("Before Tenaxx can do anything Nathik flicks the box. I starts floating next to him. Green light poors from it untill someone is standing where the box was.")
                    G.write("The person looks like a hologram. You can see that the box is floating inside where her heart would be.")
                    G.write("Soul: Where am I? The last thing I remember was... Nathik? What are we doing here.")
                    G.write("Tenaxx: That doesn't prove anything!")
                    G.write("Nathik: There will be wreckoning for this one day. Mark my words.")
                    G.write("With that Nathik storms off with the ghost girl walking behind him.")
                else:
                    G.write("Nathik: Don't you have someone else to talk to?")
                os.system("PAUSE")
        return True



    def finished_map():
        G.write("You go bellow deck.")
        G.write("You wake up from your sea sickness induced coma. It's dark out and there are lanterns on deck.")
        G.write("Coming up on the deck you can see a glow of the horizon.")
        G.write("Steve: The sun must be rising.")
        head_summoner.say("fire")
        G.write("You almost jump into the sea. How did a Centaur sneak up on you?")
        G.write("Steve: But aren't we still two days sailing from the Islands?")
        head_summoner.say("fire2")
        G.write("Steve: No one told me the islands where volcanic.")
        head_summoner.say("fire3")
        G.write("Steve: Oh... That's bad.")
        G.write("Dredall doesn't answer and just walks away.")

ship.layout = G.np.array([[G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Building, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Pit, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Cave, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water], \
                            [G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Building, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water, G.Tiles.Water]])


class island(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start(self):
        G.write("Landing on the Shores of the Hunirst Chain.")
        G.write("The entire island is covered in cooled molten rock. It looks like it's been paved over.")
        G.write("You can hear the rowing of the dragon from here. Fire, lava, and ash can be seen shooting up into the sky.")
        G.write("You're dragged along up the slope until you have a line of sight on the dragon.")
        G.write("It's the size of an apartment building. Brown scales cover it from head to toe.")
        G.write("The ground is covered in pools of molten rock.")

    def send_data(self, til, plyr=False):
        if til == (0,4) or til == (1,4) or til == (2,4) or til == (3,4) \
                        or til == (4,4) or til == (5,4) or til == (6,4):
            if plyr == True:
                G.write("You can't pass the lava")
            return False

        if til == (2,1) or til == (4,1) or til == (2,2) or til == (3,3) or til == (4,3):
            if plyr is True:
                G.write("Before you can do anything Dredall starts talking.")
                G.write("Dredall: This is where we must part ways. You survise is no longer required.")
                G.write("He seems to be talking to you.")
                G.write("Steve: Umm... What do you mean?")
                G.write("Dredall: You were never meant to actually fight the dragon. We'll explain everything later. Morena.")
                os.system("PAUSE")
                global end_map
                end_map = end_map + 1
        return True

    def finished_map(self):
        G.write("You look at Morena just in time to see her grin as she hits you very hard with her cain.")
        G.write("You fall to the ground as everything goes black.")


island = island('island')

island.layout = G.np.array([[G.Tiles.Water, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Lava], \
                            [G.Tiles.Water, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Lava], \
                            [G.Tiles.Water, G.Tiles.Ice, G.Tiles.Ice, G.Tiles.Wall, G.Tiles.Lava], \
                            [G.Tiles.Water, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Ice, G.Tiles.Lava], \
                            [G.Tiles.Water, G.Tiles.Ice, G.Tiles.Wall, G.Tiles.Ice, G.Tiles.Lava], \
                            [G.Tiles.Water, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Lava], \
                            [G.Tiles.Water, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Lava]])


class ship_hull(G.array_map):
    def __init__(self, name):
        super().__init__(name)

    def on_start(self):
        G.write("You come to in the hull of the ship. Everyone is standing around you.")
        G.write("Steve: What's going on.")
        G.write("Tenaxx: Good, you're awake. I shall explain what happened, and what's going to happen.")
        G.write("Tenaxx: We don't actually need you. Killing the world dragon is very easy really.")
        G.write("Tenaxx: However when we aren't doing this. We enjoy doing far more interesting things.")
        G.write("Tenaxx: Droxone builds things, Morena and I experiment, as does Nathik. Dredall, well he goes home.")
        G.write("Tenaxx: All the countries back us financially. We can all ask for almost anything and get it.")
        G.write("Tenaxx: A few countries do so because they like just one of us.")
        G.write("Tenaxx: As is turns out, Barnabas is quit popular. We don't need him, but if he's not here several countries don't care about this.")
        G.write("Nathik: If they knew how easy it was they really wouldn't care.")
        G.write("Tenaxx: That too.")
        os.system("PAUSE")
        os.system('cls')
        G.write("Steve: So you killed me because you wanted countries to keep giving you stuff?")
        G.write("Dredall: We didn't kill you.")
        G.write("Steve: Then what about the cat?")
        G.write("Droxone: What cat? No one said anything about a cat. You were just a random spirit floating around.")
        G.write("At this point you see a cat walk up to Morena. It rubs up against her.")
        G.write("Steve: That cat! That cat was following me the whole day I died. It tried to lead me around.")
        G.write("Everyone looks at Morena.")
        os.system("PAUSE")
        os.system('cls')
        G.write("Morena: I may have sent Fluffy out that day. I didn't tell him to kill someone though.")
        G.write("One of Droxone's many gadets starts wirring and flashing. He looks at it for a moment.")
        G.write("Droxone: My lie detector doesn't believe you and neither do I.")
        G.write("Nathik: Nor I.")
        G.write("Everyone is glaring at Morena.")
        G.write("Morena: Fine. I get bored after centuries of life.")
        G.write("Tenaxx: Well, we were going to kill you again, but if you died before your time that wouldn't be fair.")
        G.write("Steve: So you're aren't going to kill me?")
        G.write("Tenaxx: We shall vote on it!")
        G.write("Steve: What?!")
        G.write("Try and convince them not to kill you.")

    def send_data(self, til, plyr=False):
        if til == (1,1):
            if plyr is True:
                G.write("Nathik: Why should we spair you?")
                G.write("What do you say?")
                G.write("1: Because it's your fault that I died, and you should make ammends for that.")
                G.write("2: Because it will really annoy Morena, and we can both make fun of her for it for years.")
                choice = int(input(""))
                if choice is 1:
                    global Nathik_s
                    Nathik_s = Nathik_s - 1
                else:
                    Nathik_s = Nathik_s + 1
            return True

        if til == (1,4):#Droxone
            if plyr is True:
                G.write("Droxone: Why should we spair you?")
                G.write("What do you say?")
                G.write("1: Because you people killed me for no reason!")
                G.write("2: Because you're con artists and I died because of it.")
                choice = int(input(""))
                if choice is 1:
                    global Droxone_s
                    Droxone_s = Droxone_s + 1
                else:
                    Droxone_s = Droxone_s - 1

        if til == (2,2):#Dredall
            if plyr is True:
                G.write("Dredall: Why should we spair you?")
                G.write("What do you say?")
                G.write("1: Because I was unjustly killed.")
                G.write("2: Because I desirve a shot at life.")
                choice = int(input(""))
                if choice is 1:
                    global Dredall_s
                    Dredall_s = Dredall_s + 1
                else:
                    Dredall_s = Dredall_s - 1

        if til == (2,4):#Morena
            if plyr is True:
                G.write("Morena: Why should we spair you?")
                G.write("What do you say?")
                G.write("1: Because getting bored doesn't justify killing people.")
                G.write("2: Because I could still be useful to you as Barnabas.")
                choice = int(input(""))
                if choice is 1:
                    global Morena_s
                    Morena_s = Morena_s - 1
                else:
                    Morena_s = Morena_s + 1

        if til == (3,3):#Tenaxx
            if plyr is True:
                G.write("If you talk to Tenaxx you can no longer talk to anyone else. Are you sure you would like to go onto the vote?")
                move_on = int(input("1:yes, 2:no"))
                if move_on is 1:
                    G.write("Tenaxx: Why should we spair you?")
                    G.write("What do you say?")
                    G.write("1: Because using me for funding is evil.")
                    G.write("2: You could get more money out of me alive then dead.")
                    choice = int(input(""))
                    if choice is 1:
                        global Tenaxx_s
                        Tenaxx_s = Tenaxx_s - 1
                    else:
                        Tenaxx_s = Tenaxx_s + 1
                    global end_map
                    end_map = end_map + 1
                else:
                    G.write("Not yet.")

    def finished_map(self):
        G.write("Tenaxx: Well, shall we vote?")
        if Droxone_s > 1:
            global spair
            spair = spair + 1
            G.write("Droxone: I vote to spair him.")
        else:
            global kill
            kill = kill + 1
            G.write("Droxone: I vote we kill him.")

        if Nathik_s > 3:
            spair = spair + 1
            G.write("Nathik: I vote to spair him.")
        else:
            kill = kill + 1
            G.write("Nathik: I vote we kill him.")

        if Tenaxx_s > 2:
            spair = spair + 1
            G.write("Tenaxx: I vote we spair him.")
        else:
            kill = kill + 1
            G.write("Tenaxx: I vote we kill him.")

        if Morena_s > 1:
            spair = spair + 1
            G.write("Morena: I vote we spair him.")
        else:
            kill = kill + 1
            G.write("Morena: I vote we kill him.")

        if Dredall_s > 2:
            spair = spair + 1
            G.write("Dredall: I vote we spair him.")
        else:
            kill = kill + 1
            G.write("Dredall: I vote we kill him.")

        if kill > spair:
            G.write("Tenaxx: Well it appears we shall kill him anyway!")
            G.write("Steve: Wait wait wa...")
            G.write("Tenaxx snaps his fingers and everything goes black.")
        else:
            G.write("Tenaxx: It appears we shall spair you, today.")
            G.write("")




ship_hull = ship_hull('ship_hull')

ship_hull.layout = G.np.array([[G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building], \
                                [G.Tiles.Building, G.Tiles.Ice, G.Tiles.Building, G.Tiles.Building, G.Tiles.Ice, G.Tiles.Building], \
                                [G.Tiles.Building, G.Tiles.Building, G.Tiles.Ice, G.Tiles.Building, G.Tiles.Ice, G.Tiles.Building], \
                                [G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Ice, G.Tiles.Building, G.Tiles.Building], \
                                [G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building], \
                                [G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building, G.Tiles.Building]])





#
# NPCs
#

#The group who is in charge of bringing Barnabas the Dragon Slayer back.
head_alchemist = G.NPC("Droxone Iseas", fortess_room, 20, 20)
head_necromancer = G.NPC("Nathik the Undead", fortess_room, 20, 20)
head_wizard = G.NPC("Tenaxx the Storm Master", fortess_room, 20, 20)
head_witch = G.NPC("Morena Wyrm", fortess_room, 20, 20)
head_summoner = G.NPC("Dredall the Centaur", fortess_room, 20, 20)

#Group leaders
king_blaive = G.NPC("King Blaive", G.loc_man, 20, 20)
queen_gisella = G.NPC("Queen Gisella", G.loc_man, 20, 20)
lord_basequin = G.NPC("Lord Basequin", G.loc_man, 20, 20)
lady_aalis = G.NPC("Lady Aalis", G.loc_man, 20, 20)
count_seri = G.NPC("Count Seri", G.loc_man, 20, 20)
countess_rohez = G.NPC("Countess Rohez", G.loc_man, 20, 20)
king_gilford = G.NPC("King Gilford", G.loc_man, 20, 20)
queen_misuki = G.NPC("Queen Misuki", G.loc_man, 20, 20)
king_britius = G.NPC("King Britius", G.loc_man, 20, 20)
lord_wilmot = G.NPC("Lord Wilmot", G.loc_man, 20, 20)
lady_symonne = G.NPC("Lady Symonne", G.loc_man, 20, 20)
mirage_paradox = G.NPC("Mirage of Paradox", G.loc_man, 20, 20)
magroch_natzarson = G.NPC("Magroch Natzarson", G.loc_man, 20, 20)
zeom_flifnas = G.NPC("Zeom Flifnas", G.loc_man, 20, 20)
king_artur = G.NPC("King Artur", G.loc_man, 20, 20)
queen_cusal = G.NPC("Queen Cusal", G.loc_man, 20, 20)
princess_di = G.NPC("Princess Di", G.loc_man, 20, 20)
lady_gill = G.NPC("Lady Gill", G.loc_man, 20, 20)

#Higher powers

#Generic NPCs to just use for anything
phone = G.NPC("Steve's Phone", G.loc_man, 20, 20)
cat = G.NPC("Fluffy", G.loc_man, 20, 20)
news_reader = G.NPC("Anchor", G.loc_man, 20, 20)
steves_boss = G.NPC("The Boss", G.loc_man, 20, 20)
arms_master_npc = G.NPC("Greg", G.loc_man, 20, 20)
co_worker = G.NPC("Lary", G.loc_man, 20, 20)
knifeman = G.NPC("Knifeman", G.loc_man, 20, 20)
pes_emily = G.NPC("Emily", G.loc_man, 20, 20)
pes_steven = G.NPC("Steven", G.loc_man, 20, 20)


#Adding Dialogue
news_reader.add_dialogue("news1", "Reporter: Wall street took another big hit today, with the dow dropping another 40 points to hit a fifty year low.")
news_reader.add_dialogue("news2", "Reporter: Many local companies are laying off up to half of their work force.")
news_reader.add_dialogue("news3", "Reporter: Police are warning people to be careful. A knifeman who killed two people last week was spotted.")
co_worker.add_dialogue("greating", "Lary: Hey Steve! Are you in trouble?")
co_worker.add_dialogue("fired", "Lary: I hope you don't get let go too. Who else am I going to complain too?")
co_worker.add_dialogue("weekend", "Lary: Are we still doing stuff this weekend?")
cat.add_dialogue("meowq", "Cat: Meow?")
cat.add_dialogue("meowl", "Cat: Meow!")
cat.add_dialogue("meow", "Cat: Meow.")
cat.add_dialogue("purr", "Cat: purrrrrr")
knifeman.add_dialogue("cops", "Knifeman: Are you a cop?")
phone.add_dialogue("hello", "Phone: Hello Steve. It is time to wake up. You have work at 8:00. It is going to rain tod...")
steves_boss.add_dialogue("greating", "Boss: Hello Steve, nice to see you. You are falling behind on all your work. Come see me after your shift.")
steves_boss.add_dialogue("fired", "Boss: I'm sorry, but we have to let you go. We're downsizing. Please clear out you stuff by tomorrow morning, goodbye.")
pes_emily.add_dialogue("move", "Pedestrian: Why are you just standing there? People are walking here!")
pes_emily.add_dialogue("look_out", "Pedestrian: Look Out! A car!")
head_witch.add_dialogue("first", "???: We got em! We got em!")
head_necromancer.add_dialogue("first", "???: I told you we would get the right spirit evetually.")
head_summoner.add_dialogue("first", "???: Shut up Necromancer. I only tolerate you while you're useful.")
head_witch.add_dialogue("insult_n", "???: He doesn't remember you Nathik! Hehehe! He doesn't remember you!")
head_witch.add_dialogue("insult_n2", "???: He's the reason you're undead and he doesn't even remember you!")
head_necromancer.add_dialogue("insult_w", "Nathik: I may be dead, but at least I don't age anymore... Morena.")
head_summoner.add_dialogue("calm", "???: Now now, Nathik be nice. Morena stop beating up the necromancer with your cane, please.")
head_wizard.add_dialogue("hello", "???: Dredall will calm them down soon enough. It's been a long time Barnabas.")
head_wizard.add_dialogue("confustion", "???: Memory loss isn't a normal side effect of resurection.")
head_wizard.add_dialogue("blame", "???: Droxone, your devises must be off.")
head_alchemist.add_dialogue("sigh", "Droxone: Not as off as your brain you old sack of glitter.")
head_wizard.add_dialogue("hearinglose", "???: What did you say? I can't hear so well anymore.")
head_alchemist.add_dialogue("backtrack", "Droxone: I said none of my stuff is the issue, Tenaxx. Check Morena's potion.")
head_alchemist.add_dialogue("get1", "Droxone: Hi Barnabus. I'm Droxone, the new alchemist on the team.")
head_alchemist.add_dialogue("get2", "Droxone: The resurrection chambers, where you're always brought back.")
head_necromancer.add_dialogue("get1", "Nathik: Oh yes. You...")
head_necromancer.add_dialogue("get2", "Nathik: You were always stupid Barnabas. You were always forgetful.")
head_necromancer.add_dialogue("get3", "Nathik: You only ever succeded because of what others did. What we gave up.")
head_necromancer.add_dialogue("get4", "Nathik: It doesn't surprise me that you don't remember anything. Why worry your pretty head over it, ay?")
head_wizard.add_dialogue("get1", "Tenaxx: Ah yes, our champion! Young again and ready to save us... again.")
head_wizard.add_dialogue("get2", "Tenaxx: Nonsence, The memory loss is a slight oddity, but you are still my long time friend.")
head_wizard.add_dialogue("get3", "Tenaxx: It's great to see you again, Barnabas. Now down to business.")
head_witch.add_dialogue("get1", "Morena: Don't Ma'am me you little worm. You still owe me for that last card game.")
head_witch.add_dialogue("get2", "Morena: Oh yes. The memory loss. Ironicly, I forgot about that. We were very good friends before you died.")
head_witch.add_dialogue("get3", "Morena: I trained you quite a bit back in our day. You were a very powerful witch.")
head_witch.add_dialogue("get4", "Morena: One of my best aprintises. It is very good that you're now back.")
head_witch.add_dialogue("get5", "Morena: Well of course. Tell me, what's the last thing you remember?")
head_summoner.add_dialogue("get1", "Dredall: Hello my old friend. It is good to see you again.")
head_summoner.add_dialogue("get2", "Dredall: You will be out of practice after all this time in the afterlife.")
head_summoner.add_dialogue("get3", "Dredall: Maybe this time around you will master some of what I have to teach you.")
head_summoner.add_dialogue("get4", "Dredall: Why, summoning of course. You were always myserable at it. Maybe you will learn this time.")
head_wizard.add_dialogue("expo1", "Tenaxx: So now that we have Barnabas back, we may begin preperations for re-killing the world dragon...")
head_wizard.add_dialogue("expo2", "Tenaxx: Mapoantain.")
head_wizard.add_dialogue("expo3", "Tenaxx: Now, Barnabas. You seem to be having a few memory troubles. How much do you remember?")
head_alchemist.add_dialogue("shock", "Droxone: Wait, you actually don't remember anything?")
head_summoner.add_dialogue("solution", "Dredall: There is a way to test this. Come Barnabas.")
head_summoner.add_dialogue("weapon", "Dredall: Pick a weapon to use. We shall see how much you remember.")
head_summoner.add_dialogue("warhammer", "Dredall: I see you must remember something to pick such a weapon.")
head_summoner.add_dialogue("wrong_weapon", "Dredall: I didn't think you enjoied using that weapon.")
head_witch.add_dialogue("wand", "Morena: I see you finally want to learn a better way to win battles. May I aid you?")
head_witch.add_dialogue("(:", "Morena: I look forward to it.")
head_witch.add_dialogue("wait", "Morena: The offer stays open if you have a change of heart.")
head_summoner.add_dialogue("train", "Dredall: Now that you have chosen a weapon. You may practice here. I will call our arms master to duel with you.")
head_necromancer.add_dialogue("rust", "Nathik: Nonsence. You aren't made of metal.")
head_summoner.add_dialogue("spar", "Dredall: Greg will spar with you. Once you've shaken the rust off we may go to kill the world dragon.")
head_wizard.add_dialogue("already", "Tenaxx: We did that the first time around. Why would we put them back?")
head_alchemist.add_dialogue("yahn", "Droxone: Greg will take you to your chambers once you're done. Bye.")
head_witch.add_dialogue("come", "Morena: If you wish to learn to use that thing, I'll be in the library.")
arms_master_npc.add_dialogue("first", "Greg: Would you care to start now?")
arms_master_npc.add_dialogue("confus", "Greg: How is that? You're one of the best swordsmen in the history of this land.")
arms_master_npc.add_dialogue("realize", "Greg: That would make sense. You aren't holding your weapon correctly. You're clumbsy, and don't know what to do with yourself. That's why you keep wringing your hands.")
arms_master_npc.add_dialogue("sad", "Greg: That's to bad. I wanted to ask you about some things, but I guess you wouldn't know the answer.")
arms_master_npc.add_dialogue("expl1", "Greg: I do believe todays sparing session should turn into a history lession. Maybe I can jog your memory.")
arms_master_npc.add_dialogue("expl2", "Greg: Where you are is easy enough. You are in the resurrection fortress in ______, which is on the continent of _______, in The Ancient Lands.")
arms_master_npc.add_dialogue("expl3", "Greg: Most people just call it Alnues.")
arms_master_npc.add_dialogue("ask", "Greg: Is any of this jogging your memory?")
arms_master_npc.add_dialogue("expl4", "Greg: We have ages that are 300 years long. This is the seventh age. Barnabas was born in the first, as was Tenaxx the Stormmaster.")
arms_master_npc.add_dialogue("expl5", "Greg: The two of you along with 4 other people who are long sinse dead killed the world dragon.")
arms_master_npc.add_dialogue("expl6", "Greg: Morena replaced the other witch as high cover leader afterward. The necromancer vanished, as did the summoner.")
arms_master_npc.add_dialogue("expl7", "Greg: The origonal alchemist died of old age. As have most of the rest. Droxone is in his thirties.")
arms_master_npc.add_dialogue("expl8", "Greg: Every time the world dragon comes back, the five resurect you to help them kill it.")
arms_master_npc.add_dialogue("lieyes", "Greg: This perfectly fine. At least we know the memories are there now.")
arms_master_npc.add_dialogue("lieno", "Greg: We'll keep trying. You'll remember who you were eventually.")
arms_master_npc.add_dialogue("lieyes2", "Greg: If you remember than we don't need to practice at all. Even rusty you're a better swordsman than I?")
arms_master_npc.add_dialogue("lieno2", "Greg: I don't believe we should spar today. I don't think you remember how.")
arms_master_npc.add_dialogue("gowhere", "Greg: Would you like me to take you anywhere?")
arms_master_npc.add_dialogue("treasure", "Greg: Somewhere very interesting.")
arms_master_npc.add_dialogue("coolstuff", "Greg: Welcome to the Treasury. This room holds some of the most amazing things in Alnues and beyond.")
arms_master_npc.add_dialogue("coolstuff2", "Greg: this is all stuff one of the six has at some point aquiered. You're one of them so you can take anything with your name on it.")
arms_master_npc.add_dialogue("goback", "Greg: I should probably take you back now. If you will, sir.")
head_wizard.add_dialogue("studyhello", "Tenaxx: Why hello Barnabas. How was your sparing session?")
head_wizard.add_dialogue("plan1", "Tenaxx: Same as always, but you don't remember.")
head_wizard.add_dialogue("plan2", "Tenaxx: We go to the Huninst Chain, where the world dragon always appears.")
head_wizard.add_dialogue("plan3", "Tenaxx: Droxone will prep a battle area with his things to make it easier.")
head_wizard.add_dialogue("plan4", "Tenaxx: Nathik provides the cannon fodder, Dredall provides the might, I provide protection from his fire, Morena keeps us all alive.")
head_wizard.add_dialogue("roles", "Tenaxx: I'm a wizard, weilder of elemental powers. Nathik is a necromancer. Dredall is a beast summoner. Droxone is an alchemist. Morena is a witch.")
head_summoner.add_dialogue("great", "Dredall: Hello, Barnabas. What brings you here?")
head_summoner.add_dialogue("home", "Dredall: Your home has long sinse fallen into the sea. You know this.")
head_summoner.add_dialogue("earth", "Dredall: I had feared this. We cannot send you back. You must aid us whether you wish to or not.")
head_summoner.add_dialogue("useless", "Dredall: It can be anyone. We only need someone to focus our power through. It doesn't matter that you've never weilded a weapon before.")
head_summoner.add_dialogue("truth", "Dredall: The others just need to believe you're real. As do the people.")
head_summoner.add_dialogue("defen", "Dredall: Yes, this is the first time we grabbed the wrong soul from the afterlife.")
head_summoner.add_dialogue("goaway", "Dredall: For the sake of this world you are going to go through with this.")
head_alchemist.add_dialogue("radio", "Droxone: Just open the door and come in. I can see you, Barnabas.")
head_alchemist.add_dialogue("blewup", "Droxone: Hey, sorry for my appearance. I just had a mishap.")
head_alchemist.add_dialogue("memoryloss", "Droxone: Wow, you must have memory loss. Barnabas wouldn't every accept anything less then to prostate at his feet.")
head_alchemist.add_dialogue("thought", "Droxone: Hmm... It is possible. I don't understand how they track down the right spirit, I just prep the body.")
head_alchemist.add_dialogue("body", "Droxone: You haven't looked in a mirror have you? You have a different body than you did when you were alive.")
head_alchemist.add_dialogue("body2", "Droxone: Nathik and I have to make a body before the other three get your spirit.")
head_alchemist.add_dialogue("body3", "Droxone: Some of your parts are mechanical, others were reanimated. I then tie it all together with a Phylosophers Stone.")
head_alchemist.add_dialogue("concern", "Droxone: Are you alright? You're looking paler than you should.")
head_necromancer.add_dialogue("what", "Nathik: Who is it?")
head_necromancer.add_dialogue("mad", "Nathik: What would cause you to be so stupid as to come here? You aren't welcome!")
head_necromancer.add_dialogue("apol", "Nathik: It's about three hundred years too late for that, Barnabas.")
head_necromancer.add_dialogue("ask", "Nathik: You killed me! You stabbed me from behind after tricking me and left me to die of blood loss! Do you know how long that takes?!")
head_necromancer.add_dialogue("ask2", "Nathik: Hours! It took hours for me too die! When my enchantments kicked in it took even longer because of how bad the death was! You tourchered me for days!")
head_witch.add_dialogue("training", "Morena: I'm glad you came. I was wondering whether or not you would.")
head_witch.add_dialogue("training2", "Morena: Well, we don't have time for real training, but I have a few things you may want.")
head_witch.add_dialogue("training3", "Morena: I've been trying to convince you that my way will kill the world dragon forever for so many centuries. Finally we'll end this!")
head_witch.add_dialogue("training4", "Morena: Take up these items and end this once and for all!")
head_witch.add_dialogue("takeitems", "Morena: For the first time in centuries we can kill this thing for good! I won't have to put up with Tenaxx or Dredall ever again!")
head_witch.add_dialogue("regect", "Morena: Very well. We will put the beast down for a time, but in two hundred years you will come back and do it all again, and again, and, again.")
head_witch.add_dialogue("curio", "Morena: There are many places you could be right now. Here isn't likely. Why have you come?")
head_witch.add_dialogue("curio2", "Morena: We're going to continue the endless cycle of killing the world dragon only to have it come back in two hundred years.")
head_witch.add_dialogue("curio3", "Morena: All because our leadership is in the hands of Tenaxx and Dredall. Two of the biggest idiots to come out of the Cypus Sea shores in eons.")
head_witch.add_dialogue("endtalk", "Morena: You should go and prepare for the trip. Off with you.")
head_wizard.add_dialogue("leave", "Tenaxx: Hello, Barnabas. We will be leaving for the Hunirst Chain in just over an hour.")
head_wizard.add_dialogue("leave2", "Tenaxx: You will be taken to the ship as soon as you've finished your meal/")
head_necromancer.add_dialogue("box", "Nathik: Yes, where did you find this?")
head_necromancer.add_dialogue("boxt", "Nathik: That thief! Of course he took it! He can't do anything for himself.")
head_necromancer.add_dialogue("boxl", "Nathik: That is quite odd. You wouldn't have stollen it, for you have no consept of what it does.")
head_necromancer.add_dialogue("boxl2", "Nathik: I guess I should thank you for giving it back. Thank you.")
head_alchemist.add_dialogue("island", "Droxone: It's my first time going to this island. I've never faced the World Dragon before. Can you still remember nothing?")
head_alchemist.add_dialogue("islandh", "Droxone: Well at least I'm not the only one who's never done this before, or at least can't remember doing it.")
head_alchemist.add_dialogue("islandl", "Droxone: That's good. Then only one person is new.")
head_alchemist.add_dialogue("island2", "Droxone: This is like reflex for everyone else. No matter how much you can remember, we'll all be fine. You're turning green again.")
head_summoner.add_dialogue("fire", "Dredall: No. That is the Dragon.")
head_summoner.add_dialogue("fire2", "Dredall: Yes. What you're seeing is light from molten rock reflecting off smoke.")
head_summoner.add_dialogue("fire3", "Dredall: They aren't.")


def map_move(mapid, you):
    global end_map
    end_map = 0
    mapid.on_start()
    os.system("PAUSE")
    G.loc_man.load_map(mapid)
    while end_map != 1:
        print(end_map)
        direct_m = str(input("Move: wasd"))
        if direct_m == "w":
            G.loc_man.move(you, G.Directions.Up)
            print("in w")
        if direct_m == "s":
            G.loc_man.move(you, G.Directions.Down)
            print("in s")
        if direct_m == "a":
            G.loc_man.move(you, G.Directions.Left)
            print("in a")
        if direct_m == "d":
            G.loc_man.move(you, G.Directions.Right)
            print("in d")
    G.loc_man.load_map(mapid)
    mapid.finished_map()
    os.system("PAUSE")
    os.system('cls')

steve = G.player("Steve", G.loc_man, 0, 1, steve_inv, steve_stats)
while True:



    G.write("To move, use 'wasd' keys to indicate dirrection, then hit 'Enter' to confirm.")
    G.write("Please don't tap on the keys unless indicated. This can interfear with the next choice.")
    G.write("Bright blue tiles indicate that you are supposed to interact with them.")
    G.write("You can sometimes do many things in one room. Don't leave unless you're sure you want to.")
    G.write("Are you ready to start?")
    os.system("PAUSE")
    os.system('cls')
    steve_a = G.player("Steve", appartment_map, 0, 1, steve_inv, steve_stats)
    ap_map = False
    map_move(appartment_map, steve_a)
    steve_f = G.player("Steve", fortess_room, 2, 3, steve_inv, steve_stats)
    map_move(fortess_room, steve_f)
    steve_ar = G.player("Steve", arena_map, 0, 2, steve_inv, steve_stats)
    map_move(arena_map, steve_ar)
    while current_til != (0,0):
        steve_hall = G.player("Steve", hallway_map, 0, 2, steve_inv, steve_stats)
        map_move(hallway_map, steve_hall)

        if current_til == (0,2):
            steve_lib = G.player("Steve", library_room, 7, 5, steve_inv, steve_stats)
            map_move(library_room, steve_lib)
        if current_til == (0,4):
            steve_ten = G.player("Steve", tenaxx_study, 2, 5, steve_inv, steve_stats)
            map_move(tenaxx_study, steve_ten)
        if current_til == (0,6):
            steve_dre = G.player("Steve", dradall_study, 2, 5, steve_inv, steve_stats)
            map_move(dradall_study, steve_dre)
        if current_til == (3,2):
            steve_dro = G.player("Steve", droxone_study, 2, 5, steve_inv, steve_stats)
            map_move(droxone_study, steve_dro)
        if current_til == (3,4):
            steve_nat = G.player("Steve", nathik_study, 2, 5, steve_inv, steve_stats)
            map_move(nathik_study, steve_nat)
        if current_til == (3,6):
            steve_treas = G.player("Steve", treasury, 3, 4, steve_inv, steve_stats)
            map_move(treasury, steve_treas)
    curiosity = True
    box = True
    steve_room = G.player("Steve", your_room, 2, 4, steve_inv, steve_stats)
    map_move(your_room, steve_room)
    steve_gh = G.player("Steve", great_hall, 0, 4, steve_inv, steve_stats)
    map_move(great_hall, steve_gh)
    steve_ship = G.player("Steve", ship, 5, 5, steve_inv, steve_stats)
    map_move(ship, steve_ship)
    steve_is = G.player("Steve", island, 1, 3, steve_inv, steve_stats)
    map_move(island, steve_is)
    steve_hull = G.player("Steve", ship_hull, 3, 1, steve_inv, steve_stats)
    map_move(ship_hull, steve_hull)
    os.system("PAUSE")
    os.system('cls')
    G.write("The End")

    G.write("You final standing with Droxone(max:3):")
    print(str(Droxone_s))
    G.write("You final standing with Nathik(max:5):")
    print(str(Nathik_s))
    G.write("You final standing with Tenaxx(max:3):")
    print(str(Tenaxx_s))
    G.write("You final standing with Morena(max:5):")
    print(str(Morena_s))
    G.write("You final standing with Dredall(max:4):")
    print(str(Dredall_s))


    os.system("PAUSE")
    
