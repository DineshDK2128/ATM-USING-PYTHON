import mysql.connector,datetime
def data_insert(name,password):
            amount=int(input("\ nEnter Your Amount : "))
            user_acc =mysql.connector.connect(
            host="localhost",
            user="root",
            password="6383007540",
            database="Bank"
           )
            mycursor=user_acc.cursor()
            current_time = datetime.datetime.now()
            data_insert="insert into user_acc(Name,Password,deposit_amount,register_date) value(%s,%s,%s,%s)"
            data=(name,password,amount,current_time)
            mycursor.execute(data_insert,data)
            user_acc.commit()
            print("Account Create Successful!")
def data_view(name,password):
            user_acc =mysql.connector.connect(
            host="localhost",
            user="root",
            password="6383007540",
            database="Bank"
           )
            mycursor=user_acc.cursor()
            mycursor.execute(f"select * from user_acc where name='{name}' and password='{password}'")
            show=mycursor.fetchall()

            if show !=[]:
                u_n=show[0]
                user_name=u_n[0]
                bal=u_n[2]
                old_withdraw=u_n[3]
                print("\n Login SuccessFul!")
                select=int(input("\n 1. show Balance  \n 2. Deposit \n 3. withdraw   \n"))
                if select == 1:
                    print(f"current Balance is {bal}")
                elif select == 2:
                   dep=int(input("\n How much You Want to Deposit : "))
                   new=dep+bal
                   deposit(new,bal,name)
                elif select == 3:
                    dep=int(input("\n How much You Want to Withdraw : "))
                    new=bal-dep
                    old_with=old_withdraw+dep
                    if dep > bal:
                        print(f"Available balance is {bal}")

                        
                    else:
                        withdraw(new,name,old_with)
            else:
                print(" \n User Not Present")
def deposit(new,bal,name):
            user_acc=mysql.connector.connect(
            host="localhost",
            user="root",
            password="6383007540",
            database="Bank"
           )
            mycursor=user_acc.cursor()
            mycursor.execute(f"update user_acc set deposit_amount='{new}' where name='{name}'")
            user_acc.commit()
            show=mycursor.fetchall()
def withdraw(new,name,old_with):
            user_acc=mysql.connector.connect(
            host="localhost",
            user="root",
            password="6383007540",
            database="Bank"
           )
            mycursor=user_acc.cursor()
            update_deposit=f"update user_acc set deposit_amount='{new}' where name='{name}'"
            update_withdraw=f"update user_acc set withdraw='{old_with}' where name='{name}'"
            mycursor.execute(update_deposit)
            user_acc.commit()
            mycursor=user_acc.cursor()
            mycursor.execute(update_withdraw)
            user_acc.commit()
            show=mycursor.fetchall()
           
def data_search():
            name=input("\n Enter Your Name: ")
            password=input("\n Enter Your Password: ")
            user_acc=mysql.connector.connect(
            host="localhost",
            user="root",
            password="6383007540",
            database="Bank"
           )
            mycursor=user_acc.cursor()
            mycursor.execute(f"select * from user_acc where name='{name}' and password='{password}'")
            show=mycursor.fetchall()
            if show !=[]:
                u_n=show[0]
                user_name=u_n[0]
                user_pass=u_n[1]
                user_deposit=u_n[2]
                user_withdraw=u_n[3]
                print(f" \n Name = {user_name} \n Balance = {user_deposit} \n Withdraw = {user_withdraw}")
            else:
                print("User NOt Present\n ")

def out():
    print("\n Welcome To SBI Bank")
    admin=int("\n 1.Create Account  \n 2.Login Your Account  \n\n ENTER YOUR OPTION: " )
    
    if admin == 1:
        name=input("\n Enter Your Name: ")
        password=input("\n Enter Your Password: ")
        data_insert(name,password)

    elif admin ==2:
       name=input("\n Enter Your Name: ")
       password=input("\n Enter Your Password: ")
       data_view(name,password)


out()



