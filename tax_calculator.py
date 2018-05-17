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
lo_mein = G.heal_item('Lo Mein', "Alton Brown's signature Lo Mein. You'd slurp the noodles if he weren't watching.", 7, 15)
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
high_kick = G.attack('High Kick', 'Lean back and kick high with your good leg.', 15, 85)
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
user_collection = G.player_collection(50, [tso_chicken, lo_mein, msg_noodles], [])
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
black_suit = G.battler('The Man in the Black Suit', None, None, None, black_suit_collection, black_suit_stats)

# NPCs
alton = G.NPC('Alton Brown', None, None, None)
alton.add_dialogue('thanks-for-tipping', f'"Thanks, {user.name}. It means a lot that you\'d support my small business.", says {alton.name}.')
alton.add_dialogue('law-run-in', f'"I\'ve had run-ins with the law before, {user.name}! I\'m not looking to do it again!"')

suit_narrator = G.NPC('The man in a black suit', None, None, None)
suit_narrator.add_dialogue('initial-encounter', '"Where do you think you\'re going?"')
suit_narrator.add_dialogue('tax-confront', "\"Thought you'd just be able to get away with evading taxes?\"")
suit_narrator.add_dialogue('avoid-this', ["\"Well, you might've been able to avoid taxes...\"", "\"but you won't be able to avoid this!\""])
suit_narrator.add_dialogue('use-buff', '"I was hoping it would\'t come to this..."')

narrator = G.NPC('Narrator', None, None, None)
narrator.add_dialogue('get-user-name', 'What is your name?')
narrator.add_dialogue('describe-setting', ["You find yourself at \"Alton Brown's Noodle Shack\".", 'You come here once a month to stock up on noodle-related supplies, and --- as he so lovingly puts it --- "oriental wares".', '\n\nAlton has been so good to you for so long, you feel like you should tip him.', 'Will you tip?'])
narrator.add_dialogue('user-tipped', 'You decided to tip Alton. After all, he deserves it.')
narrator.add_dialogue('user-no-tip', ["You decided not to tip Alton. It would set a precedent, and you'd always have to tip from now on.", '\n\nHe lets out a slight look of disappointment, if even for a second.'])
narrator.add_dialogue('try-to-leave', ["You take your things and turn to leave. You take five steps before the door busts open with a gust of wind so powerful that it blows the curtains back at the other side of the restaurant.", 'A glare prevents you from seeing clearly, but you make out the shape of a man standing in the doorway.'])
narrator.add_dialogue('enemy-spotted', ['The figure steps forward, and the sun retreats behind it like water, revealing a man in a black suit.', 'You stare at each other as a deep silence falls upon the earth, like something seen in a classic Western movie.', 'You turn around, but Alton is nowhere to be seen.', 'Calling out, he responds from under the counter.'])
narrator.add_dialogue('back-to-reality', ['Your head snaps back from where Alton lay beneath the counter.', f'{suit_narrator.name} now faces you fists raised, ready to pounce.'])
narrator.add_dialogue('enemy-attacks', [f'{suit_narrator.name} runs forward towards you and takes a swing.', 'You drop to the ground in an effort to dodge.', 'He tries to kick you, but you roll away.', 'Adrenaline begins to pump through your veins as you desparately attempt being hit. You have nothing to defend yourself with.', '\n\nOn the ground, you notice three weapons that Alton stores under tables.', 'The oppurtunity to grab one arises.', 'Which do you choose?'])
narrator.add_dialogue('use-item', 'PLACEHOLDER')

#
# Functions #
#
def let_read():
    input('Press enter to continue')
    G.clr_console()

def bat_check():
    if black_suit.stats.health <= 50:
        suit_narrator.say('use-item')
        narrator.say('use-item')
        black_suit.use_item(black_suit_buff)
        black_suit.equip(black_suit_buffed)

def win():
    pass

def lose():
    pass

#
# Battle Managers
#
# Black belt
class belt_bat_man(G.battle_manager):
    def player_win:
        win()

    def player_lose:
        lose()

