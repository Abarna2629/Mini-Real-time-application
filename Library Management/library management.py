import os
import random
import datetime
admin=[{'name':'admin1','pass':'1','Email':'admin1@gmail.com'},{'name':'admin2','pass':'2','Email':'admin2@gmail.com'}]
user=[{'name':'user1','pass':'1','Email':'user1@gmail.com','wallet':2000,'ordercount':0},{'name':'user2','pass':'2','Email':'user2@gmail.com','wallet':2000,'ordercount':0}]
books=[{'book_name':'My life,My vision','author':'Baba Ramdev','isbn':1000,'rent':100,'stock':5,'price':450},
        {'book_name':'Darkness to light','author':'Lamar Odom','isbn':1001,'rent':150,'stock':10,'price':450},
        {'book_name':'We are Displaced','author':'Malala Yousafzai','isbn':1002,'rent':50,'stock':15,'price':500},
        {'book_name':'My Journey','author':'APJ','isbn':1003,'rent':150,'stock':20,'price':450},
        {'book_name':'Wings of fire','author':'APJ','isbn':1004,'rent':150,'stock':25,'price':450}]
cart_list=[]
book_history=[]
initial_stock=[{'book_name':'My life,My vision','stock':5},{'book_name':'Darkness to light','stock':10},{'book_name':'We are Displaced','stock':15},
                {'book_name':'My Journey','stock':10},{'book_name':'Wings of fire','stock':10}]
status=[]
sample=[]
id=0
#to generate random number
def randomnum():
    randomlist = []
    for i in range(1):
        n = random.randint(1000, 9000)
        randomlist.append(n)
    return randomlist[0]
#admin login
def adm():
    while(True):
        print("\t-----LOGIN TO CONTINUE-----")
        print("1.Login\n2.Logout")
        b=int(input("Enter choice : "))
        if(b==1):
            admin_email=input("Enter admin's mail : ")
            admin_password=input("Enter admin's password : ")
            for i in admin:
                if(i['Email']==admin_email and i['pass']==admin_password):
                    print("\n")
                    os.system('cls')
                    print("\tWELCOME",i['name'],"!!!")
                    input("\tPress Enter to continue.....")
                    admin_options()
            else:
                print("Admin not found")
        elif(b==2):
            break
#admin options
def admin_options():
    while(True):
        print("1.Add admin\n2.Add user\n3.Books\n4.Report\n5.View book status\n6.Exit")
        c=int(input("Enter choice : "))
        if(c==1):
            os.system('cls')
            admin_add_admin()
        elif(c==2):
            os.system('cls')
            admin_add_user()
        elif(c==3):
            os.system('cls')
            admin_book()
        elif(c==4):
            os.system('cls')
            admin_report()
        elif(c==5):
            os.system('cls')
            admin_check_book_status()
        elif(c==6):
            break
#admin options---> add admin
def admin_add_admin():
    admin_d={}
    while(True):
        print("\t-----ADD ADMIN-----")
        print("1.Add admin\n2.Exit")
        c=int(input("Enter choice : "))
        if(c==1):
            name=input("Enter admin's name : ")
            passwd=input("Enter admin's password : ")
            email=input("Enter admin's mail : ")
            for i in admin:
                if(name != i['name'] and email != i['Email']):
                    admin_d['name']=name
                    admin_d['pass']=passwd
                    admin_d['Email']=email
                else:
                    print("Email id already exist...\nTry with different name")
            if(len(admin)!=0):
                admin.append(admin_d)
                print("Admin added successfully")
        elif(c==2):
            break
#admin option --->add user
def admin_add_user():
    user_d={}
    while(True):
        print("\t-----ADD USER-----")
        print("1.Add user\n2.Exit")
        c=int(input("Enter choice : "))
        if(c==1):
            name=input("Enter user's name : ")
            passwd=input("Enter user's password : ")
            email=input("Enter user's mail : ")
            for i in user:
                if(name not in i['name'] and email not in i['Email']):
                    user_d['name']=name
                    user_d['pass']=passwd
                    user_d['Email']=email
                    user_d['wallet']=2000
                    user_d['ordercount']=0
                else:
                    print("Email id already exist...\nTry with different name")
            if(len(admin)!=0):
                admin.append(user_d)
                print("User added successfully")
        elif(c==2):
            break
