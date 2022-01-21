import os
import datetime
admins=[{'name':'admin',"passwd":'123'}]
merchants=[{'merchant_id':1,'name':'merch1',"pass":"1",'status':'approved'},
            {'merchant_id':2,'name':'merch2','pass':'2','status':'approved'},
            {'merchant_id':3,'name':'merch3','pass':'3','status':'rejected'},
            {'merchant_id':4,'name':'merch4','pass':'4','status':'approved'}]
users=[{'name':'user1',"pass":"1",'wallet':10000,'order_count':0},
        {'name':'user2','pass':'2','wallet':10000,'order_count':0},
        {'name':'user3',"pass":"3",'wallet':10000,'order_count':0},
        {'name':'user4',"pass":"4",'wallet':10000,'order_count':0}]
category=['electronics','fashion','stationary','accessories']
new_merchants=[]
products=[{'name':'merch1','product_id':'1','product_name':'smart watch','amount':10000,'stock':100,'discount':5,'category':'electronics'},
          {'name':'merch2','product_id':'2','product_name':'water bottle','amount':200,'stock':100,'discount':10,'category':'stationary'},
          {'name':'merch3','product_id':'3','product_name':'note','amount':50,'stock':100,'discount':5,'category':'stationary'},
          {'name':'merch1','product_id':'4','product_name':'pen','amount':100,'stock':10,'discount':10,'category':'stationary'},
          {'name':'merch1','product_id':'5','product_name':'pencil','amount':20,'stock':10,'discount':2,'category':'stationary'},
          {'name':'merch2','product_id':'6','product_name':'perfume','amount':500,'stock':100,'discount':10,'category':'accessories'},
          {'name':'merch2','product_id':'7','product_name':'mouse','amount':200,'stock':100,'discount':5,'category':'electronics'},
          {'name':'merch1','product_id':'7','product_name':'mouse','amount':500,'stock':100,'discount':3,'category':'electronics'},
          {'name':'merch3','product_id':'9','product_name':'smart watch','amount':300,'stock':20,'discount':10,'category':'electronics'},
          {'name':'merch3','product_id':'17','product_name':'mouse','amount':300,'stock':100,'discount':7,'category':'electronics'}]
cart=[]
user_review=[]
order_history=[]
freq_customer=[]
sales_review=[]
print("\t\t WELCOME TO AMAZON")
#print("\n1.Admin\n2.Merchant\n3.User\n4.Exit")
#to verify admins account
def adm():
    print("Welcome Admin")
    print("1.Login\n2.Logout")
    ch=int(input("Enter Admins choice : "))
    if(ch==1):
        name=input("Enter Admin name : ")
        passwd=input("Enter Admins password : ")
        for i in admins:
            if(name== i['name'] and passwd== i['passwd']):
                os.system('cls')
                print("welcome",name)
                while(True):
                    print("1.Add merchant\n2.Remove merchant\n3.Approve merchant\n4.View Merchants\n5.View Products\n6.View category\n7.Add category\n8.Exit")
                    val=int(input("Enter Admins choice : "))
                    if(val==1):
                        os.system('cls')
                        adm_add_merchant()
                    elif(val==2):
                        os.system('cls')
                        adm_remove_merchant()
                    elif(val==3):
                        adm_approve()
                    elif(val==4):
                        os.system('cls')
                        print("\tVIEW MERCHANTS")
                        view_merchants()
                    elif(val==5):
                        os.system('cls')
                        print("\tView available products")
                        for i in products:
                            print("MERCHANT NAME : ",i['name'],"\nPRODUCT_NAME :",i['product_name'],"\nAMOUNT: ",i['amount'],"\nDISCOUNT:",i['discount'],"\nCATEGORY : ",i['category'])
                            print()
                    elif(val==6):
                        os.system('cls')
                        print("\tVIEW CATEGOTORIES")
                        print("\tAVAILABLE CATEGORIES ARE.....")
                        for i in category:
                            print("Category : ",i,sep=' ')
                        print()
                    elif(val==7):
                        os.system('cls')
                        print("\tADD CATEGORY")
                        print("\tAvailable categories are")
                        for i in category:
                            print("CATEGORY ",i)
                        k=input("Enter category:")
                        if(k not in category):
                            category.append(k)
                            print("Category added successfully!!")
                        else:
                            print("Category already exist")
                    
                    elif(val==8):
                        break
                    else:
                        print("Invalid Choice")
            else:
                os.system('cls')
                print("Admin not found!!!")
                input("Enter to continue")
