#CONNECT TO NORTHWIND DATABASE
import sqlite3    
conn = sqlite3.connect('northwind.db')
c = conn.cursor()

#CREATE LIST OF TABLES
def create_table_list():
    table_query = "SELECT name FROM sqlite_master WHERE type='table';"
    c.execute(table_query)
    tables = c.fetchall()

    tables_list = []
    for table in tables:
        tables_list.append(table[0])
    return tables_list

#DISPLAY THE TABLES
def print_tables(tables_list):
    print('TABLES:')
    for table in tables_list:
        print(table)
    print()

#DISPLAY VALUES OF USER-PICKED TABLE
def user_view_table(tables_list):
    user_pick = input('Enter a table to view: ')
    while user_pick not in tables_list:
        user_pick = input('Table not found. Please enter a table to view: ')
    if user_pick in tables_list:
        print(user_pick + ": ")
        query = (f'SELECT * FROM {user_pick}')
        c.execute(query)
        contents = c.fetchall()
        for row in contents:
            print(row)
    print()
    return user_pick

#INSERT, UPDATE, DELETE FROM CUSTOMERS TABLE
def revise_customers():
    print('Revise Customers Table:')
    revision_options = ['update', 'insert', 'delete']
    user_option = input("Which revision? (type update, insert, or delete): ")
    while user_option not in revision_options:
        user_option = input("Error: revision not found. Type update, insert, or delete: ")
    if user_option == 'insert':
        customer_ID = input("What is the customerID? (Must be 5 letters): ")
        while len(customer_ID) != 5:
            customer_ID = input("Must be 5 letters. Enter again: ")
        company_name = input("What is the company name?: ")
        customer_insert = (customer_ID, company_name)
        c.execute(
            'INSERT INTO Customers (CustomerID, CompanyName) VALUES (?, ?)',
            customer_insert
        )
    elif user_option == 'update':
        customer_ID = input('Choose a CustomerID to update: ')
        new_company_name = input('Enter new company name: ')
        c.execute(
            'UPDATE Customers SET CompanyName = ? WHERE ?',
            (new_company_name, customer_ID)
        )
    elif user_option == 'delete':
        customer_ID = input('Choose a CustomerID to delete: ')
        c.execute('DELETE FROM Customers WHERE CustomerID = ?', (customer_ID,))

        

def main():
    tables = create_table_list()
    print_tables(tables)
    table_view = user_view_table(tables)
    revise_customers()
    

main()
conn.close()


