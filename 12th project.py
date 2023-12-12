'''install:
    -pyttsx3(on mac download homebrew on to laptop then install portaudio and pyaudio on terminal
             on windows download the whellfile for pyaudio)
    -speech-recognition on macos or speech_recognition for windows

   in lisn 22:
   -for macos use engine = pyttsx3.init('nsss')
   -for windows use engine = pyttsx3.init('sapi5')

   in line 27:
   -change the speaking rate according to your convenience

   in line mydb = sql.connect(host="localhost", user="root", passwd="mysql@123"):
   -change the password '''

import random
import mysql.connector as sql
import pyttsx3
import speech_recognition as sr
import datetime
engine = pyttsx3.init('nsss') #if running on windows use 'sapi5' instead of 'nsss' for macos
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
newvolume = 5
newvoicerate = 225
engine.setProperty('rate', newvoicerate)
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', newvolume)


def speak(audio):  # used for voice
    engine.say(audio)
    engine.runAndWait()


def wishMe():  # used for wishing user according to real time
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


def takeCommand():  # used to take reply from the user

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as z:  # when it does not understand the statement
        print(z)
        print("Say that again please...")
        speak("Say that again please")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()

print("""********************************
*                              *
****   LIBRARY MANAGEMENT   ****    
*                              *
********************************""")

speak("welcome to LIBRARY MANAGEMENT")
print("I am Bob, here to assist you\nJust tell me what you need from the menu below")
speak("I am Bob, here to assist you. Just tell me what you need from the menu below")

# CREATING DATABASE
mydb = sql.connect(host="localhost", user="root", passwd="mysql@123")
cursor = mydb.cursor()
cursor.execute("create database if not exists library")
cursor.execute("use library")

# CREATING REQUIRED TABLES

cursor.execute("create table if not exists library_master(cardno char(10) primary key,name_of_person varchar(30),phone_no char(10),address varchar(30),dob date)")
cursor.execute("create table if not exists books(book_no varchar(5) primary key,book_name varchar(100),genre varchar(30),authors_name varchar(30),language varchar(15),status varchar(20))")
cursor.execute("create table if not exists library_transaction(cardno char(10),foreign key(cardno) references library_master(cardno),book_name varchar(20),return_by date,date_of_lend date,date_of_return date,pay_fine int)")
cursor.execute("create table if not exists buy_new_books(orderno varchar(6) primary key,ordered_by char(10),foreign key(ordered_by) references library_master(cardno),name_of_book varchar(20),del_date date,price varchar(5),status varchar(20))")
cursor.execute("create table if not exists borrow_history(cardno char(10),foreign key(cardno) references library_master(cardno),book_no varchar(5),foreign key(book_no) references books(book_no),borrowed_books varchar(30),returned_books varchar(30))")
cursor.execute("select * from books")
e=cursor.fetchone()
if e == None:
    bnames = ["In Search of Lost Time","Ulysses","Don Quixote","The Great Gatsby","One Hundred Years of Solitude","Moby Dick","War and Peace","Lolita","Hamlet","The Catcher in the Rye","The Odyssey","The Brothers Karamazov","Crime and Punishment","Madame Bovary","The Divine Comedy","The Adventures of Huckleberry Finn","Alice s Adventures in Wonderland","Pride and Prejudice","Wuthering Heights","To the Lighthouse"]
    autname=["Marcel Proust","James Joyce","Miguel de Cervantes","F. Scott Fitzgerald","Gabriel Garcia Marquez","Herman Melville","Leo Tolstoy","Vladimir Nabokov","William Shakespeare","J. D. Salinger","Homer","Fyodor Dostoyevsky","Fyodor Dostoyevsky","Gustave Flaubert"," by Dante Alighieri","Mark Twain","Lewis Carroll","Jane Austen","Emily Brontë","Virginia Woolf"]
    genres=["Fiction","Non-Fiction","Action","Autobiography","Biography","Classic","Diary","Fiction","Non-Fiction","Action","Autobiography","Biography","Classic","Diary","Fiction","Non-Fiction","Action","Autobiography","Biography","Classic"    ]
    for m in range(0,20):
        b=bnames[m]
        a=autname[m]
        g=genres[m]
        nu=str(m)
        l="English"
        cursor.execute("insert into books values('" + nu + "','" + b + "','" + g + "','" + a + "','" + l + "','New Arrival')")
    mydb.commit()
    cursor.execute('insert into library_master values("7777777777","Aarya","7777777777","wkjhdio","2003-07-07")')
    cursor.execute('insert into library_master values("9999999999","Bhuvan","9999999999","wkjhdio","2003-06-21")')
    cursor.execute('insert into library_master values("5555555555","Kushagra","5555555555","wkjhdio","2003-09-14")')
    mydb.commit()