#to add merchant by admin
def adm_add_merchant():
    print("\tADD MERCHANTS")
    d={} 
    while(True):            
        print("1.Add merchant \n2.Exit")
        v=int(input("Enter admin's choice : "))
        if(v==1):
            id=int(input("Enter id : "))
            name=input("Enter merchants name : ")
            passwd=input("Enter merchants password : ")
            flag=1
            for i in merchants:
                if(name==i['name'] ):
                    flag=0
            if(flag==1):
                d['merchant_id']=id
                d['name']=name
                d['pass']=passwd
                d['status']='approved'
                merchants.append(d)
                print("\n")
                print("\tMerchant added successfully")
            else:
                print("\tUser name already exist..\nPlease try again with another name")
        elif(v==2):
            break
#to remove a merchant by admin
def adm_remove_merchant():
    print("\tREMOVE MERCHANTS")
    while(True):
        print("1.Remove merchant\n2.Exit")
        n=int(input("Enter merchant's choice : "))
        if(n==1):
            name=input("Enter merchants name to be removed : ")
            for i in merchants:
                if(i['name']==name):
                    i['status']='removed'
                    print("\tMerchant removed successfully")
                    break
            else:
                print("No such merchant exist")
        elif(n==2):
            break              
# to approve new merchants account by admin
def adm_approve():
    os.system('cls')
    print("\tAPPROVE MERCHANTS")
    print("1.Approve/Reject\n2.Exit")
    val=int(input("Enter choice: "))
    while(True):
        if(val==1):
            if(len(new_merchants)!=0):
                for i in new_merchants:
                    print(i)
                    print("1.Yes-- To add merchant\n2.No-- To deny request")
                    n=int(input("Enter choice to accept or reject : "))
                    if(n==1):
                        i['status']='approved'
                        merchants.append(i)
                        print("Merchant added successfully")
                        new_merchants.remove(i)
                        break
                        
                    elif(n==2):
                        i['status']='rejected'
                        print("Merchant rejected")
                        
            else:
                print("No request found")
                break
        elif(val==2):
            break
# to view merchants
def view_merchants():
    if(len(merchants)!=0):
        for i in merchants:
            print("Merchant name : {},\nStatus :{}".format(i['name'],i['status']))
            print("\n")
