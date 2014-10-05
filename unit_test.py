
import math

## Unit test for Task 1 (function read_graph_from_file).
def unit_test_read_graph_from_file(filename,
                                   ex_neighbour_list,
                                   ex_pos_list):
    assert len(ex_neighbour_list) == len(ex_pos_list), "Incorrect arguments to unit_test_read_graph_from_file!"
    print("Testing Task 1 (read_graph_from_file) on " + filename)
    # check that the file exists
    try:
        testfile = open(filename, "r")
        testfile.close()
    except FileNotFoundError:
        print("File " + filename + " not found: skipping this test.")
        print("(Make sure you download this file from wattle and save")
        print("it in the same directory as the program modules.)")
        return "Skipped"
    # call function, get return values; it should not raise an exception.
    try:
        (neighbour_list, pos_list) = read_graph_from_file(filename)
    except Exception as exc:
        print("Calling read_graph_from_file on " + filename +
              " raised exception " + str(exc))
        return "Failed"
    # check that return values are lists
    if not isinstance(neighbour_list, list):
        print("The neighbour_list returned by function read_graph_from_file is not a list!")
        return "Failed"
    if not isinstance(pos_list, list):
        print("The position_list returned by function read_graph_from_file is not a list!")
        return "Failed"
    # check list lengths are consistent...
    if len(neighbour_list) != len(pos_list):
        print("The length of the returned neighbours list (== number of nodes) is {} but the length of the return node position list is {}; they should be the same".format(len(neighbour_list), len(pos_list)))
        return "Failed"
    # ...and correct
    if len(neighbour_list) != len(ex_neighbour_list):
        print("The returned graph has {} nodes: the correct number is {}".format(len(neighbour_list), len(ex_neighbour_list)))
        return "Failed"
    # check neighbour lists are correct:
    all_ok = True
    for i in range(len(neighbour_list)):
        if neighbour_list[i] != ex_neighbour_list[i]:
            # if not exactly equal, try sorting
            sorted_list = sorted(neighbour_list[i])
            if sorted_list == ex_neighbour_list[i]:
                print("The neighbour list of node {} in the returned graph is {}: it the right elements but in the wrong order (they should be sorted in increasing order)".format(i, neighbour_list[i]))
                all_ok = False
            else:
                print("The neighbour list of node {} in the returned graph is {}: it should be {}".format(i, neighbour_list[i], ex_neighbour_list[i]))
                all_ok = False
    if not all_ok:
        return "Failed"
    # check node positions are correct:
    all_ok = True
    for i in range(len(neighbour_list)):
        if pos_list[i] != ex_pos_list[i]:
            print("The value for node {} in the returned node position list is {}: it should be {}".format(i, pos_list[i], ex_pos_list[i]))
            all_ok = False
    if not all_ok:
        return "Failed"
    return "Passed"

## Unit test for Task 2 (function label_graph_components).
def unit_test_label_graph_components(test_id, neighbour_list, ex_label_list):
    assert len(neighbour_list) == len(ex_label_list), "Incorrect arguments to unit_test_label_graph_components!"
    print("Testing Task 2 (label_graph_components) on " + test_id)
    # call function, get return values; it should not raise an exception.
    try:
        label_list = label_graph_components(neighbour_list)
    except Exception as exc:
        print("Calling label_graph_components on " + test_id + " : " +
              str(neighbour_list) + " raised exception " + str(exc))
        return "Failed"
    # check that the function returned a list!
    if not isinstance(label_list, list):
        print("Function label_graph_components did not return a list!")
        return "Failed"
    # check list lengths are consistent...
    if len(neighbour_list) != len(label_list):
        print("The length of the returned label list is {} but the number of nodes is {}: they should be the same".format(len(label_list), len(neighbour_list)))
        return "Failed"
    # check that component numbers are 0 .. k-1
    if min(label_list) != 0:
        print("The smallest component label in the returned list is {}: component labels should be 0 .. number_of_components - 1".format(min(label_list)))
        return "Failed"
    if max(label_list) != max(ex_label_list):
        print("The highest component label in the returned list is {}: component labels should be 0 .. number_of_components - 1, number of components is {}".format(max(label_list), max(ex_label_list) + 1))
        return "Failed"
    # for each pair of nodes (excl. symmetric), check their labels:
    all_ok = True
    for i in range(len(neighbour_list)):
        for j in range(i + 1, len(neighbour_list)):
            if ex_label_list[i] == ex_label_list[j]:
                if label_list[i] != label_list[j]:
                    print("In the returned label_list, nodes {} and {} have different labels: they should be the same".format(i, j))
                    all_ok = False
            else:
                if label_list[i] == label_list[j]:
                    print("In the returned label_list, nodes {} and {} have equal labels: they should be different".format(i, j))
                    all_ok = False
    if not all_ok:
        return "Failed"
    return "Passed"