class katana_bat_man(belt_bat_man):
    def battle(self, plyr, enemy, spec_effect=None):
        self.determine_first_turn(plyr, enemy)

        while (plyr.stats.health > 0) and (enemy.stats.health > 0):
            # Allow player to read before clearing screen

            # Check to make sure no effects are active that shouldn't be
            self.refresh_active_effect(plyr, enemy)

            # Run the spec_effect if there is one specified
            if spec_effect is not None:
                spec_effect()

            # Increase turn counter
            self.battle_dict['turn_counter'] += 1

            # Check if player is attacking or defending
            try:
                temp_power = 1
                # Determine whose turn it is
                if self.battle_dict['turn'] == Turn.Attack:
                    plyr.add_item(stamina, 1)
                    def active_debuff_check():
                        if (self.effect_dict['reverse_effect_player'] != []) or (self.effect_dict['reverse_effect_enemy'] != []):
                            return True
                        else:
                            return False

                    while True:
                        try:
                            # Clear console and then redraw HP
                            self.draw_hp(plyr, enemy)

                            print("\n1. Attack\n2. Use Item")

                            if active_debuff_check() is True:
                                print("3. Status Effects")

                            print("Enter a number to select an option.")

                            user_choice = input("\nChoice: ")

                            if user_choice == '1':
                                # Player chooses to attack #
                                # Determine attack and use it
                                self.draw_hp(plyr, enemy)

                                self.switch_turn([temp_power, plyr.stats.power], self.use_attack(plyr, enemy, self.plyr_choose_attack(plyr)))
                            elif user_choice == '2':
                                # Player choose to use an item #
                                self.draw_hp(plyr, enemy)
                                self.switch_turn([temp_power, plyr.stats.power], self.use_item(plyr, self.plyr_choose_item(plyr)))
                            elif (user_choice == '3') and (active_debuff_check() is True):
                                self.draw_hp(plyr, enemy)
                                self.stat_change_writeout()
                            else:
                                input('Invalid input.')
                        except ChooseAgain:
                            pass

                if self.battle_dict['turn'] == Turn.Defend:
                    while True:
                        enemy_choice = self.randnum(100)
                        # Test if enemy uses item
                        if enemy_choice <= self.chance_item(enemy):
                            self.switch_turn([temp_power, enemy.stats.power], self.enemy_use_item(enemy))
                        else:
                            # Attack
                            self.switch_turn([temp_power, enemy.stats.power], self.use_attack(enemy, plyr, self.enemy_determine_attack(enemy)))

            except TurnComplete:
                input('\nPress enter to continue.')
                pass

        if plyr.stats.health > 0:
            self.player_win(plyr, enemy)
        else:
            self.player_lose(plyr, enemy)

class chop_bat_man(katana_bat_man):
    def plyr_choose_attack:
        while True:
            choices = [self.randnum(len(plyr.attacks)), self.randnum(len(plyr.attacks))]
            if choices[0] != choices[1]:
                break

        # Prompt user
        print('\nEnter a number to attack. \nType "info [number]" for more info about the attack.\nType "q" to return to the previous menu.')
        while True:
            user_choice = str(input('\nChoice: '))
            try:
                # Determine action based on input
                if "info" in user_choice:
                    self.attack_info(plyr.collection.items, plyr.attacks[int(user_choice.split(' ')[1]) - 1])
                elif user_choice.lower() == 'q':
                    raise ChooseAgain
                else:
                    # Convert user_choice to indexable integer
                    user_choice = int(user_choice) - 1

                    try:
                        if plyr.attacks[user_choice].ammo_type in plyr.collection.items:
                            return plyr.attacks[user_choice]
                        else:
                            print("You don't have the correct item to use this attack.")
                    except AttributeError:
                        return plyr.attacks[user_choice]

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
        user_tipped = None
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

    weapon_choice = None

    if dialogue is False:
        print('Choose your weapon.')

    while weapon_choice is None:
        print(f"\n1. Katana\n-------------------\n'{katana.dscrpt}'")
        print(f"\n2. Black Belt\n-------------------\n'{black_belt.dscrpt}'")
        print(f"\n3. Chop Sticks\n-------------------\n'{chop_sticks.dscrpt}'")
        print('\nEnter a number to make your choice.')
        weapon_choice = input('\nChoice: ')

        if weapon_choice == '1':
            user.equip(katana)
            katana_bat_man.battle(user, black_suit, bat_check)
        elif weapon_choice == '2':
            print('Special effects: Stamina will regenerate once per turn to allow for the use of special attacks.')
            let_read()
            user.equip(black_belt)
            belt_bat_man.battle(user, black_suit, bat_check)
        elif weapon_choice == '3':
            print('Special effects: Stamina will regenerate and two random attacks will be generated twice every turn, and the player can choose from one each time.')
            let_read()
            user.equip(chop_sticks)
            user.add_item(spray_can, 5)
            chop_bat_man.battle(user, black_suit, bat_check)
        else:
            print('Invalid input')

if __name__ == '__main__':
    main()
