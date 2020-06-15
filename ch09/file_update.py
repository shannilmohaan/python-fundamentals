# This program will update a file
import os
#create the original file - account.txt
def create_file():
    with open ("accounts.txt" , mode = 'w') as accounts:
        accounts.write("100 Shanil 100.50\n")
        accounts.write("200 Ramya 200.50\n")
        accounts.write("300 Aaaarrav 300.50\n")

def update_file():
    original_file = open ("accounts.txt",mode = 'r')
    temp_file = open("temp.txt",mode = 'w')
    with original_file,temp_file:
        for records in original_file:
            #check if the record is the one which needs update
            acct_no,name,balance = records.split()
            if int(acct_no) == 300:
                record = ' '.join([acct_no,"Aarav",balance,"\n"])
                temp_file.write(record)
            else:
                temp_file.write(records)

if __name__ == '__main__':
    create_file()
    update_file()
    os.remove("accounts.txt")
    os.rename("temp.txt","accounts.txt")