# to verify merchant account and to add new merchant
#existing merchant-->add product,remove product,stock check,stock update,view your products,compare product,exit
#new merchant-->create account-->wait for admin approval
def merchant():
   while(True):
        d={}
        print("\tWelcome Merchant")
        print("1.Exixting merchant\n2.New merchant\n3.Exit")
        ch=int(input("Enter Merchants choice : "))
        ref=None
        #if merchant exis--->Add product\n2.Remove product\n3.Stock check\n4.Stock update\n5.View your stock\n6.View Review\n7.Exit
        if(ch==1):
            name=input("Enter Merchants name : ")
            passwd=input("Enter Merchants password : ")
            for i in merchants:
                if(name== i['name'] and passwd== i['pass'] and i['status']=='approved'):
                    ref=i
                    print("welcome",name)
                    while(True):
                        print("\n")
                        print("1.Add product\n2.Remove product\n3.Stock check\n4.Stock update\n5.View your product\n6.Compare products\n7.View Review\n8.Frequent customer\n9.sales review\n10.Exit")
                        print("\n\n")
                        val=int(input("Enter merchants choice : "))
                        if(val==1):
                            os.system('cls')
                            print("\twelcome to Add product")
                            merch_add_product(name)
                        elif(val==2):
                            os.system('cls')
                            print("\tWelcome to Remove product")
                            merch_remove_product(name)
                        elif(val==3):
                            os.system('cls')
                            print("\tWelcome to Stock check")
                            merch_stock_check(name)
                        elif(val==4):
                            print("\tWelcome to update stock")
                            merch_stock_update(name)
                        elif(val==5):
                            merch_view_product(name)
                        elif(val==6):
                            merch_compare_product(name)
                        elif(val==7):
                            print("\tWelcome to view the reviews of your product")
                            #print(user_review)
                            view_review(name)
                        elif(val==8):
                            #print(freq_customer)
                            if(len(freq_customer)!=0):
                                for i in freq_customer:
                                    if(i['name']==name):
                                        print("Username : {} \nProductname :{} \nOrdercount :{}".format(i['user_name'],i['product_name'],i['order_count']))
                                        print("\n")
                            else:
                                print("No customer purchased your produc")
                           
                        elif(val==9):
                            salesreview(name)
                        elif(val==10):
                            break
            
                        else:
                            print("Invalid Choice")
                elif(name== i['name'] and passwd== i['pass'] and i['status']=='rejected'):
                    print("Your account has been rejected")
                    break
                elif(name== i['name'] and passwd== i['pass'] and i['status']=='removed'):
                    print("Your account has been removed.\nPlease contact admin to get details")
                    break
                elif(name== i['name'] and passwd== i['pass'] and i['status']=='pending'):
                    print("Your account is still pending for approval..\nTry again later")
                    break
      
        #if merchant does not exist
        elif(ch==2):
            while(True):            
                print("1.Request to approve\n2.Exit")
                v=int(input("Enter merchants's choice : "))
                if(v==1):
                    name=input("Enter merchants name : ")
                    passwd=input("Enter merchants password : ")
                    flag=1
                    for i in users:
                        if(name==i['name'] ):
                            flag=0
                    if(flag==1):
                        d['name']=name
                        d['pass']=passwd
                        d['status']='pending'
                        new_merchants.append(d)
                        merchants.append(d)
                            
                    else:
                        print("User name already exist..\n Please try again with another name")
                elif(v==2):
                    break
        elif(ch==3):
            break           
# to verify user
#if user exist---->1.search\n2.Filter\n3.Order\n4.Add to cart\n5.Exit , # new user
def user():
    while(True):
        d={}
        print("Welcome user")
        print("1.Exixting user\n2.New user\n3.Exit")
        ch=int(input("Enter user choice : "))
#if user exist---->search\n2.Filter\n3.Order\n4.Add to cart\n5.Exit
        if(ch==1):
            name=input("Enter  user name : ")
            passwd=input("Enter user's password : ")
            user=0
            u=None
            for i in users:
                if(name== i['name'] and passwd== i['pass']):
                    user=i
                    u=i['name']
                    os.system('cls')
                    print("\twelcome",name)
                    while(True):
                        print("1.search\n2.Filter\n3.Order\n4.view cart\n5.Check wallet balance\n6.View Order History\n7.Exit")
                        print("\n")
                        val=int(input("Enter users choice : "))
                        print("\n")
                        if(val==1):
                            user_search_product()
                        elif(val==2):
                            while(True):
                                print("1.Filter by brand\n2.Filter by product\n3.Filter by amount\n4.Filter by discount\n5.Exit")
                                print("\n")
                                k=int(input("Enter your choice : "))
                                if(k==1):
                                    user_filter_brand()
                                elif(k==2):
                                    user_filter_product()
                                elif(k==3):
                                    user_filter_amount()
                                elif(k==4):
                                    user_filter_discount()
                                elif(k==5):
                                    break
                        elif(val==3):
                            print("\tPlace your Order here")
                            order(user,u)
                        elif(val==4):
                            os.system('cls')
                            print("\tView your cart")
                            if(len(cart)!=0):
                                for i in cart:
                                    print(i)
                            else:
                                print("No product in your cart")
                        elif(val==5):
                            check_wallet_balance(user)
                        elif(val==6):
                            os.system('cls')
                            print("\tView your Orders Here")
                            if(len(order_history)!=0):
                                for i in order_history:
                                    print(i,sep="\n")
                                print("\n")
                            else:
                                print("No orders places so far...")
                        elif(val==7):
                            break
                        else:
                            print("Invalid Choice")            
