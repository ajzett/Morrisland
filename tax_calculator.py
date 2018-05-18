from sys import path
path.append('./Gilbo-API/')
path.append('./Gilbo-API/deps/')
import Gilbo as G

#
# Objects #
#

# Ammo #
stamina = G.item('Stamina', "Your body's natural energy.", 0)
spray_can = G.item('Pepper Spray', 'A can of pepper spray.', 10)

# Buffs/Heals #
# Buffs
black_suit_buff = G.stat_item('Mysterious Orange Liquid', 'A mysterious orange liquid that was used by the Man in the Black Suit.', 1000, 10, 0, 25, 5, -10)
msg = G.stat_item('MSG', 'Super Salt. Seriously bad for you, but a seriously wild ride.', 5, 2, 0, 10, 0, 10)
# Add function to summon General Tso's chicken if consumed
tso_chicken = G.stat_item("General Tso's Chicken", "Nothing incites a fighting spirit like the effigy of General Tso's Chicken. Why did the General only have one?", 20, 3, 30)

# Heals
noodles = G.heal_item('Noodles', "A cup of Alton Brown's world-famous noodles.", 10, 10)
msg_noodles = G.heal_item('MSG Noodles', "Alton Brown's noodles, now with 150% more MSG. It seems to good to be true, so you'll probably pay for it later...", 2, 20)
lo_mein = G.heal_item('Lo Mein', "Alton Brown's signature Lo Mein. You'd slurp the noodles if he weren't watchinG.", 7, 15)
sushi_roll = G.heal_item('California Roll', 'California Roll hand-crafted by Alton Brown. You can smell the seacost.', 5, 5)

stim_pack = G.heal_item('Stim Pack', 'A stim pack issued by FBI agents that frequently see combat.', 500, 10)

# Debuffs
surprise_debuff = G.stat_item("Caught By Surprise", "Someone was caught by surprise and suffered the consequence.", 0, 1, -5, -5, -5, -7)
defense_down = G.stat_item ('Defense Down', "The bearer's defense has been lowered.", 0, 3, -5, 0, -10)
enrage_debuff = G.stat_item('Enraged', 'The bearer has been taunted, leaving them stronger, but also reckless.', 0, 2, 0, 10, -15, 5)
irritated_eyes = G.stat_item('Irritated Eyes', "The bearer's eyes have been irritated by some chemical, causing them to miss attacks and present openings in their defense.", 0, 2, 0, -6, -10)

# Attacks #
# For katana
quick_draw = G.ammo_attack('Quick Draw', 'Draw your sword from its sheath at lightning speed.', 5, stamina, 3, 100, surprise_debuff)
cross_slash = G.ammo_attack('Cross Slash', 'Quickly slash twice at your oppnent, weakening their defense.', 6, stamina, 1, 100, defense_down)
parry = G.attack('Parry', 'Parry an attack from your opponent, enraging them while leaving them defenseless.', 2, 100, enrage_debuff)
sword_dance = G.attack('Sword Dance', 'Weave around the enemy slicing so thinly it would appear to be a dance.', 8)

# For black belt
charge = G.attack('Charge', 'Charge towards the enemy with great force', 10)
flying_kick = G.attack('Flying Scissor Kick', 'Leap at the enemy with a Scissor Kick.', 20, 65)
high_kick = G.attack('High Kick', 'Lean back and kick high with your good leG.', 15, 85)
low_sweep = G.ammo_attack('Low Sweep', 'Sweep your leg and temporarily disarm the apponent.', 8, stamina, 1, 100, surprise_debuff)

# For pre-buff blacksuit
shin_kick = G.attack('Shin Kick', "Kick your opponent's shin.", 8)
pepper_spray = G.ammo_attack('Use Pepper Spray', "Shoot pepper spray into the eyes of your opponent.", 2, spray_can, 1, 90, irritated_eyes)
throw_chair = G.attack('Throw Chair', 'Grab a nearby chair and throw it at the opponent.', 25, 60)
punch = G.attack('Punch', 'Deliver a flurry of punches to your opponent.', 13, 90)

# For buffed blacksuit
bash = G.attack('Skull Bash', 'Bash your head into the oppnent.', 11)
throw_table = G.attack('Throw Table', 'Throw a table at your opponent.', 30, 45)