#admin options ---->Books(add books,modify books,View books)
def admin_book():
    while(True):
        print("1.Add books\n2.Modify books\n3.View books\n4.Exit")
        d=int(input("Enter choice : "))
        if(d==1):
            os.system('cls')
            admin_add_book()
        elif(d==2):
            os.system('cls')
            admin_book_modify()
        elif(d==3):
            os.system('cls')
            admin_view_book()
        elif(d==4):
            break
#admin option---->add book---->to add book
def admin_add_book():
    add_books={}
    initial={}
    while(True):
        print("\t-----ADD BOOKS-----")
        print("1.Add books\n2.Exit")
        e=int(input("Enter choice : "))
        if(e==1):
            book_name=input("Enter book name : ")
            book_author=input("Enter book author : ")
            book_isbn=randomnum()
            book_rent=int(input("Enter book rent : "))
            book_stock=int(input("Enter book stock : "))
            book_price=int(input("Enter book price : "))
            for i in books:
                if(i['book_name']!=book_name and i['author']!=book_author):
                    add_books['book_name']=book_name
                    add_books['author']=book_author
                    add_books['isbn']=book_isbn
                    add_books['rent']=book_rent
                    add_books['stock']=book_stock
                    add_books['price']=book_price
                    initial['book_name']=book_name
                    initial['stock']=book_stock
                else:
                    print("Book already exist")
            if(len(books)!=0):
                books.append(add_books)
                print("Books added successfully!!!")
            if(len(initial)!=0):
                initial_stock.append(initial)

        elif(e==2):
            break
#admin option---->modify book---->remove,stock check,stock update
def admin_book_modify():
    while(True):
        print("\t-----MODIFY BOOKS-----")
        print("1.Remove book\n2.Stock Check\n3.Stock update\n4.Exit")
        f=int(input("Enter choice : "))
        if(f==1):#remove book
            os.system('cls')
            admin_remove_book()
        elif(f==2):#stock check
            os.system('cls')
            admin_stock_check()
        elif(f==3):#stock update
            os.system('cls')
            admin_stock_update()
        elif(f==4):
            break
#admin option----->remove book
def admin_remove_book():
    while(True):
        print("\t-----REMOVE BOOK-----")
        print("1.Remove book\n2.Exit")
        g=int(input("Enter choice : "))
        if(g==1):
            name=input("Enter book name : ")
            for i in books:
                if(i['book_name']==name):
                    books.remove(i)
                    print("Book removed successfully!!!")
                else:
                    print("Book not found!!!")
        elif(g==2):
            break
#admin option------>stock check
def admin_stock_check():
    while(True):
        print("\t-----STOCK CHECK-----")
        print("1.Stock check\n2.Exit")
        h=int(input("Enter choice : "))
        if(h==1):
            for i in books:
                print("Book Name : {}\nStock :{}".format(i['book_name'],i['stock']))
                print("\n")
        elif(h==2):
            break
#admin option----->stock update
def admin_stock_update():
    while(True):
        print("\t-----STOCK UPDATE-----")
        print("1.Stock update\n2.Exit")
        a=int(input("Enter choice : "))
        if(a==1):
            name=input("Enter book name : ")
            value=int(input("Enter stock value : "))
            for i in books:
                if(i['book_name']==name):
                    i['stock']+=value
                    print("Stock updated successfully")
        elif(a==2):
            break
#admin option--->view books
def admin_view_book():
    while(True):
        print("\t-----VIEW BOOKS-----")
        print("1.View books\n2.Exit")
        b=int(input("Enter choice : "))
        if(b==1):
            for i in books:
                print("Book name : {},\nISBN :{},\nAuthor : {},\nRent :{},\nStock : {},\nPrice : {}".format(i['book_name'],i['isbn'],i['author'],i['rent'],i['stock'],i['price']))
                print("\n")
        elif(b==2):
            break
