#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for ele in row:
            print("{:d}".format(ele),
                  end="" if row[len(row)-1] == ele else " ")
        print("".format())