else:
    unread=cursor.fetchall()
Program = True
while Program == True:

    cursor.execute("select cardno from library_master")
    cardnos = cursor.fetchall()
    cursor.execute("select count(*) from library_master")
    cont = cursor.fetchall()
    mydb.close()
    mydb = sql.connect(host="localhost", user="root", passwd="mysql@123")
    cursor = mydb.cursor()
    cursor.execute("use library")
    cursor.execute("select book_name from books")
    books = cursor.fetchall()
    mydb.close()
    mydb = sql.connect(host="localhost", user="root", passwd="mysql@123")
    cursor = mydb.cursor()
    cursor.execute("use library")
    cursor.execute("select book_no from books")
    bookno = cursor.fetchall()
    mydb.close()
    mydb = sql.connect(host="localhost", user="root", passwd="mysql@123")
    cursor = mydb.cursor()
    cursor.execute("use library")
    cursor.execute("select book_name from books")
    books = cursor.fetchall()
    mydb.close()
    mydb = sql.connect(host="localhost", user="root", passwd="mysql@123")
    cursor = mydb.cursor()
    cursor.execute("use library")
    cursor.execute("select book_no from books")
    bookno = cursor.fetchall()
    n = cont[0]
    cardno = ""
    name_of_person = ""
    phone_no = ""
    address = ""
    dob = ""
    name_of_personN = ""
    mydb = sql.connect(host="localhost", user="root", passwd="mysql@123")
    cursor = mydb.cursor()
    cursor.execute("use library")
    cursor.execute("select book_no from books")
    bookno = cursor.fetchall()
    returnby = datetime.date.today()


    def create_id():
        print("FILL ALL PERSONAL DETAILS OF ACCOUNT HOLDER")
        speak("FILL ALL PERSONAL DETAILS OF ACCOUNT HOLDER")
        for x in range(0, 100):
            cardno = str(input("enter 10 digit card number:"))
            if (len(cardno) == 10) and not any(cardno in i for i in cardnos) and cardno.isdecimal():
                break
            elif any(cardno in i for i in cardnos):
                print("Card number already exists")
                continue
            elif not (len(cardno) == 10):
                print("Card number must have 10 digits")
                continue
            elif cardno.isalpha():
                print("card number must contain only digits")
        for i in range(0, 100):
            name_of_person = str(input("Enter name (limit 30 characters):"))
            if (len(name_of_person) < 30):
                break
            else:
                print("Name can have only 30 characters")
        for i in range(0, 100):
            phone_no = str(input("Enter phone number:"))
            if (len(phone_no) == 10) and phone_no.isdecimal():
                break
            else:
                print("Invalid phone number")
        for i in range(0, 100):
            address = str(input("Enter the address (max 30 words):"))
            nw = len(address.split())
            if nw < 30:
                break
            else:
                print("max 30 words")
        for i in range(0, 100):
            dob = input(
                "Enter the date of birth(yyyy-mm-dd)\nIF NOT ENTERED IN PROPER FORMAT PROGRAM WILL TERMINATE:\n")
            year, month, day = dob.split('-')
            isValidDate = True
            try:
                datetime.datetime(int(year), int(month), int(day))
            except ValueError:
                isValidDate = False
            if (isValidDate):
                break
            else:
                print("Input date in (yyyy-mm-dd) format")
        cursor.execute(
            "insert into library_master values('" + cardno + "','" + name_of_person + "','" + phone_no + "','" + address + "','" + dob + "')")
        mydb.commit()
        print("ACCOUNT HAS BEEN SUCCESSFULLY CREATED !! !")


    orderno = ''

    print("""
|   create a new account    |   display account information   |   update card holder information   |  delete account      |  
|                           |                                 |                                    |                      |
|   add new book            |   display book details          |   update book details              |  delete book         |   
|                           |                                 |                                    |                      |
|   borrow a book           |   return a book                 |   display borrowing history        |   order a new book   |
|                           |                                 |                                    |                      |
|   display ordered books   |   update order details          |   display ordering history         |   EXIT               |""")
    print("\nWait for Listening... then speak ")

    speak("tell me your choice")
    query = takeCommand().lower()

    if 'create a new account' in query:
        speak("you chose to create an account")
        create_id()

    # TO CREATE A LIBRARY ACCOUNT

    # TO SEE DETAILS OF CARD HOLDER
    elif 'display account information' in query:
        speak("you selected display account information")
        for x in range(0, 100):
            cardno = str(input("Enter card number:"))
            if any(cardno in i for i in cardnos):
                break
            else:
                print("Card number does not exist")
                cho = int(input("1:to create an account /n 2:enter card number again"))
                if cho == 1:
                    create_id()
                    break
                if cho == 2:
                    continue
        cursor.execute("select  *  from library_master where cardno='" + cardno + "'")
        for i in cursor:
            print(i)
        continue
    # TO UPDATE CARD HOLDER INFORMATION

    elif 'update card holder information' in query:
        speak("you have selected to update card holder information")
        for x in range(0, 100):
                print("press 1 to update name:")
                print(" ")
                print("press 2 to update phone number:")
                print(" ")
                print("press 3 to update address:")
                print(" ")
                print("press 4 to update date of birth:")
                print(" ")
                print("press 5 to go back to previous menu:")
                print(" ")
                speak(
                    "press 1 to update name. press 2 to update phone number. press 3 to update address. press 4 to update date of birth. press 5 to go back to previous menu.")
                speak("enter your choice")
                ch1 = int(input("Enter your choice:"))

                # TO UPDATE NAME

                if ch1 == 1:
                    for x in range(0, 100):
                        cursor.execute("select * from library_master")
                        for j in cursor:
                            print(j)
                        cardno = str(
                            input("Enter card number:"))
                        speak("Enter card number")
                        if any(cardno in i for i in cardnos):
                            name_of_personN = str(input("Enter new name:"))
                            cursor.execute(
                                "update library_master set name_of_person='" + name_of_personN + "' where cardno='" + cardno + "'")
                            mydb.commit()
                            print("*Name has been updated*")
                            speak("Name has been updated")
                            cursor.execute("select * from library_master")
                            for b in cursor:
                                print(b)
                            break
                        else:
                            print("Card number does not exist")
                            speak("Card number does not exist")
                            cho = int(input("1:to create an account /n 2:enter card number again"))
                            if cho == 1:
                                create_id()
                                break
                            if cho == 2:
                                continue
                        break

                # TO UPDATE PHONE NUMBER

                if ch1 == 2:
                    cursor.execute("select * from library_master")
                    for i in cursor:
                        print(i)
                    for i in range(0, 100):
                        cardno = str(
                            input("Enter card number:"))
                        speak("Enter card number")  # corresponding card number (card number entered previously)
                        if any(cardno in i for i in cardnos):
                            for i in range(0, 100):
                                phone_no = str(input("Enter new phone number:"))
                                speak("Enter new phone number")
                                if (len(phone_no) == 10) and cardno.isdecimal():
                                    break
                                else:
                                    print("Invalid phone number")
                                    speak("Invalid phone number")
                            cursor.execute(
                                "update library_master set phone_no='" + phone_no + "' where cardno='" + cardno + "'")
                            mydb.commit()
                            print("*Number has been updated*")
                            speak("your number has been updated")
                            cursor.execute("select * from library_master")
                            for j in cursor:
                                print(j)
                            break
                        else:
                            print("Card number does not exist")
                            cho = int(input("1:to create an account /n 2:enter card number again"))
                            if cho == 1:
                                create_id()
                                break
                            if cho == 2:
                                continue
                        break
                        # TO UPDATE ADDRESS

                if ch1 == 3:
                    cursor.execute("select * from library_master")
                    for i in cursor:
                        print(i)
                    for x in range(0, 100):
                        cardno = str(
                            input("Enter card number:"))
                        if any(cardno in i for i in cardnos):
                            address = str(input("Enter new address:"))
                            cursor.execute(
                                "update library_master set address='" + address + "' where cardno='" + cardno + "'")
                            mydb.commit()
                            print("*Address has been updated*")
                            cursor.execute("select * from library_master")
                            for j in cursor:
                                print(j)
                            break
                        else:
                            print("Card number does not exist")
                            cho = int(input("1:to create an account /n 2:enter card number again"))
                            if cho == 1:
                                create_id()
                                break
                            if cho == 2:
                                continue
                        break

                    # TO UPDATE DATE OF BIRTH

                if ch1 == 4:
                    cursor.execute("select * from library_master")
                    for i in cursor:
                        print(i)
                    for x in range(0, 100):
                        cardno = str(input("Enter card number:"))
                        if any(cardno in i for i in cardnos):
                            dob = str(input("Enter new date of birth(yyyy-mm-dd):"))
                            cursor.execute("update library_master set dob='" + dob + "' where cardno='" + cardno + "'")
                            mydb.commit()
                            print("*Date of birth has been updated*")
                            cursor.execute("select * from library_master")
                            for i in cursor:
                                print(i)
                            break
                        else:
                            print("Card number does not exist")
                            cho = int(input("1:to create an account /n 2:enter card number again"))
                            if cho == 1:
                                create_id()
                                break
                            if cho == 2:
                                continue
                        break
                if ch1 == 5:
                    break
            # TO DELETE AN ACCOUNT

    elif 'delete account' in query:
        speak("you have opted to delete account")
        cursor.execute("select * from library_master")
        for i in cursor:
            print(i)
        for x in range(0, 100):
            cardno = str(input("Enter card number:"))
            if any(cardno in i for i in cardnos):
                cursor.execute("delete from library_master where cardno='" + cardno + "'")
                mydb.commit()
                print("*Removed successfully*")
                cursor.execute("select * from library_master")
                for i in cursor:
                    print(i)
                break
            else:
                print("Card number does not exist")
                cho = int(input("1:to create an account /n 2:enter card number again"))
                if cho == 1:
                    create_id()
                    break
                if cho == 2:
                    continue
        continue

    # TO ADD NEW BOOK

    elif 'add new book' in query:
        speak("you have opted to donate a new book to the library")
        for x in range(0, 100):
            cardno = str(input("Enter card number:"))
            if any(cardno in i for i in cardnos):
                print("FILL ALL BOOK DETAILS ")
                for i in range(0, 100):
                    book_name = str(input("enter book  name:"))
                    if any(book_name in i for i in books):
                        print("Book already exists")
                        continue
                    else:
                        break
                for i in range(0, 100):
                    book_no = str(input("Enter number (limit 5 digits):"))
                    if not any(book_no in i for i in bookno) and len(book_no) <= 5 and book_no.isdigit():
                        break
                    elif len(book_no) >= 5:
                        print("Book no limit 5 digits")
                        continue
                    elif not book_no.isdigit():
                        print("Must be only digits")
                    else:
                        print("Book with this no already exists")
                        continue
                for i in range(0, 100):
                    genre = str(input("Enter genre:"))
                    if len(genre) < 30:
                        break
                    else:
                        continue
                for i in range(0, 100):
                    authors_name = str(input("Enter the authors name (max 30 letters):"))
                    if len(authors_name) > 30:
                        print("Author name limit 30 characters")
                        continue
                    else:
                        break
                language = str(input("Enter the language of book:"))
                cursor.execute(
                    "insert into books values('" + book_no + "','" + book_name + "','" + genre + "','" + authors_name + "','" + language + "','New Arrival')")
                mydb.commit()
                print("Book added successfully*")
                speak("Book added successfully")
                for j in cursor:
                    print(j)
                break
            else:
                print("Card number does not exist")
                cho = int(input("1:to create an account /n 2:enter card number again"))
                if cho == 1:
                    create_id()
                    break
                if cho == 2:
                    continue
            continue
            # TO SEE BOOK DETAILS
    elif 'display book details' in query:
        speak("you have opted to see book details")
        cursor.execute("select book_no,book_name from books order by book_no+0")
        b = cursor.fetchall()
        for row in b:
            print(row)
        for x in range(0, 100):
            book_no = str(input("Enter Book Number:"))
            if bookno == None:
                print("No books please choose to add new books")
                speak("No books. Please choose to add book")
                break
            if any(book_no in i for i in bookno) and len(book_no) <= 5:
                break
            elif len(book_no) >= 5:
                print("Book no limit 5 digits")
                speak("book number limit is 5 digits")
                continue
            elif not any(book_no in i for i in bookno):
                print("Book no doesn't exist")
                speak("book does not exit")
                continue
        cursor.execute("select  *  from books where book_no='" + book_no + "'")
        for i in cursor:
            print(i)
        continue
        # TO UPDATE BOOK DETAILS

    elif 'update book details' in query:
        speak("you have chosen to update book details")
        for i in range(0, 100):
            cardno = str(input("Enter card number:"))
            if any(cardno in i for i in cardnos):
                break
            else:
                print("Card number does not exist")
                cho = int(input("1:to create an account /n 2:enter card number again"))
                if cho == 1:
                    create_id()
                    break
                if cho == 2:
                    continue
        for x in range(100):
                print("press 1 to update Book name")
                print(" ")
                print("press 2 to update genre")
                print(" ")
                print("press 3 to update Author Name")
                print(" ")
                print("press 4 to update Language")
                print(" ")
                print("press 5 to exit")
                print("")
                speak("enter your choice")
                ch1 = int(input("Enter your choice:"))
                if ch1 == 1:
                    cursor.execute("select book_no,book_name from books order by book_no+0")
                    for a in cursor:
                        print(a)
                    for k in range(0, 100):
                        book_no = str(input("Enter book number:"))
                        if any(book_no in i for i in bookno) and len(book_no) <= 5:
                            break
                        elif len(book_no) >= 5:
                            print("Book no limit 5 digits")
                            continue
                        elif not any(book_no in i for i in bookno):
                            print("Book no doesnt exist")
                            continue
                    name_of_book = str(input("Enter new name:"))
                    cursor.execute(
                        "update books set book_name='" + name_of_book + "' where book_no='" + book_no + "'")
                    mydb.commit()
                    print("*Name has been updated*")
                    cursor.execute("select * from books order by book_no+0")
                    for i in cursor:
                        print(i)
                    # TO UPDATE GENRE

                if ch1 == 2:
                    cursor.execute("select book_no,book_name,genre from books order by book_no+0")
                    for i in cursor:
                        print(i)
                    for i in range(0, 100):
                        book_no = str(input("Enter book number:"))
                        if any(book_no in i for i in bookno) and len(book_no) <= 5:
                            break
                        elif len(book_no) >= 5:
                            print("Book no limit 5 digits")
                            continue
                        elif not any(book_no in i for i in bookno):
                            print("Book no doesnt exist")
                            continue
                    genre = str(input("Enter new genre:"))
                    cursor.execute("update books set genre='" + genre + "' where book_no='" + book_no + "'")
                    mydb.commit()
                    print("*Genre has been updated*")
                    cursor.execute("select * from books order by book_no+0")
                    for j in cursor:
                        print(j)

                # TO UPDATE AUTHOR NAME

                if ch1 == 3:
                    cursor.execute("select book_no,book_name,authors_name from books order by book_no+0")
                    for i in cursor:
                        print(i)
                    book_no = str(input("Enter book number:"))
                    for i in range(100):
                        if any(book_no in i for i in bookno) and len(book_no) <= 5:
                            break
                        elif len(book_no) >= 5:
                            print("Book no limit 5 digits")
                            continue
                        elif not any(book_no in i for i in bookno):
                            print("Book no doesnt exist")
                            continue
                    author = str(input("Enter new authors name:"))
                    cursor.execute(
                        "update books set authors_name='" + author + "' where book_no='" + book_no + "'")
                    mydb.commit()
                    print("*Authors name has been updated*")
                    cursor.execute("select * from books order by book_no+0")
                    for i in cursor:
                        print(i)

                # TO UPDATE LANGUAGE

                if ch1 == 4:
                    cursor.execute("select book_no,book_name,language from books order by book_no+0")
                    for i in cursor:
                        print(i)
                    book_no = str(input("Enter book number:"))
                    for i in range(100):
                        if any(book_no in i for i in bookno) and len(book_no) <= 5:
                            break
                        elif len(book_no) >= 5:
                            print("Book no limit 5 digits")
                            continue
                        elif not any(book_no in i for i in bookno):
                            print("Book no doesnt exist")
                            continue
                    language = str(input("Enter new language:"))
                    cursor.execute("update books set language='" + language + "' where book_no='" + book_no + "'")
                    mydb.commit()
                    print("*Language has been updated*")
                    cursor.execute("select * from books order by book_no+0")
                    for i in cursor:
                        print(i)
                if ch1 == 5:
                    break

        continue
    # TO DELETE A BOOK

    elif 'delete book' in query:
        speak("you have opted to delete book")
        for i in range(0, 100):
            cardno = str(input("Enter card number:"))
            if any(cardno in i for i in cardnos):
                cursor.execute("select book_no,book_name from books order by book_no+0")
                for i in cursor:
                    print(i)
                for b in range(1, 100):
                    book_no = str(input("Enter book number:"))
                    cursor.execute("delete from books where book_no='" + book_no + "'")
                    mydb.commit()
                    print("*Removed successfully*")
                    cursor.execute("select * from books order by book_no+0")
                    for i in cursor:
                        print(i)
                    break
                break


            else:
                print("Card number does not exist")
                cho = int(input("1:to create an account /n 2:enter card number again"))
                if cho == 1:
                    create_id()
                    break
                if cho == 2:
                    continue
        continue

    # TO BORROW A BOOK

    elif 'borrow a book' in query:
        speak("you have opted to borrow a book")
        for i in range(0, 100):
            cardno = str(input("Enter card number:"))
            if any(cardno in i for i in cardnos):
                cursor.execute("select date_of_lend from library_transaction where cardno=""'" + cardno + "'")
                ck=cursor.fetchall()
                if ck !=[]:
                    print("You can borrow only one book at a time")
                    speak("You can borrow only one book at a time")
                    break
                cursor.execute("select book_no,book_name from books where status!='Borrowed' order by book_no+0")
                for i in cursor:
                    print(i)
                bno = str(input("Enter book number:"))
                cursor.execute("select book_name from books where book_no=""'"+bno+"'")
                bona=str(cursor.fetchall())
                bkna = ''
                for i in range(len(bona)):
                    if ((bona[i] >= 'A' and bona[i] <= 'Z') or (bona[i] >= 'a' and bona[i] <= 'z')):
                        bkna += bona[i]
                date_of_lend = datetime.date.today()
                dlends = date_of_lend.strftime('%Y/%m/%d')
                returnby = date_of_lend + datetime.timedelta(weeks=3)
                retbys = returnby.strftime('%Y/%m/%d')
                print(
                    "Return book withing three weeks\nReturn by:" + retbys + "\nElse pay a fine of Rs100 for every day delayed")
                cursor.execute("insert into library_transaction (cardno,book_name,date_of_lend,return_by) values('" + cardno + "','" + bno+ "','" + dlends + "','" + retbys + "')")
                cursor.execute("update books set status='Borrowed' where book_no=""'"+bno+"'")
                cursor.execute("insert into borrow_history values(""'"+cardno+"','"+bno+"','"+bkna+"','Not returned')")
                cursor.execute("update books set status='Borrowed' where book_no=""'"+bno+"'")
                mydb.commit()
                break
            else:
                print("Card number does not exist")
                cho = int(input("1:to create an account /n 2:enter card number again"))
                if cho == 1:
                    create_id()
                    break
                if cho == 2:
                    continue
        continue

    # TO RETURN A BOOK

    elif 'return a book' in query:
        speak("you have opted to return a book")
        for k in range(0, 100):
            cardno = str(input("Enter card number:"))
            if any(cardno in i for i in cardnos):
                cursor.execute("select borrowed_books from borrow_history where cardno=""'" + cardno + "'")
                check = cursor.fetchall()
                if check == [] or check == ["None"]:
                    print("You have not borrowed a book")
                    speak("You have not borrowed a book")
                    break
                cursor.execute("select book_name from library_transaction where cardno=""'" + cardno + "'")
                borbooklst = str(cursor.fetchall())
                bkn = ''
                for i in range(len(borbooklst)):
                    if ((borbooklst[i] >= 'A' and borbooklst[i] <= 'Z') or (
                            borbooklst[i] >= 'a' and borbooklst[i] <= 'z')):
                        bkn += borbooklst[i]
                cursor.execute("select book_no from books where book_name=""'" + bkn + "' order by book_no+0")
                bnlst = str(cursor.fetchall())
                bn = ""
                for i in range(len(bnlst)):
                    if (bnlst[i].isdigit()):
                        bn = bn + bnlst[i]
                if any(cardno in i for i in cardnos) and check != None:
                    for a in range(0, 100):
                        date_of_return = input("Enter date of returning(yyyy-mm-dd):")
                        year, month, day = date_of_return.split('-')
                        isValidDate = True
                        try:
                            date_of_return = datetime.date(int(year), int(month), int(day))
                        except ValueError:
                            isValidDate = False
                        if (isValidDate):
                            break
                        else:
                            print("Input date in (yyyy-mm-dd) format")
                    cursor.execute("select date_of_lend from library_transaction where cardno=""'" + cardno + "'")
                    date_of_lent1 = str(cursor.fetchall())
                    z1 = ''
                    z2 = ''
                    for j in date_of_lent1:
                        if j.isnumeric() or j.isspace():
                            z1 = z1 + j
                    zf1 = z1.replace(" ", "-")
                    year, month, day = zf1.split('-')
                    date_of_lent = datetime.date(int(year), int(month), int(day))
                    cursor.execute("select return_by from library_transaction where cardno=""'" + cardno + "'")
                    returnby1 = str(cursor.fetchall())
                    for j in returnby1:
                        if j.isnumeric() or j.isspace():
                            z2 = z2 + j
                    zf2 = z2.replace(" ", "-")
                    year, month, day = zf2.split('-')
                    returnby = datetime.date(int(year), int(month), int(day))
                    if date_of_return > returnby:
                        print("Delayed return")
                        delay = (date_of_return - returnby).days
                        pay_fine = delay * 10
                        print("Delayed by ", delay, " pay fine of ", pay_fine)
                    elif date_of_return < returnby and date_of_return > date_of_lent:
                        print("Return before due date\n no fine!!")
                    elif date_of_return < date_of_lent:
                        print("Enter a valid date\nDate entered is before date of borrowing")
                        continue
                    cursor.execute("update library_transaction set date_of_return='" + str(
                        date_of_return) + "' where cardno='" + cardno + "'")
                    cursor.execute(
                        "update library_transaction set pay_fine='" + str(pay_fine) + "' where cardno='" + cardno + "'")
                    cursor.execute("update books set status='Available' where book_no=""'" + bn + "'")
                    cursor.execute("update borrow_history set returned_books=""'" + bn + "'")
                    cursor.execute("update borrow_history set borrowed_books='None'")
                    mydb.commit()
                    break
                elif not any(cardno in i for i in cardnos):
                    print("Card number does not exist")
                    cho = int(input("1:to create an account /n 2:enter card number again"))
                    if cho == 1:
                        create_id()
                        break
                    if cho == 2:
                        continue
                continue
            else:
                print("Card number does not exist")
                cho = int(input("1:to create an account /n 2:enter card number again"))
                if cho == 1:
                    create_id()
                    break
                if cho == 2:
                    continue
        continue
    # TO SEE BORROWING HISTORY

    elif 'display borrowing history' in query:
        speak("you have opted to see borrowing history")
        for i in range(0, 100):
            cardno = str(input("Enter card number:"))
            if any(cardno in i for i in cardnos):
                cursor.execute("select  *  from library_transaction where cardno='" + cardno + "'")
                c=cursor.fetchall()
                if c == []:
                    print("There are no transactions in your name")
                for k in c:
                    print(k)
                break
            else:
                print("Card number does not exist")
                cho = int(input("1:to create an account /n 2:enter card number again"))
                if cho == 1:
                    create_id()
                    break
                if cho == 2:
                    continue
            continue
    # TO ORDER A NEW BOOK

    elif 'order a new book' in query:
        speak("you have opted to order a new book")
        for i in range (100):
            cardno = str(input("Enter card number:"))
            if any(cardno in i for i in cardnos):
                orderno = str(random.randint(0, 999999))
                name_of_book = str(input("Enter the name of the book:"))
                del_date = ""
                for j in range(0, 100):
                    del_date = input("enter the expected delivery date of books(yyyy-mm-dd):")
                    today = str(datetime.date.today())
                    year, month, day = del_date.split('-')
                    isValidDate = True
                    try:
                        del_date = datetime.date(int(year), int(month), int(day))
                    except ValueError:
                        isValidDate = False
                    if (isValidDate):
                        if del_date >= today:
                            break
                        if del_date <= today:
                            print("Enter a future date")
                            continue
                    else:
                        print("Input date in (yyyy-mm-dd) format")
                for k in range(100):
                    price = str(input("Enter the price of the book:Rs"))
                    if price.isdigit():
                        break
                    else:
                        print("Price can only contain digirs not alphabets and special characters ")
                        continue
                cursor.execute("insert into buy_new_books values('" + orderno + "','" +cardno+ "','" + name_of_book + "','" + str(del_date) + "','" + price + "','Not delivered')")
                mydb.commit()
                break
            else:
                print("Card number does not exist")
                cho = int(input("1:to create an account /n 2:enter card number again"))
                if cho == 1:
                    create_id()
                    break
                if cho == 2:
                    continue

    # TO DISPLAY ALL ORDERED BOOKS
    elif 'display ordered books' in query:
        speak("you have opted see all ordered books")
        cursor.execute("select orderno,name_of_book from buy_new_books")
        for i in cursor:
            print(i)
    # TO UPDATE ORDER DETAILS

    elif 'update order details' in query:
        speak("you have opted to update order details")
        for i in range (100):
            cardno = str(input("Enter card number:"))
            if any(cardno in i for i in cardnos):
                cursor.execute("select orderno from buy_new_books where ordered_by='" + cardno + "'")
                orno = cursor.fetchall()
                if orno == []:
                    print("You have not ordered any books")
                    break
                if any(cardno in i for i in cardnos):
                    for i in range(100):
                        print("press 1 to update name of book\n")
                        print("press 2 to update delivery date\n")
                        print("press 3 to update price\n")
                        print("press 4 to update delivery status\n")
                        print("press 5 to exit")
                        ch1 = int(input("Enter your choice:"))
                        # TO UPDATE BOOK NAME
                        if ch1 == 1:
                            if any(cardno in i for i in cardnos):
                                cursor.execute("select * from buy_new_books")
                                for i in cursor:
                                    print(i)
                                    orderno = str(input("Enter order number:"))
                                    name_of_book = str(input("Enter new name:"))
                                    cursor.execute(
                                        "update buy_new_books set name_of_book='" + name_of_book + "' where orderno='" + orderno + "'")
                                    mydb.commit()
                                    print("*Name has been updated*")
                                    cursor.execute("select * from buy_new_books")
                                    for i in cursor:
                                        print(i)
                            continue
                        # TO UPDATE DELIVERY DATE

                        if ch1 == 2:
                            if any(cardno in i for i in cardnos):
                                cursor.execute("select * from buy_new_books")
                                for i in cursor:
                                    print(i)
                                    orderno = str(input("Enter order number:"))
                                    for i in range(0, 100):
                                        del_date = str(input("enter the expected delivery date of books(yyyy-mm-dd):"))
                                        today = str(datetime.date.today())
                                        year, month, day = del_date.split('-')
                                        isValidDate = True
                                        try:
                                            datetime.datetime(int(year), int(month), int(day))
                                        except ValueError:
                                            isValidDate = False
                                        if (isValidDate):
                                            if del_date >= today:
                                                break
                                            if del_date <= today:
                                                print("Enter a future date")
                                                continue
                                        else:
                                            print("Input date in (yyyy-mm-dd) format")
                                        cursor.execute(
                                            "update buy_new_books set del_date='" + del_date + "' where orderno='" + orderno + "'")
                                        mydb.commit()
                                        print("*Delivery date has been updated*")
                                        cursor.execute("select * from buy_new_books")
                                        for i in cursor:
                                            print(i)
                            continue

                        # TO UPDATE PRICE

                        if ch1 == 3:
                            if any(cardno in i for i in cardnos):
                                cursor.execute("select * from buy_new_books")
                                for i in cursor:
                                    print(i)
                                    orderno = str(input("Enter order number:"))
                                    for k in range(100):
                                        price = str(input("Enter the price of the book:Rs"))
                                        if price.isdigit():
                                            break
                                        else:
                                            print("Price can only contain digirs not alphabets and special characters ")
                                            continue
                                    cursor.execute(
                                        "update buy_new_books set price='" + price + "' where orderno='" + orderno + "'")
                                    mydb.commit()
                                    print("*Price has been updated*")
                                    cursor.execute("select * from buy_new_books")
                                    for i in cursor:
                                        print(i)
                            continue

                        # TO UPDATE DELIVERY STATUS

                        if ch1 == 4:
                            if any(cardno in i for i in cardnos):
                                cursor.execute("select * from buy_new_books")
                                for i in cursor:
                                    print(i)
                                orderno = str(input("Enter order number:"))
                                status = input("Enter delivery status:")
                                cursor.execute(
                                    "update buy_new_books set status='" + status + "' where orderno='" + orderno + "'")
                                mydb.commit()
                                print("*Status has been updated*")
                                cursor.execute("select * from buy_new_books")
                                for i in cursor:
                                    print(i)
                            continue
                        elif ch1 == 5:
                            break
                        else:
                            print("Enter a valid choice")
                            continue
                    break
                else:
                    print("Card number does not exist")
                    cho = int(input("1:to create an account /n 2:enter card number again"))
                    if cho == 1:
                        create_id()
                        break
                    if cho == 2:
                        continue
            else:
                print("Card number does not exist")
                cho = int(input("1:to create an account /n 2:enter card number again"))
                if cho == 1:
                    create_id()
                    break
                if cho == 2:
                    continue
    # TO DISPLAY ORDERING HISTORY

    elif 'display ordering history' in query:
        speak("you have opted to see ordering history")
        for i in range(100):
            cardno = str(input("Enter card number:"))
            if any(cardno in i for i in cardnos):
                orderno = str(input("Enter order number:"))
                cursor.execute("select * from buy_new_books where ordered_by='" + cardno + "'")
                ck=cursor.fetchall()
                if ck ==[]:
                    print("You have not ordered and books")
                for i in ck:
                    print(i)
                break
        continue
    # TO EXIT THE PROGRAM

    elif 'exit' in query:
        print("Thank you for using LIBRARY MANAGEMENT")
        speak("Thank you for using LIBRARY MANAGEMENT")
        Program = False

    else:
        print("I didn't get you please repeat")
        speak("I didn't get you please repeat")