#user login
def use():
    while(True):
        print("\t-----LOGIN TO CONTINUE-----")
        print("1.Login\n2.Logout")
        c=int(input("Enter choice : "))
        if(c==1):
            email=input("Enter user's mail : ")
            password=input("Enter user's password : ")
            for i in user:
                if(i['Email']==email and i['pass']==password):
                    w=i
                    print("\n")
                    print("\tLogged in successfully")
                    user_option(w)
            else:
                print("Mail and password does not match")
                   
        elif(c==2):
            break
#user option
def user_option(w):
    os.system('cls')
    while(True):
        print("1.View books\n2.Search book\n3.Borrow book\n4.View history\n5.View cart\n6.Wallet balance\n7.View status\n8.update status\n9.Exit")
        b=int(input("Enter choice : "))
        if(b==1):
            os.system('cls')
            user_view_books()
        elif(b==2):
            os.system('cls')
            user_search_books()
        elif(b==3):
            os.system('cls')
            user_borrow_book(w)
        elif(b==4):
            os.system('cls')
            user_view_booking_history(w)
        elif(b==5):
            os.system('cls')
            user_view_cart()
        elif(b==6):
            os.system('cls')
            user_wallet_balance(w)
        elif(b==7):
            os.system('cls')
            user_check_status(w)
        elif(b==8):
            os.system('cls')
            user_update_book_status(w)
        elif(b==9):
            break
#user option---->view books
def user_view_books():
    cart={}
    global id
    while(True):
        print("\t-----VIEW BOOKS-----")
        print("1.View books\n2.Exit")
        b=int(input("Enter choice : "))
        if(b==1):
            for i in books:
                print("Book name : {},\nISBN :{},\nAuthor : {},\nRent :{},\nStock : {},\nPrice : {}".format(i['book_name'],i['isbn'],i['author'],i['rent'],i['stock'],i['price']))
                print("\n")
        elif(b==2):
            break
#user option---->search books
def user_search_books():
    while(True):
        print("\t-----SEARCH BOOKS-----")
        print("1.Search by Book\n2.Search by Author\n3.Exit")
        c=int(input("Enter choice : "))
        if(c==1):
            os.system('cls')
            user_search_book_name()
        elif(c==2):
            os.system('cls')
            user_search_book_author()
        elif(c==3):
            break
#user option---->search by book
def user_search_book_name():
    global id
    cart={}
    while(True):
        print("\t-----SEARCH BOOK BY NAME")
        print("1.Search book\n2.Exit")
        d=int(input("Enter choice : "))
        if(d==1):
            book_name=input("Enter book name : ")
            for i in books:
                if(i['book_name']==book_name):
                    print("Book name : {},\nISBN :{},\nAuthor : {},\nRent :{},\nStock : {},\nPrice : {}".format(i['book_name'],i['isbn'],i['author'],i['rent'],i['stock'],i['price']))
                    print("\n")
                    
                    print("1.Add to cart\n2.Next\n3.Back\n")
                    e = int(input("Enter your choice: "))
                    if(e == 1):
                        cart_list.append(i)
                        print('Added to cart successfully\n')
                        input("PRESS ENTER TO CONTINUE.....")
                    elif(e == 2):
                        continue
                    elif(e==3):
                        break
        elif(d==2):
            break
#user option---->search book by author
def user_search_book_author():
    global id
    cart={}
    while(True):
        print("\t-----SEARCH BOOK BY NAME")
        print("1.Search book\n2.Exit")
        d=int(input("Enter choice : "))
        if(d==1):
            author_name=input("Enter author name : ")
            for i in books:
                if(i['author']==author_name):
                    print("Book name : {},\nISBN :{},\nAuthor : {},\nRent :{},\nStock : {},\nPrice : {}".format(i['book_name'],i['isbn'],i['author'],i['rent'],i['stock'],i['price']))
                    print("\n")
                    
                    print("1.Add to cart\n2.Next\n3.Back\n")
                    e = int(input("Enter your choice: "))
                    if(e == 1):
                        cart_list.append(i)
                        print('Added to cart successfully\n')
                        input("PRESS ENTER TO CONTINUE.....")
                    elif(e == 2):
                        continue
                    elif(e==3):
                        break
        elif(d==2):
            break
