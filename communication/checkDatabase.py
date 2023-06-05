#Cross references the database checking if any value matches the specified values (must be run in new_env)
import numpy as np
import csv

def euclidian_distance(tensor1,tensor2):
    return np.linalg.norm(np.array(tensor1) - np.array(tensor2))


def parse_database(input_array):
    flag = False
    with open('database.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            
            array = eval(row[1])
            
            dist =euclidian_distance(array,input_array)
            if dist <0.6:
                flag = True
    return flag

def append_database(input_array):
    column_name = ["id","facialFeatures"]
    with open('database.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(column_name)
        writer.writerow(input_array)