#!/usr/bin/python3

def search_replace(my_list, search, replace):
    while True:
        try:
            x = my_list.index(search)
            my_list[x] = replace
        except ValueError:
            return my_list
        except:
            return None