#user option----->view cart
def user_view_cart():
    while(True):
        print("\t-----VIEW CART-----")
        print("1.View cart\n2.Exit")
        d=int(input("Enter choice : "))
        if(d==1):
            if(len(cart_list)!=0):  
                for i in cart_list:
                    print("Book name : {}\nISBN :{},\nAuthor : {}\nRent :{}\nStock : {}\nPrice : {}".format(i['book_name'],i['isbn'],i['author'],i['rent'],i['stock'],i['price']))
                    print("\n")
            else:
                print("No item available in cart")
        elif(d==2):
            break
#user option----->borrow book
def user_borrow_book(w):
    status_d={}
    history={}
    while(True):
        print("\t-----BORROW BOOK-----")
        print("1.Borrow book\n2.Back")
        f=int(input("Enter your choice : "))
        if(f==1):
            for j in cart_list:
                print("Book name : {}\nISBN :{}\nAuthor : {}\nRent :{}\nStock : {}\nPrice : {}".format(j['book_name'],j['isbn'],j['author'],j['rent'],j['stock'],j['price']))
                print("\n")
            name=input("Enter book name : ")
            for i in cart_list:
                if(i not in sample):
                    if(i['book_name']==name):
                        if(i['stock']>=1):
                            i['stock']-=1
                            if(w['wallet']>=500):
                                w['wallet']-=i['rent']
                                #print(w['ordercount'])
                                if(w['ordercount']<=2):
                                    #print(w['ordercount'])
                                    w['ordercount']+=1
                                    print("\nBook borrowed successfully\nBook should be return within given date\n")
                                    d=datetime.datetime.now()

                                    history['User_name']=w['name']
                                    history['book_name']=j['book_name']
                                    history['isbn']=j['isbn']
                                    history['author']=j['author']
                                    history['price']=j['price']
                                    history['borrow Date']=d
                                    history['Due Date']=d+datetime.timedelta(days=14)
                                    book_history.append(history)
                                    cart_list.remove(i)
                                    sample.append(i)

                                    status_d['book_name']=j['book_name']
                                    status_d['User_name']=w['name']
                                    status_d['Borrow Date']=d
                                    status_d['Due Date']=d+datetime.timedelta(days=14)
                                    status_d['Status']='Borrowed'
                                    status.append(status_d)

                                    input("Press enter to continue....")
                                    break
                                else:
                                    print("Order limit has reached")
                                    break
                            else:
                                print("Insufficient balance in wallet")
                                input("\nPress Enter to continue")
                                break
                        else:
                            print("Book out of stock")
                            input("\nPress enter to continue....")
                    else:
                        print("Book does not exist")
                        input("\nPress Enter to continue")
                else:
                    print("Same book cant be borrowed twice\n")
                    input("\nPress enter to continue")
        elif(f==2):
            break
#user option----->check wallet balance
def user_wallet_balance(w):
    while(True):
        print("\t-----WALLET BALANCE-----")
        print("1.Check wallet balance\n2.Exit")
        g=int(input("Enter choice : "))
        if(g==1):
            for i in user:
                print("Your wallet balance is ",w['wallet'])
                input("\tPress Enter to continue")
                break
        elif(g==2):
            break
#to view book history
def user_view_booking_history(w):
    while(True):
        print("\t-----VIEW BOOK HISTORY-----")
        print("1.View history\n2.Exit\n")
        f=int(input("Enter choice : "))
        print("\n")
        if(f==1):
            if(len(book_history)!=0):
                for i in book_history:
                    if(i['User_name']==w['name']):
                        print("Book name : {}\nUsername :{}\nBorrow Date :{}\nDue Date :{}\n".format(i['book_name'],i['User_name'],i['borrow Date'],i['Due Date'],))
                        print()
            else:
                print("No booking history found\n")
        elif(f==2):
            break
