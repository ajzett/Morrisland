from sys import path
path.append('./Gilbo/')
path.append('./Gilbo/deps/')
import Gilbo as G
import os
from sys import stdout




#
# Story Variables #
#
class_type = 0
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
mana = item("Mana", "Used to fuel spells", 10)

arrow = G.item("Arrow", "A common arrow, can be found almost anywhere", .1)
cursed_arrow = G.item("A cursed arrow", "", 10)
snipers_arrow = G.item("Will always hit and cit", "", 10)
black_arrow = G.item("Negates all armor", "", 10)
life_drain_arrow = G.item("Drains the health of anything hit with it", "", 10)
rope_arrow = G.item("Launches a rope a long distance", "", 5)

bolt = G.item("A plain crossbow bolt", "", 1)

dart = G.item("", "", 1)

# Legendary Items
philosophers_stone = G.item("A stone that can give you eternal life", "", 200)
shanams_ring = G.item("A ring that lets your summon a massive creature to fight for you", "", 200)
bruldrins_stone = G.item("Makes the owner a God of Death", "", 3000)


#
# End of items
#




#
# NPCs
#

#The group who is in charge of bringing Barnabas the Dragon Slayer back.
head_alchemist = G.NPC("Droxone Iseas", G.loc_man, 20, 20)
head_necromancer = G.NPC("Nathik the Undead", G.loc_man, 20, 20)
head_wizard = G.NPC("Tenaxx the Storm Master", G.loc_man, 20, 20)
head_witch = G.NPC("Morena Wyrm", G.loc_man, 20, 20)
head_summoner = G.NPC("Dredall the Centaur", G.loc_man, 20, 20)

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
co_worker = G.NPC("Lary", G.loc_man, 20, 20)
knifeman = G.NPC("Knifeman", G.loc_man, 20, 20)
pes_emily = G.NPC("Emily", G.loc_man, 20, 20)
pes_steven = G.NPC("Steven", G.loc_man, 20, 20)


#Adding Dialogue
news_reader.add_dialogue("news1", "Reporter: Wall street took another big hit today, with the down dropping another 400 points to hit a fifty year low.")
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
steves_boss.add_dialogue("greating", "Boss: Hello Steve. You are falling behind on all your work. Come see me after your shift.")
steves_boss.add_dialogue("fired", "Boss: I'm sorry, but we have to let you go. We're downsizing. Please clear out you stuff by tomorrow morning.")
pes_emily.add_dialogue("move", "Pedestrian: Why are you just standing there? People are walking here!")
pes_emily.add_dialogue("look_out", "Pedestrian: Look Out! A car!")
head_witch.add_dialogue("first", "???: We got em! We got em!")
head_necromancer.add_dialogue("first", "???: I told you we would get the right spirit evetually.")
head_summoner.add_dialogue("first", "???: Shut up necromancer. I only tolerate you while you're useful.")
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


#
# End of NPCs
#

#
# Attacks
#
daggar_stab = G.attack(1, 3, "You stab something with a small knife", 1)
sword_slash = G.attack(2, 5, "You slash at your opponent", 1)
sword_thrust = G.attack(2, 10, "You run your opponent through", 1)
rapier_slash = G.attack(3, 4, "You slash", 2)
rapier_thrust = G.attack(3, 8, "You stab", 1)
wood_bludgeon = G.attack(2, 3, "You hit them really hard", 2)
brass_punch = G.attack(1, 3, "You punch them in the face", 2)
far_shot = G.ammo_attack(40, 6, "You shoot something really far away", 1, 40, arrow)
near_shot = G.ammo_attack(10, 4, "You shoot something near you", 1, 85, arrow)
face_shot = G.ammo_attack(3, 8, "You shoot someone right in front of you", 1, 70, arrow)
bolt_shot = G.ammo_attack(20, 10, "You shoot a crossbow", 1, 90, bolt)
axe_cleave = G.attack(2, 5, "You hit with an axe", 1)
pike_stab = G.attack(4, 3, "You stab something with a pike", 1)
mace_hit = G.attack(2, 5, "You hit them with your mace", 1)
throw_spear = G.ammo_attack(6, 4, "You through your spear", 1, 60, arrow)
spear_stab = G.attack(3, 2, "You stab with the spear", 1)
flail_hit = G.attack(3, 5, "You hit with your flail", 1)
war_hammer_hit = G.attack(1, 4, "You hit with a hammer", 1)
blowgun_shot = G.ammo_attack(10, 1, "You hit with a dart", 1, 80, dart)
push = G.attack(1, 3, "You push with your shield", 1)

