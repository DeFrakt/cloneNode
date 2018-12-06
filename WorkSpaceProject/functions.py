#Import modules
import json
import copy

#Adding Entity
def add_entity(data):
    #convert JSON to dictionary:
    try:
        entity = json.loads(data)
        print("Initial JSON file input")
        print("*"*40)
        print(entity,"\n")
        return entity
    except ValueError as error:
        print("Invalid JSON data: %s" % error)

#Find entity
def find_entity(id_num, master_entity):    
        for value in master_entity['entities']:
                if(value['entity_id'] == id_num):
                        print("Found:",value)
                        return value
               
#Find related links 'to'
def find_links_to(id_num, master_entity, link_key):
    found_links = []
    for value in master_entity['links']:
        if(value['from'] == id_num):
                #gather 'to' ID to cross check other 'from'
                link_check = value['to'] 
                found_links.append(link_check)
                print("Found Related Links From:",value, "\n")
                #add to Master Link key        
                link_key['found_links'].append(value)      
    return found_links

#Find related links 'from'
def find_links_from(id_num, master_entity, link_key):
    found_links = []
    for value in master_entity['links']:
        if(value['to'] == id_num):
                #gather 'to' ID to cross check other 'to'
                link_check = value
                found_links.append(link_check)
                print("Found Related Links To:",value, "\n")
                #add to Master Link key        
                link_key['found_links'].append(value)      

#Find Max ID
def max_ID(dictionary):
    max = 0
    for value in dictionary['entities']:
        v = value['entity_id']
        if(v > max):
                max = v
    return max
              
#Clone entity
def clone_entity(entity, number, master_entity, link_key, cloned):
        if(entity):
                #check if entity has been cloned, exit if so
                for clone_id in cloned:
                        if(entity['entity_id'] == clone_id):
                                return False
                #add key for links
                link_key['key'].append({'original': entity['entity_id'], 'new':number + 2})
                #clone entity - max number id + 2
                new_entity = copy.deepcopy(entity)      
                new_entity['entity_id'] = number + 2
                #add back to Master Entity
                master_entity['entities'].append(new_entity)
                #add cloned entity to master cloned array
                cloned.append(entity['entity_id'])
                print("New Entity Added:", new_entity, "\n")
                return False
        else:
                return True   

#Create link
def clone_links(master_entity, link_key, clone_link):
        if(clone_link):
                #copy link
                new_link = copy.deepcopy(clone_link)
                #loop thru found links
                for key in link_key['key']:
                        # cross check new ID & copy
                        if(key['original'] == clone_link['from']):
                                new_link['from'] = key['new']
                        if(key['original'] == clone_link['to']):
                                new_link['to'] = key['new']
                print("Cloned Link: ", new_link)      
                # add back to Master Entity
                master_entity['links'].append(new_link)
               
    
        