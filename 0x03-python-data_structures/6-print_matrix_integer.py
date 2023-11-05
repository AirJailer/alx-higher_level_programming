#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print_ = ""
        for j in i:
            print_ += str(j)
            print_ += " "
        print("{}".format(print_))