#Magic Attacks
fire_needle = G.ammo_attack(5, 4, "You send a needle of fire at your opponent", 1, 70, mana)
icicle = G.ammo_attack(5, 6, "You send a spike of ice at your opponent", 1, 60, mana)
eletricute = G.ammo_attack(2, 7, "", 1, 100, mana)
blind = G.ammo_attack(3, 2, "", 1, 50, mana)

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
warhammer = G.weapon("War Hammer", "", 3, 3, warhammer_linked)
blowgun_linked = [blowgun_shot]
blowgun = G.weapon("Blowgun", "", 1, 1, blowgun_linked)
club_linked = [wood_bludgeon]
club = G.weapon("Club", "", 1, 2, club_linked)
s_and_s_linked = [push, sword_slash, sword_thrust, wood_bludgeon]
shield_sword = G.weapon("Sword and Shield", "", 12, 3, s_and_s_linked, armr=3)
oak_wand_linked = [fire_needle, icicle, eletricute, blind]
oak_wand = G.weapon("Wand", "", 20, 4, oak_wand_linked)



#
# Armor
#
basic_armor = G.armor("Leather Armor", "", 4, armr=3)
steel_armor = G.armor("Steel Armor", "", 15, armr=6)
ench_basic_armor = G.armor("Enchanted Leather Armor", "", 10, armr=5, agil=2)
ench_steel_armor = G.armor("Enchanted Steel Armor", "", 25, armr=10, stren=4)
mythril_armor = G.armor("Mythril Armor", "", 75, armr=25, pwr=1, agil=3, stren=5)


#
# Potions
#
minor_health = G.stat_item("Minor Health Potion", "", 10, 1, hp=10)
health_potion = G.stat_item("Health Potion", "", 15, 1, hp=15)
major_health = G.stat_item("Major Health Potion", "", 20, 1, hp=20)
iron_skin_potion = G.stat_item("Iron Skin Potion", "", 10, 5, armr=5)
strength_potion = G.stat_item("Stength Potion", "", 10, 5, stren=5)
grace_potion = G.stat_item("Grace Potion", "", 20, 5, agil=3, pwr=1, armr=1)
giant_potion = G.stat_item("Giant Potion", "", 10, 5, stren=5, hp=10, pwr=-1, agil=-2, armr=2)
durable_potion = G.stat_item("Durable Potion", "", 10, 5, hp=20, armr=6)




weapon_choice = [daggar, sword, rapier, quarterstaff, brass_knuckles, long_bow, short_bow, cross_bow, axe, pike, mace, spear, warhammer, blowgun, club, shield_sword, oak_wand]

steve_stats = G.battler_stats(100, 5, 0, 5, 1)
arms_master_stats = G.battler_stats(100, 10, 0, 7, 3)
steve_stuff = []
steve_using = []
steve_inv = G.player_collection(10, steve_stuff, steve_using)
arms_m_stuff = [shield_sword, daggar, basic_armor, minor_health]
arms_m_using = []
arms_m_inv = G.battler_collection(arms_m_stuff, arms_m_using)
arms_m_inv.equip(basic_armor)
arms_m_inv.equip(shield_sword)


steve = G.player("Steve", G.loc_man, 1, 3, steve_inv, steve_stats)
arms_master = G.battler("Greg", G.loc_man, 2, 3, )
#chamber = G.array_map("Chamber")
#chamber.layout = G.np.array([[G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall, G.Tiles.Wall][G.Tiles.Wall, G.Tiles.Dirt, G.Tiles.Dirt, G.Tiles.Dirt,]])



#
# Actual Game #
#


