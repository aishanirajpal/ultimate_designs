#pygame initialization
import pygame
import csv
import os
from csv import writer
from datetime import datetime
import sys

###########################
###########################

pygame.init()
pygame.display.set_caption('ULTIMATE DESIGNS')

###########################
#pages
start_pg = True
admin_pg = False
user_pg = False
old_user_pg = False
old_user_pg1 = False
old_user_pg2 = False
old_user_pgw = False
newuser_pg0 = False
newuser_pg1 = False
newuser_pg2 = False
newuser_pg3 = False
newuser_pg4 = False
newuser_pg_ar = False
admin_pg0 = False
admin_pg1 = False
admin_pg2 = False
admin_pg3 = False
admin_pg4 = False
admin_pg5 = False
admin_pg6 = False
admin_pg_profit_loss_usr = False
admin_pg_d4 = False
admin_pg_d5 = False
admin_pg_ch = False
admin_pg_ls = False
find_usr_id = False
ch_username_cond = False
ata_pg = False
write_in_file = False
view_records = False
write_in_interior = False
read_user_checkid = False
read_interior = False
read_interior_year = False
ch_username = False
ch_bp = False
ch_ex = False
ch_ex_pg = False
ch_ex_ar_pg = False  
ch_ar = False
ch_pg = False
admin_ch_status = False
ch_stat = False
app = True

###########################
#coordinates
b_x = 140
b_y = 480
b_x1 = b_x 
b_y1 = b_y + 40
b_x2 = b_x+40
b_y2 = 300
b_x3 = b_x+40
b_y3 = b_y2 + 40
b_x4 = b_x
b_y4 =b_y+80
b_x5=456
b_y5=580

###########################
#display
icon=pygame.image.load('final1.png')
ic1=pygame.image.load('a1.png')
ic3=pygame.image.load('AA.png')
ic4=pygame.image.load('offices1.jpg')
ic5=pygame.image.load('apartment2.jpg')
ic6=pygame.image.load('studio2.jpg')
ic7=pygame.image.load('bunglow1.jpg')
ic8=pygame.image.load('offer4.png')
ic9=pygame.image.load('congrats.png')
ic10=pygame.image.load('b11.png')
ic11=pygame.image.load('b12.png')
ic12=pygame.image.load('b22.png')
ic13=pygame.image.load('c1.png')
ic14=pygame.image.load('c2.png')
ic15=pygame.image.load('b23.png')
ic16=pygame.image.load('c3.png')
ic17=pygame.image.load('c4.png')


###########################
#colors
white = (255, 255, 255)
black = (0,0,0)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)
color_light = (255,232,198) 
color_dark = (50,50,50)
colour_bg=(255,236,159)
f=(255,30,30)

###########################
#fonts     
font = pygame.font.SysFont('calibri', 18)
fontrec=pygame.font.SysFont('arial black',11)
font2 = pygame.font.SysFont('arial black', 22)
fonthead=pygame.font.SysFont('Algerian',85)
font3 = pygame.font.SysFont('Algerian',30)
font4 = pygame.font.SysFont('Algerian',22)
font5=pygame.font.SysFont('arial black',15)
font7=pygame.font.SysFont('arial black',18)
font6= pygame.font.SysFont('Algerian',27)
font8= pygame.font.SysFont('Algerian',20)


###########################
bp_ls = ["APARTMENT", "OFFICE", "STUDIO", "BUNGALOW", "NA"]
bp_ls_cost = [60000, 50000, 30000, 80000, 0]
extra_ls = ["TILING", "WHITEWASH", "FURNITURE", "COMBO 1", "COMBO 2", "COMBO 3", "COMBO 4", "NA"]
extra_ls_cost = [200, 300, 500]

#FUNCTIONS
def get_usrID():
    user = open('USERS.csv', 'r')
    ar = []
    us=csv.reader(user)
    lines = 0
    for row in us:
        ar.append(row)
        lines += 1
    user.close()
    if lines == 1:
        prev_ID = 1000
    else:
        prev_ID = (ar[len(ar)-1][0])
    return prev_ID

def read():
    try:
        user=open('USERS.csv','r')
        r = csv.reader(user)
        file_data = list(r)
        user.close()
        print(file_data)
        
        
    except FileNotFoundError :
        print('File does not exist')

###########################
#textboxes
base_font = pygame.font.Font(None, 32)
color_active = pygame.Color('lightpink')
color_passive = pygame.Color('white')

