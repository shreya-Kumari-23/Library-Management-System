from prettytable import PrettyTable
from db_connection import get_db_connection

db = get_db_connection()

# Function to report issued books:
def report_issued_books():
    print("\n╔══════════════════════════════╗")
    print("║      ISSUED BOOKS' LIST      ║")
    print("╚══════════════════════════════╝\n")
    sql7="select * from issue;"
    c=db.cursor()
    c.execute(sql7)
    res=c.fetchall()
    l2=[]
    t1=PrettyTable(["STUDENT'S NAME","BOOK'S CODE","REGISTRATION NUMBER","DATE OF RETURN"])
    for i in res:
        l2.append([i[0],i[1],i[2],i[3]])
    t1.add_rows(l2)
    print(t1)
    main()
    
# Function to report returned books:
def report_returned_books():
    print("\n╔══════════════════════════════╗")
    print("║     RETURNED BOOKS' LIST     ║")
    print("╚══════════════════════════════╝\n")
    sql8="select*from rturn;"
    c=db.cursor()
    c.execute(sql8)
    res=c.fetchall()
    l3=[]
    t2=PrettyTable(["STUDENT'S NAME","BOOK'S CODE","REGISTRATION NUMBER","DATE OF RETURN"])
    for i in res:
        l3.append([i[0],i[1],i[2],i[3]])
    t2.add_rows(l3)
    print(t2)
    main()
