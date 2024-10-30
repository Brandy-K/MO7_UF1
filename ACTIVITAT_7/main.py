# Main to call all the functions
import create
import create_table as ct
import read
import update
import delete


def main():
    # Call the function for creating the table
    ct.create_table()
    # Call the function for inserting data into the table
    create.insert_records(5, "Brandy", "DAW", "FP", "2A", "A01")
    create.insert_records(1, "Bruno", "DAW", "FP", "2A", "A01")
    create.insert_records(3, "Peter", "DAM", "FP", "2B", "A02")
    create.insert_records(4, "Doua", "ASIX", "FP", "2A", "A05")
    # Call the function for reading the data
    read.read_table()
    # Call the function for updating the data
    update.update_table(1,"Sherile")
    # Call function for deleting data


if __name__ == "__main__":
    main()  # To start the program