G.write("7:10am")
G.write("Monday, March 4th.")
G.write("Your apartment.")
os.system('cls')
phone.say("hello")
G.write("Your cat knocks your phone on the floor")
G.write("Wait... You don't own a cat. You're not that sad!")
G.write("Yet...")
cat.say("meowl")
os.system('cls')
G.write("The cat jumps down onto the floor and goes into the other room. You hear the TV turn on.")
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
    os.system('cls')
    G.write("As you walk out of your door you see a lot of cops on the other side of the street.")
    G.write("The knifeman you saw on TV is in the back of one of the patrol cars.")
    os.system('cls')
    G.write("You get to work without a problem")
    steves_boss.say("greating")
    G.write("*Gulp*")
    G.write("You quickly get down to work.")
    co_worker.say("greating")
    G.write("I don't know.")
    co_worker.say("fired")
    G.write("I'm sure you could find someone. I won't be able to make rent if I'm fired.")
    co_worker.say("weekend")
    G.write("I don't know.")
    os.system('cls')
    G.write("You go to get coffee")
    cat.say("meowq")
    G.write("Why are you still here!?")
    os.system('cls')
    G.write("At the end of the day you go to the Boss's office")
    steves_boss.say("fired")
    G.write("You leave the room and start packing up.")
    G.write("The cat is sitting on your desk.")
    cat.say("purr")
    os.system('cls')
    G.write("You leave the office building with a medium box of stuff.")
    G.write("You look back up at your old office building.")
    G.write("The cat is sitting on a ledge, staring at you.")
    pes_emily.say("move")
    G.write("Sorry")
    G.write("What is with that cat? We does it keep following you?")
    cat.say("meowl")
    G.write("While staring at the cat, you hear brakes scretching")
    pes_emily.say("look_out")
    G.write("You hear a crunch and everything goes black.")


else:
    os.system('cls')
    G.write("You ignore the cat and get ready to go to work.")
    news_reader.say("news1")
    news_reader.say("news2")
    G.write("You hope you don't get laid off. This world is horrible.")
    cat.say("meowl")
    G.write("You should get to work early.")
    os.system('cls')
    G.write("You walk out onto the street.")
    G.write("You hear sirens.")
    G.write("That's not important. You take your usual route to work.")
    G.write("If you cut through this ally it will be faster.")
    G.write("You here someone walking behind you.")
    os.system('cls')
    knifeman.say("cops")
    G.write("Before you can respond to the man he thrusts his hand toward your stomach.")
    G.write("Did he punch you?")
    G.write("You look down.")
    G.write("There's a knife sticking out of your gut.")
    G.write("The last thing you see is the cat.")
    cat.say("purr")
    os.system('cls')
head_witch.say("first")
head_necromancer.say("first")
head_summoner.say('first')
G.write("Whaaa?")
G.write("Who are y...")
G.write("You voice trails off as you look up at five old 'people'.")
os.system('cls')
G.write("A super old and croutched woman started crowing.")
head_witch.say("insult_n")
head_witch.say("insult_n2")
head_necromancer.say("insult_w")
G.write("The woman, Morena, slapped the talking corpse.")
G.write("The two started squabbling even more.")
os.system('cls')
head_summoner.say("calm")
G.write("The man who had just spoken was really tall.")
G.write("You look down from his face to his body.")
G.write("He has a horses body.")
os.system('cls')
head_wizard.say("hello")
G.write("B-b-b-barn who?")
head_wizard.say("confustion")
head_wizard.say("blame")
head_alchemist.say("sigh")
head_wizard.say("hearinglose")
head_alchemist.say("backtrack")
G.write("Now the other two start squablling")
os.system('cls')
G.write("Who do you want to talk to?")
one_of_five = int(input("1:Droxone, 2:Nathik, 3:Tenaxx, 4:Morena, 5:Dredall"))
os.system('cls')
if one_of_five is 1:
    G.write("You get up off the table.")
    G.write("You walk over to Droxone, who is by far the youngest of all the five.")
    G.write("Hello?")
    head_alchemist.say("get1")
    G.write("Steve: I'll start with a simple question, where am I?")
    G.write("The men, who can't be much older than you, looks very confused.")
    head_alchemist.say("get2")
    G.write("Steve: My name isn't Barnabas, it's Steve.")
    G.write("Before he can say anything else someone calls everyone to attention.")
    Droxone_s = Droxone_s + 1