# Weapons #
# User Weapons
chop_sticks = G.weapon('Chop Sticks', 'A pair of chopsticks you had used to eat your meal. If you believe in yourself, who knows what might happen?', 1, [sword_dance, quick_draw, cross_slash, parry, charge, flying_kick, low_sweep, high_kick, punch, shin_kick, pepper_spray, throw_chair, bash, throw_table], 5, 5, 5, 5, 1) # generate random attack from ALL attacks defined
katana = G.weapon('Katana', 'A weapon proven deadly when used in the right hands. Catch your enemies by surprise, or just impress them with your collection.', 100, [sword_dance, quick_draw, cross_slash, parry], 5, 8, 0, 12) # status weapon
black_belt = G.weapon('Black Belt', 'A weapon worn around the waist. Grants user impeccable hand-to-hand combat ability. Or, supposedly, it could be used to towel-snap your opponent.', 5, [charge, flying_kick, low_sweep, high_kick], 10, 10, 5) # regular damage
# Boss Weapons
black_suit_prebuff = G.weapon("Agent's Arsenal", 'An array of items and techniques known and used by the FBI.', 1000, [punch, shin_kick, pepper_spray, throw_chair])
black_suit_buffed = G.weapon('Herculean Brawn', "After injection of a mysterious liquid, the FBI agent has turned into a terrifying bruiser.", 5000, [bash, punch, shin_kick, throw_table])

# Entity-related #

# Collections
user_collection = G.player_collection(50, [tso_chicken, lo_mein, msg_noodles, katana, chop_sticks, black_belt], [])
user_collection.add_item(noodles, 2)
user_collection.add_item(sushi_roll, 3)
user_collection.add_item(stamina, 2)

black_suit_collection = G.battler_collection(1000, [black_suit_prebuff, black_suit_buffed], [black_suit_prebuff])
black_suit_collection.add_item(stim_pack, 6)
# Stat Lists
user_stats = G.battler_stats(100, 10, 10, 10)
black_suit_stats = G.battler_stats(300, 12, 15, 10)

# Battlers
user = G.player('Ed', None, None, None, user_collection, user_stats)
black_suit = G.battler('The Man', None, None, None, black_suit_collection, black_suit_stats)

# NPCs
alton = G.NPC('Alton Brown', None, None, None)
alton.add_dialogue('thanks-for-tipping', f'"Thanks, {user.name}. It means a lot that you\'d support my small business.", says {alton.name}.')
alton.add_dialogue('law-run-in', f'"I\'ve had run-ins with the law before, {user.name}! I\'m not looking to do it again!"')

suit_narrator = G.NPC('The man in a black suit', None, None, None)
suit_narrator.add_dialogue('initial-encounter', '"Where do you think you\'re going?"')
suit_narrator.add_dialogue('tax-confront', "\"Thought you'd just be able to get away with evading taxes?\"")
suit_narrator.add_dialogue('avoid-this', ["\"Well, you might've been able to avoid taxes...\"", "\"but you won't be able to avoid this!\""])
suit_narrator.add_dialogue('use-buff', '"I was hoping it would\'t come to this..."')
suit_narrator.add_dialogue('the-plunge',  ["\n\n\"Command,\" he begins as a sly smile crosses his face,",  "\"this guy isn't cooperatinG.\"", "\"I'm going to use...", "the system.\"\n\n"])
suit_narrator.add_dialogue('spare-the-cash', '"You just couldn\'t spare the 9%, could you?"')

narrator = G.NPC('Narrator', None, None, None)
narrator.add_dialogue('get-user-name', 'What is your name?')
narrator.add_dialogue('describe-setting', ["You find yourself at \"Alton Brown's Noodle Shack\".", 'You come here once a month to stock up on noodle-related supplies, and --- as he so lovingly puts it --- "oriental wares".', '\n\nAlton has been so good to you for so long, you feel like you should tip him.', 'Will you tip?'])
narrator.add_dialogue('user-tipped', 'You decided to tip Alton. After all, he deserves it.')
narrator.add_dialogue('user-no-tip', ["You decided not to tip Alton. It would set a precedent, and you'd always have to tip from now on.", '\n\nHe lets out a slight look of disappointment, if even for a second.'])
narrator.add_dialogue('try-to-leave', ["You take your things and turn to leave. You take five steps before the door busts open with a gust of wind so powerful that it blows the curtains back at the other side of the restaurant.", 'A glare prevents you from seeing clearly, but you make out the shape of a man standing in the doorway.'])
narrator.add_dialogue('enemy-spotted', ['The figure steps forward, and the sun retreats behind it like water, revealing a man in a black suit.', 'You stare at each other as a deep silence falls upon the earth, like something seen in a classic Western movie.', 'You turn around, but Alton is nowhere to be seen.', 'Calling out, he responds from under the counter.'])
narrator.add_dialogue('back-to-reality', ['Your head snaps back from where Alton lay beneath the counter.', f'{suit_narrator.name} now faces you fists raised, ready to pounce.'])
narrator.add_dialogue('enemy-attacks', [f'{suit_narrator.name} runs forward towards you and takes a swing.', 'You drop to the ground in an effort to dodge.', 'He tries to kick you, but you roll away.', 'Adrenaline begins to pump through your veins as you desparately attempt being hit. You have nothing to defend yourself with.', '\n\nOn the ground, you notice three weapons that Alton stores under tables.', 'The oppurtunity to grab one arises.', 'Which do you choose?'])
narrator.add_dialogue('use-item', [f'A breafcase comes crashing through the roof. {black_suit.name} reaches up to catch it with perfect timing, as if it had happened a million times before.', "Out of the breafcase, he takes a needle containing a strange, orange liquid.", f"{black_suit.name} raises his hand to his ear and speaks into a small microphone."])
narrator.add_dialogue('the-plunge', ['You get a bad feeling as he flicks off his earpiece.', "You hear the buzzing of wild chatter from the man's earpiece, which now hangs from his shirt.", 'As he drains the liquid you stand transfixed as he swells into a grotesquely muscular creature.', "His suit tears with his newly increased size.", "\n\nThe very moment when you become grounded enough to run, he glares at you.", 'He grins.'])

