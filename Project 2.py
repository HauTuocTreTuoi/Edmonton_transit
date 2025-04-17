# ID 3157775
# Lab X13L - Bao Nguyen Doan

from graphics import *
from datetime import date
import pickle


#Menu
#################################################################
def menu() -> str:
    '''
purpose: print menu
parameter: none
return value: command
     '''    
    
    print()
    print('Edmonton Transit System')
    print('---------------------------------')
    print('(1) Load route data')
    print('(2) Load shapes data')
    print('(3) Load disruptions data')
    print()
    print('(4) Print shape IDs for a route')
    print('(5) Print coordinates for a shape ID')
    print('(6) Find longest shape for route')
    print()
    print('(7) Save routes and shapes in a pickle')
    print('(8) Load routes and shapes from a pickle')
    print()
    print('(9) Interactive map')
    print('(0) Quit')
    command = input("Enter Command: ")
    return command 


# clean data for option 1 and 2 (not work for 3)
#################################################################
def cleaned_data(file):
    '''
purpose: clean data(turn them into a list)
parameter: file
return value: clean data
     '''        
    f = open(file, 'r')
    label = f.readline()
    lines = f.read().strip('\n').split(",")
    cleaned_lines = []
    for i in lines:
        for x in i.split('\n'):
            cleaned_lines.append(x)   
    
    return cleaned_lines



# Helper function for option 1 
#################################################################
def store_route_name(cleaned_route):
    '''
purpose: store route name
parameter: cleaned route
return value: partial route data
     '''        
    route_id = []
    route_name = []
    
    for i in range (len(cleaned_route)):
        if i % 9 ==0:
            route_id.append(cleaned_route[i])
        if i % 9 ==3:
            route_name.append(cleaned_route[i])
            
    data = {}
    
    for i in range(len(route_id)):
        data.update({route_id[i]: 
                     {'route name':route_name[i],
                      'shape id':[]}})
                      
    return data



def store_shape_id(data,cleaned_trip):
    '''
purpose: store route 
parameter: data from store_route, cleaned trips.txt
return value: full route data
     '''        
    shape_id = []
    route_id = []
    for i in range (len(cleaned_trip)):
        if i % 9 ==6:
            shape_id.append(cleaned_trip[i])   
        if i % 9 ==0:
            route_id.append(cleaned_trip[i])  
            
    add_data = {}
    for i in range(len(route_id)):
        add_data.update({route_id[i]:[]})
    
    
    for i in range(len(route_id)):
        if shape_id[i] not in add_data[route_id[i]]:
            add_data[route_id[i]].append(shape_id[i])     
    for i in add_data:
            data[i]['shape id'] = add_data[i]    
        
    return data
            
# Helper function for option 2
#################################################################
def shapes_id(cleaned_shape):
    '''
purpose: store shape data
parameter: cleaned shape
return value: shape_data
     '''        
    
    shape_data = {}
    shape_id = []
    shape_pt_lat = []
    shape_pt_lon = []
    coords = []
    
    for i in range (len(cleaned_shape)):
        if i % 4 == 0:
            shape_id.append(cleaned_shape[i])
        if i % 4 == 1:
            shape_pt_lat.append(cleaned_shape[i])
        if i % 4 == 2:
            shape_pt_lon.append(cleaned_shape[i])
    
    for i in range(len(shape_pt_lat)):
        coord_i = (shape_id[i],shape_pt_lat[i],shape_pt_lon[i])
        coords.append(coord_i)    
    
    for i in range(len(coords)):
        shape_data.update({coords[i][0]:[]})
        
    for i in range(len(coords)):
            shape_data[coords[i][0]].append((coords[i][1],coords[i][2])) 
                
    return shape_data        
    
        


# Option 4
#################################################################
def search_route(data):
    '''
purpose: search route
parameter: route data
return value: none
     '''        
    route_choice = input("Enter route: ")
    if route_choice not in data:
        print(f'\t ** NOT FOUND **')    
    
    else:
        print(f"Shapes ids for route [{data[route_choice]['route name']}]")
        for i in range (len(data[route_choice]['shape id'])):
            print(f"\t {data[route_choice]['shape id'][i]}")
            

# Option 5
#################################################################
def search_coords(shape_data):
    '''
purpose: search coords
parameter: shape data
return value: none
     '''        
    shape_choice = input("Enter shape ID: ")
    if shape_choice not in shape_data:
        print(f'\t ** NOT FOUND **')    
        
    else:
        print(f'Shapes ids for {shape_choice} are')
        for i in range (len(shape_data[shape_choice])):
            print(f"\t {shape_data[shape_choice][i]}")
        
        
        
        #print(len(shape_data[shape_choice]))
        
    


