## u5021276

## Implementing this function is task 1:
def read_graph_from_file(filename):
    '''This function reads a graph from a file and returns a tuple of
    two lists: (neighbours, positions): neighbours is the neighbour
    list representation of the graph; positions is the list of node
    positions (this is used only for displaying the graph on screen).
    For a detailed description of the neighbour list data structure
    and graph file format, see the assignment specification page in
    wattle.'''

    graph_file = open(filename,"r")

    positions_list = []
    neighbour_dict = {}
    line_num = 1
    node_num = 0

    # files always start with 3 column lines representing nodes
    col_count = (3,)
    # parse the graph file
    while True:

        # read a line
        line = graph_file.readline()
        # end of file, break loop
        if not line: break
        # increment the line count
        line_num = line_num + 1
        # remove newlines, split the line via commas
        columns = line.rstrip().split(',')
        # convert elements to integers
        try:
            columns = [int(n) for n in columns]
        except ValueError:
            raise FileFormatError(filename, line_num, "Incorrect elements! All elements must be integers.")
        # get the length count for the columns
        length = len(columns)

        # check if the number of columns in the file are valid
        if length in col_count:

            if length == 3:

                # expects the next line to be 3 columns or 2 columns
                col_count = (3, 2)

                # N case (nodes)
                # columns[0] => node
                # columns[1] => posx
                # columns[2] => posy
                
                # check that the node numbers are incremental
                if not node_num == columns[0]:
                    raise FileFormatError(filename, line_num, "Incorrect node number! Nodes must increment from 0 to N-1 where N is the number of Node lines.")

                positions_list.append((columns[1], columns[2]))

                # increment the node number
                node_num = node_num + 1

            elif length == 2:

                # expects the next line to be 2 columns only
                col_count = (2,)

                # M case (links)
                # columns[0] => node1
                # columns[1] => node2
                
                if columns[0] < 0 or columns[0] > node_num or columns[1] < 0 or columns[1] > node_num:
                    raise FileFormatError(filename, line_num, "Incorrect link node number! Nodes must be between 0 and N-1 where N is the number of nodes.")

                if not columns[0] in neighbour_dict:
                    neighbour_dict[columns[0]] = []
                
                if not columns[1] in neighbour_dict:
                    neighbour_dict[columns[1]] = []

                neighbour_dict[columns[0]].append(columns[1])
                neighbour_dict[columns[1]].append(columns[0])

        else:

            raise FileFormatError(filename, line_num, "Incorrect file format! File needs to start with nodes with 3 columns, then with links with 2 columns.")

    # close the file!
    graph_file.close()

    # find nodes that have no neighbours! And mark them as an empty list in the neighbours dictionary
    list_of_nodes_from_positions = list(range(0, len(positions_list)))
    list_of_nodes_from_neighbours = neighbour_dict.keys()
    difference_list = list(set(list_of_nodes_from_positions) - set(list_of_nodes_from_neighbours))
    for node in difference_list:
        neighbour_dict[node] = []

    # converting our neighbour_dict into a neighbour_list while sorting it in order of node index
    neighbour_list = [value for (key, value) in sorted(neighbour_dict.items())]

    # sorting the neighbours in ascending order
    for index, neighbours in enumerate(neighbour_list):
        neighbour_list[index] = sorted(neighbours)

    # debugging code left here
    # with open("log_neighbour.txt", "w") as log:
    #    log.write(repr(neighbour_list))
    # with open("log_positions.txt", "w") as log:
    #    log.write(repr(positions_list))

    return (neighbour_list, positions_list)

## Implementing this function is task 2:
def label_graph_components(neighbour_list):
    '''This function takes as input the neighbour list representation of
    a graph and returns a list with the component number for each node in
    the graph. Components must be numbered consecutively, starting from
    zero.'''
    ## You MUST REPLACE the following return statement with your code:
    return []

## Implementing this function is task 3:
def get_component_density(label, neighbour_list, label_list):
    '''This function takes a component label, the neighbour list
    representation of a graph and a list of component labels
    (one for each node in the graph), and should calculate and return
    the link density in the component with the given label. The link
    density is defined as the number of links (in that component)
    divided by the number of nodes (in that component). If there
    are no nodes with the given component label, the function
    should raise an error.'''
    ## You MUST REPLACE the following return statement with your code:
    return 0.0


## The code below defines a custom exception type for format errors in
## the graph file. Catching format errors in the input file is one
## important part of task 1. When you detect an error in the input file,
## you should raise a file format error. This is done as follows:
##
##   raise FileFormatError(filename, line_number, message)
##
## where filename is the name of the incorrect file, line_number the
## line in the file where the error occurred, and message is a string
## that describes the error. You are free to make up your own error
## messages, but keep in mind that they should be helpful to the user.

class FileFormatError (Exception):
    def __init__(self, filename, line_num, message):
        super(Exception, self).__init__()
        self.filename = filename
        self.line_num = line_num
        self.message = message
    def __str__(self):
        return self.filename + ", line " + str(self.line_num) + ": " + self.message
