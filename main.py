import tkinter as tk
from tkinter import *
import time
from socket import *

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="Escanear Host", width=15,bg='brown',fg='white',
                                command=self.create_window)
        self.button.place(x=200,y=130)
        self.button = tk.Button(self, text="Escanear Rede", width=15,bg='brown',fg='white',
                                command=self.crtd_window1)
        self.button.place(x=200,y=230)


    def scanTCP(self,t_IP,port_):

        s = socket(AF_INET,SOCK_STREAM)
        setdefaulttimeout(1)

        try: 
            conn = s.connect_ex((t_IP,int(port_)))

            if(conn == 0) :                
                s.close()
                return str("Porta aberta: " +str(port_) +" - "+ str(getservbyport(port_, "tcp")))

        except:
            pass

        return None

    def scanUDP(self,t_IP,port_):

        try:
            s = socket(AF_INET,SOCK_DGRAM)
            conn = s.connect_ex((t_IP,int(port_)))

            if(conn == 0) :
                return  str("Porta aberta: " + str(port_)+" - " + str(getservbyport(port_, "udp")))

            s.close()

        except:
            pass

    def scan(addr):
        s = socket(AF_INET,SOCK_STREAM)
        setdefaulttimeout(2)
        result = s.connect_ex((addr,135))
        if result == 0:
            return 1
        else :
            return 0

    def create_window(self):
        t = tk.Toplevel(self)
        t.geometry('500x500')
        t.wm_title("Escanear Host")

        label_0 = Label(t, text="Escanear Host",width=20,font=("bold", 20))
        label_0.place(x=90,y=53)
        
        label_1 = Label(t, text="IP:",width=37,font=("bold", 9))
        label_1.place(x=20,y=230)

        self.entry_1 = Entry(t)
        self.entry_1.place(x=280,y=230)

        label_2 = Label(t, text="Porta Inicial",width=37,font=("bold", 9))
        label_2.place(x=20,y=280)

        self.entry_2 = Entry(t)
        self.entry_2.place(x=280,y=280)

        label_3 = Label(t, text="Porta Final",width=30,font=("bold", 10))
        label_3.place(x=40,y=330)

        self.entry_3 = Entry(t)
        self.entry_3.place(x=280,y=330)

        label_4 = Label(t, text="Protocolo TCP (1) ou UDP (2)",width=30,font=("bold", 10))
        label_4.place(x=40,y=380)
       
        px = 280
        py = 380

        self.entry_p = Entry(t)
        self.entry_p.place(x=px,y=py)

        Button(t, text='Escanear Host',width=20,bg='brown',fg='white',command=self.crtd_window).place(x=180,y=470)

    def crtd_window(self):

        c = tk.Toplevel(self)
        c.geometry('500x600')
        c.wm_title("Portas")

        label_0 = Label(c, text="Portas",width=20,font=("bold", 20))
        label_0.place(x=90,y=53)

        b = self.entry_p.get()
        range_max = int(self.entry_3.get())
        range_min = int(self.entry_2.get())
        t_IP = self.entry_1.get()  

        xl=50
        yl= 100

        if int(b) == 1:
            for i in range(range_min,range_max+1):
                pr = self.scanTCP(t_IP ,i)
                if pr != None:
                    label_0 = Label(c, text=pr,width=20,font=("bold", 10))
                    label_0.place(x=xl,y=yl)
                    yl+=30

        if int(b) == 2:
            for i in range(range_min,range_max+1):
                pr = self.scanUDP(t_IP ,i)
                if pr != None:
                    label_0 = Label(c, text=pr,width=20,font=("bold", 10))
                    label_0.place(x=xl,y=yl)
                    yl+=30

    def crtd_window1(self):
        t = tk.Toplevel(self)
        t.geometry('500x600')
        t.wm_title("Escanear Rede")

        label_0 = Label(t, text="Escanear Rede (range 255 IPs)",width=40,font=("bold", 15))
        label_0.place(x=20,y=53)
        
        label_1 = Label(t, text="IP Rede:",width=37,font=("bold", 9))
        label_1.place(x=20,y=230)

        self.entry_1 = Entry(t)
        self.entry_1.place(x=280,y=230)

        label_IPi = Label(t, text="IP Inicial (0 a 255)",width=30,font=("bold", 10))
        label_IPi.place(x=40,y=280)

        self.entry_ipi = Entry(t)
        self.entry_ipi.place(x=280,y=280)

        label_IPF = Label(t, text="IP Final (0 a 255)",width=30,font=("bold", 10))
        label_IPF.place(x=40,y=320)

        self.entry_ipf = Entry(t)
        self.entry_ipf.place(x=280,y=320)

        label_PI = Label(t, text="Porta Inicial",width=30,font=("bold", 10))
        label_PI.place(x=40,y=370)

        self.entry_pi = Entry(t)
        self.entry_pi.place(x=280,y=370)

        label_PF = Label(t, text="Porta Final",width=30,font=("bold", 10))
        label_PF.place(x=40,y=420)

        self.entry_pf = Entry(t)
        self.entry_pf.place(x=280,y=420)


        label_4 = Label(t, text="Protocolo TCP (1) ou UDP (2)",width=30,font=("bold", 10))
        label_4.place(x=40,y=470)
        px = 280
        py = 470
        self.entry_p = Entry(t)
        self.entry_p.place(x=px,y=py)

        Button(t, text='Escanear Rede',width=20,bg='brown',fg='white',command=self.crtd_window3).place(x=180,y=520)

    def crtd_window3(self):

            c = tk.Toplevel(self)
            c.geometry('500x600')
            c.wm_title("Portas")

            label_0 = Label(c, text="Portas",width=20,font=("bold", 20))
            label_0.place(x=90,y=53)

            b = self.entry_p.get()
            range_max = int(self.entry_pf.get())
            range_min = int(self.entry_pi.get())
            t_IP = self.entry_1.get()  
            st1 = int(self.entry_ipi.get())
            en1 = int(self.entry_ipf.get())

            xl=50
            yl= 100

            net1 = t_IP.split('.')
            net2 = net1[0] +"."+ net1[1] + "." + net1[2] + "."
            for ip in range(st1,en1):
                try:
                    addr = net2 + str(ip)

                    if int(b) == 1:
                        label_0 = Label(c, text=addr,width=20,font=("bold", 10))
                        label_0.place(x=xl,y=yl)

                        yl+=30

                        for i in range(range_min,range_max+1):
                            pr = self.scanTCP(addr ,i)
                            if pr != None:
                                label_0 = Label(c, text=(pr),width=20,font=("bold", 10))
                                label_0.place(x=xl+80,y=yl)
                                yl+=30

                    if int(b) == 2:
                        for i in range(range_min,range_max+1):
                            pr = self.scanUDP(addr ,i)
                            if pr != None:
                                label_0 = Label(c, text=(pr),width=20,font=("bold", 10))
                                label_0.place(x=xl+80,y=yl)
                                yl+=30
                except:
                    print("ip n exitste")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x500')
    root.title("Network Scanner")
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()