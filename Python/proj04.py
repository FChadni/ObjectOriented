###########################################################
#  Computer Project #4
#
#  Algorithm
#import pylab to define do_plot labels.
#def open_file(): open a file as inputed if not show error and ask to input again untill right file found.
#def read_file(fp): The the open file, but do not print the entire file.
#def find_average(data_lst):take the sum from data lines and then divide by number of people.
#def find_median(data_lst):
#def get_range(data_lst, percent): 
#def get_percent(data_lst, salary):
#def main(): call for it to graph the lowest 40. find "r" and "p" or if nothing is entered stop the program.

import pylab

def do_plot(x_vals, y_vals, year):
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in " + str(year))
    pylab.plot(x_vals, y_vals)
    pylab.show()

def open_file():
    while True:
        year_str = input("Enter a year where 1990 <= year <= 2015: ")
        try:
            if not (int(year_str) <= 2015 and int(year_str) >= 1990) : raise ValueError
        except ValueError:
            print("Error in year. Please try again.")
            continue
        try:
            file = open("year" + year_str + ".txt")
            return file
        except FileNotFoundError:
            print("Error in file name: year1999.txt  Please try again.")
            continue
        
def read_file(fp):
    lines = list(fp.readlines())
    return lines[2:]

def find_average(data_lst):
    numOfPeople = int(str(data_lst[-1].split()[4]).replace(",",""))
    sum = 0.0
    for x in data_lst:
        t = x.split()
        sum += float(t[6].replace(",", ""))
    return sum/numOfPeople

def find_median(data_lst):
    m = 100
    aveIncome = 0
    for x in data_lst:
        t = x.split()
        if abs(float(t[5]) - 50) < m:
            m = abs(float(t[5]) - 50)
            aveIncome = float(t[7].replace(",", ""))
    return aveIncome

def get_range(data_lst, percent):
    for x in data_lst:
        t = x.split()
        if float(t[5]) >= percent:
            return (float(t[0].replace(",", "")), float(t[2].replace(",", ""))), float(t[5]), float(t[7].replace(",", ""))

def get_percent(data_lst, salary):
    for x in data_lst[:-1]:
        t = x.split()
        if salary < float(t[2].replace(",", "")) and salary >= float(t[0].replace(",", "")):
            return (float(t[0].replace(",", "")), float(t[2].replace(",", ""))), float(t[5])
    return (float(t[0].replace(",", "")), float("inf")), float(t[5])

def main():
    # Insert code here to determine year, average, and median
    file = open_file()
    year = int(file.name[4:8])
    data_list = read_file(file)
    avg = find_average(data_list)
    median = find_median(data_list)
    print("Year   ", "Mean         ", "Median    ")
    print("{:4d}  ".format(year), "${:<13,.2f}".format(avg), "${:<13,.2f}".format(median)  )


    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes':
        y_vals = []
        x_vals = []
        for line in data_list[:40]:
            line_1st = line.split()
            y_vals.append(float(line_1st[4]))
            x_vals.append(float(line_1st[0].replace(",", "")))
            do_plot(x_vals, y_vals, year)

    choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
    # Insert code here to handle choice
    while choice:
        if choice == 'r':
            percent = float(input("Enter a percent: "))
            if percent <= 100 and percent >= 0:
                print("{:4.2f}% of incomes are below ${:<13,.2f}.".format(percent, get_range(data_list, percent)[0][0]))
            else:
                print("Error in percent. Please try again")

        elif choice == 'p':
            income = float(input("Enter an income: "))
            if income >= 0:
                print("An income of ${:<13,.2f} is in the top {:4.2f}% of incomes.".format(income, get_percent(data_list, income)[1]))
            else:
                print("Error: income must be positive")

        elif choice == '\n':
            break

        else:
            print("Error in selection.")

        choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")


if __name__ == "__main__":
    main()
