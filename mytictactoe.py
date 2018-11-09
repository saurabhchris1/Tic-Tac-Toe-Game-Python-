from tkinter import *
class TicTacToeBoard:
    
    global player_symbol
    player_symbol = "X"

    global move
    move = {0: "", 1 : "", 2 : "", 3 : "", 4 : "", 5 : "", 6 : "", 7 : "", 8 : ""}

    global button_ref
    button_ref = []




    global m
    
    m = 1
    
    def __init__(self, root):
        self.root = root
        


    def process_event(self,index):

        global m
        global move
        global player_symbol
        global button_ref
        global comp_index_save
        if m < 9:
            if m == 1:


                    button_ref[index].config(text = player_symbol,state=DISABLED)
                    move[index] = player_symbol
                    player_symbol = "X"
                    if index != 7:
                        button_ref[index + 1].config(text = player_symbol,state=DISABLED)
                        comp_index_save = index + 1
                        move[comp_index_save] = player_symbol
                        player_symbol = "O"
                        self.label_bottom.config(text = "Your Turn")
                    else:
                        button_ref[0].config(text = player_symbol,state=DISABLED)
                        comp_index_save = 0
                        move[comp_index_save] = player_symbol
                        player_symbol = "O"
                        self.label_bottom.config(text = "Your Turn")


            else:
                button_ref[index].config(text = player_symbol,state=DISABLED)
                move[index] = player_symbol
                player_symbol = "X"
                if (comp_index_save) in (1,3):
                    if "O" != move[comp_index_save + 4] and "X" != move[comp_index_save + 4]:
                        button_ref[comp_index_save + 4].config(text = player_symbol,state=DISABLED)
                        move[comp_index_save + 4] = player_symbol

                        for k in move:

                            if move[k] == "":
                                button_ref[k].config(state= DISABLED)

                        self.label_bottom.config(text = "I WIN!")






                    else:
                        count = 0
                        a = 0
                        for k in move:
                            if move[k] == "":
                                a = k
                                count = count + 1
                        if count != 1:

                            if comp_index_save == 1:
                                button_ref[comp_index_save + 4 + 1].config(text = player_symbol,state=DISABLED)
                                comp_index_save = comp_index_save + 4 + 1
                                move[comp_index_save] = player_symbol
                                player_symbol = "O"
                                self.label_bottom.config(text = "Your Turn")
                            else: 
                                button_ref[0].config(text = player_symbol,state=DISABLED)
                                comp_index_save = 0
                                move[comp_index_save] = player_symbol
                                player_symbol = "O"
                                self.label_bottom.config(text = "Your Turn")

                        else:
                            button_ref[a].config(text = player_symbol,state=DISABLED)
                            self.label_bottom.config(text = "CAT'S GAME")


                elif (comp_index_save) in (5,7):
                    if "O" != move[comp_index_save - 4] and "O" != move[comp_index_save - 4]:
                            button_ref[comp_index_save - 4].config(text = player_symbol,state=DISABLED)
                            comp_index_save = comp_index_save - 4
                            move[comp_index_save] = player_symbol
                            for k in move:

                                if move[k] == "":
                                    button_ref[k].config(state= DISABLED)
                            self.label_bottom.config(text = "I WIN!")

                    else:

                        count = 0
                        a = 0
                        for k in move:
                            if move[k] == "":
                                a = k
                                count = count + 1
                        if count != 1:
                            button_ref[comp_index_save - 4 + 1].config(text = player_symbol,state=DISABLED)
                            comp_index_save = comp_index_save - 4 + 1
                            move[comp_index_save] = player_symbol
                            player_symbol = "O"
                            self.label_bottom.config(text = "Your Turn")
                        else:
                            button_ref[a].config(text = player_symbol,state=DISABLED)
                            for k in move:

                                if move[k] == "":
                                    button_ref[k].config(state= DISABLED)
                            self.label_bottom.config(text = "CAT'S GAME")

                elif comp_index_save in (0,2):


                    if "O" != move[comp_index_save + 4] and "X" != move[comp_index_save + 4]:

                        button_ref[comp_index_save + 4].config(text = player_symbol,state=DISABLED)
                        comp_index_save = comp_index_save + 4
                        move[comp_index_save] = player_symbol
                        for k in move:

                            if move[k] == "":
                                button_ref[k].config(state= DISABLED)
                        self.label_bottom.config(text = "I WIN!")

                    else:
                        count = 0
                        a = 0
                        for k in move:
                            if move[k] == "":
                                a = k
                                count = count + 1
                        if count != 1:


                            button_ref[comp_index_save + 4 + 1].config(text = player_symbol,state=DISABLED)
                            comp_index_save = comp_index_save + 4 + 1
                            move[comp_index_save] = player_symbol
                            player_symbol = "O"
                            self.label_bottom.config(text = "Your Turn")

                        else:
                            button_ref[a].config(text = player_symbol,state=DISABLED)
                            for k in move:

                                if move[k] == "":
                                    button_ref[k].config(state= DISABLED)
                            self.label_bottom.config(text = "CAT'S GAME")
                elif comp_index_save == 4:
                    if "O" != move[0] and "X" != move[0]:
                        button_ref[0].config(text = player_symbol,state=DISABLED)
                        comp_index_save = 0
                        move[comp_index_save] = player_symbol

                        for k in move:

                            if move[k] == "":
                                button_ref[k].config(state= DISABLED)

                        self.label_bottom.config(text = "I WIN!")

                    else:
                        count = 0
                        a = 0
                        for k in move:
                            if move[k] == "":
                                a = k
                                count = count + 1
                        if count != 1:

                            button_ref[1].config(text = player_symbol,state=DISABLED)
                            comp_index_save = 1
                            move[comp_index_save] = player_symbol
                            player_symbol = "O"
                            self.label_bottom.config(text = "Your Turn")
                        else:
                            button_ref[a].config(text = player_symbol,state=DISABLED)

                            for k in move:

                                if move[k] == "":
                                    button_ref[k].config(state= DISABLED)

                            self.label_bottom.config(text = "CAT'S GAME")


                elif (comp_index_save) == (6):
                    if "O" != move[comp_index_save - 4] and "X" != move[comp_index_save - 4]:
                        button_ref[comp_index_save - 4].config(text = player_symbol,state=DISABLED)
                        comp_index_save = comp_index_save - 4
                        move[comp_index_save] = player_symbol

                        for k in move:

                            if move[k] == "":
                                button_ref[k].config(state= DISABLED)

                        self.label_bottom.config(text = "I WIN!")

                    else:

                        count = 0
                        a = 0
                        for k in move:
                            if move[k] == "":
                                a = k
                                count = count + 1
                        if count != 1:

                            button_ref[comp_index_save - 4 +1].config(text = player_symbol,state=DISABLED)
                            comp_index_save = comp_index_save - 4 + 1
                            move[comp_index_save] = player_symbol
                            player_symbol = "O"
                            self.label_bottom.config(text = "Your Turn")

                        else:
                            button_ref[a].config(text = player_symbol,state=DISABLED)

                            for k in move:

                                if move[k] == "":
                                    button_ref[k].config(state= DISABLED)

                            self.label_bottom.config(text = "CAT'S GAME")




            m = m + 2




    def grid(self):
        
        global player_symbol
        button1 = Button(self.root,text = "", font=('Courier', 70), width=2, command=lambda: self.process_event(0))
        button1.grid(row=0,column=0, sticky = "snew")
        button_ref.append(button1)

        button2 = Button(self.root,text = "", font=('Courier', 70),width=2, command=lambda: self.process_event(1))
        button2.grid(row=0,column=1, sticky = "snew")
        button_ref.append(button2)

        button3 = Button(self.root,text = "", font=('Courier', 70),width=2, command=lambda: self.process_event(2))
        button3.grid(row=0,column=2, sticky = "snew")
        button_ref.append(button3)

        button4 = Button(self.root,text = "", font=('Courier', 70),width=2, command=lambda: self.process_event(3))
        button4.grid(row=1,column=2, sticky = "snew")
        button_ref.append(button4)

        button5 = Button(self.root,text = "", font=('Courier', 70),width=2, command=lambda: self.process_event(4))
        button5.grid(row=2,column=2, sticky = "snew")
        button_ref.append(button5)

        button6 = Button(self.root,text = "", font=('Courier', 70),width=2, command=lambda: self.process_event(5))
        button6.grid(row=2,column=1, sticky = "snew")
        button_ref.append(button6)

        button7 = Button(self.root,text = "", font=('Courier', 70),width=2, command=lambda: self.process_event(6))
        button7.grid(row=2,column=0, sticky = "snew")
        button_ref.append(button7)

        button8 = Button(self.root,text = "", font=('Courier', 70),width=2, command=lambda: self.process_event(7))
        button8.grid(row=1,column=0, sticky = "snew")
        button_ref.append(button8)

        button9 = Button(self.root,text = "", font=('Courier', 70),width=2, command=lambda: self.process_event(8))
        button9.grid(row=1,column=1, sticky = "snew")
        button_ref.append(button9)

        self.label_bottom = Label(self.root, text="")
        self.label_bottom.grid(row=3, column=0,columnspan=2)

        quitButton = Button(self.root, text="QUIT", fg="red", command = self.root.destroy)
        quitButton.grid(row=3, column=2)




        button9.config(text = player_symbol, font=('Courier', 70), state=DISABLED)
        move[8] = player_symbol
        player_symbol = "O"
        self.label_bottom.config(text = "Your Turn")