# new user
        elif(ch==2):
            os.system('cls')
            d={}
            print("1.Create account\n2.Exit")
            a=int(input("Enter choice : "))
            if(a==1):
                name=input("Enter user name : ")
                passwd=input("Enter password : ")
                flag=1
                for i in users:
                    if(name==i['name'] ):
                        flag=0
                if(flag==1):
                    d['name']=name
                    d['pass']=passwd
                    d['wallet']=20000
                    users.append(d)
                else:
                    print("User name already exist..\n Please try again with another name")
            elif(a==2):
                break
        elif(ch==3):
            break
#to add products by merchant
def merch_add_product(name):
    os.system('cls')
    print("\tADD YOUR PRODUCTS")
    while(True):
        d={}
        count_not=0
        count_in=0
        print("1.Add product\n2.Exit")
        val=int(input("Enter choice : "))
        if(val==1):
            os.system('cls')
            product_id=int(input("Enter product id : "))
            product_name=input("Enter product name : ")
            amount=int(input("Enter product price : "))
            stock=int(input("Enter stock : "))
            discount=int(input("Enter discount amount :"))
            category1=input("Enter product category : ")
            if(category1 in category):
                for i in products:
                    if(product_name not in i['product_name']):
                        count_not+=1
                    else:
                        count_in+=1
                if(count_not==len(products)):
                    d['name']=name
                    d['product_id']=product_id
                    d['product_name']=product_name
                    d['amount']=amount
                    d['stock']=stock
                    d['discount']=discount
                    d['category']=category1
                    products.append(d)
                    print("\n")
                    print("Product added successfully")
                else:
                    print("Product already exist")
                    break
            else:
                print("Category not available")
        elif(val==2):
            break
#to remove products by merchant
def merch_remove_product(name):
    os.system('cls')
    print("\tREMOVE PRODUCT")
    while(True):
        print("1.Remove product\n2.Exit")
        val=int(input("Enter choice : "))
        temp=[]
        if(val==1):
            m=input("Enter product name: ")
            for i in products:
                if(name==i['name']and m==i['product_name']):
                    temp.append(i)
                    products.remove(i)
                    print("\n")
                    print("Product removed successfully!!!")
                    print("\n")
                    break
            
        elif(val==2):
            break
#to check stock
def merch_stock_check(name):
     os.system('cls')
     print("\tCHECK YOUR STOCK")
     while(True):
        print("1.Check stock\n2.Exit")
        val=int(input("Enter choice : "))
        l=[]
        if(val==1):
            if(len(products)!=0):
                for i in products:
                    if(name==i['name']):
                        print("\nPRODUCT NAME : ",i['product_name'],"\nSTOCK : ",i['stock'])
                print("\n")            
            else:
                print("product does not exist")
        elif(val==2):
            break
#to update stock
def merch_stock_update(name):
    os.system('cls')
    print("\tUPDATE YOUR STOCK")
    while(True):
        print("1.Update stock\n2.Exit")
        val=int(input("Enter choice : "))
        if(val==1):
            name1=input("Enter product name : ")
            for i in products:
                if(name==i['name']):
                    if(name1==i['product_name']):
                        stock=int(input("Enter stock value : "))
                        i['stock']+=stock
                        print("\n")
                        break
            else:
                print("Product not found")   
        elif(val==2):
            break
#to view his product by merchant
def merch_view_product(name):
    os.system('cls')
    print("\tWelcome to view your products")
    if(len(products)!=0):
        for i in products:
            if(i['name']==name):
                print("MERCHANT NAME : ",i['name'],"\nPRODUCT_NAME :",i['product_name'],"\nAMOUNT: ",i['amount'],"\nCATEGORY : ",i['category'])
                print()
    else:
        print("No product found")
