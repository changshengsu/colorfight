from colorfight import Colorfight
import time
import random
from colorfight.constants import BLD_GOLD_MINE, BLD_ENERGY_WELL, BLD_FORTRESS

# Create a Colorfight Instance. This will be the object that you interact
# with.
game = Colorfight()

# Connect to the server. This will connect to the public room. If you want to
# join other rooms, you need to change the argument
game.connect(room = 'public4')

# game.register should return True if succeed.
# As no duplicate usernames are allowed, a random integer string is appended
# to the example username. You don't need to do this, change the username
# to your ID.
# You need to set a password. For the example AI, the current time is used
# as the password. You should change it to something that will not change 
# between runs so you can continue the game if disconnected.




if game.register(username = 'at&t', \
        password = '123'):
    # This is the game loop
    while True:
        # The command list we will send to the server
        cmd_list = []
        # The list of cells that we want to attack
        my_attack_list = []
        # update_turn() is required to get the latest information from the
        # server. This will halt the program until it receives the updated
        # information. 
        # After update_turn(), game object will be updated.   
        game.update_turn()

        # Check if you exist in the game. If not, wait for the next round.
        # You may not appear immediately after you join. But you should be 
        # in the game after one round.
        if game.me == None:
            continue

        me = game.me

        attackingList = []
        i = 0
        class okCell:
            def __init__(self, pos, attack_cost):
                self.pos = pos
                self.age = age

        # game.me.cells is a dict, where the keys are Position and the values
        # are MapCell. Get all my cells.

        for cell in game.me.cells.values():
            # Check the surrounding position

            if cell.building.can_upgrade and \
                cell.building.is_home and \
                cell.building.upgrade_gold < me.gold and \
                cell.building.upgrade_energy < me.energy:
                    cmd_list.append(game.upgrade(cell.position))
                    print("We upgraded ({}, {})".format(cell.position.x, cell.position.y))
                    me.gold   -= cell.building.upgrade_gold
                    me.energy -= cell.building.upgrade_energy

            if cell.building.can_upgrade and \
                    (cell.building.is_home or cell.building.level < me.tech_level) and \
                    cell.building.upgrade_gold < me.gold and \
                    cell.building.upgrade_energy < me.energy:
                cmd_list.append(game.upgrade(cell.position))
                print("We upgraded ({}, {})".format(cell.position.x, cell.position.y))
                me.gold   -= cell.building.upgrade_gold
                me.energy -= cell.building.upgrade_energy
            
            if cell.owner == me.uid and cell.building.is_empty and me.gold >= 100 and me.tech_level == 2:
                #building = random.choice([BLD_FORTRESS, BLD_GOLD_MINE, BLD_ENERGY_WELL])
                if cell.natural_gold > cell.natural_energy:
                    building = BLD_GOLD_MINE
                else:
                    building = BLD_ENERGY_WELL
                cmd_list.append(game.build(cell.position, building))
                print("We build {} on ({}, {})".format(building, cell.position.x, cell.position.y))
                me.gold -= 100

            if cell.owner == me.uid and cell.building.is_empty and me.gold >= 100 and me.tech_level == 3:
                #building = random.choice([BLD_FORTRESS, BLD_GOLD_MINE, BLD_ENERGY_WELL])
                building = BLD_ENERGY_WELL
                cmd_list.append(game.build(cell.position, building))
                print("We build {} on ({}, {})".format(building, cell.position.x, cell.position.y))
                me.gold -= 100
            if cell.owner == me.uid and cell.building.is_empty and me.gold >= 100 and me.tech_level == 3:
                #building = random.choice([BLD_FORTRESS, BLD_GOLD_MINE, BLD_ENERGY_WELL])
                building = BLD_GOLD_MINE
                cmd_list.append(game.build(cell.position, building))
                print("We build {} on ({}, {})".format(building, cell.position.x, cell.position.y))
                me.gold -= 100


        #for cell in game.me.cells.values():
            # Check the surrounding position
            
         #   for pos in cell.position.get_surrounding_cardinals():
                # Get the MapCell object of that position
          #      c = game.game_map[pos]

           #     attackingList.append(c)
            #    attackingList.sort( key = lambda x: x.attack_cost)


        #for i in range(0,len(attackingList)):
         #   if attackingList[i].attack_cost < me.energy and attackingList[i].owner != game.uid \
          #      and attackingList[i].position not in my_attack_list:
            
           #     cmd_list.append(game.attack(attackingList[i].position,attackingList[i].attack_cost))
            #    print("We are attacking ({}, {}) with {} energy".format(pos.x, pos.y, c.attack_cost))
             #   game.me.energy -= c.attack_cost
              #  my_attack_list.append(c.position)
                

        for cell in game.me.cells.values():
            # Check the surrounding position
            
            for pos in cell.position.get_surrounding_cardinals():
                # Get the MapCell object of that position
                c = game.game_map[pos]
                

                 


                if c.attack_cost < me.energy and c.owner != game.uid \
                        and c.position not in my_attack_list and cell.is_empty == False:# \
                       # and len(me.cells) < 95:
                    
                    cmd_list.append(game.attack(pos, c.attack_cost))
                    print("We are attacking ({}, {}) with {} energy".format(pos.x, pos.y, c.attack_cost))
                    game.me.energy -= c.attack_cost
                    my_attack_list.append(c.position)

                if c.attack_cost < me.energy and c.owner != game.uid \
                        and c.position not in my_attack_list and me.tech_level==2:# \
                       # and len(me.cells) < 95:
                    
                    cmd_list.append(game.attack(pos, c.attack_cost))
                    print("We are attacking ({}, {}) with {} energy".format(pos.x, pos.y, c.attack_cost))
                    game.me.energy -= c.attack_cost
                    my_attack_list.append(c.position)

            
            # If we can upgrade the building, upgrade it.
            # Notice can_update only checks for upper bound. You need to check
            # tech_level by yourself. 
           # if cell.building.can_upgrade and \
            #        (cell.building.is_home or cell.building.level < me.tech_level) and \
             #       cell.building.upgrade_gold < me.gold and \
              #      cell.building.upgrade_energy < me.energy:
               # cmd_list.append(game.upgrade(cell.position))
                #print("We upgraded ({}, {})".format(cell.position.x, cell.position.y))
                #me.gold   -= cell.building.upgrade_gold
                #me.energy -= cell.building.upgrade_energy

            
                
            

            if cell.owner == me.uid and cell.building.is_empty and me.gold >= 100 and len(me.cells) < 100:
                #building = random.choice([BLD_FORTRESS, BLD_GOLD_MINE, BLD_ENERGY_WELL])
                building = BLD_ENERGY_WELL
                cmd_list.append(game.build(cell.position, building))
                print("We build {} on ({}, {})".format(building, cell.position.x, cell.position.y))
                me.gold -= 100
            if cell.owner == me.uid and cell.building.is_empty and me.gold >= 100 and len(me.cells) > 100 and len(me.cells) < 125:
                #building = random.choice([BLD_FORTRESS, BLD_GOLD_MINE, BLD_ENERGY_WELL])
                building = BLD_GOLD_MINE
                cmd_list.append(game.build(cell.position, building))
                print("We build {} on ({}, {})".format(building, cell.position.x, cell.position.y))
                me.gold -= 100
            
        
        # Send the command list to the server
        result = game.send_cmd(cmd_list)
        print(result)