#admin report
def admin_report():
    while(True):
        print("1.Less Quantity book\n2.Unused book\n3.Exit")
        val=int(input("Enter choice : "))
        if(val==1):
            os.system('cls')
            print("\t-----LESS QUANTITY BOOK-----")
            l=[]
            for i in books:
                l.append(i['stock'])
            l.sort()
            for i in books:
                if(l[0]==i['stock']):
                    print(i)
            print("\nKindly update the stock!!!")
            input("Press Enter to continue")
            break
        elif(val==2):
            os.system('cls')
            print("****UNUSED BOOKS****\n")
            l = []
            l1 = []
            ind = []
            val_ind = []
            for i in initial_stock:
                l.append(i['stock'])
            for j in books:
                l1.append(j['stock'])
            for i in range(len(l)):
                for j in l1:
                    if(l[i] == j):
                        ind.append(j)
                    else:
                        continue
            for x in ind:
                val_ind.append(l.index(x))
                #print(l)
                #print(l1)
                #print(ind)
                #print(val_ind)
            for i in val_ind:
                for j in books:
                    print(books[i])
                    break
            input("PRESS ENTER TO CONTINUE.....")
        elif(val==3):
            break
# admin option----->book status
def admin_check_book_status():
    while(True):
        print("\t-----CHECK STATUS OF BOOKS-----")
        print("1.Check status\n2.Exit")
        f=int(input("Enter your choice : "))
        if(f==1):
            if(len(status)!=0):
                for i in status:
                    print("Book name : {}\nUsername :{}\nBorrow Date :{}\nDue Date :{}\nStatus : {}".format(i['book_name'],i['User_name'],i['Borrow Date'],i['Due Date'],i['Status']))
                    print() 
            else:
                print("No status found")
        elif(f==2):
            break
#user option---->return book or update book status
def user_update_book_status(w):
    while(True):
        print("\t-----UPDATE BORROWED BOOK STATUS-----")
        print("1.Update book status\n2.Exit")
        a=int(input("Enter choice : "))
        if(a==1):
            for i in status:
                if(i['User_name']==w['name']):
                    print("Book name : {}\nUsername :{}\nBorrow Date :{}\nDue Date :{}\nStatus : {}".format(i['book_name'],i['User_name'],i['Borrow Date'],i['Due Date'],i['Status']))
                    print()
            for i in status:
                if(i['User_name']==w['name']):
                    c=input("Enter Book name : ")
                    if(i['book_name']==c):
                         for k in books:
                            if(k['book_name']==c):
                                amount=k['price']
                                print("1.Return book\n2.Lost book")
                                b=int(input("Enter choice : "))
                                if(b==1):
                                    i['Status']="Returned"
                                    k['stock']+=1
                                    print("Status updated successfully")
                                    
                                elif(b==2):
                                    i['Status']="Lost"
                                    for j in user:
                                        ans=amount/2
                                        j['wallet']-=ans
                                        print("Since you lost the book",c,"half of the book price has been collected as fine\nThe actual price of the book is",amount)
                                        break
                                    print("Status updated Successfully")
                    ##for i in status:
                        #print(i)
        elif(a==2):
            break
#user option---->check status
def user_check_status(w):
    while(True):
        print("\t----CHECK STATUS-----")
        print("1.Check\n2.Exit")
        a=int(input("Enter choice : "))
        if(a==1):
            for i in status:
                if(i['User_name']==w['name']):
                    print("Book name : {}\nUsername :{}\nBorrow Date :{}\nDue Date :{}\nStatus : {}".format(i['book_name'],i['User_name'],i['Borrow Date'],i['Due Date'],i['Status']))
                    print()    
        elif(a==2):
            break
#driver code
while(True):
    print("\t-----WELCOME TO ABC LIBRARY!!!-----")
    print("1.Admin\n2.User\n3.Exit")
    print("\n")
    a=int(input("Enter choice : "))
    if(a==1):
        os.system('cls')
        adm()
    elif(a==2):
        os.system('cls')
        use()
    elif(a==3):
        exit()
    else:
        print("Invalid input")