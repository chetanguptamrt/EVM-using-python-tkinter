from tkinter import *
from tkinter.messagebox import showerror,showinfo
from tkinter.simpledialog import askstring
import set_default
import pickle
from functools import partial
class Pass:
    def __init__(self,current_password='12345678'):
        self.current_password=current_password
class Participant:
    def __init__(self,parti_list,vote_list):
        self.parti_list=parti_list
        self.vote_list=vote_list
def show_about():
    showinfo('About','EVM version 1.0\nMade by chetanguptamrt')
def show_contact():
    showinfo('Contact us','Contact us on twitter\n - @chetanguptamrt')
def update_vote(vote):
    with open('assets\\participants.dat',mode='rb') as f:
        obj=pickle.load(f)
        list1=obj.parti_list
        list2=obj.vote_list
        list2[vote]+=1
    with open('assets\\participants.dat',mode='wb') as f:
        stu=Participant(list1,list2)
        pickle.dump(stu,f)
    update_list()
def turn_on_off_vote_button():
    if admin_panel_update==True:
        for i in list_frame:
            i[1].config(state='disable')
def update_list():
    global list_frame
    for i in list_frame:
        for j in i:
            j.destroy()
    list_frame=[]
    i=0
    with open('assets\\participants.dat',mode='rb') as f:
        obj=pickle.load(f)
        for i in range(len(obj.parti_list)):
            list_lbl1=Label(frame_1,text=obj.parti_list[i],font='lucida 12',bg='#ffffff')
            list_lbl1.grid(row=i+1,column=0)
            list_btn2=Button(frame_1,text='Vote',font='lucida 10',bg='#4BCFFA',padx=8,command=partial(update_vote,i))
            list_btn2.grid(row=i+1,column=1,pady=(0,1))
            list_lbl3=Label(frame_1,text=obj.vote_list[i],font='lucida 12',bg='#ffffff')
            list_lbl3.grid(row=i+1,column=2)
            list_frame.append([list_lbl1,list_btn2,list_lbl3])
    empty_space=15-len(obj.parti_list)
    for j in range(empty_space):
        list_lbl1=Label(frame_1,text='<empty>',font='lucida 12',bg='#ffffff',fg='#A4B0BD')
        list_lbl1.grid(row=i+j+2,column=0)
        list_btn2=Button(frame_1,text='Vote',font='lucida 10',bg='#4BCFFA',padx=8,state='disable')
        list_btn2.grid(row=i+j+2,column=1,pady=(0,1))
        list_lbl3=Label(frame_1,text='0',font='lucida 12',bg='#ffffff',fg='#A4B0BD')
        list_lbl3.grid(row=i+j+2,column=2)
        list_frame.append([list_lbl1,list_btn2,list_lbl3])
    turn_on_off_vote_button()
def add_participants(event=0):
    global list_frame
    if participant_name.get()=='':
        pass
    elif len(participant_name.get())<=16:
        with open('assets\\participants.dat',mode='rb') as f:
            obj=pickle.load(f)
        
        if participant_name.get() not in obj.parti_list:
            list1=obj.parti_list
            list1.append(participant_name.get())
            list2=[]
            for i in range(len(list1)):
                list2.append(0)
            with open('assets\\participants.dat',mode='wb') as f:
                stu=Participant(list1,list2)
                pickle.dump(stu,f)
            participant_name.set('')
            update_list()
        else:
            showerror('Error',f'{participant_name.get()} are already exist.')
    else:
        showerror('Error','Participants name must be in 1-16 charactor')
def remove_participants(event=0):
    global list_frame
    if remove_participant_name.get()=='':
        pass
    else:
       
        with open('assets\\participants.dat',mode='rb') as f:
            obj=pickle.load(f)
        if remove_participant_name.get() in obj.parti_list:
            list1=obj.parti_list
            list2=[]
            list1.remove(remove_participant_name.get())
            for i in range(len(list1)):
                list2.append(0)
            with open('assets\\participants.dat',mode='wb') as f:
                stu=Participant(list1,list2)
                pickle.dump(stu,f)
            remove_participant_name.set('')
            update_list()
        else:
            showerror('Error',f'{remove_participant_name.get()} is not exist.')
            remove_participant_name.set('')
def set_default_setting():
    set_default.set_pass()
    update_list()
def pass_change():
    with open('Assets\\pass.dat',mode="rb") as f:
        obj=pickle.load(f)
    if new_password.get()==repeat_password.get() and current_password.get()==obj.current_password:
        with open('Assets\\pass.dat',mode='wb') as f:
            stu=Pass(new_password.get())
            pickle.dump(stu,f)
        showinfo('Information','Successfully change password')
        new_password.set('')
        repeat_password.set('')
        current_password.set('')
    else:
        showerror('Error','Please write correct info')
def show_password():
    global ad_en1,ad_en2,ad_en3,show_pass
    if show_pass==1:
        ad_en1.config(show='')
        ad_en2.config(show='')
        ad_en3.config(show='')
        show_pass=0
    elif show_pass==0:
        ad_en1.config(show='*')
        ad_en2.config(show='*')
        ad_en3.config(show='*')
        show_pass=1
def admin_panel_off():
    global f2,admin_panel_update
    root.geometry('400x600')
    f2.destroy()
    ad_pnl_btn.config(state='normal')
    admin_panel_update=False
    update_list()