while app:
    screen = pygame.display.set_mode((496, 620)) 
    
    user_name = ''
    color_usrname = color_passive  
    colour_name_active = False

    user_id = ''
    color_usrid = color_passive  
    colour_usrid_active = False

    area=''
    color_area = color_passive  
    colour_area_active = False

    area_ch=''
    color_area = color_passive
    colour_char_active = False

    pr = ''
    cp = ''
    sp = ''
    color_txt1_prod = color_passive
    txt1_prod_active = False
    txt1_prod_type = False

    color_txt2_cp = color_passive
    txt2_cp_active = False
    txt2_cp_type = False

    color_txt3_sp = color_passive
    txt3_sp_active = False
    txt3_sp_type = False


    year = ''
    month= ''

    color_txt1_yr = color_passive
    txt1_yr_active = False
    txt1__yrtype = False

    color_txt2_mon = color_passive
    txt2_mon_active = False
    txt2_mon_type = False

    year=''
    color_year = color_passive
    year_active = False

    user_id_chstat = ''
    color_userid_chstat = color_passive  
    colour_userid_chstat_active = False

            
    ###########################
    while start_pg:
        screen.fill(colour_bg)
        
        wel_txt = fonthead.render("WELCOME", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (253, 60)
        screen.blit(wel_txt, wel_Rect)
        screen.blit(icon,(10,105))

        but1_txt = font2.render("USER", True,white)
        but2_txt = font2.render("ADMIN", True, white)
        but3_txt = font2.render("ABOUT THE APP", True, white)

        mouse = pygame.mouse.get_pos()

        if b_x <= mouse[0] <= b_x+220 and b_y <= mouse[1] <= b_y+30: 
                pygame.draw.rect(screen,color_light,[b_x,b_y,220,30])
        else: 
                pygame.draw.rect(screen,color_dark,[b_x,b_y,220,30])

        if b_x1 <= mouse[0] <= b_x1+220 and b_y1 <= mouse[1] <= b_y1+30: 
                pygame.draw.rect(screen,color_light,[b_x1,b_y1,220,30])
        else: 
                pygame.draw.rect(screen,color_dark,[b_x1,b_y1,220,30])

        if b_x4 <= mouse[0] <= b_x4+220 and b_y4 <= mouse[1] <= b_y4+30: 
                pygame.draw.rect(screen,color_light,[b_x4,b_y4,220,30])
        else: 
                pygame.draw.rect(screen,color_dark,[b_x4,b_y4,220,30]) 

        screen.blit(but1_txt , (b_x+67,b_y))
        screen.blit(but2_txt , (b_x1+60,b_y1))
        screen.blit(but3_txt , (b_x4+10,b_y4))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_pg = False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_x <= mouse[0] <= b_x+220 and b_y <= mouse[1] <= b_y+30:
                    start_pg = False
                    user_pg = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_x1 <= mouse[0] <= b_x1+220 and b_y1<= mouse[1] <= b_y1+30:
                    start_pg = False
                    admin_pg = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_x4 <= mouse[0] <= b_x4+220 and b_y4 <= mouse[1] <= b_y4+30:
                    start_pg = False
                    ata_pg = True
                    
        pygame.display.flip()

    ###########################    
    while ata_pg:
        
        b_xg=350
        b_yg=560
        but_back=font2.render("GO BACK", True,white)
        
        s1=pygame.display.set_mode((500,600)) 
        screen.fill(colour_bg)

        wel_txt = font3.render("ABOUT THE APP:", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (250,20)
        screen.blit(wel_txt, wel_Rect)
        screen.blit(ic3,(0,60))

        mouse = pygame.mouse.get_pos()

        if b_xg <= mouse[0] <= b_xg+130 and b_yg<= mouse[1] <= b_yg+30:
            pygame.draw.rect(screen,color_light,[b_xg,b_yg,130,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg,b_yg,130,30])

        screen.blit(but_back, (b_xg+10,b_yg))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ata_pg = False
                app = False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg <= mouse[0] <= b_xg+130 and b_yg <= mouse[1] <= b_yg+30:
                    start_pg = True
                    ata_pg = False
                    admin_pg = False
                    user_pg = False
                    old_user_pg = False
                    old_user_pg1 = False
                    old_user_pg2 = False
                    old_user_pgw = False
                    newuser_pg0 = False
                    newuser_pg1 = False
                    newuser_pg2 = False
                    newuser_pg3 = False
                    newuser_pg4 = False
                    newuser_pg_ar = False
                    admin_pg0 = False
                    admin_pg1 = False
                    admin_pg2 = False
                    admin_pg3 = False
                    admin_pg4 = False
                    admin_pg5 = False
                    admin_pg6 = False
                    admin_pg_profit_loss_usr = False
                    admin_pg_d4 = False
                    admin_pg_d5 = False
                    admin_pg_ch = False
                    admin_pg_ls = False
                    find_usr_id = False
                    ch_username_cond = False
                    write_in_file = False
                    view_records = False
                    write_in_interior = False
                    read_user_checkid = False
                    read_interior = False
                    read_interior_year = False
                    ch_username = False
                    ch_bp = False
                    ch_ex = False
                    ch_ex_pg = False
                    ch_ex_ar_pg = False 
                    ch_ar = False
                    ch_pg = False
                    admin_ch_status = False
                    ch_stat = False
                    app = True


        pygame.display.flip()

    ###########################
    while user_pg:
        screen.fill(colour_bg)
        
        wel_txt = font3.render("HELLO THERE FELLOW CUSTOMER!", True, black)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (245,260)
        screen.blit(wel_txt, wel_Rect)
        screen.blit(ic1,(0,0))
        screen.blit(ic1,(200,360))
        

        but1_txt = font2.render("SIGN UP", True, white)
        but2_txt = font2.render("LOGIN", True, white)

        mouse = pygame.mouse.get_pos()

        if b_x2 <= mouse[0] <= b_x2+120 and b_y2 <= mouse[1] <= b_y2+30: 
                pygame.draw.rect(screen,color_light,[b_x2,b_y2,120,30])
        else: 
                pygame.draw.rect(screen,color_dark,[b_x2,b_y2,120,30])

        if b_x3 <= mouse[0] <= b_x3+120 and b_y3 <= mouse[1] <= b_y3+30: 
                pygame.draw.rect(screen,color_light,[b_x3,b_y3,120,30])
        else: 
                pygame.draw.rect(screen,color_dark,[b_x3,b_y3,120,30]) 

        screen.blit(but1_txt , (b_x2+10,b_y2))
        screen.blit(but2_txt , (b_x3+20,b_y3))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user_pg = False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_x2 <= mouse[0] <= b_x2+350 and b_y2 <= mouse[1] <= b_y2+30:
                    user_pg = False
                    newuser_pg0 = True
                    find_usr_id = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_x3 <= mouse[0] <= b_x3+400 and b_y3 <= mouse[1] <= b_y3+30:
                    user_pg = False
                    old_user_pg = True
                    
        pygame.display.flip()

    if find_usr_id:
        prevID = get_usrID()
        userid = int(prevID)+1


    while newuser_pg0:
        screen.fill(colour_bg)
        
        id_txt = "Your user ID is: " +  str(userid)
        usrid_txt = font3.render(id_txt, True, black)
        usrid_Rect = usrid_txt.get_rect()
        usrid_Rect.center = (240, 240)

        name_txt = font6.render("Please Enter your name below:", True, red)
        name_Rect = wel_txt.get_rect()
        name_Rect.center = (260,280)

        txt_x = 40
        txt_y = 310

        but_x=180
        but_y=350
        
        button_txt = font2.render("Enter", True,red)

        
        mouse = pygame.mouse.get_pos()
        if but_x<= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30: 
                pygame.draw.rect(screen,white,[but_x,but_y,130,30])
        else: 
                pygame.draw.rect(screen,color_light,[but_x,but_y,130,30])
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if txt_x <= mouse[0] <= txt_x+400 and txt_y <= mouse[1] <= txt_y+30: 
                    colour_name_active = True
                else:
                    color_name_active = False

                if but_x <= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30:
                    newuser_pg0 = False
                    newuser_pg1 = True


            if event.type == pygame.KEYDOWN:
      
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
      
                    # get text input from 0 to -1 i.e. end.
                    user_name = user_name[:-1]
      
                # Unicode standard is used for string
                # formation
                else:
                    user_name += event.unicode
          
        if colour_name_active:
            color_usrname = color_active
        else:
            color_usrname = color_passive

        pygame.draw.rect(screen, color_usrname, (txt_x, txt_y, 400, 30))
        txt_surface = base_font.render(user_name, True, black)
        
        screen.blit(usrid_txt, usrid_Rect)
        screen.blit(name_txt, name_Rect)
        screen.blit(txt_surface, (txt_x+10, txt_y))
        screen.blit(button_txt, (but_x+30, but_y))
        screen.blit(ic11,(230,420))
        screen.blit(ic12,(20,10))
        pygame.display.flip()
        
    while newuser_pg1:
        screen.fill(colour_bg)

        bx1=260
        by1=250
        bx2=40
        by2=300
        bx3=40
        by3=500
        bx4=290
        by4=520
        bx5=100
        by5=580

        wel_txt = font3.render("CHOOSE YOUR BUILDING PLAN:", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (250,20)
        screen.blit(wel_txt, wel_Rect)
        screen.blit(ic4,(260,60))
        screen.blit(ic5,(40,60))
        screen.blit(ic6,(40,340))
        screen.blit(ic7,(290,300))

        but1_txt = font2.render(bp_ls[0], True,red)
        but2_txt = font2.render(bp_ls[1], True, red)
        but3_txt = font2.render(bp_ls[2], True, red)
        but4_txt = font2.render(bp_ls[3], True,red)
        but5_txt = font2.render("NO BUILDING PLAN", True,red)
        
        
        mouse = pygame.mouse.get_pos()

        if bx2 <= mouse[0] <= bx2+170 and by2 <= mouse[1] <= by2+30: 
                pygame.draw.rect(screen,white,[bx2,by2,170,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx2,by2,170,30])

        if bx1<= mouse[0] <= bx1+130 and by1 <= mouse[1] <= by1+30: 
                pygame.draw.rect(screen,white,[bx1,by1,130,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx1,by1,130,30])

        if bx3 <= mouse[0] <= bx3+170 and by3 <= mouse[1] <= by3+30: 
                pygame.draw.rect(screen,white,[bx3,by3,170,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx3,by3,170,30])

        if bx4<= mouse[0] <= bx4+200 and by4 <= mouse[1] <= by4+30: 
                pygame.draw.rect(screen,white,[bx4,by4,200,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx4,by4,200,30])

        if bx5<= mouse[0] <= bx5+300 and by5 <= mouse[1] <= by5+30: 
                pygame.draw.rect(screen,white,[bx5,by5,300,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx5,by5,300,30])

        screen.blit(but1_txt , (bx2+10,by2))
        screen.blit(but2_txt , (bx1+20,by1))
        screen.blit(but3_txt , (bx3+35,by3))
        screen.blit(but4_txt , (bx4+35,by4))
        screen.blit(but5_txt , (bx5+20,by5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                newuser_pg1= False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bx2 <= mouse[0] <= bx2+170 and by2 <= mouse[1] <= by2+30:
                    bp=bp_ls[0]
                    cost=bp_ls_cost[0]
                    newuser_pg1 = False
                    newuser_pg2 = True
                    
                if bx1 <= mouse[0] <= bx1+130 and by1 <= mouse[1] <= by1+30:
                    bp=bp_ls[1]
                    cost=bp_ls_cost[1]
                    newuser_pg1 = False
                    newuser_pg2 = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bx3<= mouse[0] <= bx3+170 and by3 <= mouse[1] <= by3+30:
                    bp=bp_ls[2]
                    cost=bp_ls_cost[2]
                    newuser_pg1 = False
                    newuser_pg2 = True
                    

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bx4 <= mouse[0] <= bx4+200 and by4 <= mouse[1] <= by4+30:
                    bp=bp_ls[3]
                    cost=bp_ls_cost[3]
                    newuser_pg1 = False
                    newuser_pg2 = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bx5 <= mouse[0] <= bx5+300 and by5 <= mouse[1] <= by5+30:
                    bp=bp_ls[4]
                    cost=bp_ls[4]
                    newuser_pg1 = False
                    newuser_pg2 = True
                    

        pygame.display.flip()

    while newuser_pg2:
        bx1=20
        by1=40
        bx2=bx1
        by2=by1+40
        bx3=bx1
        by3=by1+80
        bx4=bx1
        by4=by1+120
        bx5=bx1
        by5=by1+160
        bx6=bx1
        by6=by1+200
        bx7=bx1
        by7=by1+240
        bx8=bx1
        by8=by1+280
        
        screen.fill(colour_bg)

        wel_txt = font4.render("CHOOSE ACCORDING TO YOUR REQUIREMENT:", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (250,20)
        screen.blit(wel_txt, wel_Rect)
        screen.blit(ic8,(100,350))

        but1_txt = font5.render("TILING", True,red)
        but2_txt = font5.render("WHITEWASH", True, red)
        but3_txt = font5.render("FURNITURE", True, red)
        but4_txt = font5.render("TILING AND WHITEWASH : COMBO 1", True,red)
        but5_txt = font5.render("TILING AND FURNITURE : COMBO 2", True,red)
        but6_txt = font5.render("WHITEWASH AND FURNITURE : COMBO 3", True,red)
        but7_txt = font5.render("TILING,WHITEWASH & FURNITURE : COMBO 4", True,red)
        but8_txt = font5.render("NO REQUIREMENTS", True,red)

        mouse = pygame.mouse.get_pos()

        if bx1 <= mouse[0] <= bx1+170 and by1 <= mouse[1] <= by1+30: 
                pygame.draw.rect(screen,white,[bx1,by1,170,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx1,by1,170,30])

        if bx2<= mouse[0] <= bx2+170 and by2 <= mouse[1] <= by2+30: 
                pygame.draw.rect(screen,white,[bx2,by2,170,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx2,by2,170,30])

        if bx3 <= mouse[0] <= bx3+170 and by3 <= mouse[1] <= by3+30: 
                pygame.draw.rect(screen,white,[bx3,by3,170,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx3,by3,170,30])

        if bx4<= mouse[0] <= bx4+400 and by4 <= mouse[1] <= by4+30: 
                pygame.draw.rect(screen,white,[bx4,by4,400,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx4,by4,400,30])

        if bx5<= mouse[0] <= bx5+400 and by5 <= mouse[1] <= by5+30: 
                pygame.draw.rect(screen,white,[bx5,by5,400,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx5,by5,400,30])

        if bx6<= mouse[0] <= bx6+400 and by6 <= mouse[1] <= by6+30: 
                pygame.draw.rect(screen,white,[bx6,by6,400,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx6,by6,400,30])

        if bx7<= mouse[0] <= bx7+410 and by7 <= mouse[1] <= by7+30: 
                pygame.draw.rect(screen,white,[bx7,by7,410,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx7,by7,410,30])

        if bx8<= mouse[0] <= bx8+200 and by8 <= mouse[1] <= by8+30: 
                pygame.draw.rect(screen,white,[bx8,by8,200,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx8,by8,200,30])

        screen.blit(but1_txt , (bx2+20,by1))
        screen.blit(but2_txt , (bx1+20,by2))
        screen.blit(but3_txt , (bx3+20,by3))
        screen.blit(but4_txt , (bx4+20,by4))
        screen.blit(but5_txt , (bx5+20,by5))
        screen.blit(but6_txt , (bx6+20,by6))
        screen.blit(but7_txt , (bx7+10,by7))
        screen.blit(but8_txt , (bx8+20,by8))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                newuser_pg2= False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if bx2 <= mouse[0] <= bx2+170 and by2 <= mouse[1] <= by2+30:
                    extra=extra_ls[1]
                    newuser_pg2 = False
                    newuser_pg_ar = True
                    
                if bx1 <= mouse[0] <= bx1+130 and by1 <= mouse[1] <= by1+30:
                    extra=extra_ls[0]
                    newuser_pg2 = False
                    newuser_pg_ar = True

                if bx3<= mouse[0] <= bx3+170 and by3 <= mouse[1] <= by3+30:
                    extra=extra_ls[2]
                    newuser_pg2 = False
                    newuser_pg_ar = True
                    
                if bx4 <= mouse[0] <= bx4+400 and by4 <= mouse[1] <= by4+30:
                    extra=extra_ls[3]
                    newuser_pg2 = False
                    newuser_pg_ar = True

                if bx5 <= mouse[0] <= bx5+300 and by5 <= mouse[1] <= by5+30:
                    extra=extra_ls[4]
                    newuser_pg2 = False
                    newuser_pg_ar = True

                if bx6 <= mouse[0] <= bx6+400 and by6 <= mouse[1] <= by6+30:
                    extra=extra_ls[5]
                    newuser_pg2 = False
                    newuser_pg_ar = True

                if bx7 <= mouse[0] <= bx7+600 and by7 <= mouse[1] <= by7+30:
                    extra=extra_ls[6]
                    newuser_pg2 = False
                    newuser_pg_ar = True

                if bx8 <= mouse[0] <= bx8+300 and by8 <= mouse[1] <= by8+30:
                    write_in_file=True
                    extra=extra_ls[7]
                    area=0
                    cost+=0
                    newuser_pg2 = False
                    newuser_pg3 = True

        pygame.display.flip()

    while newuser_pg_ar:
        screen.fill(colour_bg)
        name_txt = font8.render("Please Enter Estimated Area(in m^2) below:", True, red)
        name_Rect = wel_txt.get_rect()
        name_Rect.center = (250,280)

        txt_x = 40
        txt_y = 310

        but_x=180
        but_y=350
        
        button_txt = font2.render("Enter", True,red)

        
        mouse = pygame.mouse.get_pos()
        if but_x<= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30: 
                pygame.draw.rect(screen,white,[but_x,but_y,130,30])
        else: 
                pygame.draw.rect(screen,color_light,[but_x,but_y,130,30])
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if txt_x <= mouse[0] <= txt_x+400 and txt_y <= mouse[1] <= txt_y+30: 
                    colour_area_active = True
                else:
                    color_area_active = False

                if but_x <= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30:
                    newuser_pg_ar = False
                    newuser_pg3 = True
                    write_in_file=True


            if event.type == pygame.KEYDOWN:
      
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
      
                    # get text input from 0 to -1 i.e. end.
                    area = area[:-1]
      
                # Unicode standard is used for string
                # formation
                else:
                    area += event.unicode
          
        if colour_area_active:
            color_area = color_active
        else:
            color_area = color_passive

        pygame.draw.rect(screen, color_area, (txt_x, txt_y, 400, 30))
        txt_surface = base_font.render(area, True, black)
            
        
        screen.blit(name_txt, name_Rect)
        screen.blit(txt_surface, (txt_x+10, txt_y))
        screen.blit(button_txt, (but_x+30, but_y))
        screen.blit(ic11,(230,420))
        screen.blit(ic12,(20,10))
        pygame.display.flip()


    if write_in_file:
        area=int(area)
        
        if extra == extra_ls[0]:
            cost += area*extra_ls_cost[0]
        elif extra == extra_ls[1]:
            cost += area*extra_ls_cost[1]
        elif extra == extra_ls[2]:
            cost += area*extra_ls_cost[2]
        elif extra == extra_ls[3]:
            cost += area*(extra_ls_cost[0] + extra_ls_cost[1])
            cost -= 10000
        elif extra == extra_ls[4]:
            cost += area*(extra_ls_cost[0] + extra_ls_cost[2])
            cost -= 10000
        elif extra == extra_ls[5]:
            cost += area*(extra_ls_cost[2] + extra_ls_cost[1])
            cost -= 10000
        elif extra == extra_ls[6]:
            cost += area*(extra_ls_cost[0] + extra_ls_cost[1] + extra_ls_cost[2])
            cost -= 15000
        elif extra == extra_ls[7]:
            cost += 0
            
        prevID = get_usrID()

        try:
            with open('USERS.csv','a',newline='') as f:
                us=writer(f)
                #userid=int(prevID)+1
                status="UNDER PROCESS"
                #uname=user_name
                now=datetime.now()
                month=now.strftime('%B')
                year=now.strftime("%Y")
                rec=[userid,user_name,bp,extra,area,cost,status,month,year]
                us.writerow(rec)
                f.close()
        except FileNotFoundError:
            print("FILE DOES NOT EXIST")
       
    while newuser_pg3:

        b_xg=350
        b_yg=560
        but_back=font2.render("GO BACK", True,white)
        
        screen.fill(colour_bg)


        wel_txt = font6.render("YOU ARE NOW AN OFFICIAL CUSTOMER!", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (250,320)
        screen.blit(wel_txt, wel_Rect)
        screen.blit(ic9,(0,0))

        wel_txt = font6.render("YOUR USERID IS" + str(userid), True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (250,360)
        screen.blit(wel_txt, wel_Rect)

        wel_txt = font2.render("HOPING YOU'LL LEAVE WITH A SMILE :)", True, black)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (250,440)
        screen.blit(wel_txt, wel_Rect)

        wel_txt = font.render("Please Go Back and Login to check your details", True, black)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (260,480)
        screen.blit(wel_txt, wel_Rect)

        mouse = pygame.mouse.get_pos()

        if b_xg <= mouse[0] <= b_xg+130 and b_yg<= mouse[1] <= b_yg+30:
            pygame.draw.rect(screen,color_light,[b_xg,b_yg,130,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg,b_yg,130,30])

        screen.blit(but_back, (b_xg+10,b_yg))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                newuser_pg3= False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg <= mouse[0] <= b_xg+130 and b_yg<= mouse[1] <= b_yg+30:
                    start_pg = True
                    ata_pg = False
                    admin_pg = False
                    user_pg = False
                    old_user_pg = False
                    old_user_pg1 = False
                    old_user_pg2 = False
                    old_user_pgw = False
                    newuser_pg0 = False
                    newuser_pg1 = False
                    newuser_pg2 = False
                    newuser_pg3 = False
                    newuser_pg4 = False
                    newuser_pg_ar = False
                    admin_pg0 = False
                    admin_pg1 = False
                    admin_pg2 = False
                    admin_pg3 = False
                    admin_pg4 = False
                    admin_pg5 = False
                    admin_pg6 = False
                    admin_pg_profit_loss_usr = False
                    admin_pg_d4 = False
                    admin_pg_d5 = False
                    admin_pg_ch = False
                    admin_pg_ls = False
                    find_usr_id = False
                    ch_username_cond = False
                    write_in_file = False
                    view_records = False
                    write_in_interior = False
                    read_user_checkid = False
                    read_interior = False
                    read_interior_year = False
                    ch_username = False
                    ch_bp = False
                    ch_ex = False
                    ch_ex_pg = False
                    ch_ex_ar_pg = False  
                    ch_ar = False
                    ch_pg = False
                    admin_ch_status = False
                    ch_stat = False
                    app = True

        pygame.display.flip()


    while old_user_pg:
        screen.fill(colour_bg)

        id_txt = font6.render("Please Enter your User Id below:", True, red)
        id_Rect = wel_txt.get_rect()
        id_Rect.center = (260,260)

        txt_x = 40
        txt_y = 280

        but_x=180
        but_y=320
        
        button_txt = font2.render("Enter", True,red)

        
        mouse = pygame.mouse.get_pos()
        if but_x<= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30: 
                pygame.draw.rect(screen,white,[but_x,but_y,130,30])
        else: 
                pygame.draw.rect(screen,color_light,[but_x,but_y,130,30])
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if txt_x <= mouse[0] <= txt_x+400 and txt_y <= mouse[1] <= txt_y+30: 
                    colour_usrid_active = True
                else:
                    color_usrid_active = False

                if but_x <= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30:
                    old_user_pg = False
                    old_user_pg1 = True


            if event.type == pygame.KEYDOWN:
      
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
      
                    # get text input from 0 to -1 i.e. end.
                    user_id = user_id[:-1]
      
                # Unicode standard is used for string
                # formation
                else:
                    user_id += event.unicode
          
        if colour_usrid_active:
            color_usrid = color_active
        else:
            color_usrid = color_passive

        pygame.draw.rect(screen, color_usrid, (txt_x, txt_y, 400, 30))
        txt_surface = base_font.render(user_id, True, black)
        

        
        screen.blit(id_txt, id_Rect)
        screen.blit(txt_surface, (txt_x+10, txt_y))
        screen.blit(button_txt, (but_x+30, but_y))
        screen.blit(ic13,(230,420))
        screen.blit(ic14,(10,10))
        pygame.display.flip()



    while old_user_pg1:
        screen.fill(colour_bg)

        wel_txt = font3.render("YOUR DETAILS", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (253, 20)
        screen.blit(wel_txt, wel_Rect)
        screen.blit(ic15,(5,420))
        
        b_xg=10
        b_yg=580
        b_xg1=250
        b_yg1=580
        
        but_back=font2.render("GO BACK", True,white)
        but_change=font2.render("CHANGE DETAILS", True,white)
        
        user=open('USERS.csv','r')
        us=csv.reader(user)
        flag=0
        
        for rec in us:
            if (rec[0]==user_id):
                id_txt = font7.render("USERID:" + ' ' + rec[0], True, black)
                id_Rect = id_txt.get_rect()
                id_Rect.topleft = (20,60)
                screen.blit(id_txt, id_Rect)
                
                name_txt = font7.render("NAME:" + ' ' +  rec[1], True, black)
                name_Rect = name_txt.get_rect()
                name_Rect.topleft = (20,100)
                screen.blit(name_txt, name_Rect)

                plan_txt = font7.render("BUILDING PLAN:" + ' ' +  rec[2], True, black)
                plan_Rect = plan_txt.get_rect()
                plan_Rect.topleft = (20,140)
                screen.blit(plan_txt, plan_Rect)

                ex_txt = font7.render("EXTRA REQUIREMENTS:", True, black)
                ex1_txt = font7.render("  " + rec[3], True, black)
                ex_Rect = ex_txt.get_rect()
                ex1_Rect = ex1_txt.get_rect()
                ex_Rect.topleft = (20,180)
                ex1_Rect.topleft = (20,200)
                screen.blit(ex_txt, ex_Rect)
                screen.blit(ex1_txt, ex1_Rect)

                area_txt = font7.render("AREA:" + ' ' +  rec[4], True, black)
                area_Rect = area_txt.get_rect()
                area_Rect.topleft = (20,240)
                screen.blit(area_txt, area_Rect)

                cost_txt = font7.render("ESTIMATED COST:" + ' ' + rec[5], True, black)
                cost_Rect = cost_txt.get_rect()
                cost_Rect.topleft = (20,280)
                screen.blit(cost_txt, cost_Rect)

                stat_txt = font7.render("STATUS:" + ' ' + rec[6], True, black)
                stat_Rect = stat_txt.get_rect()
                stat_Rect.topleft = (20,320)
                screen.blit(stat_txt, stat_Rect)

                mon_txt = font7.render("MONTH OF REGISTRATION:" + ' ' +  rec[7], True, black)
                mon_Rect = mon_txt.get_rect()
                mon_Rect.topleft = (20,360)
                screen.blit(mon_txt, mon_Rect)

                yr_txt = font7.render("YEAR OF REGISTRATION:" + ' ' +  rec[8], True, black)
                yr_Rect = yr_txt.get_rect()
                yr_Rect.topleft = (20,400)
                screen.blit(yr_txt, yr_Rect)
                flag=1

        mouse = pygame.mouse.get_pos()
        if b_xg <= mouse[0] <= b_xg+130 and b_yg<= mouse[1] <= b_yg+30:
            pygame.draw.rect(screen,color_light,[b_xg,b_yg,130,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg,b_yg,130,30])

        if b_xg1 <= mouse[0] <= b_xg1+240 and b_yg1<= mouse[1] <= b_yg1+30:
            pygame.draw.rect(screen,color_light,[b_xg1,b_yg1,240,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg1,b_yg1,240,30])

        screen.blit(but_back, (b_xg+10,b_yg))
        screen.blit(but_change, (b_xg1+10,b_yg1))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                old_user_pg1 = False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg <= mouse[0] <= b_xg+130 and b_yg <= mouse[1] <= b_yg+30:
                    start_pg = True
                    ata_pg = False
                    admin_pg = False
                    user_pg = False
                    old_user_pg = False
                    old_user_pg1 = False
                    old_user_pg2 = False
                    old_user_pgw = False
                    newuser_pg0 = False
                    newuser_pg1 = False
                    newuser_pg2 = False
                    newuser_pg3 = False
                    newuser_pg4 = False
                    newuser_pg_ar = False
                    admin_pg0 = False
                    admin_pg1 = False
                    admin_pg2 = False
                    admin_pg3 = False
                    admin_pg4 = False
                    admin_pg5 = False
                    admin_pg6 = False
                    admin_pg_profit_loss_usr = False
                    admin_pg_d4 = False
                    admin_pg_d5 = False
                    admin_pg_ch = False
                    admin_pg_ls = False
                    find_usr_id = False
                    ch_username_cond = False
                    write_in_file = False
                    view_records = False
                    write_in_interior = False
                    read_user_checkid = False
                    read_interior = False
                    read_interior_year = False
                    ch_username = False
                    ch_bp = False
                    ch_ex = False
                    ch_ex_pg = False
                    ch_ex_ar_pg = False  
                    ch_ar = False
                    ch_pg = False
                    admin_ch_status = False
                    ch_stat = False
                    app = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg1 <= mouse[0] <= b_xg1+240 and b_yg1 <= mouse[1] <= b_yg1+30:
                    old_user_pg1 = False
                    old_user_pg2 = True

            if flag==0:
                old_user_pg1 = False
                old_user_pgw = True

        pygame.display.flip()

    while old_user_pgw:
        scr1 = pygame.display.set_mode((500,150))
        b_xg=350
        b_yg=110
        but_back=font2.render("GO BACK", True,white)
        screen.fill(colour_bg)

        wel_txt = font3.render("USER ID NOT FOUND", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (230,50)
        screen.blit(wel_txt, wel_Rect)

        wel_txt = font.render("PLEASE REGISTER YOURSELF OR TRY AGAIN", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (230,70)
        screen.blit(wel_txt, wel_Rect)

        mouse = pygame.mouse.get_pos()

        if b_xg <= mouse[0] <= b_xg+130 and b_yg<= mouse[1] <= b_yg+30:
            pygame.draw.rect(screen,color_light,[b_xg,b_yg,130,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg,b_yg,130,30])

        screen.blit(but_back, (b_xg+10,b_yg))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                old_user_pgw = False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg <= mouse[0] <= b_xg+130 and b_yg <= mouse[1] <= b_yg+30:
                    start_pg = False
                    ata_pg = False
                    admin_pg = False
                    user_pg = False
                    old_user_pg = False
                    old_user_pg1 = True
                    old_user_pg2 = False
                    old_user_pgw = False
                    newuser_pg0 = False
                    newuser_pg1 = False
                    newuser_pg2 = False
                    newuser_pg3 = False
                    newuser_pg4 = False
                    newuser_pg_ar = False
                    admin_pg0 = False
                    admin_pg1 = False
                    admin_pg2 = False
                    admin_pg3 = False
                    admin_pg4 = False
                    admin_pg5 = False
                    admin_pg6 = False
                    admin_pg_profit_loss_usr = False
                    admin_pg_d4 = False
                    admin_pg_d5 = False
                    admin_pg_ch = False
                    admin_pg_ls = False
                    find_usr_id = False
                    ch_username_cond = False
                    write_in_file = False
                    view_records = False
                    write_in_interior = False
                    read_user_checkid = False
                    read_interior = False
                    read_interior_year = False
                    ch_username = False
                    ch_bp = False
                    ch_ex = False
                    ch_ex_pg = False
                    ch_ex_ar_pg = False  
                    ch_ar = False
                    ch_pg = False
                    admin_ch_status = False
                    ch_stat = False
                    app = True

        pygame.display.flip()

    while old_user_pg2:
        screen.fill(colour_bg)

        bx1=60
        by1=280
        bx2=bx1
        by2=by1+40
        bx3=bx1
        by3=by1+80
        bx4=bx1
        by4=by1+120
        
        wel_txt = font3.render("WHAT DO YOU WANT TO CHANGE?", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (250,240)
        screen.blit(wel_txt, wel_Rect)
        screen.blit(ic16,(190,420))
        screen.blit(ic16,(20,0))


        but1_txt = font5.render("USERNAME", True,red)
        but2_txt = font5.render("BUILDING PLAN", True, red)
        but3_txt = font5.render("EXTRA REQUIREMENTS", True, red)
        but4_txt = font5.render("AREA", True,red)

        mouse = pygame.mouse.get_pos()

        if bx1 <= mouse[0] <= bx1+250 and by1 <= mouse[1] <= by1+30: 
                pygame.draw.rect(screen,white,[bx1,by1,250,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx1,by1,250,30])

        if bx2<= mouse[0] <= bx2+250 and by2 <= mouse[1] <= by2+30: 
                pygame.draw.rect(screen,white,[bx2,by2,250,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx2,by2,250,30])

        if bx3 <= mouse[0] <= bx3+250 and by3 <= mouse[1] <= by3+30: 
                pygame.draw.rect(screen,white,[bx3,by3,250,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx3,by3,250,30])

        if bx4<= mouse[0] <= bx4+250 and by4 <= mouse[1] <= by4+30: 
                pygame.draw.rect(screen,white,[bx4,by4,250,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx4,by4,250,30])

        screen.blit(but1_txt , (bx2+20,by1))
        screen.blit(but2_txt , (bx1+20,by2))
        screen.blit(but3_txt , (bx3+20,by3))
        screen.blit(but4_txt , (bx4+20,by4))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                old_user_pg= False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if bx1 <= mouse[0] <= bx1+400 and by1 <= mouse[1] <= by1+30:
                    old_user_pg2 = False
                    ch_username_cond = True
                    ch_username = True
                    
                if bx2 <= mouse[0] <= bx2+400 and by2 <= mouse[1] <= by2+30: 
                    old_user_pg2 = False
                    ch_bp = True

                if bx3 <= mouse[0] <= bx3+400 and by3 <= mouse[1] <= by3+30: 
                    old_user_pg2 = False
                    ch_ex = True
                    
                if bx4 <= mouse[0] <= bx4+400 and by4 <= mouse[1] <= by4+30: 
                    old_user_pg2 = False
                    ch_ar = True

        pygame.display.flip()

    if ch_username_cond:
        base_font = pygame.font.Font(None, 32)
        user_name_ch = ''
        color_active = pygame.Color('lightpink')
        color_passive = pygame.Color('white')
        color_usrname = color_passive
        colouractive = False

        while ch_username:
            screen.fill(colour_bg)

            user=open('USERS.csv','r')
            r = csv.reader(user)
            file_data = list(r)
            user.close()

            index = -1
            for i in range(len(file_data)):
                for j in range(len(file_data[i])):
                    if file_data[i][j] == user_id:
                        index = i
                        break


            name_txt = font6.render("Please Enter your name below:", True, red)
            name_Rect = wel_txt.get_rect()
            name_Rect.center = (260,280)

            txt_x = 40
            txt_y = 310

            but_x=180
            but_y=350
            
            button_txt = font2.render("Enter", True,red)

            
            mouse = pygame.mouse.get_pos()
            if but_x<= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30: 
                    pygame.draw.rect(screen,white,[but_x,but_y,130,30])
            else: 
                    pygame.draw.rect(screen,color_light,[but_x,but_y,130,30])
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if txt_x <= mouse[0] <= txt_x+400 and txt_y <= mouse[1] <= txt_y+30: 
                        colouractive = True
                    else:
                        coloractive = False

                    if but_x <= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30:
                        ch_username = False
                        ch_pg = True


                if event.type == pygame.KEYDOWN:
          
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
          
                        # get text input from 0 to -1 i.e. end.
                        user_name_ch = user_name[:-1]
          
                    # Unicode standard is used for string
                    # formation
                    else:
                        user_name_ch += event.unicode
              
            if colouractive:
                color_usrname = color_active
            else:
                color_usrname = color_passive

            pygame.draw.rect(screen, color_usrname, (txt_x, txt_y, 400, 30))
            txt_surface = base_font.render(user_name_ch, True, black)
            

            screen.blit(name_txt, name_Rect)
            screen.blit(txt_surface, (txt_x+10, txt_y))
            screen.blit(button_txt, (but_x+30, but_y))
            screen.blit(ic11,(230,420))
            screen.blit(ic12,(20,10))
            pygame.display.flip()

        user=open('USERS.csv','r')
        r = csv.reader(user)
        file_data = list(r)
        user.close()

        index = -1
        for i in range(len(file_data)):
            for j in range(len(file_data[i])):
                if file_data[i][j] == user_id:
                    index = i
                    break
        file_data[index][1]=user_name_ch

        user = open('USERS.csv','w', newline = '')           
        write=csv.writer(user)
        write.writerows(file_data)
        user.close()

    while ch_bp:
        screen.fill(colour_bg)

        user=open('USERS.csv','r')
        r = csv.reader(user)
        file_data = list(r)
        user.close()

        index = -1
        for i in range(len(file_data)):
            for j in range(len(file_data[i])):
                if file_data[i][j] == user_id:
                    index = i
                    break
        file_data[index][5] = int(file_data[index][5])
        
        if file_data[index][2] == bp_ls[0]:
            prev_bp_cost = bp_ls_cost[0]
            
        elif file_data[index][2] == bp_ls[1]:
            prev_bp_cost = bp_ls_cost[1]
            
        elif file_data[index][2] == bp_ls[2]:
            prev_bp_cost = bp_ls_cost[2]
            
        elif file_data[index][2] == bp_ls[3]:
            prev_bp_cost = bp_ls_cost[3]
            
        elif file_data[index][2] == bp_ls[4]:
            prev_bp_cost = bp_ls_cost[4]

        bx1=260
        by1=250
        bx2=40
        by2=300
        bx3=40
        by3=500
        bx4=290
        by4=520
        bx5=100
        by5=580

        wel_txt = font3.render("CHOOSE YOUR BUILDING PLAN:", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (250,20)
        screen.blit(wel_txt, wel_Rect)
        screen.blit(ic4,(260,60))
        screen.blit(ic5,(40,60))
        screen.blit(ic6,(40,340))
        screen.blit(ic7,(290,300))

        but1_txt = font2.render(bp_ls[0], True,red)
        but2_txt = font2.render(bp_ls[1], True, red)
        but3_txt = font2.render(bp_ls[2], True, red)
        but4_txt = font2.render(bp_ls[3], True,red)
        but5_txt = font2.render("NO BUILDING PLAN", True,red)
        
        
        mouse = pygame.mouse.get_pos()

        if bx2 <= mouse[0] <= bx2+170 and by2 <= mouse[1] <= by2+30: 
                pygame.draw.rect(screen,white,[bx2,by2,170,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx2,by2,170,30])

        if bx1<= mouse[0] <= bx1+130 and by1 <= mouse[1] <= by1+30: 
                pygame.draw.rect(screen,white,[bx1,by1,130,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx1,by1,130,30])

        if bx3 <= mouse[0] <= bx3+170 and by3 <= mouse[1] <= by3+30: 
                pygame.draw.rect(screen,white,[bx3,by3,170,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx3,by3,170,30])

        if bx4<= mouse[0] <= bx4+200 and by4 <= mouse[1] <= by4+30: 
                pygame.draw.rect(screen,white,[bx4,by4,200,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx4,by4,200,30])

        if bx5<= mouse[0] <= bx5+300 and by5 <= mouse[1] <= by5+30: 
                pygame.draw.rect(screen,white,[bx5,by5,300,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx5,by5,300,30])

        screen.blit(but1_txt , (bx2+10,by2))
        screen.blit(but2_txt , (bx1+20,by1))
        screen.blit(but3_txt , (bx3+35,by3))
        screen.blit(but4_txt , (bx4+35,by4))
        screen.blit(but5_txt , (bx5+20,by5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ch_bp = False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bx2 <= mouse[0] <= bx2+170 and by2 <= mouse[1] <= by2+30:
                    file_data[index][2]=bp_ls[0]
                    file_data[index][5] -= prev_bp_cost
                    file_data[index][5]+=bp_ls_cost[0]
                    ch_bp = False
                    ch_pg = True
                    
                if bx1 <= mouse[0] <= bx1+130 and by1 <= mouse[1] <= by1+30:
                    file_data[index][2]=bp_ls[1]
                    file_data[index][5] -= prev_bp_cost
                    file_data[index][5]+=bp_ls_cost[1]
                    ch_bp = False
                    ch_pg = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bx3<= mouse[0] <= bx3+170 and by3 <= mouse[1] <= by3+30:
                    file_data[index][2]=bp_ls[2]
                    file_data[index][5] -= prev_bp_cost
                    file_data[index][5]+=bp_ls_cost[2]
                    ch_bp = False
                    ch_pg = True
                    

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bx4 <= mouse[0] <= bx4+200 and by4 <= mouse[1] <= by4+30:
                    file_data[index][2]=bp_ls[3]
                    file_data[index][5] -= prev_bp_cost
                    file_data[index][5]+=bp_ls_cost[4]
                    ch_bp = False
                    ch_pg = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bx5 <= mouse[0] <= bx5+300 and by5 <= mouse[1] <= by5+30:
                    file_data[index][2]=bp_ls[4]
                    file_data[index][5] -= prev_bp_cost
                    file_data[index][5]+=bp_ls_cost[4]
                    ch_bp = False
                    ch_pg = True

        user = open('USERS.csv','w', newline = '')           
        write=csv.writer(user)
        write.writerows(file_data)
        user.close()

        pygame.display.flip()

    if ch_ex:

        user=open('USERS.csv','r')
        r = csv.reader(user)
        file_data = list(r)
        user.close()

        index = -1
        for i in range(len(file_data)):
            for j in range(len(file_data[i])):
                if file_data[i][j] == user_id:
                    index = i
                    break

        file_data[index][5] = int(file_data[index][5])
        file_data[index][4] = int(file_data[index][4])
        cur_area = file_data[index][4]

        if int(cur_area) == 0:
            ch_ex_ar_pg = True
        else:
            ch_ex_pg = True

    while ch_ex_ar_pg:
        screen.fill(colour_bg)
        name_txt = font8.render("Please Enter Estimated Area(in m^2) below:", True, red)
        name_Rect = wel_txt.get_rect()
        name_Rect.center = (250,280)

        txt_x = 40
        txt_y = 310

        but_x=180
        but_y=350
        
        button_txt = font2.render("Enter", True,red)

        
        mouse = pygame.mouse.get_pos()
        if but_x<= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30: 
                pygame.draw.rect(screen,white,[but_x,but_y,130,30])
        else: 
                pygame.draw.rect(screen,color_light,[but_x,but_y,130,30])
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if txt_x <= mouse[0] <= txt_x+400 and txt_y <= mouse[1] <= txt_y+30: 
                    colour_area_active = True
                else:
                    color_area_active = False

                if but_x <= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30:
                    ch_ex_ar_pg = False
                    ch_ex_pg = True
                    cur_area = int(area)
                    file_data[index][4] = cur_area
                    #write_in_file=True


            if event.type == pygame.KEYDOWN:
      
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
      
                    # get text input from 0 to -1 i.e. end.
                    area = area[:-1]
      
                # Unicode standard is used for string
                # formation
                else:
                    area += event.unicode
          
        if colour_area_active:
            color_area = color_active
        else:
            color_area = color_passive

        pygame.draw.rect(screen, color_area, (txt_x, txt_y, 400, 30))
        txt_surface = base_font.render(area, True, black)
            
        
        screen.blit(name_txt, name_Rect)
        screen.blit(txt_surface, (txt_x+10, txt_y))
        screen.blit(button_txt, (but_x+30, but_y))
        screen.blit(ic11,(230,420))
        screen.blit(ic12,(20,10))
        pygame.display.flip()


    while ch_ex_pg:
        
        if file_data[index][3] == extra_ls[0]:
            prev_ex_cost = cur_area*extra_ls_cost[0]
            
        elif file_data[index][3] == extra_ls[1]:
            prev_ex_cost = cur_area*extra_ls_cost[1]
            
        elif file_data[index][3] == extra_ls[2]:
            prev_ex_cost = cur_area*extra_ls_cost[2]
            
        elif file_data[index][3] == extra_ls[3]:
            prev_ex_cost = cur_area*(extra_ls_cost[0]+extra_ls_cost[1])-10000
            
        elif file_data[index][3] == extra_ls[4]:
            prev_ex_cost = cur_area*(extra_ls_cost[2]+extra_ls_cost[0])-10000
            
        elif file_data[index][3] == extra_ls[5]:
            prev_ex_cost = cur_area*(extra_ls_cost[2]+extra_ls_cost[1])-10000
            
        elif file_data[index][3] == extra_ls[6]:
            prev_ex_cost = cur_area*(extra_ls_cost[2]+extra_ls_cost[1]+extra_ls_cost[0])-15000
                                     
        elif file_data[index][3] == extra_ls[7]:
            prev_ex_cost = cur_area*0
        
        screen.fill(colour_bg)
        bx1=20
        by1=40
        bx2=bx1
        by2=by1+40
        bx3=bx1
        by3=by1+80
        bx4=bx1
        by4=by1+120
        bx5=bx1
        by5=by1+160
        bx6=bx1
        by6=by1+200
        bx7=bx1
        by7=by1+240
        bx8=bx1
        by8=by1+280
        
        screen.fill(colour_bg)

        wel_txt = font4.render("CHOOSE ACCORDING TO YOUR REQUIREMENT:", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (250,20)
        screen.blit(wel_txt, wel_Rect)
        screen.blit(ic8,(100,350))

        but1_txt = font5.render("TILING", True,red)
        but2_txt = font5.render("WHITEWASH", True, red)
        but3_txt = font5.render("FURNITURE", True, red)
        but4_txt = font5.render("TILING AND WHITEWASH : COMBO 1", True,red)
        but5_txt = font5.render("TILING AND FURNITURE : COMBO 2", True,red)
        but6_txt = font5.render("WHITEWASH AND FURNITURE : COMBO 3", True,red)
        but7_txt = font5.render("TILING,WHITEWASH & FURNITURE : COMBO 4", True,red)
        but8_txt = font5.render("NO REQUIREMENTS", True,red)

        mouse = pygame.mouse.get_pos()

        if bx1 <= mouse[0] <= bx1+170 and by1 <= mouse[1] <= by1+30: 
                pygame.draw.rect(screen,white,[bx1,by1,170,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx1,by1,170,30])

        if bx2<= mouse[0] <= bx2+170 and by2 <= mouse[1] <= by2+30: 
                pygame.draw.rect(screen,white,[bx2,by2,170,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx2,by2,170,30])

        if bx3 <= mouse[0] <= bx3+170 and by3 <= mouse[1] <= by3+30: 
                pygame.draw.rect(screen,white,[bx3,by3,170,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx3,by3,170,30])

        if bx4<= mouse[0] <= bx4+400 and by4 <= mouse[1] <= by4+30: 
                pygame.draw.rect(screen,white,[bx4,by4,400,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx4,by4,400,30])

        if bx5<= mouse[0] <= bx5+400 and by5 <= mouse[1] <= by5+30: 
                pygame.draw.rect(screen,white,[bx5,by5,400,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx5,by5,400,30])

        if bx6<= mouse[0] <= bx6+400 and by6 <= mouse[1] <= by6+30: 
                pygame.draw.rect(screen,white,[bx6,by6,400,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx6,by6,400,30])

        if bx7<= mouse[0] <= bx7+410 and by7 <= mouse[1] <= by7+30: 
                pygame.draw.rect(screen,white,[bx7,by7,410,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx7,by7,410,30])

        if bx8<= mouse[0] <= bx8+200 and by8 <= mouse[1] <= by8+30: 
                pygame.draw.rect(screen,white,[bx8,by8,200,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx8,by8,200,30])

        screen.blit(but1_txt , (bx2+20,by1))
        screen.blit(but2_txt , (bx1+20,by2))
        screen.blit(but3_txt , (bx3+20,by3))
        screen.blit(but4_txt , (bx4+20,by4))
        screen.blit(but5_txt , (bx5+20,by5))
        screen.blit(but6_txt , (bx6+20,by6))
        screen.blit(but7_txt , (bx7+10,by7))
        screen.blit(but8_txt , (bx8+20,by8))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                newuser_pg2= False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bx2 <= mouse[0] <= bx2+170 and by2 <= mouse[1] <= by2+30:#change qar to area
                    file_data[index][3]=extra_ls[0]
                    file_data[index][5] -= prev_ex_cost
                    file_data[index][5]+=cur_area*extra_ls_cost[0]
                    ch_ex_pg = False
                    ch_pg = True
                    
                if bx1 <= mouse[0] <= bx1+130 and by1 <= mouse[1] <= by1+30:#change qar to area
                    file_data[index][3]=extra_ls[1]
                    file_data[index][5] -= prev_ex_cost
                    file_data[index][5]+= cur_area*extra_ls_cost[1]
                    ch_ex_pg = False
                    ch_pg = True

                if bx3<= mouse[0] <= bx3+170 and by3 <= mouse[1] <= by3+30:#change qar to area
                    file_data[index][3]=extra_ls[2]
                    file_data[index][5] -= prev_ex_cost
                    file_data[index][5]+= cur_area*extra_ls_cost[2]
                    ch_ex_pg = False
                    ch_pg = True
                    
                if bx4 <= mouse[0] <= bx4+400 and by4 <= mouse[1] <= by4+30:#change qar to area
                    file_data[index][3]=extra_ls[3]
                    file_data[index][5] -= prev_ex_cost
                    file_data[index][5]+= cur_area*(extra_ls_cost[0]+extra_ls_cost[1])
                    file_data[index][5]-=10000
                    ch_ex_pg = False
                    ch_pg = True

                if bx5 <= mouse[0] <= bx5+300 and by5 <= mouse[1] <= by5+30:#change qar to area
                    file_data[index][3]=extra_ls[4]
                    file_data[index][5] -= prev_ex_cost
                    file_data[index][5]+= cur_area*(extra_ls_cost[0]+extra_ls_cost[2])
                    file_data[index][5]-=10000
                    ch_ex_pg = False
                    ch_pg = True

                if bx6 <= mouse[0] <= bx6+400 and by6 <= mouse[1] <= by6+30:#change qar to area
                    file_data[index][3]=extra_ls[5]
                    file_data[index][5] -= prev_ex_cost
                    file_data[index][5]+= cur_area*(extra_ls_cost[1]+extra_ls_cost[2])
                    file_data[index][5]-=10000
                    ch_ex_pg = False
                    ch_pg = True

                if bx7 <= mouse[0] <= bx7+600 and by7 <= mouse[1] <= by7+30:#change qar to area
                    file_data[index][3]=extra_ls[6]
                    file_data[index][5] -= prev_ex_cost
                    file_data[index][5]+= cur_area*(extra_ls_cost[0]+extra_ls_cost[2]+extra_ls_cost[1])
                    file_data[index][5]-=15000
                    ch_ex_pg = False
                    ch_pg = True

                if bx8 <= mouse[0] <= bx8+300 and by8 <= mouse[1] <= by8+30:
                    file_data[index][3]=extra_ls[7]
                    file_data[index][5] -= prev_ex_cost
                    file_data[index][5]+=0
                    ch_ex_pg = False
                    ch_pg = True

        user = open('USERS.csv','w', newline = '')           
        write=csv.writer(user)
        write.writerows(file_data)
        user.close()

        pygame.display.flip()


    if ch_ar:

        user=open('USERS.csv','r')
        r = csv.reader(user)
        file_data = list(r)
        user.close()

        index = -1
        for i in range(len(file_data)):
            for j in range(len(file_data[i])):
                if file_data[i][j] == user_id:
                    index = i
                    break

        file_data[index][5] = int(file_data[index][5])
        cur_cost = file_data[index][5]
        cur_area = file_data[index][4]

        if file_data[index][2] == bp_ls[0]:
            prev_bp_cost = bp_ls_cost[0]
                
        elif file_data[index][2] == bp_ls[1]:
            prev_bp_cost = bp_ls_cost[1]
                
        elif file_data[index][2] == bp_ls[2]:
            prev_bp_cost = bp_ls_cost[2]

        elif file_data[index][2] == bp_ls[3]:
            prev_bp_cost = bp_ls_cost[3]
                
        elif file_data[index][2] == bp_ls[4]:
            prev_bp_cost = bp_ls_cost[4]


        if file_data[index][3] == extra_ls[3] or file_data[index][3] == extra_ls[4] or file_data[index][3] == extra_ls[5]:
            ex_cost_offer = 10000
        elif file_data[index][3] == extra_ls[6]:
            ex_cost_offer = 15000
        else:
            ex_cost_offer = 0    

        while ch_ar:
            screen.fill(colour_bg)

            name_txt = font8.render("Please Enter Estimated Area(in m^2) below:", True, red)
            name_Rect = wel_txt.get_rect()
            name_Rect.center = (250,280)

            txt_x = 40
            txt_y = 310

            but_x=180
            but_y=350
            
            button_txt = font2.render("Enter", True,red)

            
            mouse = pygame.mouse.get_pos()
            if but_x<= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30: 
                    pygame.draw.rect(screen,white,[but_x,but_y,130,30])
            else: 
                    pygame.draw.rect(screen,color_light,[but_x,but_y,130,30])
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if txt_x <= mouse[0] <= txt_x+400 and txt_y <= mouse[1] <= txt_y+30: 
                        colour_char_active = True
                    else:
                        color_char_active = False

                    if but_x <= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30:
                        ch_ar = False
                        ch_pg = True

                if event.type == pygame.KEYDOWN:
          
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
          
                        # get text input from 0 to -1 i.e. end.
                        area_ch = area[:-1]
          
                    # Unicode standard is used for string
                    # formation
                    else:
                        area_ch += event.unicode
              
            if colour_char_active:
                color_area = color_active
            else:
                color_area = color_passive

            pygame.draw.rect(screen, color_area, (txt_x, txt_y, 400, 30))
            txt_surface = base_font.render(area_ch, True, black)
            file_data[index][4] = area_ch
            
            screen.blit(name_txt, name_Rect)
            screen.blit(txt_surface, (txt_x+10, txt_y))
            screen.blit(button_txt, (but_x+30, but_y))
            screen.blit(ic11,(230,420))
            screen.blit(ic12,(20,10))

            pygame.display.flip()

        cur_area = int(cur_area)
        cur_cost -= prev_bp_cost
        cur_cost += ex_cost_offer
        cur_cost /= cur_area
        cur_cost *= int(area_ch)
        cur_cost -= ex_cost_offer
        cur_cost += prev_bp_cost

        file_data[index][5] = int(cur_cost)
                            
        user = open('USERS.csv','w', newline = '')           
        write=csv.writer(user)
        write.writerows(file_data)
        user.close()
        
    while ch_pg:
        screen.fill(colour_bg)


        b_xg=10
        b_yg=580
        b_xg1=250
        b_yg1=580
        
        but_back=font2.render("GO BACK", True,white)
        but_change=font2.render("CHANGE DETAILS", True,white)
        
        screen.fill(colour_bg)


        wel_txt = font6.render("YOUR DETAILS HAVE BEEN MODIFIED", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (250,320)
        screen.blit(wel_txt, wel_Rect)
        screen.blit(ic9,(0,0))

        wel_txt = font2.render("HOPING YOU'LL LEAVE WITH A SMILE :)", True, black)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (250,440)
        screen.blit(wel_txt, wel_Rect)

        wel_txt = font.render("Please GO BACK and Login to check your details", True, black)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (260,480)
        screen.blit(wel_txt, wel_Rect)

        wel_txt = font.render("If you want to change something else,click CHANGE DETAILS", True, black)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (260,510)
        screen.blit(wel_txt, wel_Rect)

        mouse = pygame.mouse.get_pos()

        if b_xg <= mouse[0] <= b_xg+130 and b_yg<= mouse[1] <= b_yg+30:
            pygame.draw.rect(screen,color_light,[b_xg,b_yg,130,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg,b_yg,130,30])

        if b_xg1 <= mouse[0] <= b_xg1+240 and b_yg1<= mouse[1] <= b_yg1+30:
            pygame.draw.rect(screen,color_light,[b_xg1,b_yg1,240,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg1,b_yg1,240,30])

        screen.blit(but_back, (b_xg+10,b_yg))
        screen.blit(but_change, (b_xg1+10,b_yg1))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ch_pg = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg <= mouse[0] <= b_xg+130 and b_yg <= mouse[1] <= b_yg+30:
                    start_pg = True
                    ata_pg = False
                    admin_pg = False
                    user_pg = False
                    old_user_pg = False
                    old_user_pg1 = False
                    old_user_pg2 = False
                    old_user_pgw = False
                    newuser_pg0 = False
                    newuser_pg1 = False
                    newuser_pg2 = False
                    newuser_pg3 = False
                    newuser_pg4 = False
                    newuser_pg_ar = False
                    admin_pg0 = False
                    admin_pg1 = False
                    admin_pg2 = False
                    admin_pg3 = False
                    admin_pg4 = False
                    admin_pg5 = False
                    admin_pg6 = False
                    admin_pg_profit_loss_usr = False
                    admin_pg_d4 = False
                    admin_pg_d5 = False
                    admin_pg_ch = False
                    admin_pg_ls = False
                    find_usr_id = False
                    ch_username_cond = False
                    write_in_file = False
                    view_records = False
                    write_in_interior = False
                    read_user_checkid = False
                    read_interior = False
                    read_interior_year = False
                    ch_username = False
                    ch_bp = False
                    ch_ex = False
                    ch_ex_pg = False
                    ch_ex_ar_pg = False  
                    ch_ar = False
                    ch_pg = False
                    admin_ch_status = False
                    ch_stat = False
                    app = True


            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg1 <= mouse[0] <= b_xg1+240 and b_yg1 <= mouse[1] <= b_yg1+30:
                    start_pg = False
                    ata_pg = False
                    admin_pg = False
                    user_pg = False
                    old_user_pg = False
                    old_user_pg1 = False
                    old_user_pg2 = True
                    old_user_pgw = False
                    newuser_pg0 = False
                    newuser_pg1 = False
                    newuser_pg2 = False
                    newuser_pg3 = False
                    newuser_pg4 = False
                    newuser_pg_ar = False
                    admin_pg0 = False
                    admin_pg1 = False
                    admin_pg2 = False
                    admin_pg3 = False
                    admin_pg4 = False
                    admin_pg5 = False
                    admin_pg6 = False
                    admin_pg_profit_loss_usr = False
                    admin_pg_d4 = False
                    admin_pg_d5 = False
                    admin_pg_ch = False
                    admin_pg_ls = False
                    find_usr_id = False
                    ch_username_cond = False
                    write_in_file = False
                    view_records = False
                    write_in_interior = False
                    read_user_checkid = False
                    read_interior = False
                    read_interior_year = False
                    ch_username = False
                    ch_bp = False
                    ch_ex = False
                    ch_ex_pg = False
                    ch_ex_ar_pg = False  
                    ch_ar = False
                    ch_pg = False
                    admin_ch_status = False
                    ch_stat = False
                    app = True

        pygame.display.flip()


    while admin_pg:
        bx1=20
        by1=220
        bx2=bx1
        by2=by1+40
        bx3=bx1
        by3=by1+80
        bx4=bx1
        by4=by1+120
        bx5=bx1
        by5=by1+160
        bx6=bx1
        by6=by1+200
        screen.fill(colour_bg)

        b_xg=20
        b_yg=560
        but_back=font2.render("GO BACK", True,white)

        mouse = pygame.mouse.get_pos()

        if b_xg <= mouse[0] <= b_xg+130 and b_yg<= mouse[1] <= b_yg+30:
            pygame.draw.rect(screen,color_light,[b_xg,b_yg,130,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg,b_yg,130,30])

        screen.blit(but_back, (b_xg+10,b_yg))

        wel_txt = font3.render("HOW CAN WE HELP YOU TODAY?", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (253, 180)
        screen.blit(wel_txt, wel_Rect)
        screen.blit(ic10,(310,490))
        screen.blit(ic10,(40,10))

        but1_txt = font5.render("View records of users", True,red)
        but2_txt = font5.render("Enter records of products", True, red)
        but3_txt = font5.render("Check profit or loss in a particular project", True, red)
        but4_txt = font5.render("Check profit/loss in a month", True,red)
        but5_txt = font5.render("Check profit/loss in an year", True,red)
        but6_txt = font5.render("Change status of your projects", True,red)

        mouse = pygame.mouse.get_pos()

        if bx1 <= mouse[0] <= bx1+400 and by1 <= mouse[1] <= by1+30: 
                pygame.draw.rect(screen,white,[bx1,by1,400,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx1,by1,400,30])

        if bx2<= mouse[0] <= bx2+400 and by2 <= mouse[1] <= by2+30: 
                pygame.draw.rect(screen,white,[bx2,by2,400,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx2,by2,400,30])

        if bx3 <= mouse[0] <= bx3+400 and by3 <= mouse[1] <= by3+30: 
                pygame.draw.rect(screen,white,[bx3,by3,400,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx3,by3,400,30])

        if bx4<= mouse[0] <= bx4+400 and by4 <= mouse[1] <= by4+30: 
                pygame.draw.rect(screen,white,[bx4,by4,400,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx4,by4,400,30])

        if bx5<= mouse[0] <= bx5+400 and by5 <= mouse[1] <= by5+30: 
                pygame.draw.rect(screen,white,[bx5,by5,400,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx5,by5,400,30])

        if bx6<= mouse[0] <= bx6+400 and by6 <= mouse[1] <= by6+30: 
                pygame.draw.rect(screen,white,[bx6,by6,400,30])
        else: 
                pygame.draw.rect(screen,color_light,[bx6,by6,400,30])


        screen.blit(but1_txt , (bx2+20,by1))
        screen.blit(but2_txt , (bx1+20,by2))
        screen.blit(but3_txt , (bx3+20,by3))
        screen.blit(but4_txt , (bx4+20,by4))
        screen.blit(but5_txt , (bx5+20,by5))
        screen.blit(but6_txt , (bx6+20,by6))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                old_user_pg= False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if bx1 <= mouse[0] <= bx1+400 and by1 <= mouse[1] <= by1+30: 
                    admin_pg = False
                    admin_pg1 = True
                    view_records = True
                    
                if bx2 <= mouse[0] <= bx2+400 and by2 <= mouse[1] <= by2+30: 
                    admin_pg = False
                    admin_pg2 = True

                if bx3 <= mouse[0] <= bx3+400 and by3 <= mouse[1] <= by3+30: 
                    admin_pg = False
                    admin_pg3 = True
                    
                if bx4 <= mouse[0] <= bx4+400 and by4 <= mouse[1] <= by4+30: 
                    admin_pg = False
                    admin_pg4 = True

                if bx5 <= mouse[0] <= bx5+400 and by5 <= mouse[1] <= by5+30: 
                    admin_pg = False
                    admin_pg5 = True

                if bx6 <= mouse[0] <= bx6+400 and by6 <= mouse[1] <= by6+30:
                    admin_pg = False
                    admin_ch_status = True
                    admin_pg6 = True

                if b_xg <= mouse[0] <= b_xg+130 and b_yg <= mouse[1] <= b_yg+30:
                    start_pg = True
                    ata_pg = False
                    admin_pg = False
                    user_pg = False
                    old_user_pg = False
                    old_user_pg1 = False
                    old_user_pg2 = False
                    old_user_pgw = False
                    newuser_pg0 = False
                    newuser_pg1 = False
                    newuser_pg2 = False
                    newuser_pg3 = False
                    newuser_pg4 = False
                    newuser_pg_ar = False
                    admin_pg0 = False
                    admin_pg1 = False
                    admin_pg2 = False
                    admin_pg3 = False
                    admin_pg4 = False
                    admin_pg5 = False
                    admin_pg6 = False
                    admin_pg_profit_loss_usr = False
                    admin_pg_d4 = False
                    admin_pg_d5 = False
                    admin_pg_ch = False
                    admin_pg_ls = False
                    find_usr_id = False
                    ch_username_cond = False
                    write_in_file = False
                    view_records = False
                    write_in_interior = False
                    read_user_checkid = False
                    read_interior = False
                    read_interior_year = False
                    ch_username = False
                    ch_bp = False
                    ch_ex = False
                    ch_ex_pg = False
                    ch_ex_ar_pg = False 
                    ch_ar = False
                    ch_pg = False
                    admin_ch_status = False
                    ch_stat = False
                    app = True

        pygame.display.flip()

    if view_records:
        try:
            user=open('USERS.csv','r')
            r = csv.reader(user)
            file_data = list(r)
            user.close()
           # line = [[0]*len(file_data[0])]*len(file_data)

        except FileNotFoundError :
            print('File does not exist')
            

    while admin_pg1:
        scr = pygame.display.set_mode((1300, 620)) 
        screen.fill(colour_bg)

        x_t = 50
        y_t = 20

        b_xg=1162
        b_yg=570
    
        but_back=font2.render("GO BACK", True,white)

        mouse = pygame.mouse.get_pos()

        if b_xg <= mouse[0] <= b_xg+130 and b_yg<= mouse[1] <= b_yg+30:
            pygame.draw.rect(screen,color_light,[b_xg,b_yg,130,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg,b_yg,130,30])


        
        for i in range(len(file_data)+1):
            pygame.draw.line(screen, (0,0,0),(x_t-50,(y_t+20)*i),(1300,(y_t+20)*i), 5)

        for i in range(11):
            pygame.draw.line(screen, (0,0,0),((x_t+95)*i,y_t-20),((x_t+95)*i,620), 5)

        #pygame.draw.line(screen, (255,0,0), (100, 100), (200, 100), 5)

        for i in range(len(file_data)):
            for j in range(len(file_data[i])):
                wel_txt = fontrec.render(file_data[i][j], True, red)
                wel_Rect = wel_txt.get_rect()
                wel_Rect.center = (x_t+(150*j),y_t+(40*i))
                screen.blit(wel_txt, wel_Rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ch_pg = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg <= mouse[0] <= b_xg+130 and b_yg <= mouse[1] <= b_yg+30:
                    admin_pg_ls = False
                    start_pg = False
                    ata_pg = False
                    admin_pg = True
                    user_pg = False
                    old_user_pg = False
                    old_user_pg1 = False
                    old_user_pg2 = False
                    old_user_pgw = False
                    newuser_pg0 = False
                    newuser_pg1 = False
                    newuser_pg2 = False
                    newuser_pg3 = False
                    newuser_pg4 = False
                    newuser_pg_ar = False
                    admin_pg0 = False
                    admin_pg1 = False
                    admin_pg2 = False
                    admin_pg3 = False
                    admin_pg4 = False
                    admin_pg5 = False
                    admin_pg6 = False
                    admin_pg_profit_loss_usr = False
                    admin_pg_d4 = False
                    admin_pg_d5 = False
                    admin_pg_ch = False
                    find_usr_id = False
                    ch_username_cond = False
                    write_in_file = False
                    view_records = False
                    write_in_interior = False
                    read_user_checkid = False
                    read_interior = False
                    read_interior_year = False
                    ch_username = False
                    ch_bp = False
                    ch_ex = False
                    ch_ex_pg = False
                    ch_ex_ar_pg = False  
                    ch_ar = False
                    ch_pg = False
                    admin_ch_status = False
                    ch_stat = False
                    app = True
        
        screen.blit(but_back, (b_xg+10,b_yg))
        pygame.display.flip()


    while admin_pg2:
        screen.fill(colour_bg)

        det_txt = font6.render("ENTER THE FOLLOWING DETAILS:", True, red)
        det_Rect = wel_txt.get_rect()
        det_Rect.center = (250,40)

        prod_txt = font6.render("PRODUCT:", True, red)
        prod_Rect = wel_txt.get_rect()
        prod_Rect.center = (250,100)

        cp_txt = font6.render("COST PRICE:", True, red)
        cp_Rect = wel_txt.get_rect()
        cp_Rect.center = (250,190)

        sp_txt = font6.render("SELLING PRICE:", True, red)
        sp_Rect = wel_txt.get_rect()
        sp_Rect.center = (250,  280)

        txt_x1 = 40
        txt_y1 = 120

        txt_x2 = 40
        txt_y2 = 210

        txt_x3 = 40
        txt_y3 = 300

        but_x=180
        but_y=360
        
        button_txt = font2.render("Enter", True,red)

        
        mouse = pygame.mouse.get_pos()
        if but_x<= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30: 
                pygame.draw.rect(screen,white,[but_x,but_y,130,30])
        else: 
                pygame.draw.rect(screen,color_light,[but_x,but_y,130,30])
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if txt_x1 <= mouse[0] <= txt_x1+400 and txt_y1 <= mouse[1] <= txt_y1+30: 
                    txt1_prod_type = True
                    txt2_cp_type = False
                    txt3_sp_type = False
                    txt1_prod_active = True
                else:
                    txt1_prod_active = False

                if txt_x2 <= mouse[0] <= txt_x2+400 and txt_y2 <= mouse[1] <= txt_y2+30: 
                    txt2_cp_type = True
                    txt1_prod_type = False
                    txt3_sp_type = False
                    txt2_cp_active = True
                else:
                    txt2_cp_active = False

                if txt_x3 <= mouse[0] <= txt_x3+400 and txt_y3 <= mouse[1] <= txt_y3+30: 
                    txt3_sp_type = True
                    txt1_prod_type = False
                    txt2_cp_type = False
                    txt3_sp_active = True
                else:
                    txt3_sp_active = False

            if event.type == pygame.KEYDOWN:
      
                if event.key == pygame.K_BACKSPACE:
                    if txt1_prod_type:
                        pr = pr[:-1]
                    elif txt2_cp_type:
                        cp = cp[:-1]
                    elif txt3_sp_type:
                        sp = sp[:-1]
                else:
                    if txt1_prod_type:
                        pr += event.unicode
                    elif txt2_cp_type:
                        cp += event.unicode
                    elif txt3_sp_type:
                        sp += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if but_x <= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30:
                    admin_pg2 = False
                    write_in_interior = True
                    admin_pg_ls = True


        if txt1_prod_active:
            color_txt1_prod = color_active
        else:
            color_txt1_prod = color_passive

        if txt2_cp_active:
            color_txt2_cp = color_active
        else:
            color_txt2_cp = color_passive

        if txt3_sp_active:
            color_txt3_sp = color_active
        else:
            color_txt3_sp = color_passive
        
        pygame.draw.rect(screen, color_txt1_prod, (txt_x1, txt_y1, 400, 30))
        pygame.draw.rect(screen, color_txt2_cp, (txt_x2, txt_y2, 400, 30))
        pygame.draw.rect(screen, color_txt3_sp, (txt_x3, txt_y3, 400, 30))
        txt_surface1 = base_font.render(pr, True, black)
        txt_surface2 = base_font.render(cp, True, black)
        txt_surface3 = base_font.render(sp, True, black)
        
        screen.blit(txt_surface1, (txt_x1+10, txt_y1))
        screen.blit(txt_surface2, (txt_x2+10, txt_y2))
        screen.blit(txt_surface3, (txt_x3+10, txt_y3))

        screen.blit(ic17,(300,400))
        screen.blit(ic17,(0,400))
        
        screen.blit(det_txt, det_Rect)
        screen.blit(prod_txt, prod_Rect)
        screen.blit(cp_txt, cp_Rect)
        screen.blit(sp_txt, sp_Rect)
        
        screen.blit(button_txt, (but_x+30, but_y))

        pygame.display.flip()

    if write_in_interior:
        interior=open('INTERIOR.csv','a',newline='')
        n=interior.tell()
        inte=csv.writer(interior)
        if n==0:
            inte.writerow(['PRODUCT','COST PRICE','SELLING PRICE','PROFIT'])
        if int(sp)-int(cp)>0:
            profit=int(sp)- int(cp)
            loss='-'
        elif int(sp)-int(cp)<0:
            profit='-'
            loss=int(cp)-int(sp)
        intrec=[pr,cp,sp,profit,loss]
        inte.writerow(intrec)
        interior.close()

    while admin_pg_ls:
        b_xg=10
        b_yg=580
        b_xg1=250
        b_yg1=580
    
        but_back=font2.render("GO BACK", True,white)
        but_change=font2.render("ADD MORE", True,white)
        
        screen.fill(colour_bg)


        wel_txt = font6.render("YOUR RECORDS ARE NOW ADDED", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (250,320)
        screen.blit(wel_txt, wel_Rect)
        screen.blit(ic9,(0,0))

        wel_txt = font2.render("HOPING YOU'LL LEAVE WITH A SMILE :)", True, black)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (250,440)
        screen.blit(wel_txt, wel_Rect)

        wel_txt = font.render("Please GO BACK and check profit or loss of your company", True, black)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (260,480)
        screen.blit(wel_txt, wel_Rect)

        wel_txt = font.render("If you want to add more records,click ADD MORE", True, black)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (260,510)
        screen.blit(wel_txt, wel_Rect)

        mouse = pygame.mouse.get_pos()

        if b_xg <= mouse[0] <= b_xg+130 and b_yg<= mouse[1] <= b_yg+30:
            pygame.draw.rect(screen,color_light,[b_xg,b_yg,130,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg,b_yg,130,30])

        if b_xg1 <= mouse[0] <= b_xg1+240 and b_yg1<= mouse[1] <= b_yg1+30:
            pygame.draw.rect(screen,color_light,[b_xg1,b_yg1,240,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg1,b_yg1,240,30])

        screen.blit(but_back, (b_xg+10,b_yg))
        screen.blit(but_change, (b_xg1+10,b_yg1))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ch_pg = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg <= mouse[0] <= b_xg+130 and b_yg <= mouse[1] <= b_yg+30:
                    admin_pg_ls = False
                    start_pg = True
                    ata_pg = False
                    admin_pg = False
                    user_pg = False
                    old_user_pg = False
                    old_user_pg1 = False
                    old_user_pg2 = False
                    old_user_pgw = False
                    newuser_pg0 = False
                    newuser_pg1 = False
                    newuser_pg2 = False
                    newuser_pg3 = False
                    newuser_pg4 = False
                    newuser_pg_ar = False
                    admin_pg0 = False
                    admin_pg1 = False
                    admin_pg2 = False
                    admin_pg3 = False
                    admin_pg4 = False
                    admin_pg5 = False
                    admin_pg6 = False
                    admin_pg_profit_loss_usr = False
                    admin_pg_d4 = False
                    admin_pg_d5 = False
                    admin_pg_ch = False
                    find_usr_id = False
                    ch_username_cond = False
                    write_in_file = False
                    view_records = False
                    write_in_interior = False
                    read_user_checkid = False
                    read_interior = False
                    read_interior_year = False
                    ch_username = False
                    ch_bp = False
                    ch_ex = False
                    ch_ex_pg = False
                    ch_ex_ar_pg = False  
                    ch_ar = False
                    ch_pg = False
                    admin_ch_status = False
                    ch_stat = False
                    app = True
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg1 <= mouse[0] <= b_xg1+240 and b_yg1 <= mouse[1] <= b_yg1+30:
                    admin_pg_ls = False
                    start_pg = False
                    ata_pg = False
                    admin_pg = False
                    user_pg = False
                    old_user_pg = False
                    old_user_pg1 = False
                    old_user_pg2 = False
                    old_user_pgw = False
                    newuser_pg0 = False
                    newuser_pg1 = False
                    newuser_pg2 = False
                    newuser_pg3 = False
                    newuser_pg4 = False
                    newuser_pg_ar = False
                    admin_pg0 = False
                    admin_pg1 = False
                    admin_pg2 = True
                    admin_pg3 = False
                    admin_pg4 = False
                    admin_pg5 = False
                    admin_pg6 = False
                    admin_pg_profit_loss_usr = False
                    admin_pg_d4 = False
                    admin_pg_d5 = False
                    admin_pg_ch = False
                    admin_pg_ls = False
                    find_usr_id = False
                    ch_username_cond = False
                    write_in_file = False
                    view_records = False
                    write_in_interior = False
                    read_user_checkid = False
                    read_interior = False
                    read_interior_year = False
                    ch_username = False
                    ch_bp = False
                    ch_ex = False
                    ch_ex_pg = False
                    ch_ex_ar_pg = False  
                    ch_ar = False
                    ch_pg = False
                    admin_ch_status = False
                    ch_stat = False
                    app = True

        pygame.display.flip()
           
    usrid_active = False
    while admin_pg3:
        screen.fill(colour_bg)
        id_txt = font8.render("Enter USERID of the project to be checked:", True, red)
        id_Rect = wel_txt.get_rect()
        id_Rect.center = (240,260)

        txt_x = 40
        txt_y = 280

        but_x=180
        but_y=320
        
        button_txt = font2.render("Enter", True,red)

        
        mouse = pygame.mouse.get_pos()
        if but_x<= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30: 
                pygame.draw.rect(screen,white,[but_x,but_y,130,30])
        else: 
                pygame.draw.rect(screen,color_light,[but_x,but_y,130,30])
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if txt_x <= mouse[0] <= txt_x+400 and txt_y <= mouse[1] <= txt_y+30: 
                    usrid_active = True
                else:
                    usrid_active = False

                if but_x <= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30:
                    admin_pg3 = False
                    read_user_checkid = True
                    admin_pg_profit_loss_usr = True


            if event.type == pygame.KEYDOWN:
      
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
      
                    # get text input from 0 to -1 i.e. end.
                    user_id = user_id[:-1]
      
                # Unicode standard is used for string
                # formation
                else:
                    user_id += event.unicode
          
        if usrid_active:
            color_usrid = color_active
        else:
            color_usrid = color_passive

        pygame.draw.rect(screen, color_usrid, (txt_x, txt_y, 400, 30))
        txt_surface = base_font.render(user_id, True, black)
        
        screen.blit(id_txt, id_Rect)
        screen.blit(txt_surface, (txt_x+10, txt_y))
        screen.blit(button_txt, (but_x+30, but_y))
        screen.blit(ic13,(230,420))
        screen.blit(ic14,(10,10))

        pygame.display.flip()

    if read_user_checkid:
        found=0
        user=open('USERS.csv','r')
        us=csv.reader(user)
        next(us)
        cp=0
        sp=0
        user.seek(0)
        for REC in us:
            if REC[0]==user_id:
                found=1
                if found==1:
                    sp=int(REC[5])
                    if extra_ls[0] == (REC[3]):
                        cp+=int(150*(int(REC[4])))
                    elif extra_ls[1] == REC[3]:
                        cp+=int(275*(int(REC[4])))
                    elif extra_ls[2] == REC[3]:
                        cp+=int(480*(int(REC[4])))
                    elif extra_ls[3] == REC[3]:
                        cp+=int((150+275)*(int(REC[4])))
                    elif extra_ls[4] == REC[3]:
                        cp+=int((150+480)*(int(REC[4])))
                    elif extra_ls[5] == REC[3]:
                        cp+=int((480+275)*(int(REC[4])))
                    elif extra_ls[6] == REC[3]:
                        cp+=int((150+275+480)*(int(REC[4])))
                    elif extra_ls[7] == REC[3]:
                        cp+=0
        user.close()
        
    while admin_pg_profit_loss_usr:
        screen.fill(colour_bg)

        b_xg=20
        b_yg=560
    
        but_back=font2.render("GO BACK", True,white)

        mouse = pygame.mouse.get_pos()

        if b_xg <= mouse[0] <= b_xg+130 and b_yg<= mouse[1] <= b_yg+30:
            pygame.draw.rect(screen,color_light,[b_xg,b_yg,130,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg,b_yg,130,30])

        screen.blit(but_back, (b_xg+10,b_yg))

        det_txt = font6.render("YOUR REQUIRED DETAILS ARE:", True, red)
        det_Rect = wel_txt.get_rect()
        det_Rect.center = (240,250)
        screen.blit(det_txt, det_Rect)

        det_txt = font2.render("COST PRICE:" + ' ' + str(cp), True, black)
        det_Rect = wel_txt.get_rect()
        det_Rect.center = (300,290)
        screen.blit(det_txt, det_Rect)

        det_txt = font2.render("SELLING PRICE:" + ' ' + str(sp), True, black)
        det_Rect = wel_txt.get_rect()
        det_Rect.center = (300,330)
        screen.blit(det_txt, det_Rect)

        screen.blit(ic13,(230,420))
        screen.blit(ic14,(10,10))

        if cp>sp:
            det_txt = font2.render('LOSS OF Rs.' + ' ' + str(cp-sp), True, black)
            det_Rect = wel_txt.get_rect()
            det_Rect.center = (300,370)
            screen.blit(det_txt, det_Rect)

        elif sp>cp:
            det_txt = font2.render('PROFIT OF Rs.' + ' ' + str(sp-cp), True, black)
            det_Rect = wel_txt.get_rect()
            det_Rect.center = (300,370)
            screen.blit(det_txt, det_Rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ata_pg = False
                app = False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg <= mouse[0] <= b_xg+130 and b_yg <= mouse[1] <= b_yg+30:
                    start_pg = False
                    ata_pg = False
                    admin_pg = True
                    user_pg = False
                    old_user_pg = False
                    old_user_pg1 = False
                    old_user_pg2 = False
                    old_user_pgw = False
                    newuser_pg0 = False
                    newuser_pg1 = False
                    newuser_pg2 = False
                    newuser_pg3 = False
                    newuser_pg4 = False
                    newuser_pg_ar = False
                    admin_pg0 = False
                    admin_pg1 = False
                    admin_pg2 = False
                    admin_pg3 = False
                    admin_pg4 = False
                    admin_pg5 = False
                    admin_pg6 = False
                    admin_pg_profit_loss_usr = False
                    admin_pg_d4 = False
                    admin_pg_d5 = False
                    admin_pg_ch = False
                    admin_pg_ls = False
                    find_usr_id = False
                    ch_username_cond = False
                    write_in_file = False
                    view_records = False
                    write_in_interior = False
                    read_user_checkid = False
                    read_interior = False
                    read_interior_year = False
                    ch_username = False
                    ch_bp = False
                    ch_ex = False
                    ch_ex_pg = False
                    ch_ex_ar_pg = False 
                    ch_ar = False
                    ch_pg = False
                    admin_ch_status = False
                    ch_stat = False
                    app = True

            

        pygame.display.flip()



    while admin_pg4:
        screen.fill(colour_bg)
        
        yr_txt = font8.render("Enter year of the projects to be checked:", True, red)
        yr_Rect = wel_txt.get_rect()
        yr_Rect.center = (240,220)

        mot_txt = font8.render("Enter month of the projects to be checked:", True, red)
        mot_Rect = wel_txt.get_rect()
        mot_Rect.center = (240,330)

        txt_x1 = 40
        txt_y1 = 250

        txt_x2 = 40
        txt_y2 = 350

        but_x=180
        but_y=390
        
        button_txt = font2.render("Enter", True,red)

        
        mouse = pygame.mouse.get_pos()
        if but_x<= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30: 
                pygame.draw.rect(screen,white,[but_x,but_y,130,30])
        else: 
                pygame.draw.rect(screen,color_light,[but_x,but_y,130,30])
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if txt_x1 <= mouse[0] <= txt_x1+400 and txt_y1 <= mouse[1] <= txt_y1+30: 
                    txt1_yr_type = True
                    txt2_mon_type = False
                    txt1_yr_active = True
                else:
                    txt1_yr_active = False

                if txt_x2 <= mouse[0] <= txt_x2+400 and txt_y2 <= mouse[1] <= txt_y2+30: 
                    txt2_mon_type = True
                    txt1_yr_type = False
                    txt2_mon_active = True
                else:
                    txt2_mon_active = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if but_x <= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30:
                    admin_pg4 = False
                    read_interior = True
                    admin_pg_d4 = True

                

            if event.type == pygame.KEYDOWN:
      
                if event.key == pygame.K_BACKSPACE:
                    if txt1_yr_type:
                        year = year[:-1]
                    elif txt2_mon_type:
                        month = month[:-1]
                else:
                    if txt1_yr_type:
                        year += event.unicode
                    elif txt2_mon_type:
                        month += event.unicode
          
        if txt1_yr_active:
            color_txt1_yr = color_active
        else:
            color_txt1_yr = color_passive

        if txt2_mon_active:
            color_txt2_mon = color_active
        else:
            color_txt2_mon = color_passive
            
        pygame.draw.rect(screen, color_txt1_yr, (txt_x1, txt_y1, 400, 30))
        pygame.draw.rect(screen, color_txt2_mon, (txt_x2, txt_y2, 400, 30))
        txt_surface1 = base_font.render(year, True, black)
        txt_surface2 = base_font.render(month, True, black)
        
        screen.blit(txt_surface1, (txt_x1+10, txt_y1))
        screen.blit(txt_surface2, (txt_x2+10, txt_y2))

        screen.blit(ic14,(0,0))
        screen.blit(ic16,(200,420))
        
        screen.blit(yr_txt, yr_Rect)
        screen.blit(mot_txt, mot_Rect)
        screen.blit(button_txt, (but_x+30, but_y))

        pygame.display.flip()

    if read_interior:
        user=open('USERS.csv','r')
        us=csv.reader(user)
        next(us)
        sp=0
        cp=0
        net=0
        for REC in us:
            if REC[8].upper()==year.upper():
                if REC[7].upper()==month.upper():
                    flag=1
                    if flag==1:
                        sp=int(REC[5])
                    if extra_ls[0] == (REC[3]):
                        cp+=int(150*(int(REC[4])))
                    elif extra_ls[1] == REC[3]:
                        cp+=int(275*(int(REC[4])))
                    elif extra_ls[2] == REC[3]:
                        cp+=int(480*(int(REC[4])))
                    elif extra_ls[3] == REC[3]:
                        cp+=int((150+275)*(int(REC[4])))
                    elif extra_ls[4] == REC[3]:
                        cp+=int((150+480)*(int(REC[4])))
                    elif extra_ls[5] == REC[3]:
                        cp+=int((480+275)*(int(REC[4])))
                    elif extra_ls[6] == REC[3]:
                        cp+=int((150+275+480)*(int(REC[4])))
                    elif extra_ls[7] == REC[3]:
                        cp+=0
                    net+=sp-cp
            
        user.close()


    while admin_pg_d4:

        screen.fill(colour_bg)
        screen.blit(ic11,(230,420))
        screen.blit(ic12,(20,10))

        b_xg=20
        b_yg=560
    
        but_back=font2.render("GO BACK", True,white)

        mouse = pygame.mouse.get_pos()

        if b_xg <= mouse[0] <= b_xg+130 and b_yg<= mouse[1] <= b_yg+30:
            pygame.draw.rect(screen,color_light,[b_xg,b_yg,130,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg,b_yg,130,30])

        screen.blit(but_back, (b_xg+10,b_yg))

        if net<0:
                det_txt = font4.render('LOSS OF Rs.' + ' ' + str(abs(net)) +' '+ "in" + ' ' + str(month) + ',' +str(year), True, black)
                det_Rect = wel_txt.get_rect()
                det_Rect.center = (250,310)
                screen.blit(det_txt, det_Rect)
                
        if net>0:

                det_txt = font4.render('PROFIT OF Rs.' +  ' '  + str(abs(net)) +' '+ "in" + ' ' +  str(month) + ',' +str(year), True, black)
                det_Rect = wel_txt.get_rect()
                det_Rect.center = (250,310)
                screen.blit(det_txt, det_Rect)
                
        if net==0:

                det_txt = font4.render("NEITHER PROFIT NOR LOSS" + " "+ "IN" + ' ' +str(month) + ',' +str(year), True, red)
                det_Rect = wel_txt.get_rect()
                det_Rect.center = (250,310)
                screen.blit(det_txt, det_Rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ata_pg = False
                app = False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg <= mouse[0] <= b_xg+130 and b_yg <= mouse[1] <= b_yg+30:
                    start_pg = False
                    ata_pg = False
                    admin_pg = True
                    user_pg = False
                    old_user_pg = False
                    old_user_pg1 = False
                    old_user_pg2 = False
                    old_user_pgw = False
                    newuser_pg0 = False
                    newuser_pg1 = False
                    newuser_pg2 = False
                    newuser_pg3 = False
                    newuser_pg4 = False
                    newuser_pg_ar = False
                    admin_pg0 = False
                    admin_pg1 = False
                    admin_pg2 = False
                    admin_pg3 = False
                    admin_pg4 = False
                    admin_pg5 = False
                    admin_pg6 = False
                    admin_pg_profit_loss_usr = False
                    admin_pg_d4 = False
                    admin_pg_d5 = False
                    admin_pg_ch = False
                    admin_pg_ls = False
                    find_usr_id = False
                    ch_username_cond = False
                    write_in_file = False
                    view_records = False
                    write_in_interior = False
                    read_user_checkid = False
                    read_interior = False
                    read_interior_year = False
                    ch_username = False
                    ch_bp = False
                    ch_ex = False
                    ch_ex_pg = False
                    ch_ex_ar_pg = False 
                    ch_ar = False
                    ch_pg = False
                    admin_ch_status = False
                    ch_stat = False
                    app = True
            

        pygame.display.flip()



    while admin_pg5:
        screen.fill(colour_bg)
        
        yr_txt = font8.render("Enter year of the projects to be checked:", True, red)
        yr_Rect = wel_txt.get_rect()
        yr_Rect.center = (240,260)

        txt_x = 40
        txt_y = 280

        but_x=180
        but_y=320
        
        button_txt = font2.render("Enter", True,red)

        
        mouse = pygame.mouse.get_pos()
        if but_x<= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30: 
                pygame.draw.rect(screen,white,[but_x,but_y,130,30])
        else: 
                pygame.draw.rect(screen,color_light,[but_x,but_y,130,30])
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if txt_x <= mouse[0] <= txt_x+400 and txt_y <= mouse[1] <= txt_y+30: 
                    year_active = True
                else:
                    year_active = False

                if but_x <= mouse[0] <= but_x+130 and but_y <= mouse[1] <= but_y+30:
                    admin_pg5 = False
                    read_interior_year = True
                    admin_pg_d5 = True


            if event.type == pygame.KEYDOWN:
      
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
      
                    # get text input from 0 to -1 i.e. end.
                    year = year[:-1]
      
                # Unicode standard is used for string
                # formation
                else:
                    year += event.unicode
          
        if year_active:
            color_year = color_active
        else:
            color_year = color_passive

        pygame.draw.rect(screen, color_year, (txt_x, txt_y, 400, 30))
        txt_surface = base_font.render(year, True, black)
        
        screen.blit(yr_txt, yr_Rect)
        screen.blit(txt_surface, (txt_x+10, txt_y))
        screen.blit(button_txt, (but_x+30, but_y))
        screen.blit(ic13,(230,420))
        screen.blit(ic14,(10,10))
        
        pygame.display.flip()

    if read_interior_year:
        f=0
        user=open('USERS.csv','r')
        us=csv.reader(user)
        next(us)
        sp=0
        cp=0
        net=0
        for REC in us:
            if REC[8]==year:
                f=1
                if f==1:
                    flag=1
                    if flag==1:
                        sp=int(REC[5])
                    if extra_ls[0] == (REC[3]):
                        cp+=int(150*(int(REC[4])))
                    elif extra_ls[1] == REC[3]:
                        cp+=int(275*(int(REC[4])))
                    elif extra_ls[2] == REC[3]:
                        cp+=int(480*(int(REC[4])))
                    elif extra_ls[3] == REC[3]:
                        cp+=int((150+275)*(int(REC[4])))
                    elif extra_ls[4] == REC[3]:
                        cp+=int((150+480)*(int(REC[4])))
                    elif extra_ls[5] == REC[3]:
                        cp+=int((480+275)*(int(REC[4])))
                    elif extra_ls[6] == REC[3]:
                        cp+=int((150+275+480)*(int(REC[4])))
                    elif extra_ls[7] == REC[3]:
                        cp+=0
                    net+=sp-cp


    while admin_pg_d5:
        screen.fill(colour_bg)
        screen.blit(ic11,(230,420))
        screen.blit(ic12,(20,10))

        b_xg=20
        b_yg=560
    
        but_back=font2.render("GO BACK", True,white)

        mouse = pygame.mouse.get_pos()

        if b_xg <= mouse[0] <= b_xg+130 and b_yg<= mouse[1] <= b_yg+30:
            pygame.draw.rect(screen,color_light,[b_xg,b_yg,130,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg,b_yg,130,30])

        screen.blit(but_back, (b_xg+10,b_yg))

        if net<0:
                det_txt = font4.render('LOSS OF Rs.' + ' ' + str(abs(net)) + ' ' + "IN YEAR" + ' ' + str(year), True, black)
                det_Rect = wel_txt.get_rect()
                det_Rect.center = (200,310)
                screen.blit(det_txt, det_Rect)
                
        if net>0:

                det_txt = font4.render('PROFIT OF Rs.' + ' ' + str(abs(net)) + ' ' + "IN YEAR" + ' ' + str(year), True, black)
                det_Rect = wel_txt.get_rect()
                det_Rect.center = (200,310)
                screen.blit(det_txt, det_Rect)
                
        if net==0:

                det_txt = font4.render("NEITHER PROFIT NOR LOSS IN YEAR" + ' ' + str(year), True, red)
                det_Rect = wel_txt.get_rect()
                det_Rect.center = (250,310)
                screen.blit(det_txt, det_Rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ata_pg = False
                app = False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg <= mouse[0] <= b_xg+130 and b_yg <= mouse[1] <= b_yg+30:
                    start_pg = False
                    ata_pg = False
                    admin_pg = True
                    user_pg = False
                    old_user_pg = False
                    old_user_pg1 = False
                    old_user_pg2 = False
                    old_user_pgw = False
                    newuser_pg0 = False
                    newuser_pg1 = False
                    newuser_pg2 = False
                    newuser_pg3 = False
                    newuser_pg4 = False
                    newuser_pg_ar = False
                    admin_pg0 = False
                    admin_pg1 = False
                    admin_pg2 = False
                    admin_pg3 = False
                    admin_pg4 = False
                    admin_pg5 = False
                    admin_pg6 = False
                    admin_pg_profit_loss_usr = False
                    admin_pg_d4 = False
                    admin_pg_d5 = False
                    admin_pg_ch = False
                    admin_pg_ls = False
                    find_usr_id = False
                    ch_username_cond = False
                    write_in_file = False
                    view_records = False
                    write_in_interior = False
                    read_user_checkid = False
                    read_interior = False
                    read_interior_year = False
                    ch_username = False
                    ch_bp = False
                    ch_ex = False
                    ch_ex_pg = False
                    ch_ex_ar_pg = False 
                    ch_ar = False
                    ch_pg = False
                    admin_ch_status = False
                    ch_stat = False
                    app = True
                
        pygame.display.flip()

    if admin_ch_status:
        user=open('USERS.csv','r')
        r = csv.reader(user)
        file_data = list(r)
        user.close()

    while admin_pg6:
        screen.fill(colour_bg)

        x_t = 40
        y_t = 20

        x_t1=170
        y_t1=20

        x_t2 =330
        y_t2 =20

        b_xg=20
        b_yg=560
    
        but_back=font2.render("GO BACK", True,white)
        
        for i in range(len(file_data)):
            for j in range(len(file_data[i])):
                wel_txt = font5.render(file_data[i][0].upper(), True, black)
                wel_Rect = wel_txt.get_rect()
                wel_Rect.topleft = (x_t,y_t+(40*i))
                screen.blit(wel_txt, wel_Rect)

        for i in range(len(file_data)):
            for j in range(len(file_data[i])):
                wel_txt = font5.render(file_data[i][1].upper(), True, black)
                wel_Rect = wel_txt.get_rect()
                wel_Rect.topleft = (x_t1,y_t1+(40*i))
                screen.blit(wel_txt, wel_Rect)

        for i in range(len(file_data)):
            for j in range(len(file_data[i])):
                wel_txt = font5.render(file_data[i][6].upper(), True, black)
                wel_Rect = wel_txt.get_rect()
                wel_Rect.topleft = (x_t2,y_t2+(40*i))
                screen.blit(wel_txt, wel_Rect)

##        id_txt = font.render("Enter USERID of project whose status has to be changed :", True, red)
##        id_Rect = wel_txt.get_rect()
##        id_Rect.topleft = (250,520)

        but_x=270
        but_y=570
        
        button_txt = font7.render("CHANGE STATUS", True,red)

        
        mouse = pygame.mouse.get_pos()
        if but_x<= mouse[0] <= but_x+220 and but_y <= mouse[1] <= but_y+30: 
                pygame.draw.rect(screen,white,[but_x,but_y,220,30])
        else: 
                pygame.draw.rect(screen,color_light,[but_x,but_y,220,30])

        if b_xg <= mouse[0] <= b_xg+130 and b_yg<= mouse[1] <= b_yg+30:
            pygame.draw.rect(screen,color_light,[b_xg,b_yg,130,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg,b_yg,130,30])

        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if but_x <= mouse[0] <= but_x+220 and but_y <= mouse[1] <= but_y+30:
                    admin_pg6 = False
                    ch_stat = True
                    admin_pg_ch = True

                if b_xg <= mouse[0] <= b_xg+130 and b_yg <= mouse[1] <= b_yg+30:
                    admin_pg_ls = False
                    start_pg = False
                    ata_pg = False
                    admin_pg = True
                    user_pg = False
                    old_user_pg = False
                    old_user_pg1 = False
                    old_user_pg2 = False
                    old_user_pgw = False
                    newuser_pg0 = False
                    newuser_pg1 = False
                    newuser_pg2 = False
                    newuser_pg3 = False
                    newuser_pg4 = False
                    newuser_pg_ar = False
                    admin_pg0 = False
                    admin_pg1 = False
                    admin_pg2 = False
                    admin_pg3 = False
                    admin_pg4 = False
                    admin_pg5 = False
                    admin_pg6 = False
                    admin_pg_profit_loss_usr = False
                    admin_pg_d4 = False
                    admin_pg_d5 = False
                    admin_pg_ch = False
                    find_usr_id = False
                    ch_username_cond = False
                    write_in_file = False
                    view_records = False
                    write_in_interior = False
                    read_user_checkid = False
                    read_interior = False
                    read_interior_year = False
                    ch_username = False
                    ch_bp = False
                    ch_ex = False
                    ch_ex_pg = False
                    ch_ex_ar_pg = False  
                    ch_ar = False
                    ch_pg = False
                    admin_ch_status = False
                    ch_stat = False
                    app = True
        
        screen.blit(button_txt, (but_x+30, but_y))
        screen.blit(but_back, (b_xg+10,b_yg))
        pygame.display.flip()


    while admin_pg_ch:
        screen.fill(colour_bg)

        id_txt = font.render("PLEASE ENTER THE USERID WHOSE STATUS HAS TO BE CHANGED:", True, red)
        id_Rect = wel_txt.get_rect()
        id_Rect.center = (85,260)

        txt_x = 40
        txt_y = 280

        but_x=100
        but_y=320
        
        button_txt = font7.render("CHANGE STATUS", True,red)

        
        mouse = pygame.mouse.get_pos()
        if but_x<= mouse[0] <= but_x+220 and but_y <= mouse[1] <= but_y+30: 
                pygame.draw.rect(screen,white,[but_x,but_y,220,30])
        else: 
                pygame.draw.rect(screen,color_light,[but_x,but_y,200,30])
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if txt_x <= mouse[0] <= txt_x+400 and txt_y <= mouse[1] <= txt_y+30: 
                    colour_userid_chstat_active = True
                else:
                    colour_userid_chstat_active = False
                                
            if event.type == pygame.KEYDOWN:
      
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
      
                    # get text input from 0 to -1 i.e. end.
                    user_id_chstat = user_id_chstat[:-1]
      
                # Unicode standard is used for string
                # formation
                else:
                    user_id_chstat += event.unicode
          
        if colour_userid_chstat_active:
            color_userid_chstat = color_active
        else:
            color_userid_chstat = color_passive

        pygame.draw.rect(screen, color_userid_chstat, (txt_x, txt_y, 400, 30))
        txt_surface = base_font.render(user_id_chstat, True, black)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if but_x <= mouse[0] <= but_x+220 and but_y <= mouse[1] <= but_y+30:
                admin_pg_ch = False
                admin_pg0 = True
        
        screen.blit(id_txt, id_Rect)
        screen.blit(txt_surface, (txt_x+10, txt_y))
        screen.blit(button_txt, (but_x+20, but_y))
        screen.blit(ic13,(230,420))
        screen.blit(ic14,(10,10))
        pygame.display.flip()

    if ch_stat:
        user=open('USERS.csv','r')
        r = csv.reader(user)
        file_data = list(r)
        user.close()


        for i in range(len(file_data)):
            for j in range(len(file_data[i])):
                if file_data[i][j] == user_id_chstat:
                    index = i
                    break

        if file_data[index][6] == "UNDER PROCESS":
            file_data[index][6] = "COMPLETED"

        elif file_data[index][6] == "COMPLETED":
            file_data[index][6] = "UNDER PROCESS"

        user = open('USERS.csv','w', newline = '')           
        write=csv.writer(user)
        write.writerows(file_data)
        user.close()

    while admin_pg0:
        screen.fill(colour_bg)


        b_xg=10
        b_yg=580
        b_xg1=250
        b_yg1=580
        
        but_back=font2.render("GO BACK", True,white)
        but_change=font2.render("CHANGE STATUS", True,white)
        
        screen.fill(colour_bg)


        wel_txt = font6.render("STATUS HAS BEEN CHANGED", True, red)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (250,320)
        screen.blit(wel_txt, wel_Rect)
        screen.blit(ic9,(0,0))

        wel_txt = font.render("Please GO BACK and check the status of your clients", True, black)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (260,480)
        screen.blit(wel_txt, wel_Rect)

        wel_txt = font.render("If you want to change something else,click CHANGE STATUS", True, black)
        wel_Rect = wel_txt.get_rect()
        wel_Rect.center = (260,510)
        screen.blit(wel_txt, wel_Rect)

        mouse = pygame.mouse.get_pos()

        if b_xg <= mouse[0] <= b_xg+130 and b_yg<= mouse[1] <= b_yg+30:
            pygame.draw.rect(screen,color_light,[b_xg,b_yg,130,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg,b_yg,130,30])

        if b_xg1 <= mouse[0] <= b_xg1+240 and b_yg1<= mouse[1] <= b_yg1+30:
            pygame.draw.rect(screen,color_light,[b_xg1,b_yg1,240,30])
        else:
            pygame.draw.rect(screen,color_dark,[b_xg1,b_yg1,240,30])

        screen.blit(but_back, (b_xg+10,b_yg))
        screen.blit(but_change, (b_xg1+10,b_yg1))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                admin_pg = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg <= mouse[0] <= b_xg+130 and b_yg <= mouse[1] <= b_yg+30:
                    admin_pg0 = False
                    start_pg = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_xg1 <= mouse[0] <= b_xg1+240 and b_yg1 <= mouse[1] <= b_yg1+30:
                    admin_pg0 = False
                    admin_pg6 = True

        pygame.display.flip()