## Unit test for Task 3 (function get_component_density).
def unit_test_get_component_density(test_id, neighbour_list,
                                    label_list,
                                    ex_density):
    assert len(neighbour_list) == len(label_list), "Incorrect arguments to unit_test_get_component_density!"
    assert (max(label_list) + 1) == len(ex_density), "Incorrect arguments to unit_test_get_component_density!"
    print("Testing Task 3 (get_component_density) on " + test_id)
    all_ok = True
    for label in range(max(label_list) + 1):
        try:
            density = get_component_density(label, neighbour_list, label_list)
        except Exception as exc:
            print("Calling get_component_density on " + test_id + " : " +
                  str(neighbour_list) + " / " + str(label_list) + " with label " +
                  str(label) + " raised exception " + str(exc))
            return "Failed"
        if not isinstance(density, float):
            print("Function get_component_density did not return a float!")
            return "Failed"
        diff = math.fabs(density - ex_density[label])
        if diff > 0.01:
            print("The returned density for component label {} is {:1.3f}: this is more than 0.01 different from the expected value of {:1.3f}".format(label, density, ex_density[label]))
            all_ok = False
    if not all_ok:
        return "Failed"
    else:
        return "Passed"

## Test data

graph1_neighbour_list = [[1, 4], [0, 2, 4], [1, 3], [2, 4, 5], [0, 1, 3], [3]]
graph1_position_list = [(295, 105), (230, 170), (135, 190), (115, 90),
                        (215, 70), (35, 35)]
graph1_label_list = [0, 0, 0, 0, 0, 0]
graph1_densities = [1.167]

graph2_neighbour_list = [[4], [2, 5], [1, 3, 8], [2, 14], [0, 9], [1],
                         [10, 12], [13], [2, 14], [4, 10, 15], [6, 9], [17],
                         [6], [7, 19, 20], [3, 8], [9, 21], [22], [11, 18],
                         [17, 19], [13, 18, 26], [13, 26], [15, 27], [16, 23],
                         [22, 24, 28], [23, 25, 29], [24], [19, 20, 30, 31],
                         [21], [23, 29], [24, 28], [26, 31], [26, 30]]
graph2_position_list = [(60, 60), (180, 60), (240, 60), (360, 60), (60, 120),
                        (120, 120), (180, 120), (240, 120), (300, 120),
                        (60, 180), (120, 180), (180, 180), (240, 180),
                        (300, 180), (360, 180), (60, 240), (120, 240),
                        (180, 240), (240, 240), (300, 240), (360, 240),
                        (60, 300), (120, 300), (180, 300), (240, 300),
                        (300, 300), (360, 300), (120, 360), (180, 360),
                        (240, 360), (300, 360), (360, 360)]
graph2_label_list = [0, 1, 1, 1, 0, 1, 0, 2, 1, 0, 0, 2, 0, 2, 1, 0, 3, 2,
                     2, 2, 2, 0, 3, 3, 3, 3, 2, 0, 3, 3, 2, 2]