#discount by merchant
def merch_compare_product(name):
    os.system('cls')
    print('\t welcome to compare products')
    while(True):
        print("1.Compare based on price\n2.Compare based on discount\n3.Exit")
        val=int(input("Enter choice : "))
        if(val==1):
            os.system('cls')
            print("Compare based on price")
            print("\n")
            a=input("Enter product name : ")
            for i in products:
                if(i['product_name']==a):
                    print("BRAND NAME : ",i['name'],"\nPRODUCT NAME : ",i['product_name'],"\nPRICE: ",i['amount'])
                    print()
        elif(val==2):
            os.system('cls')
            print("Compare based on discount")
            print("\n")
            a=input("Enter product name : ")
            for i in products:
                if(i['product_name']==a):
                    print("BRAND NAME : ",i['name'],"\nPRODUCT NAME : ",i['product_name'],"\nDISCOUNT AMOUNT: ",i['discount'],"%")
                    print()
        elif(val==3):
            break
#to view review by merchant
def view_review(name):
    os.system('cls')
    print("\tVIEW YOUR PRODUCTS REVIEW HERE")
    if(len(user_review)!=0):
        for i in user_review:
            if(i['Brand_name']==name):
                print("User_name :",i['user_name'],"\nProduct_name :",i['product_name'],"\nReview :",i['review'])
    else:
        print("No review is available")
#sales review
def salesreview(name):
    os.system('cls')
    print("\tVIEW YOUR SALES REVIEW")
    if(len(sales_review)!=0):
        for i in sales_review:
            if(i['pro_merch']==name):
                print("USER NAME: {},\nPRODUCT NAME: {}, \nPRICE: {}, \nDATE: {}".format(
                        i['user_name'], i['pro_name'], i['price'], i['date']))
    else:
        print("No review available")
#to filter product by user:1.Filter by brand
def user_filter_brand():
    os.system('cls')
    print("\tFILTER BY BRAND")
    filter_brand=[]
    while(True):
        #os.system('cls')
        print("1.Filter by brand name\n2.Exit")
        val=int(input("enter choice : "))
        if(val==1):
            name=input("Enter product name : ")
            for i in products:
                if(i['product_name']==name):
                    filter_brand.append(i)
                    #print(filter_brand)
            if(len(filter_brand)!=0):
                for i in filter_brand:
                    print("Merchant name : {}, \nProduct name : {}".format(i['name'],i['product_name']))
                    print("\n")
            else:
                print("No product does not exist")
        elif(val==2):
            break       
#to filter by product by user :filter by product
def user_filter_product():
    os.system('cls')
    print("\tFILTER BY PRODUCTS")
    filter_product=[]
    #os.system('cls')
    while(True):
        print("1.Filter by product name\n2.Exit")
        val=int(input("enter choice : "))
        if(val==1):
            name=input("Enter product name : ")
            for i in products:
                if(i['product_name']==name):
                    filter_product.append(i)
                        #print(filter_product)
            if(len(filter_product)!=0):
                for i in filter_product:
                    print("Merchant name : {}, \nProduct name : {}".format(i['name'],i['product_name']))
                    print("\n")
            else:
                print("No product does not exist")
        elif(val==2):
            break   
#to filter by amount-->by user
def user_filter_amount():
    os.system('cls')
    print("\tFILTER BY AMOUNT")
    filter_amount=[]
    #os.system('cls')
    while(True):
        print("1.Filter by amount\n2.Exit")
        val=int(input("enter choice : "))
        if(val==1):
            name=input("Enter product name : ")
            amount=int(input("Enter amount : "))
            for i in products:
                if(i['product_name']==name):
                    if(i['amount']<=amount):
                        filter_amount.append(i)
            if(len(filter_amount)!=0):
                for i in filter_amount:
                    print("Merchant name : {}, \nProduct name : {}".format(i['product_name'],i['amount']))
                    print("\n")
            else:
                print("No product does not exist")
        elif(val==2):
            break