#
# Functions #
#
def let_read():
    input('Press enter to continue')
    G.clr_console()

class dialogue_index(G.IntEnum):
    black_suit = 0
    alton = 1

dialogue = [0, None]

def advance_dialogue():
    dialogue[dialogue_index.black_suit] += 1
    let_read()

user_tipped = None
def bat_check(manager):
    if (katana in user.collection.equipped) or (chop_sticks in user.collection.equipped):
        user.collection.add_item(stamina)

    if (manager.percent_health(black_suit) < 90) and (dialogue == 0):
        write(["You call out to your opponent.", '"C\'mon man, do we really have to do this?"'])
        write(['"When did you get the impression that I was doing this because I', 'HAD', 'to?"', 'he chirps back.'])
        write(['"You do get paid to do this, right?', 'This has to be a paid job."'])
        write([f'{black_suit.name}\'s face suddenly displays an intense tranquility.', '\n\n"This...', 'this is divine penance!', 'Punishment for the worst of criminals!', 'I would never ask for money.'])
        advance_dialogue()
    elif (manager.percent_health(black_suit) < 70) and (dialogue == 1):
        write(['Despite your progress in battle, you attempt to plead with the man.', '\n\n"How is this a solution?"'])
        write(['"What is the alternative?', 'Getting away with tax avoidance?"'])
        write("You didn't even give me a chance to pay for it!")
        write('"Yeah, I\'ve heard that one before. \'I was just about to pay my taxes, IRS!\' It\'s a steaming load."')
        advance_dialogue()
    elif (manager.percent_health(black_suit) < 30) and (dialogue == 3):
        write('"It\'s about the terrorists."')
        write(["You're taken aback by that statement.", '\n\n"What?"'])
        write('"We use that money to fend off the terrorists," he continues.')
        write('"..and?"')
        write('"Choosing to avoid helping the fight against the terrorists is"', '\b...', 'terrorism itself!"')
        advance_dialogue()

    if manager.percent_health(black_suit) <= 50:
        if black_suit.entity_dict['used_buff'] is False:
            suit_narrator.say('use-item')
            narrator.say('use-item')
            suit_narrator.say('the-plunge')
            narrator.say('the-plunge')
            suit_narrator.say('spare-the-cash')
            let_read()
            black_suit.use_item(black_suit_buff)
            black_suit.equip(black_suit_buffed)
            black_suit.entity_dict['used_buff'] = True
        elif (black_suit.entity_dict['used_buff'] is True) and (dialogue == 2):
            write(["Let's say that I DID forget to pay tax.", 'What would forgetting one time matter?'])
            write(["It isn't just you, you see?", "It's everyone.", 'If everyone forgot to pay their taxes one time all together...', "it's unthinkable."])
            write(['"The Government can handle about $0.05 less one time from everyone in their lives,', 'can\'t they?"'])
            write(['"You\'re terminally shortsighted."'])
            advance_dialogue()

    for effect in manager.effect_dict['reverse_effect_player']:
        if effect[2] == "General Tso's Chicken":
            if effect[0] == manager.battle_dict['turn_counter'] + itm.duration - 1:
                write('The ghost of General Tso\'s chicken rises from the deep.\n')
            write('General Tso\'s chicken helps you by doing 15 damage to the enemy.')
            manager.hit_animate()
            black_suit.stats.health -= 15

    if (manager.percent_health(user) <= 50) and (user_tipped is True):
        if dialogue[dialogue_index.alton] is None:
            write(['Alton brown leaps out from behind the counter', '"\n\nI will defend this tipping customer!"', 'he says as a chair grazes the top of his head.', '"...from behind the counter!"'])
            dialogue[dialogue_index.alton] = 0

        write('Alton brown tosses mugs at the Man in the Black Suit, dealing 15 damage.')
        let_read()
        manager.hit_animate()
        black_suit.stats.health -= 15


