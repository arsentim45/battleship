class ship(self,bow,horizontal,length,hit):
    self.bow = bow
    self.horizontal = horizontal
    self.length = length
    self.hit = hit
    #self.tuple = [(bow,horizontal) for i in range(length)]
    ships_list = []
    def __init__(bow,horizontal,length,ships_list,k):
        if horizontal == True:
            for i in range(length):
                ships_list.append((bow[0],bow[1]+i))
                unhited.append((bow[0],bow[1]+i))
        else:
            for i in range(length):
                ships_list.append((bow[0]+i, bow[1]))
                unhited.append((bow[0]+1, bow[1]))
        if k == 1:
            return ships_list
        else:
            return unhited
    ships_list = __init__(bow,horizontal,length,ships_list,1)
    unhited = __init__(bow,horizontal,length,ships_list,2)
    def shoot_at(tuple,ships_list,unhited):
        if tuple in ships_list:
            unhited.del(tuple)
        else:
            print('Mumo')


class field(self,ships):
    self.ships = ships

    def __init__(k):
        for i in range(k):
            for j in range(k):
                full_field.append((i,j))
                if (i,j) not in ships_list:
                    bool_field.append('False')
                else:
                    bool_field.append('True')


    def shoot_at(tuple):
        if tuple in ships_list:
            bool_field[i-1+j] = 'X'
            unhited.remove(tuple)
        else:
            bool_field[i - 1 + j] = 'x'
        return bool_field

    bool_field = shoot_at(tuple)
    
    def field_without_ships(bool_field):
        for i in range(len(bool_field)):
            if bool_field[i] == 'x' or bool_field[i] == 'X':
                shootings_coordinates.append((i//10+1,i%10))
        return shooting_coordinates

    def field_with_ships():

class player(self,name):
    self.name = name

    def __init__(name):

    def read_position():

class game(self,field,players,current_player):
    self.field = filed
    self.players = players
    self.current_player = current_player

    def __init__():

    def read_position():

    def field_without_ships(index):

    def field_with_ships():

