###########################################################
#  Computer Project #5
#
#  Algorithm

#First test out if csv files opens, if so continue
###Open file and then check for try and error if file not found.

#read the file of where the data are avaliable to be printed out as output.
###open as r file, commend to read lines and seperated comma.
####index[0]/column 1 contains name of each states, so define that under read lines.
####index[1] deals with crops name that must be print for mimir output tests.
####index[3] are varities, which will be ignored.
####index[4] contains the years of data values.
####index[6] contains the values from which max and min will be determined.

#Resolve the issue of printing out extra variables that are not in data output
###call for only print name of states that are avaliable in the STATE list.

#The following formatting fixes the output printing order, if this statement not stated then data gets printed randomly.
#Forment the min/max values to be printed accordingly 
###set less statement with nested dictionary to only print min val/min years.
###set greater than statment with nasted dictionary to only print max val/max years.

#Problem1: Need to remove /2 from missouri, and none printed at the end.
    #Stament using if then for "Missouri" and "None"
#Problem2: Need not to print U.S statement and other states data.
    #So by creating a line stement for STATEs will solve this prolem?

STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado',
          'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
          'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
          'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
          'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
          'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 
          'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
          'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
          'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
          'West Virginia', 'Wisconsin', 'Wyoming']

#open_file function only opens the file
def open_file(): # define file. 
    while True: #while true statement. 
        filename = input("Enter a file: ") #input file name.
        try: #If file is found, open the file to read.
            fp = open(filename,"r")
            return fp
        except FileNotFoundError: #If file not found the print the following below.
            print("File not found.") 
#read_file reads each lines as commended by.
def read_file(fp): #Read the file 
    data_Dict = {}
    fp.readline() #Read line and as defined each index below.
    for line in fp:
        line_1st = line.split(",") #split string into list on commas. 
        state_name = line_1st[0].strip() #name of states in frist index (0).
        if state_name == "Missouri 2/": #if state name is the following
            state_name = "Missouri" #then print the following rather the statement on if.
        if state_name not in STATES: #Only print data for the states defined on STATES.
            continue
        crop = line_1st[1]
        varity = line_1st[3]
        if line_1st[3] != "All GE varieties":
            continue
        year = line_1st[4] #years found in colunm 4.
        year = int(year) #years to integer values.
        val = line_1st[6]#values found on this colunm will be determind as max or min.
        val = val[:-1] #Print one value for state ohio
        if val.isdigit(): #if value is a digit, chnage to integer value. 
            val = int(val) #values into integer values.
        else:
            continue
        data = {"Max_Yr":year,"Max":val,"Min_Yr":year,"Min":val}
        if crop not in data_Dict:# 
            data_Dict[crop] = {}
        if state_name not in data_Dict[crop].keys():
            data_Dict[crop][state_name] = data 
        #Print the max/min values and max/min years in order by states   
        else:
            if val > data_Dict[crop][state_name]["Max"]: #If the value is > nested dictionary "Max"
                data_Dict[crop][state_name]["Max_Yr"] = year #Print "Max Yr" for those max values
                data_Dict[crop][state_name]["Max"] = val #print those values for "max"
            if val < data_Dict[crop][state_name]["Min"]: #same as max values instead it takes min values with less than sign
                data_Dict[crop][state_name]["Min_Yr"] = year 
                data_Dict[crop][state_name]["Min"] = val        
    return data_Dict
#data_print_table does the printing of datas in a table format from each csv file.
def data_print_table (data_Dict):
    for crop in sorted(data_Dict.keys()):#sorted to get order (alphabetically by state name)
        print("Crop: " + crop) #print name of the crop with "crop:name"
        print("{:<20s}{:<8s}{:<6s}{:<8s}{:<6s}".format("State", "Max Yr",
              "Max", "Min Yr", "Min")) #format required/used by prof(heading))
        for states in sorted(data_Dict[crop].keys()): #sorted to get prints in order 
            #formatting required/used by prof
            print("{:<20s}{:<8s}{:<6d}{:<8s}{:<6d}".format(states, str(data_Dict[crop][states]["Max_Yr"]),
            data_Dict[crop][states]["Max"],str(data_Dict[crop][states]["Min_Yr"]),data_Dict[crop][states]["Min"]))
#main file combine all the function together and returns all the statement made by other functions.
def main():
    fp = open_file() 
    read = read_file(fp)
    data = data_print_table(read)
    return(data)

if __name__ == "__main__":
    main()
                
