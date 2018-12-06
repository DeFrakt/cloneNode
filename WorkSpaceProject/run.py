#######WorkSpan HomeWork Question 2###########
###############Steven Yaussi##################
######Python 3.6.4 - run.py to execute #######

#Import modules
from command_line import *
from functions import *

#find entity from commandline
entity_to_clone = find_entity(id_clone, master_entity)
#clone entity with new ID & input to master entity
max_id = max_ID(master_entity)
#if no clone is found, stop output file
stop_output = clone_entity(entity_to_clone, max_id, master_entity, link_key, cloned)

#find related links
link_number_arr = find_links_to(id_clone, master_entity, link_key)
#loop thru all found 'from' links 
for arr_number in range(len(link_number_arr)):
    print("Start Link Num Arr", len(link_number_arr))    
    print("Link Number", link_number_arr[arr_number])
    #find next Max entity_id
    max_id = max_ID(master_entity)
    #find entity
    entity_to_clone = find_entity(link_number_arr[arr_number], master_entity)
    #clone entity with new ID
    clone_entity(entity_to_clone, max_id, master_entity, link_key, cloned)

    #find related child links
    link_number_arr_child = find_links_to(link_number_arr[arr_number], master_entity, link_key)
    for arr_number_child in range(len(link_number_arr_child)):   
        print("Link Number Child", link_number_arr_child[arr_number_child])
        #find child entity
        entity_to_clone = find_entity(link_number_arr_child[arr_number_child], master_entity)
        #clone child entity with new ID
        max_id = max_ID(master_entity)
        clone_entity(entity_to_clone, max_id, master_entity, link_key, cloned)
        #add link number to check for link & childs
        link_number_arr.append(link_number_arr_child[arr_number_child])
        print ("Updated Link Arr",link_number_arr)

#find related Parent links
find_links_from(id_clone, master_entity, link_key)

#clone all found links w/ new ID's
for clone_link in link_key['found_links']:
        clone_links(master_entity, link_key, clone_link)

#export file as .txt, JSON format
if(stop_output == False):
        with open('cloned_entities.json', 'w') as outfile:  
                json.dump(master_entity, outfile)
                print("JSON File Output")

print("\nMaster ", master_entity, "\n")
# print("Master Link Key ", link_key)
# print("Master Clone Key ", cloned)