# Option 3 
#################################################################
def load_disruption(disruptions):
    '''
purpose: load disruption data
parameter: filename
return value: date, disruption coords
     '''         
    final_date = []
    point = []
    f = open(disruptions, 'r')
    label = f.readline()
    lines = f.read().split('\n')
    #print(lines[0].split('POINT ('))
    
    for i in range(len(lines)):
        a = lines[i].split('"')
        b = lines[i].split('POINT ')
        for x in range(len(a)):
            if x % 7 == 5:
                final_date.append(a[x])
        for y in range(len(b)):
            if y % 2 == 1:
                point.append(b[y])
    
    
    final_final_date = []
    final_final_final_date = []
    for i in final_date:
        a = i.strip(',').split()
        
        final_final_date.append((a[0],a[1].strip(','),a[2]))
    
    
    for i in final_final_date:
        if i[0] == "Jan":
            x = 1
        elif i[0] == "Feb":
            x = 2
        elif i[0] == "Mar":
            x = 3    
        elif i[0] == "Apr":
            x = 4
        elif i[0] == "May":
            x = 5
        elif i[0] == "Jun":
            x = 6
        elif i[0] == "Jul":
            x = 7
        elif i[0] == "Aug":
            x = 8
        elif i[0] == "Sep":
            x = 9
        elif i[0] == "Oct":
            x = 10
        elif i[0] == "Nov":
            x = 11
        elif i[0] == "Dec":
            x = 12 
        
        final_final_final_date.append(date(int(i[2]), x, int(i[1])))
            
       
    print(final_final_final_date)
    return final_final_final_date, point
    
# Option 6
#################################################################                                
def find_longest_shape(shape_data, data):
    '''
purpose: find longest shape by coords
parameter: shape_data, data
return value: none
     '''         
    route_list = []
    count = []
    route_choice = input("Enter shape ID: ")
    if route_choice not in data:
        print(f'\t ** NOT FOUND **')    
        
    else:
        for i in range (len(data[route_choice]['shape id'])):
            route_list.append(data[route_choice]['shape id'][i])
    
        for i in route_list:
            count.append(len(shape_data[i]))
            chosen = max(count)
        for i in range(len(count)):
            if count[i] == chosen:
                print(f'The longest shape for {route_choice} is {route_list[i]} with {chosen} coordinates')
#find_longest_shape(shape_data, data1)


# Option 7 and 8  
#################################################################
def save_pickle(data, shape_data,date,point,pklfile):
    
    with open(pklfile, 'wb') as file_bin:
            pickle.dump((data, shape_data, date, point), file_bin)
            print(f"Data successfully written to data/{pklfile}")
    return pklfile
'''
purpose: save route and shape to pkl
parameter: route, shape, pkl filename
return value: pklfile
     '''        

def load_pickle(pklfile):
    
    file_bin = open(pklfile,'rb')
    data,shape,date,point = pickle.load(file_bin)
    print(f'Routes,shapes and disruptions Data structures successfully loaded from {pklfile}')
    return data,shape,date,point
     
'''
purpose: load data from pkl file
parameter: pklfile
return value: route data, shape data
     '''    


# Helper function for option 9 
#################################################################
def initialize(point)-> tuple:
    '''
purpose: draw window and initial points
parameter: disruption coords
return value: window, from,to entry
     '''         

    
    win = GraphWin('ETS Data', 800, 920)
    win.setCoords(-113.720049, 53.393703, -113.320418, 53.657116)

    
    edmonton_map = Image(Point(-113.5202, 53.525), "edmonton_map.png")
    edmonton_map.draw(win)

    
    from_text = Text(Point(-113.700, 53.637), "From:")
    from_text.setStyle('bold')
    to_text = Text(Point(-113.695, 53.628), "To:")
    to_text.setStyle('bold')

    
    from_entry = Entry(Point(-113.647, 53.637), 17)
    to_entry = Entry(Point(-113.647, 53.628), 17)
    from_entry.setFill('white')
    to_entry.setFill('white')

    
    search_button = Rectangle(Point(-113.686, 53.6125), Point(-113.625, 53.6221))
    search_button.setOutline('Black')
    search_button.setFill('green')
    search_text = Text(Point(-113.6575, 53.6175), "Search")
    search_text.setStyle('bold')
    
    
    quit_button = Rectangle(Point(-113.686, 53.5885), Point(-113.625, 53.5981))
    quit_button.setOutline('Black')
    quit_button.setFill('green')    
    quit_text = Text(Point(-113.6575, 53.5933), "Quit")
    quit_text.setStyle('bold')
   
    clear_button = Rectangle(Point(-113.686, 53.6005), Point(-113.625, 53.6101))
    clear_button.setOutline('Black')
    clear_button.setFill('green')
    clear_text = Text(Point(-113.6575, 53.6055), "Clear")
    clear_text.setStyle('bold')

    for i in point:
        x = i.strip('(').strip(')').split()
        circ = Circle(Point(float(x[0]),float(x[1])),0.0008)
        circ.setFill('red')
        circ.draw(win)
        
    
    
    from_text.draw(win)
    to_text.draw(win)
    from_entry.draw(win)
    to_entry.draw(win)
    search_button.draw(win)
    search_text.draw(win)
    clear_button.draw(win)
    clear_text.draw(win)
    quit_button.draw(win)
    quit_text.draw(win)


    return win,from_entry,to_entry
    

