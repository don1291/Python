import mysql.connector
import datetime
from dateutil.relativedelta import relativedelta

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='pynative',
                                         password='pynative@#29')
    return connection

def close_connection(connection):
    if connection:
        connection.close()
        
def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("You are connected to MySQL version: ", db_version)
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

print("Question 1: Print Database version")
read_database_version()

def get_hospital_detail(hospital_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Hospital where Hospital_Id = %s"""
        cursor.execute(select_query, (hospital_id,))
        records = cursor.fetchall()
        print("Printing Hospital record")
        for row in records:
            print("Hospital Id:", row[0], )
            print("Hospital Name:", row[1])
            print("Bed Count:", row[2])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def get_doctor_detail(doctor_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Doctor where Doctor_Id = %s"""
        cursor.execute(select_query, (doctor_id,))
        records = cursor.fetchall()
        print("Printing Doctor record")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

print("Question 2: Read given hospital and doctor details \n")
get_hospital_detail(2)
print("\n")
get_doctor_detail(105)

def get_hospital_detail(hospital_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Hospital where Hospital_Id = %s"""
        cursor.execute(select_query, (hospital_id,))
        records = cursor.fetchall()
        print("Printing Hospital record")
        for row in records:
            print("Hospital Id:", row[0], )
            print("Hospital Name:", row[1])
            print("Bed Count:", row[2])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def get_doctor_detail(doctor_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Doctor where Doctor_Id = %s"""
        cursor.execute(select_query, (doctor_id,))
        records = cursor.fetchall()
        print("Printing Doctor record")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

print("Question 2: Read given hospital and doctor details \n")
get_hospital_detail(2)
print("\n")
get_doctor_detail(105)

def get_specialist_doctors_list(speciality, salary):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """select * from Doctor where Speciality=%s and Salary > %s"""
        cursor.execute(sql_select_query, (speciality, salary))
        records = cursor.fetchall()
        print("Printing doctors whose specialty is", speciality, "and salary greater than", salary, "\n")
        for row in records:
            print("Doctor Id: ", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

print("Question 3: Get Doctors as per given Speciality\n")
get_specialist_doctors_list("Garnacologist", 30000)

def get_hospital_name(hospital_id):
    # Fetch Hospital Name using Hospital id
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Hospital where Hospital_Id = %s"""
        cursor.execute(select_query, (hospital_id,))
        record = cursor.fetchone()
        close_connection(connection)
        return record[1]
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def get_doctors(hospital_id):
    # Fetch Hospital Name using Hospital id
    try:
        hospital_name = get_hospital_name(hospital_id)
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """select * from Doctor where Hospital_Id = %s"""
        cursor.execute(sql_select_query, (hospital_id,))
        records = cursor.fetchall()

        print("Printing Doctors of ", hospital_name, "Hospital")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Hospital Name:", hospital_name)
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting doctor's data", error)

print("Question 4:  Get List of doctors of a given Hospital Id\n")
get_doctors(2)

def close_connection(connection):
    if connection:
        connection.close()

def update_doctor_experience(doctor_id):
    # Update Doctor Experience in Years
    try:
        # Get joining date
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select Joining_Date from Doctor where Doctor_Id = %s"""
        cursor.execute(select_query, (doctor_id,))
        joining_date = cursor.fetchone()

        # calculate Experience in years
        joining_date_1 = datetime.datetime.strptime(''.join(map(str, joining_date)), '%Y-%m-%d')
        today_date = datetime.datetime.now()
        experience = relativedelta(today_date, joining_date_1).years

        # Update doctor's Experience now
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """update Doctor set Experience = %s where Doctor_Id =%s"""
        cursor.execute(sql_select_query, (experience, doctor_id))
        connection.commit()
        print("Doctor Id:", doctor_id, " Experience updated to ", experience, " years")
        close_connection(connection)

    except (Exception, mysql.connector.Error) as error:
        print("Error while getting doctor's data", error)

print("Question 5: Calculate and Update experience of all doctors  \n")
update_doctor_experience(101)
