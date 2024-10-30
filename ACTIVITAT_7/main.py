# Main to call all the functions
import psycopg2
import create
import create_table as ct
import read
import update
import delete
import conn as cn

def main():
    # Call the function for creating the table
    ct.create_table()
    # Call the function for inserting data into the table
    create.insert_records(2, "Brandy", "DAW", "FP", "2A", "A01")
    # Call the function for reading the data
    read.read_table()
    # Call the function for updating the data
    # update.update_table(1,"Sherile","DAW2")
    # Call function for deleting data

if __name__ == "__main__":
 main()  # To start the program