#to filter by discount-->by user
def user_filter_discount():
    os.system('cls')
    print("\tFILTER BY DISCOUNT")
    filter_discount=[]
    savings=0
    while(True):
        print("1.Filter by discount\n2.Exit")
        val=int(input("enter choice : "))
        savings=0
        if(val==1):
            name=input("Enter product name : ")
            range=int(input("Enter price range: "))
            for i in products:
                if(i['product_name']==name and i['amount']==range):
                    s=i['amount']*(i['discount']/100)
                    savings=s
                    a=i['name'],i['product_name'],savings
                    filter_discount.extend(["Brand name: {},\nProduct name:{},\nYou can save:{}".format(i['name'],i['product_name'],savings)])
                    print("\n")
            if(len(filter_discount)>0):
                pass
            else:
                print("No result")
            for i in filter_discount:
                print(*i,sep="")
            filter_discount.clear()
            savings=0
        elif(val==2):
            break
#to place order by user
def user_search_product():
    os.system('cls')
    print("\tSEARCH PRODUCTS")
    d={}
    while(True):
        print("1.See orders available\n2.Exit")
        val=int(input("Enter your choice : "))
        print("\n")
        id_no=0
        if(val==1):
            for i in products:
                print("Brand_name: {},\nProduct_name: {},\nAmount: {},\nDiscount: {}%".format(i['name'],i['product_name'],i['amount'],i['discount']))
                print("\n")
                print("1.Add to cart\n2.Next\n3.Exit")
                print("\n")
                val1=int(input("Enter your choice : "))
                print("\n")
                if(val1==1):
                    id_no+=1
                    res=id_no,i
                    cart.append(res)
                elif(val1==2):
                    continue
                else:
                    break
            else:
                print("Product does not exist")
            
        elif(val==2):
            break            
#to place order form cart
def user_cart_order(user,u):
    os.system('cls')
    print("\tORDER FROM YOUR CART")
    print("\n")
    d={}
    r={}
    sales={}
    while(True):
        print("1.Select from cart\n2.Exit")
        val=int(input("Enter choice : "))
        if(val==1):
            for a,b in cart:
                i=a,b
                print(i)
                #print("\nID : ",a,"\nProduct Brand: ",b['name'],"\nProduct Name: ",b['product_name'],"\nPrice: ",b['amount'])
                print("\n")
                #i=a,b
                id=int(input("Enter id : "))
                if(id==a):
                    print("Type 'Y' to place order and 'N' to cancel order")
                    choice=input("Enter choice : ")
                    if(choice=="Y" or "y"):
                        if(b['amount']<=user['wallet']):
                            discount=b['amount']*(b['discount']/100)
                            amount=b['amount']-discount
                            user['wallet']-=amount
                            b['stock']-=1
                            cart.remove(i)
                            print("Order placed successfully!!!")
                            print("\n")
                            for j in users:
                                if(j['name']==u):
                                    j['order_count']+=1
                                    k=j['order_count']
                            d['name']=b['name']
                            d['product_name']=b['product_name']
                            d['user_name']=u
                            d['order_count']=k
                            dt=datetime.datetime.now()
                            freq_customer.append(d)
                            order_history.extend(["Product Brand: {},\nProduct Name: {},\nPrice: {},\nDate: {}".format(b['name'],b['product_name'],b['amount'], datetime.datetime.now())])
                            #sales_review.append([user['name'],u,b['product_name'],b['amount'], dt])
                            
                            dt=datetime.datetime.now()
                            sales['pro_merch'] = b['name']
                            sales['user_name']=u
                            sales['pro_name'] = b['product_name']
                            sales['price'] = b['amount']
                            sales['date'] = dt
                            sales_review.append(sales)
                            print("\n")
                            print("1.Give Review\n2.Skip")
                            num=int(input("Enter choice : "))
                            if(num==1):
                                review=input("Enter your review : ")
                                r['Brand_name']=b['name']
                                r['user_name']=u
                                r['product_name']=b['product_name']
                                r['review']=review
                                #ans=u,b['name'],b['product_name'],review
                                user_review.append(r)
                                break
                            elif(num==2):
                                break
                        else:
                            print("Insufficient amount in your wallet")
                    elif(choice=="N" or "n"):
                        break
        elif(val==2):
            #user_search_product()
            break
        elif(val==3):
            break