elif one_of_five is 2:
    G.write("For some reason, you walk over to the courpse, Nathik.")
    G.write("Maybe it's because you liked his joke.")
    G.write("Hello, sir?")
    head_necromancer.say("get1")
    G.write("Steve: Umm... Where am I and who do you think I am?")
    G.write("This brings an actual expression of shock to Nathik's face.")
    head_necromancer.say("get2")
    head_necromancer.say("get3")
    head_necromancer.say("get4")
    G.write("You keep you mouth shut. Nathik seems to be brooding now. You slowly walk away.")
    Nathik_s = Nathik_s + 1
elif one_of_five is 3:
    G.write("The older guy seems like the most aprotchable of the five.")
    G.write("The think his name is Tenaxx?")
    G.write("Hello... sir.")
    head_wizard.say("get1")
    G.write("Steve: I'm sorry sir, but I don't think I am who you think I am.")
    head_wizard.say("get2")
    head_wizard.say("get3")
    G.write("Tenaxx calls everyone over.")
    Tenaxx_s = Tenaxx_s + 1
elif one_of_five is 4:
    G.write("You walk over to the old lady. You can just run if she starts screaming again.")
    G.write("Hello Ma'am")
    head_witch.say("get1")
    G.write("Steve: I'm sorry, but I don't know who you think I am.")
    G.write("The woman looks at you through squinted eyes.")
    head_witch.say("get2")
    head_witch.say("get3")
    head_witch.say("get4")
    G.write("A witch? Those are real?")
    G.write("At this the Morena laughs.")
    head_witch.say("get5")
    G.write("Before you can say anything the oldest men of the five calls everyone over.")
    Morena_s = Morena_s + 1
elif one_of_five is 5:
    G.write("You get off the table and cautiously aproutch the horse person. What are they called again?")
    G.write("Really what are they called?")
    head_summoner.say("get1")
    G.write("He's got to be at least nine feet tall.")
    head_summoner.say("get2")
    head_summoner.say("get3")
    G.write("Steve: Uhhh.... What?")
    head_summoner.say("get4")
    G.write("Before you can say anything else, the old man calls everyone over.")
    Dredall_s = Dredall_s + 1
os.system('cls')
head_wizard.say("expo1")
head_wizard.say("expo2")
head_wizard.say("expo3")
G.write("Steve: There was a creepy cat, and I had cerial for breakfast.")
os.system('cls')
G.write("They all blink at you.")
head_alchemist.say("shock")
head_summoner.say("solution")
G.write("Dredall grabs you and you find your self on his back. You all walk out a side door and down a coridor.")
os.system('cls')
G.write("After a moment you walk into a large room with a clear floor. The walls are lined with weapons.")
head_summoner.say("weapon")
for i in range(len(weapon_choice)):
    stdout.write(str(i))
    stdout.write(": ")
    print(weapon_choice[i].name)

wc = int(input("What will you choice?"))
steve_inv.add_item(weapon_choice[wc], 1)
steve_inv.equip(weapon_choice[wc])
G.write(weapon_choice[wc].dscrpt)

if weapon_choice[wc].name is "War Hammer":
    head_summoner.say("warhammer")
    Dredall_s = Dredall_s + 1
elif weapon_choice[wc].name is "Wand":
    head_witch.say("wand")
    help = int(input("1: yes, 2: no"))
    if help is 1:
        G.write("You don't know how this works. Some help sounds like a great idea.")
        head_witch.say("(:")
        Morena_s = Morena_s + 1

    else:
        G.write("You aren't sure you trust her just yet.")
        head_witch.say("wait")
else:
    head_summoner.say("wrong_weapon")
head_summoner.say("train")
G.write("Steve: Does it have to be a master? Why not a beginner?")
G.write("Steve: Not that I don't know what I'm doing, which I totally do.")
G.write("Steve: I may be rusty.")
head_necromancer.say("rust")
G.write("It occurs to you that these people might not know the same sayings as you.")
os.system('clr')
G.write("Dredall leads a grizled looking man in leather armor over to you.")

first_battle = G.battle_manager()
first_battle.battle(steve, arms_master)
