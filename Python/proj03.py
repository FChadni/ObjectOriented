###########################################################################
# Computer Project 3
    #Algorithm
        # def open_file()
       # def find_min_percent(line)
       # def find_max_percent(line)
       # def find_gdp(line, index)
       # def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp)
       # def main()
###########################################################################
def open_file():
     '''Repeatedly prompt until a valid file name allows the file to be opened.''' 
     while True: 
         try:
             filename = input("Enter a file name: ") #enter the file name that needs to be open.
             fp = open("GDP.txt") if filename == "" else open(filename) #if the file name is found open it, nor show error.
             return fp
         except IOError:
             print("Error. Please try again") #print the following when incorret file entered.

def find_min_percent(line):
     '''Find the min percent change in the line; return the value and the index.'''
     min_value=10000000 ## some large value
     i = 0 #define i
     linetxt = line[76:]  #The data starts in column 76 ()
     while i < 47: #value less than 47
         value = linetxt[:12]
         value = value.rstrip() #strip the value
         value = float(value) #convert to float
         if value < min_value:  # you have found a smaller value
             min_value = value  # set min_value to that smaller value
             min_value_index = (i*12)
         linetxt = linetxt[12:] #12 columns 
         i+=1 
     return min_value, min_value_index+1 #return the values.
   
    
    
def find_max_percent(line):
     '''Find the max percent change in the line; return the value and the index.'''
     # identical/similar to the find_min_percentfunction.
     max_value=0 ## some small value
     i = 0
     linetxt = line[76:] 
     while i < 47:
         value = linetxt[:12]
         value = value.rstrip()
         value = float(value)    
         if value > float(max_value):
             max_value = value
             max_value_index = (i*12)
         linetxt = linetxt[12:]
         i+=1 
     return max_value, max_value_index+1

def find_gdp(line, index):
     '''Use the index fo find the gdp value in the line; return the value'''
     index = int(index)+75
     linetxt = line[index:]
     gdpVal = linetxt[:12]
     gdpVal = float(gdpVal) #float of GDP
    #Return
     return gdpVal

def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):  
     '''Display values; convert billions to trillions first.''' 
     print("Gross Domestic Product")  
     print("min/max     change year   GDP (trillions)") 
     print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("min",float(min_val),int(min_year),float(min_val_gdp/1000)))
     print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("max",float(max_val),int(max_year),float(max_val_gdp/1000)))

def main():                
     fp = open_file()
     linecount = 0  
     for line in fp:
         line = line.strip()
         linecount +=1      
         if linecount == 8:
             yearline1 = line     
         if linecount == 9:
             min_val = find_min_percent(line)
             max_val = find_max_percent(line)
             s_min_val = str(min_val)
             fyearind = s_min_val.find(",",0)
             minval_index = s_min_val[int(fyearind)+1:len(s_min_val)-1]
             min_val=s_min_val[1:fyearind]
             minYearIndex = int(minval_index.strip())+74
             linetxt = yearline1[minYearIndex:]
             min_year = linetxt[:8]
             s_max_val = str(max_val)
             fyearind = s_max_val.find(",",0)
             maxval_Index = s_max_val[int(fyearind)+1:len(s_max_val)-1]
             max_val=s_max_val[1:fyearind]
             maxYearIndex = int(maxval_Index.strip())+74
             linetxt = yearline1[maxYearIndex:]
             max_year = linetxt[:8]
         if linecount == 44:
             min_val_gdp = find_gdp(line,minval_index)
             max_val_gdp = find_gdp(line,maxval_Index)
     display(min_val,min_year,min_val_gdp,max_val,max_year,max_val_gdp)
# Calls the 'main' function only when you execute within Spyder (or console)
# Do not modify the next two lines.
if __name__ == "__main__":
     main()