def choice(x):
    '''
purpose: get choice
parameter: mouse click coords
return value: choice
     '''         
    choice = ''
    if -113.686 <= x.getX() <= -113.625 and 53.6125<=x.getY()<=53.6221:
        choice = 'search'
    elif -113.686<= x.getX() <= -113.625 and 53.6005<=x.getY()<=53.6101:
        choice = 'clear'
    elif -113.686<= x.getX() <= -113.625 and 53.5885<=x.getY()<=53.5981:
        choice = 'quit'
    
    return choice

def store_striped_route_name(cleaned_route):
    '''
purpose: change the route name data to match the tuple created from entry
parameter: cleaned route data
return value: dictionary with route name as a tuple consist of from and to place
     '''         
    route_id = []
    route_name = []
    strip_rnl = []
    
    for i in range (len(cleaned_route)):
        if i % 9 ==0:
            route_id.append(cleaned_route[i])
        if i % 9 ==3:
            route_name.append(cleaned_route[i])
            
    for i in route_name:
        x = i.split('-')
        if len(x) == 2:
            strip_rnl.append((x[0].lower().strip('"').strip(),x[1].lower().strip('"').strip()))
        elif len(x) == 3:
            strip_rnl.append((x[0].lower().strip('"').strip(),x[2].lower().strip('"').strip()))
        elif len(x) == 4:
            strip_rnl.append((x[0].lower().strip('"').strip(),x[3].lower().strip('"').strip()))
        elif len(x) == 1:
            #strip_rnl.append(x[0])
            a = x[0].split('via')
            
            if len(a) == 2:
                strip_rnl.append((a[0].lower().strip('"').strip(),a[1].lower().strip('"').strip()))
            else:
                b = a[0].split(' to ')
                if len(b) == 2:
                    strip_rnl.append((b[0].lower().strip('"').strip(),b[1].lower().strip('"').strip()))
                else:
                    strip_rnl.append(b[0].lower().strip('"').strip())
        
    strip_search_data = {}
    
    for i in range(len(route_id)):
        strip_search_data.update({route_id[i]: 
                     {'route name':strip_rnl[i],
                      'shape id':[]}}) 
    
    
    return strip_search_data
        
    
    
def get_search(from_location,to_location):
    '''
purpose: merge from and to entry
parameter: from, to entry from initialize
return value: user entry in tuple
     '''         
    if from_location == '':
        route_name = to_location.lower().strip()
    elif to_location == '':
        route_name = from_location.lower().strip()
    else:
        route_name = (from_location.lower().strip(), to_location.lower().strip()) 
    return route_name


def search(noti, win, route_name, shape_data, full_striped_data):
    '''
purpose: draw route when user click search
parameter: blank notification, window, route entry, route shape, data that match the type of user entry)
return value: return notification(just for notification reset purpose)
     '''         
    x = []
    count = 0
    y = ''
    
    if noti != '':
        noti.undraw()  

    route_name_list = []
    for i in full_striped_data:
        route_name_list.append(full_striped_data[i]['route name'])
    
    
    
    
    
    if route_name in route_name_list:
        for i in full_striped_data:
            if route_name == full_striped_data[i]['route name']:
                y = i
        
                
        
        new_noti = Text(Point(-113.6575, 53.5830), f'Drawing route {y}')
        new_noti.setStyle('bold')
        new_noti.setSize(17)
        new_noti.draw(win)
        noti = new_noti  
        x = full_striped_data[y]['shape id']
        
        
        for a in x:
            for o in range(len(shape_data[a])):
                x_cen = float(shape_data[a][o][1])
                y_cen = float(shape_data[a][o][0])
                
                circ = Circle(Point(x_cen, y_cen), 0.00005)
                circ.setFill('Blue')
                circ.draw(win)
        
    
    else:
        noti = Text(Point(-113.6575, 53.5830), 'NOT FOUND')
        noti.setStyle('bold')
        noti.setSize(17)
        noti.draw(win)
    
    
    return noti


