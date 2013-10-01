# !/usr/bin/python
import sys
import simplejson as json


def parse_file(infile):
    """ Parses the file to extract the information """
    data = {}
    with open(infile) as inf:
        for line in inf:
            values = line.split(' ')
            if len(values) != 4 :
                print "Invalid line. Skipping this one..."
                continue

            # Fill the info in the data struct
            name = values[0]
            info = {
                'name': name,
                'role': values[1],
                'start': int(values[2]),
                'end': int(values[3]),
            }
            
            if data.has_key(name):
                data[name]['roles'].append(info)
            else:
                data[name] = {
                    'roles': [info],
                }
            
    return data            

def set_total_years(data):
    """ Set the number of years each employee worked iin the company
    """
    for name in data.keys():
        info = data[name]
        years = sum([role['end'] - role['start'] for role in info['roles']])
        data[name]['years'] = years

    return data


def print_ex1(data):
    """ list of all employees who have had more than one role at
        the company, in alphabetical order by employee first  
        name, printed on a single line.
    """
    names_by_roles = [name for name in data.keys() if len(data[name]['roles']) > 1]
    names_by_roles.sort()
    print ', '.join(names_by_roles)
    
def print_ex2(data):
    """ How long each employee has been at the company, one per line, 
        ordered alphabetically by name 
    """
    names = data.keys()
    names.sort()
    for name in names:
        print "%s %d" % (name, data[name]['years'])

def print_ex3(data):
    """ Print the name of the employee that has spent the most number of years
        with the company
    """
    max_years = 0
    employee = '-'
    for name in data:
        if data[name]['years'] > max_years:
            max_years = data[name]['years']
            employee = name
        elif data[name]['years'] == max_years:
            employee = '-'

    print employee

def print_ex4(data):
    """ Preety print the data """
    names = data.keys()
    names.sort()
    employees = [data[name] for name in names]
    print(json.dumps(list(employees), sort_keys=True, indent=4 * ' '))


if __name__ == "__main__":
    """ Execute the program """ 

    input_file = sys.argv[1]
    data = parse_file(input_file)
    data = set_total_years(data)

    print_ex1(data)
    print_ex2(data)
    print_ex3(data)
    print_ex4(data)