graph2_densities = [0.889, 1.0, 1.1, 1.0]

graph3_neighbour_list = [[1, 6], [0, 2], [1, 3], [2, 4], [3, 5], [4, 10, 11],
                         [0, 12], [8, 13, 14], [7, 9, 13], [8, 14], [5, 15],
                         [5, 17], [6, 18], [7, 8, 14, 19], [7, 9, 13, 19, 21],
                         [10], [21, 22], [11, 23], [12, 24], [13, 14], [25],
                         [14, 16, 22, 26, 27, 28], [16, 21, 27, 28], [17, 29],
                         [18, 30], [20, 30], [21, 27], [21, 22, 26, 28],
                         [21, 22, 27], [23, 35], [24, 25, 31], [30, 32],
                         [31, 33], [32], [], [29]]
graph3_position_list = [(60, 60), (120, 60), (180, 60), (240, 60), (300, 60),
                        (360, 60), (60, 120), (120, 120), (180, 120),
                        (240, 120), (300, 120), (360, 120), (60, 180),
                        (120, 180), (180, 180), (240, 180), (300, 180),
                        (360, 180), (60, 240), (120, 240), (180, 240),
                        (240, 240), (300, 240), (360, 240), (60, 300),
                        (120, 300), (180, 300), (240, 300), (300, 300),
                        (360, 300), (60, 360), (120, 360), (180, 360),
                        (240, 360), (300, 360), (360, 360)]
graph3_label_list = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0,
                     0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 2, 0]
graph3_densities = [0.956, 1.667, 0.0]

## Main program: runs a series of tests.
if __name__ == "__main__":
    import sys
    # This is a work around for the lack of a shell menu in IDLE 3.2.
    if sys.version_info.major == 3 and sys.version_info.minor == 2:
        import imp
        if 'assign2_u5021276' in sys.modules:
            imp.reload(sys.modules['assign2_u5021276'])

    # Import the functions to be tested from the assign2_u5021276 module.
    from assign2_u5021276 import read_graph_from_file
    from assign2_u5021276 import label_graph_components
    from assign2_u5021276 import get_component_density

    ## Test task 1
    status11 = unit_test_read_graph_from_file("test_graph_1.txt", graph1_neighbour_list, graph1_position_list)
    status12 = unit_test_read_graph_from_file("test_graph_2.txt", graph2_neighbour_list, graph2_position_list)
    status13 = unit_test_read_graph_from_file("test_graph_3.txt", graph3_neighbour_list, graph3_position_list)
    print("Task 1 - read_graph_from_file:")
    print(" with input test_graph_1.txt: " + status11)
    print(" with input test_graph_2.txt: " + status12)
    print(" with input test_graph_3.txt: " + status13)

    ## Test task 2
    status21 = unit_test_label_graph_components("test graph #1", graph1_neighbour_list, graph1_label_list)
    status22 = unit_test_label_graph_components("test graph #2", graph2_neighbour_list, graph2_label_list)
    status23 = unit_test_label_graph_components("test graph #3", graph3_neighbour_list, graph3_label_list)
    print("Task 2 - label_graph_components:")
    print(" with input test graph #1: " + status21)
    print(" with input test graph #2: " + status22)
    print(" with input test graph #3: " + status23)

    ## Test task 3
    status31 = unit_test_get_component_density("test graph #1", graph1_neighbour_list, graph1_label_list, graph1_densities)
    status32 = unit_test_get_component_density("test graph #2", graph2_neighbour_list, graph2_label_list, graph2_densities)
    status33 = unit_test_get_component_density("test graph #3", graph3_neighbour_list, graph3_label_list, graph3_densities)
    print("Task 3 - get_component_density:")
    print(" with input test graph #1: " + status31)
    print(" with input test graph #2: " + status32)
    print(" with input test graph #3: " + status33)