def win():
    pass

def lose():
    pass

#
# Battle Managers
#
# Black belt
class base_bat_man(G.battle_manager):
    def player_win(self, plyr, enemy):
        # The player wins
        win()
    def player_lose(self, plyr, enemy):
        # The player loses
        lose()

class chop_bat_man(base_bat_man):
    def plyr_choose_attack(self, plyr):
        choices = []
        while True:
            choices = [self.randnum(len(plyr.attacks)), self.randnum(len(plyr.attacks))]
            if choices[0] != choices[1]:
                try:
                    plyr.attacks[choices[0]]
                    plyr.attacks[choices[1]]
                    break
                except IndexError:
                    pass

        print(f'\n1. {plyr.attacks[choices[0]].name}\n2. {plyr.attacks[choices[1]].name}')

        # Prompt user
        print('\nEnter a number to attack. \nType "info [number]" for more info about the attack.\nType "q" to return to the previous menu.')

        def replace_value(word):
            if (word == '0') or (word == 0):
                return choices[0]
            elif (word == '1') or (word == 1):
                return choices[1]

        while True:
            user_choice = input('\nChoice: ')

            try:
                # Determine action based on input
                if "info" in user_choice:
                    self.attack_info(plyr.collection.items, plyr.attacks[replace_value(int(user_choice.split(' ')[1]) - 1)])
                elif user_choice.lower() == 'q':
                    raise ChooseAgain
                else:
                    # Convert user_choice to indexable integer
                    user_choice = int(user_choice) - 1

                    try:
                        if plyr.attacks[replace_value(int(user_choice))].ammo_type in plyr.collection.items:
                            return plyr.attacks[replace_value(int(user_choice))]
                        else:
                            print("You don't have the correct item to use this attack.")
                    except AttributeError:
                        return plyr.attacks[replace_value(user_choice)]

            except (ValueError, IndexError, AttributeError):
                    print('Invalid input.')
#
# Main #
#
def main():
    print('Tax Calculator 2: The Audit\nWritten using Gilbo-API (© 2018 Adam Zett)\n')
    print('Skip dialogue?')

    dialogue = None
    while dialogue is None:
        user_choice = input('Yes or No: ')
        if user_choice.lower() == 'yes':
            dialogue = False
        elif user_choice.lower() == 'no':
            dialogue = True
        else:
            print('Invalid selection.')

    del user_choice

    G.clr_console()
    if dialogue is True:
        narrator.say('describe-setting')
        while user_tipped is None:
            user_choice = input('Yes or No: ')
            if user_choice.lower() == 'yes':
                user_tipped = True
                narrator.say('user-tipped')
                alton.say('thanks-for-tipping')
            elif user_choice.lower() == 'no':
                user_tipped = False
                narrator.say('user-no-tip')
            else:
                print('Invalid selection.')

            del user_choice

            let_read()
            narrator.say('try-to-leave')
            suit_narrator.say('initial-encounter')
            narrator.say('enemy-spotted')
            alton.say('law-run-in')

            let_read()
            suit_narrator.say('tax-confront')
            narrator.say('back-to-reality')
            suit_narrator.say('avoid-this')
            narrator.say('enemy-attacks')

    weapon_chosen = None

    if dialogue is False:
        print('Choose your weapon.')

    print(f"\n1. Katana\n-------------------\n'{katana.dscrpt}'")
    print(f"\n2. Black Belt\n-------------------\n'{black_belt.dscrpt}'")
    print(f"\n3. Chop Sticks\n-------------------\n'{chop_sticks.dscrpt}'")
    print('\nEnter a number to make your choice.')
    black_suit.entity_dict['used_buff'] = False

    while weapon_chosen is None:
        user_choice = input('\nChoice: ')
        if user_choice == '1':
            weapon_chosen = True
            print('\nSpecial effects: Stamina will regenerate once per turn to allow for the use of special attacks.')
            let_read()
            user.collection.equip(katana)
            bat_man = base_bat_man()
        elif user_choice == '2':
            weapon_chosen = True
            user.collection.equip(black_belt)
            bat_man = base_bat_man()
        elif user_choice == '3':
            weapon_chosen = True
            print('\nSpecial effects: Stamina will regenerate and two random attacks will be generated twice every turn, and the player can choose from one each time.\n')
            let_read()
            user.collection.equip(chop_sticks)
            user.collection.add_item(spray_can, 5)
            bat_man = chop_bat_man()
        else:
            print('Invalid input')

    spec_bat_check = bat_check(bat_man)
    bat_man.battle(user, black_suit, spec_bat_check)

if __name__ == '__main__':
    main()