def interactive_map(point,full_striped_data,shape_data):
    '''
purpose: gather helper function
parameter: disruption coords, striped data, route shape)
return value: none
     '''         
    win,from_entry,to_entry = initialize(point)
    notif = ''
    while True:
        x = win.getMouse()
        a = choice(x)

        if a == 'search':
            from_location = from_entry.getText()
            to_location = to_entry.getText()      
            route_name = get_search(from_location,to_location)
            notif = search(notif,win,route_name,shape_data,full_striped_data)
        elif a == 'clear':
            notif.undraw()
            from_entry.setText("")  
            to_entry.setText("")    
        elif a == 'quit':
            win.close()
            break
              
            
        
    
    


'''cleaned_route = cleaned_data('routes.txt')
cleaned_trip = cleaned_data('trips.txt')

data1 = store_route_name(cleaned_route)
data = store_shape_id(data1,cleaned_trip)
print(data)
cleaned_shape = cleaned_data("shapes.txt")
shape_data = shapes_id(cleaned_shape)

point = load_disruption(disruptions)[1]   
win,from_location,to_location,x = initialize(point)
strip_search_data = store_striped_route_name(cleaned_route)

full_striped_data = store_shape_id(strip_search_data,cleaned_trip)
print(full_striped_data)
#search(win,from_location,to_location,shape_data,full_striped_data)
choice = choice(x)
interactive_map(choice,point)
'''



def main() -> None:
    '''
purpose: main function
parameter: none
return value: none
     '''        
    command = menu()
    check1 = 0
    check2 = 0
    data = ''
    shape_data = ''
    point = ''
    while True:
        
        if command == '1':
            
            
            file_name = input("Enter a filename: ")
            if file_name == "":
                file_name = "trips.txt"
            try:
                cleaned_trip = cleaned_data(file_name)
                cleaned_route = cleaned_data('routes.txt')
                ini_data = store_route_name(cleaned_route)
                data = store_shape_id(ini_data,cleaned_trip)
                #print(data)
                print(f'Data from data/{file_name} loaded')
                
            except FileNotFoundError:
                print(f"IOError: Couldn't open {file_name}")
            
            #print(data)
                   
        elif command == '2':
            file_name = input("Enter a filename: ")
            if file_name == "":
                file_name = "shapes.txt"
            try:
                cleaned_shape = cleaned_data(file_name)
                shape_data = shapes_id(cleaned_shape)
                #print(shape_data)
                print(f'Data from data/{file_name} loaded')
            except FileNotFoundError:
                print(f"IOError: Couldn't open {file_name}")
                      
            
            
        elif command == '3':
            file_name = input("Enter a filename: ")
            if file_name == "":
                file_name = "traffic_disruptions.txt"
            try:
                date, point = load_disruption(file_name)
                print(f'Data from data/{file_name} loaded')
                
            except FileNotFoundError:
                print(f"IOError: Couldn't open {file_name}")
        elif command == '4':
            if data == '':
                print("Route data hasn't been loaded yet")
            else:
                search_route(data)           
        elif command == '5':
            if shape_data == '':
                print("Shape ID data hasn't been loaded yet")
            else:
                search_coords(shape_data)          
       
        elif command == '6':
            if shape_data != '' and data != '':
                find_longest_shape(shape_data, data)  
            else:
                print("Route or shape data hasn't been loaded yet")
        
        elif command == '7':
            if data == '' or shape_data == '' or point == '':
                print("Route, shape or disruptions data hasn't been loaded yet")
            else:
                pklfile = input("Enter a filename: ")
                if pklfile == "":
                    pklfile = "etsdata.p" 
                saved_file = save_pickle(data, shape_data,date,point,pklfile) 
                
                      
        elif command == '8':
        
                pklfile = input("Enter a filename: ")
                if pklfile == '':
                    pklfile = 'etsdata.p'
                try:
                    data, shape_data, date, point = load_pickle(pklfile)
                except FileNotFoundError:
                    print(f"IOError: Couldn't open {pklfile}")                
            
                
                           
        elif command == '9':
            
            cleaned_trip = cleaned_data('trips.txt')
            cleaned_route = cleaned_data('routes.txt')            
            strip_search_data = store_striped_route_name(cleaned_route)
            
            full_striped_data = store_shape_id(strip_search_data,cleaned_trip)            
            interactive_map(point,full_striped_data,shape_data) 
        
        elif command == '0':
            break
        else:
            print("Invalid Option")
            
        
        command = menu()   

main()