def admin_panel():
    global root,f2,ad_en1,ad_en2,ad_en3,show_pass
    root.geometry('700x600')
    show_pass=1
    current_password.set('')
    new_password.set('')
    repeat_password.set('')
    participant_name.set('')
    ad_pnl_btn.config(state='disable')
    #-------------------------------frame for admin----------------------------------
    f2=Frame(root,bd=2,relief='ridge',width=300,height=600,bg='#ffffff')
    f2.pack(side='right',anchor='ne',padx=(0,2))
    Label(f2,text='Admin panel',font='ludica 24 bold underline',height=2,width=15,bg='#ffffff').pack()
    Label(f2,text='Password Change',font='ludica 18 bold underline',height=1,width=15,bg='#ffffff').pack()
    Label(f2,text='Default password is 12345678',font='ludica 8 bold underline',fg='#FF3031',bg='#ffffff').pack(pady=(0,4))
    Label(f2,text='Old password',font='ludica 13 underline',bg='#ffffff').pack()
    ad_en1=Entry(f2,width=20,show='*',font='ludica 16',relief='solid',textvariable=current_password)
    ad_en1.pack(pady=(0,4))
    Label(f2,text='New password',font='ludica 13 underline',bg='#ffffff').pack()
    ad_en2=Entry(f2,width=20,show='*',font='ludica 16',relief='solid',textvariable=new_password)
    ad_en2.pack(pady=(0,4))
    Label(f2,text='Confirm password',font='ludica 13 underline',bg='#ffffff').pack()
    ad_en3=Entry(f2,width=20,show='*',font='ludica 16',relief='solid',textvariable=repeat_password)
    ad_en3.pack(pady=(0,4))
    f3=Frame(f2,bg='#ffffff')
    f3.pack(pady=(0,4))
    Button(f3,text='show password',command=show_password).pack(side=LEFT,padx=(0,14))
    Button(f3,text='Change password',command=pass_change).pack(side=RIGHT)
    Label(f2,text='Add participant',font='ludica 18 bold underline',height=1,width=15,bg='#ffffff').pack()
    ad_pnl_en1=Entry(f2,width=15,font='ludica 16',relief='solid',textvariable=participant_name)
    ad_pnl_en1.pack(pady=3)
    ad_pnl_en1.bind('<Return>',add_participants)
    Button(f2,text='Add participant',command=add_participants).pack()
    Label(f2,text='Remove participant',font='ludica 18 bold underline',height=1,width=15,bg='#ffffff').pack()
    ad_pnl_en2=Entry(f2,width=15,font='ludica 16',relief='solid',textvariable=remove_participant_name)
    ad_pnl_en2.pack(pady=3)
    ad_pnl_en2.bind('<Return>',remove_participants)
    Button(f2,text='Remove participant',command=remove_participants).pack()
    Label(f2,text='Warning! If add & remove participants\nthen all votes will be 0.',font='ludica 8 bold underline',fg='#FF3031',bg='#ffffff').pack(pady=1)
    Button(f2,text='<- Back to voting',command=admin_panel_off).pack(pady=1)
def admin_panel_check():
    global admin_panel_update
    pass_check=askstring('Password','Enter admin password\nDefault password is "12345678"')
    with open('Assets\\pass.dat',mode="rb") as f:
        obj=pickle.load(f)
    if pass_check==None:
        pass
    elif pass_check==obj.current_password:
        admin_panel()
        admin_panel_update=True
        turn_on_off_vote_button()
    else:
        showerror('Error','please enter correct password')
if __name__=='__main__':
    root=Tk()
    root.geometry('400x600+400+10')
    root.resizable(False,False)
    root.title('EVM by chetanguptamrt')
    root.config(bg='#ffffff')
    #-------------------------------component-------------------------------------------
    current_password=StringVar()
    new_password=StringVar()
    repeat_password=StringVar()
    participant_name=StringVar()
    remove_participant_name=StringVar()
    list_frame=[]
    admin_panel_update=False
    #-------------------------------menu------------------------------------------------
    mainmenubar=Menu(root)

    m1=Menu(mainmenubar,tearoff=0)
    m1.add_command(label="Set Default Password",command=set_default_setting)
    m1.add_separator()
    m1.add_command(label="exit",command=quit)
    mainmenubar.add_cascade(label="File",menu=m1)

    m1=Menu(mainmenubar,tearoff=0)
    m1.add_command(label="Contact us",command=show_contact)
    m1.add_command(label="About",command=show_about)
    mainmenubar.add_cascade(label="Help",menu=m1)

    root.config(menu=mainmenubar)
    #-------------------------------frame for vote----------------------------------
    f1=Frame(root,bd=2,relief='ridge',width=400,height=600,bg='#ffffff')
    f1.pack(side='left',anchor='nw',padx=(2,0))
    Label(f1,text='Electic voting machine',font='lucida 24 bold underline',width=20,height=2,bg='#ffffff').pack(padx=3)

    frame_1=Frame(f1,bd=3,relief='ridge',bg='#ffffff')
    frame_1.pack()
    Label(frame_1,text="Participants Name",font='lucida 14 bold',bg='#ffffff',justify='center').grid(row=0,column=0,padx=15)
    Label(frame_1,text="Vote",font='lucida 14 bold',bg='#ffffff',justify='center').grid(row=0,column=1,padx=15)
    Label(frame_1,text="Total",font='lucida 14 bold',bg='#ffffff',justify='center').grid(row=0,column=2,padx=15)
    update_list()

    ad_pnl_btn=Button(f1,text='Admin panel ->',command=admin_panel_check)
    ad_pnl_btn.pack(pady=(9,10))

    root.mainloop()