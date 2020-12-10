# import importlib
# import functions
# importlib.reload(functions)

def find_by_name(string):
    """
     Takes in a string that represents the name of an album.
     Should return a dictionary with the correct album, or return None
    """
    for d in info_lst:
        if d['album'] == string:
            return dict(d)
    return ("There is no album with name: '{}'").format(string)


def find_by_rank(rank):
    """
    Takes in a number that represents the rank in the list of top albums
    and returns the album with that rank. If there is no album with that rank, it returns None
    """
    for d in info_lst:
        if int(d['number']) == rank:
            return dict(d)
    return ("There is no Album with rank: '{}'").format(rank)

def find_by_year(year):
    """
    Takes in a number for the year in which an album was released and returns a list of
    albums that were released in that year. If there are no albums released in the given
    year, it returns an empty list.
    """
    lst_of_albums = []
    
    for d in info_lst:
        if int(d['year']) == year:
            lst_of_albums.append(d['album'])
            
    return lst_of_albums

def find_by_years(start_year,end_year):
    """
    Find by years - Takes in a start year and end year.
    Returns a list of all albums that were released on or between the start
    and end years. If no albums are found for those years, then an empty list is returned.
    
    params :start_year - smaller year
            end_year - bigger year
    """
    lst_of_albums = []
    
    for d in info_lst:
        if (int(d['year'])<=end_year ) and (int(d['year'])>=start_year):
            lst_of_albums.append(d['album'])
    
    return lst_of_albums

def find_by_ranks(rank_1,rank_2):
    """
    Takes in a start rank and end rank. Returns a list of albums that are
    ranked between the start and end ranks. If no albums are found for those
    ranks, then an empty list is returned.
    params :rank_1 - smaller rank
            rank_2 - bigger rank
    """
    lst_of_albums = []
    
    for d in info_lst:
        if (int(d['number'])<=rank_2 ) and (int(d['number'])>=rank_1):
            lst_of_albums.append(d['album'])
    
    return lst_of_albums