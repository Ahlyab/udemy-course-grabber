from pack import functions
from pack import banner


no = int(1)

def write_coupons (list_of_coupons_and_title):
    global no
    for indx, coupon_and_title in enumerate(list_of_coupons_and_title):
        title, link = coupon_and_title.split('||')
        coupons_file.write("\n"+ str(no) + ". " + title + "\n" + link + "\n")
        no = int(no) + 1

def discudemy():
    list_of_coupons_and_title = functions.discudemy(1)
    write_coupons(list_of_coupons_and_title)

def learnviral():
    list_of_coupons_and_title = functions.learnviral(1)
    write_coupons(list_of_coupons_and_title)

def real_disc():
    list_of_coupons_and_title = functions.real_disc(1)
    write_coupons(list_of_coupons_and_title)

def udemy_freebies():
    list_of_coupons_and_title = functions.udemy_freebies(1)
    write_coupons(list_of_coupons_and_title)

def udemy_coupons_me():
    list_of_coupons_and_title = functions.udemy_coupons_me(1)
    write_coupons(list_of_coupons_and_title)    


def main():
    discudemy()
    learnviral()
    real_disc()
    udemy_freebies()
    udemy_coupons_me()



if __name__ == '__main__' :
    banner.banner()
    banner.info()
    banner.msg()
    coupons_file = open("./coupons.txt", "w", encoding="utf-8")
    main()
    banner.end_msg()
    coupons_file.close()
