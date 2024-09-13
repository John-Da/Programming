import sqlDataBase as sqlData


# Add a Record to the DataBase
# sqlData.add_record('John', 'Adam', 'john@adam.com')

# Add Many Records to the DataBase
members_list = [
    ("Mary", "James", "mary@james.com"),
    ("Joshua", "Raintree", "josh@rain.com"),
]
# sqlData.add_manyRecord(members_list)

# Delete a Record from the DataBase
# sqlData.delete_record(4) # int(num)
# sqlData.delete_record('5') # str(num)

# Show the Record
# sqlData.show_allData()

# LookUp the Email from the Table
# sqlData.email_lookUp('mary') using LIKE
sqlData.email_lookUp("mary@james.com")  # LookUp manually
