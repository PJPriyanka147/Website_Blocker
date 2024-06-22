import datetime
import time

#Set the end time for blocking websites
end_time = datetime.datetime(2024, 6, 22, 17, 50, 0)

#Websites to block
site_block = ["www.facebook.com"]

#Path to the hosts file
host_path = "C:/Windows/System32/drivers/etc/hosts"

#IP address(loalhost) to redirect blocked sites to
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now() < end_time :
        print("Start Blocking")
        with open(host_path, "r+") as host_file :
            content = host_file.read()
            for website in site_block :
                if website not in content :
                    host_file.write(redirect +"  "+website+"\n")
                else:
                    pass
    else:
        with open(host_path, "r+") as host_file :
            content = host_file.readlines()
            host_file.seek(0) #To move the file pointer to the beginning of the file
            for lines in content :
                if not any (website in lines for website in site_block) :# Check if any website in site_block is present in the line
                    host_file.write(lines)

            host_file.truncate()
        
        
    time.sleep(5)