#to place order from search
def user_from_search_order(user,u):
    os.system('cls')
    print("ORDER BY SEARCHING PRODUCTS")
    l=[]
    d={}
    r={}
    sales={}
    while(True):
        print("1.See orders available\n2.Exit")
        val=int(input("Enter your choice : "))
        if(val==1):
            for i in products:
                print("Brand_name: {},\nProduct_name: {},\nAmount: {},\nDiscount: {}%".format(i['name'],i['product_name'],i['amount'],i['discount']))
                print("\n")
                print("1.Order now\n2.Next\n3.Exit")
                print("\n")
                val1=int(input("Enter your choice : "))
                if(val1==1):
                    print("Type 'Y' to place order and 'N' to cancel order")
                    choice=input("Enter choice : ")
                    if(choice=="Y" or "y"):
                        if(i['amount']<=user['wallet']):
                            discount=i['amount']*(i['discount']/100)
                            amount=i['amount']-discount
                            user['wallet']-=amount
                            i['stock']-=1
                            print("Order placed successfully!!!")
                            for j in users:
                                if(j['name']==u):
                                    j['order_count']+=1
                                    k=j['order_count']
                            d['name']=i['name']
                            d['product_name']=i['product_name']
                            d['user_name']=u
                            d['order_count']=k
                            freq_customer.append(d)
                            order_history.extend(["Product Brand: {},\nProduct Name: {},\nPrice: {},\nDate: {}".format(i['name'],i['product_name'],i['amount'], datetime.datetime.now())])
                            dt=datetime.datetime.now()
                            sales['pro_merch'] = i['name']
                            sales['user_name']=u
                            sales['pro_name'] = i['product_name']
                            sales['price'] = i['amount']
                            sales['date'] = dt
                            sales_review.append(sales)
                            #sales_review.extend([i['name'],u,i['product_name'],i['amount'], datetime.datetime.now()])
                            print("1.Give Review\n2.Skip")
                            num=int(input("Enter choice : "))
                            if(num==1):
                                review=input("Enter your review : ")
                                r['Brand_name']=i['name']
                                r['user_name']=u
                                r['product_name']=i['product_name']
                                r['review']=review
                                user_review.append(r)
                                break
                            elif(num==2):
                                break
                        else:
                            print("Insufficient amount in your wallet")
                    elif(choice=="N" or "n"):
                        break
                
                elif(val1==3):
                    break
            else:
                print("Product does not exist")   
        elif(val==2):
            break 

#to place order
def order(user,u):
    os.system('cls')
    print("\tPLACE YOUR ORDERS!!!")
    while(True):
        print("1.Order form cart\n2.Order form search\n3.Exit")
        val=int(input("Enter your choice : "))
        if(val==1):
            user_cart_order(user,u)
        elif(val==2):
            user_from_search_order(user,u)
        elif(val==3):
            break
#to check wallet balance
def check_wallet_balance(user):
    os.system('cls')
    print("\tCHECK YOUR WALLET BALANCE")
    for i in users:
        print("Your wallet balance is :",user['wallet'])
        break
#main coding---> program starts here      
while(True):
    print("\n1.Admin\n2.Merchant\n3.User\n4.Exit")
    a=int(input("Enter your choice : "))
    if(a==1):
        os.system('cls')
        adm()
        
    elif(a==2):
        os.system('cls')
        merchant()
        
    elif(a==3):
        os.system('cls')
        user()
        
    elif(a==4):
        exit()
    else:
        print("invalid input")