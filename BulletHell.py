#Who Did What
#Logan - Game Function, it's comments, as well as merging the Game & MainMenu functions together
#Did the game graphics & music

#Gaurav - MainMenu Function and it's comments
#Did the MainMenu graphics, buttons, and complete look of it

#imports
import pygame, math, random, tkinter
from tkinter import PhotoImage, Label, FLAT, Canvas
import customtkinter as ctk
from tkinter import *
from pygame.locals import *
from pygame import mixer

Volume = 50
Settings_opened = False
Slider_volume = 50
Difficulty = "Hard"

def mainMenu():
    
    # Main window setup
    root = ctk.CTk()
    root.title('Bullet Hell')
    root.geometry('750x750')
    root.resizable(False, False)  # lock window

    try:
        # Load the image for the first window
        root.background_image = PhotoImage(file="TkinterImages/1.png")
        # Create a canvas for the background image
        canvas = Canvas(root, width=750, height=750)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=root.background_image, anchor="nw")
    except Exception as e:
        print("Error loading image:", e)

    # Start page blinking label
    label = Label(root, text='Press any button to continue', font=('latha', 16), fg='white', bg='black', borderwidth=0, relief=FLAT)
    label.place(relx=0.5, rely=0.8, anchor='center')  # Lowered label position

    # Variables for blinking
    blink_state = True

    # Function to update label (for blinking effect)
    def update_label():
        nonlocal blink_state

        # Toggle the blink state
        blink_state = not blink_state

        # Update the label's color
        color = "white" if blink_state else "#888888"
        label.configure(fg=color)

        # Schedule the function to be called again after a short delay
        root.after(500, update_label)

    # Start the blinking effect
    update_label()

    # Function to destroy the root window and create the first new window
    def destroy_and_create_new(event=None):
        root.destroy()
        create_new_window()

    # Function to create the first new window
    def create_new_window():
        new_window = ctk.CTkToplevel()
        new_window.title('Story')
        new_window.geometry('750x750')
        new_window.resizable(False, False)  # lock window

        try:
            # Load the image
            new_window.background_image = PhotoImage(file="TkinterImages/2.png")
            # Create a canvas for the background image
            canvas = Canvas(new_window, width=750, height=750)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=new_window.background_image, anchor="nw")
        except Exception as e:
            print("Error loading image:", e)

        # Main menu label
        label = Label(new_window, text='Press any button to continue', fg='white', font=('latha', 16), bg='black', borderwidth=0, relief=FLAT)
        label.place(relx=0.5, rely=0.8, anchor='center')  # Lowered label position

        # Variables for blinking
        blink_state = True

        # Function to update label (for blinking effect)
        def update_label_2():
            nonlocal blink_state

            # Toggle the blink state
            blink_state = not blink_state

            # Update the label's color
            color = "white" if blink_state else "#888888"
            label.configure(fg=color)

            # Schedule the function to be called again after a short delay
            new_window.after(500, update_label_2)

        # Start the blinking effect
        update_label_2()

        new_window.bind('<Key>', destroy_and_create_new_2)

    # Function to destroy the first new window and create the blank window
    def destroy_and_create_new_2(event=None):
        for widget in event.widget.master.winfo_children():
            widget.destroy()
        create_blank_window(event.widget.master)

    # Function to create the blank window
    def create_blank_window(parent):
        new_window_2 = ctk.CTkToplevel(parent)
        new_window_2.title('Main Menu')
        new_window_2.geometry('750x750')
        new_window_2.resizable(False, False)  # lock window

        try:
            # Load the image for the blank window
            new_window_2.background_image = PhotoImage(file="TkinterImages/3.png")
            # Create a canvas for the background image
            canvas = Canvas(new_window_2, width=750, height=750)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=new_window_2.background_image, anchor="nw")
        except Exception as e:
            print("Error loading image:", e)

        # Add buttons
        button_play = ctk.CTkButton(new_window_2, text='Play', fg_color='red', border_color='white', border_width=1, hover_color='gray', bg_color='black', cursor='hand2', command=lambda: open_play_menu(new_window_2))
        button_play.place(relx=0.5, rely=0.4, anchor='center')

        button_settings = ctk.CTkButton(new_window_2, text='Settings & Instructions', fg_color='red', border_color='white', border_width=1, hover_color='gray', bg_color='black', cursor='hand2', command=lambda: open_settings_menu(new_window_2))
        button_settings.place(relx=0.5, rely=0.5, anchor='center')

        button_quit = ctk.CTkButton(new_window_2, text='Quit', fg_color='red', border_color='white', border_width=1, hover_color='gray', bg_color='black', cursor='hand2', command=root.quit)
        button_quit.place(relx=0.5, rely=0.6, anchor='center')

    # Function to open the play menu with '1 Player' and '2 Player' buttons
    def open_play_menu(parent):
        new_page = ctk.CTkToplevel(parent)
        new_page.title('Play Menu')
        new_page.geometry('750x750')
        new_page.resizable(False, False)  # lock window

        try:
            # Load the image for the play menu
            new_page.background_image = PhotoImage(file="TkinterImages/4.png")
            # Create a canvas for the background image
            canvas = Canvas(new_page, width=750, height=750)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=new_page.background_image, anchor="nw")
        except Exception as e:
            print("Error loading image:", e)

        # Add '1 Player' and '2 Player' buttons
        button_1p = ctk.CTkButton(new_page, text='1 Player', fg_color='red', border_color='white', border_width=1, hover_color='gray', bg_color='black', cursor='hand2', command=lambda: open_1p_menu(new_page))
        button_1p.place(relx=0.5, rely=0.4, anchor='center')

        button_2p = ctk.CTkButton(new_page, text='2 Player', fg_color='red', border_color='white', border_width=1, hover_color='gray', bg_color='black', cursor='hand2', command=lambda: open_2p_menu(new_page))
        button_2p.place(relx=0.5, rely=0.5, anchor='center')

        # Add 'Back' button
        button_back = ctk.CTkButton(new_page, text='Back', fg_color='red', border_color='white', border_width=1, hover_color='gray', bg_color='black', cursor='hand2', command=new_page.destroy)
        button_back.place(relx=0.5, rely=0.8, anchor='center')

    # Function to open the 1 Player menu with radio buttons for difficulty and player options
    def open_1p_menu(parent):
        def radio_select():
            global Difficulty, Players, player1_choice, player2_choice

            #Variables
            Players = 1
            Difficulty = "easy"
            player1_choice = "1"
            player2_choice = "1"
            
            if radio_var1.get() == "e":
                Difficulty = "easy"
                
            elif radio_var1.get() == "m":
                Difficulty = "medium"
                
            elif radio_var1.get() == "h":
                Difficulty = "hard"
            
            if radio_var2.get() == "1":
                player1_choice = "1"
            
            elif radio_var2.get() == "2":
                player1_choice = "2"
                
            elif radio_var2.get() == "3":
                player1_choice = "3"
                
            elif radio_var2.get() == "4":
                player1_choice = "4"

        radio_var1 = ctk.StringVar(value='m')
        radio_var2 = ctk.StringVar(value='1')
        
        radio_select()
        
        new_page = ctk.CTkToplevel(parent)
        new_page.title('1 Player Menu')
        new_page.geometry('750x750')
        new_page.resizable(False, False)  # lock window

        try:
            # Load the image for the 1 Player menu
            new_page.background_image = PhotoImage(file="TkinterImages/6.png")
            # Create a canvas for the background image
            canvas = Canvas(new_page, width=750, height=750)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=new_page.background_image, anchor="nw")
        except Exception as e:
            print("Error loading image:", e)

        # Radio buttons for difficulty
        radio_easy = ctk.CTkRadioButton(new_page, text='Easy', variable=radio_var1, value='e', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_easy.place(relx=0.3, rely=0.2, anchor='center')

        radio_medium = ctk.CTkRadioButton(new_page, text='Medium', variable=radio_var1, value='m', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_medium.place(relx=0.5, rely=0.2, anchor='center')

        radio_hard = ctk.CTkRadioButton(new_page, text='Hard', variable=radio_var1, value='h', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_hard.place(relx=0.7, rely=0.2, anchor='center')

        # Radio buttons for player options
        radio_skin1 = ctk.CTkRadioButton(new_page, text='Skin 1', variable=radio_var2, value='1', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_skin1.place(relx=0.2, rely=0.4, anchor='center')

        radio_skin2 = ctk.CTkRadioButton(new_page, text='Skin 2', variable=radio_var2, value='2', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_skin2.place(relx=0.4, rely=0.4, anchor='center')

        radio_skin3 = ctk.CTkRadioButton(new_page, text='Skin 3', variable=radio_var2, value='3', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_skin3.place(relx=0.6, rely=0.4, anchor='center')

        radio_skin4 = ctk.CTkRadioButton(new_page, text='Skin 4', variable=radio_var2, value='4', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_skin4.place(relx=0.8, rely=0.4, anchor='center')

        # Add 'Play' button
        button_play = ctk.CTkButton(new_page, text='Play', fg_color='red', border_color='white', border_width=1, hover_color='gray', bg_color='black', cursor='hand2', command=lambda: (Game(),new_page.destroy()))
        button_play.place(relx=0.5, rely=0.7, anchor='center')

        # Add 'Back' button
        button_back = ctk.CTkButton(new_page, text='Back', fg_color='red', border_color='white', border_width=1, hover_color='gray', bg_color='black', cursor='hand2', command=new_page.destroy)
        button_back.place(relx=0.5, rely=0.8, anchor='center')

    
    
    # Function to open the 2 Player menu with radio buttons for difficulty and player options
    def open_2p_menu(parent):
        
         # Functions for when radio_vars are selected
        def radio_select():
            global Difficulty, Players, player1_choice, player2_choice
            #Variables
            Players = 2
            Difficulty = "easy"
            player1_choice = "1"
            player2_choice = "1"
            
            try:
                nonlocal radio_var1, radio_var2, radio_var3

                if radio_var1.get() == "easy":
                    Difficulty = "easy"
                    
                elif radio_var1.get() == "medium":
                    Difficulty = "medium"
                    
                elif radio_var1.get() == "hard":
                    Difficulty = "hard"
                
                if radio_var2.get() == "1":
                    player1_choice = "1"
                
                elif radio_var2.get() == "2":
                    player1_choice = "2"
                    
                elif radio_var2.get() == "3":
                    player1_choice = "3"
                    
                elif radio_var2.get() == "4":
                    player1_choice = "4"
                
                if radio_var3.get() == "1":
                    player2_choice = "1"
                
                elif radio_var3.get() == "2":
                    player2_choice = "2"
                    
                elif radio_var3.get() == "3":
                    player2_choice = "3"
                    
                elif radio_var3.get() == "4":
                    player2_choice = "4"
                    
            except Exception as e:
                print("Error loading variables:", e)

        radio_select()
        
        new_page = ctk.CTkToplevel(parent)
        new_page.title('2 Player Menu')
        new_page.geometry('750x750')
        new_page.resizable(False, False)  # lock window

        try:
            # Load the image for the 2 Player menu
            new_page.background_image = PhotoImage(file="TkinterImages/6.png")
            # Create a canvas for the background image
            canvas = Canvas(new_page, width=750, height=750)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=new_page.background_image, anchor="nw")
        except Exception as e:
            print("Error loading image:", e)

        # Radio buttons for difficulty
        radio_var1 = ctk.StringVar(value='easy')
        
        radio_easy = ctk.CTkRadioButton(new_page, text='Easy', variable=radio_var1, value='easy', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_easy.place(relx=0.3, rely=0.2, anchor='center')

        radio_medium = ctk.CTkRadioButton(new_page, text='Medium', variable=radio_var1, value='medium', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_medium.place(relx=0.5, rely=0.2, anchor='center')

        radio_hard = ctk.CTkRadioButton(new_page, text='Hard', variable=radio_var1, value='hard', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_hard.place(relx=0.7, rely=0.2, anchor='center')

        # Radio buttons for player 1 options
        radio_var2 = ctk.StringVar(value='skin1')
        radio_skin1 = ctk.CTkRadioButton(new_page, text='Player 1 - Skin 1', variable=radio_var2, value='1', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_skin1.place(relx=0.2, rely=0.3, anchor='center')

        radio_skin2 = ctk.CTkRadioButton(new_page, text='Player 1 - Skin 2', variable=radio_var2, value='2', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_skin2.place(relx=0.4, rely=0.3, anchor='center')

        radio_skin3 = ctk.CTkRadioButton(new_page, text='Player 1 - Skin 3', variable=radio_var2, value='3', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_skin3.place(relx=0.6, rely=0.3, anchor='center')

        radio_skin4 = ctk.CTkRadioButton(new_page, text='Player 1 - Skin 4', variable=radio_var2, value='4', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_skin4.place(relx=0.8, rely=0.3, anchor='center')

        # Radio buttons for player 2 options
        radio_var3 = ctk.StringVar(value='skin1')
        radio_skin1_p2 = ctk.CTkRadioButton(new_page, text='Player 2 - Skin 1', variable=radio_var3, value='1', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_skin1_p2.place(relx=0.2, rely=0.4, anchor='center')

        radio_skin2_p2 = ctk.CTkRadioButton(new_page, text='Player 2 - Skin 2', variable=radio_var3, value='2', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_skin2_p2.place(relx=0.4, rely=0.4, anchor='center')

        radio_skin3_p2 = ctk.CTkRadioButton(new_page, text='Player 2 - Skin 3', variable=radio_var3, value='3', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_skin3_p2.place(relx=0.6, rely=0.4, anchor='center')

        radio_skin4_p2 = ctk.CTkRadioButton(new_page, text='Player 2 - Skin 4', variable=radio_var3, value='4', fg_color='red', border_color='white', hover_color='gray', bg_color='black', cursor='hand2', command= radio_select)
        radio_skin4_p2.place(relx=0.8, rely=0.4, anchor='center')
            

        # Add 'Play' button
        button_play = ctk.CTkButton(new_page, text='Play', fg_color='red', border_color='white', border_width=1, hover_color='gray', bg_color='black', cursor='hand2', command=lambda: (Game(),new_page.destroy()))
        button_play.place(relx=0.5, rely=0.7, anchor='center')

        # Add 'Back' button
        button_back = ctk.CTkButton(new_page, text='Back', fg_color='red', border_color='white', border_width=1, hover_color='gray', bg_color='black', cursor='hand2', command=new_page.destroy)
        button_back.place(relx=0.5, rely=0.8, anchor='center')
        
        radio_select()

    # Function to open the settings menu with a volume slider and save button
    def open_settings_menu(parent):
        global Settings_opened, Slider_volume
        Settings_opened = True
        
        def get_volume(value):
            global Slider_volume
            
            Slider_volume = 0
            Slider_volume = int(value)
            
        
        new_page = ctk.CTkToplevel(parent)
        new_page.title('Settings Menu')
        new_page.geometry('750x750')
        new_page.resizable(False, False)  # lock window

        try:
            # Load the image for the settings menu
            new_page.background_image = PhotoImage(file="TkinterImages/7.png")
            # Create a canvas for the background image
            canvas = Canvas(new_page, width=750, height=750)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=new_page.background_image, anchor="nw")
        except Exception as e:
            print("Error loading image:", e)

        # Volume slider
        volume_slider = ctk.CTkSlider(new_page, from_=0, to=100, number_of_steps=100, orientation='horizontal', fg_color='white', border_width=1, bg_color='black', button_color='red', command = get_volume)
        volume_slider.place(relx=0.5, rely=0.3, anchor='center')

        # Save button
        button_save = ctk.CTkButton(new_page, text='Save & Go Back', fg_color='red', border_color='white', border_width=1, hover_color='gray', bg_color='black', cursor='hand2', command=new_page.destroy)
        button_save.place(relx=0.5, rely=0.8, anchor='center')
        
        get_volume(50)

    # Function to open a blank page with a given background image
    def open_blank_page(parent, image_path):
        new_page = ctk.CTkToplevel(parent)
        new_page.title('Blank Page')
        new_page.geometry('750x750')
        new_page.resizable(False, False)  # lock window

        try:
            # Load the image for the blank page
            new_page.background_image = PhotoImage(file=image_path)
            # Create a canvas for the background image
            canvas = Canvas(new_page, width=750, height=750)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=new_page.background_image, anchor="nw")
        except Exception as e:
            print("Error loading image:", e)

        # Add 'Back' button
        button_back = ctk.CTkButton(new_page, text='Back', fg_color='red', border_color='white', border_width=1, hover_color='gray', bg_color='black', cursor='hand2', command=new_page.destroy)
        button_back.place(relx=0.5, rely=0.8, anchor='center')

    # Bind any key press to destroy the root window and create the first new window
    root.bind('<Key>', destroy_and_create_new)

    # Start the main event loop
    root.mainloop()
    
def Game():
    if not Settings_opened:
        Volume = 50
    else:
        Volume = Slider_volume
    
    #initialize pygame
    mixer.init()
    pygame.init()

    #frame rate
    clock = pygame.time.Clock()
    FPS = 60

    #load sounds
    VictoryBG = ("sounds/Music/VictoryTheme.wav")
    MainMusic = ("sounds/Music/Music2.mp3")
    DeathBg = ("sounds/Music/GameOverMusic.mp3")
    
    pygame.mixer.music.load(MainMusic)
    pygame.mixer.music.set_volume(Volume / 100)
    pygame.mixer.music.play(-1, 0.0)

    #game window dimensions
    SCREEN_HEIGHT = 750
    SCREEN_WIDTH = 750

    #game window
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.display.set_caption("Bullet Hell")

    #define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)

    #define fonts
    main_font = pygame.font.SysFont("System Bold", 40)
    large_font = pygame.font.SysFont("System Bold", 80)

    #define game variables
    time = pygame.time.get_ticks()
    cooldown = 300
    score = 0
    game_over = False
    health_available = False
    Victory = False
    Death = False

    #timer event
    timer = pygame.USEREVENT
    pygame.time.set_timer(timer, 1000)

    #load images
    bullet_img = pygame.image.load("img/Bullets/Bullet4x.png").convert_alpha()
    health_img = pygame.image.load("img/Onigiri/Onigiri.png").convert_alpha()
    
    #background images
    bg_img = pygame.image.load("img/Backgrounds/bg.png").convert_alpha()
    winner_img = pygame.image.load("img/Backgrounds/WinnerBG.png").convert_alpha()
    
    #marker images
    Player1_marker = pygame.image.load("img/Markers/Player1Marker(3xSize).png").convert_alpha()
    Player2_marker = pygame.image.load("img/Markers/Player2(x3).png").convert_alpha()

    #draw text function
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, False, text_col)
        screen.blit(img, (x, y))
    
    #play_sound functions that ensure the songs won't loop when a player dies
    def play_theme():
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.load(VictoryBG)
        pygame.mixer.music.play(1, 0.0)
    
    def play_deaththeme():
        pygame.mixer.music.fadeout(500)
        pygame.mixer.music.load(DeathBg)
        pygame.mixer.music.play(1, 0.0)
            
    
    #player1 class
        
    #comments in the player class would be the same for playertwo, other than the controls
    class Player():
        def __init__(self, x, y, hp, initial_hp, friction, acceleration):
            img = pygame.image.load(f"img/Players/Player{player1_choice}.png").convert_alpha()
            self.image = pygame.transform.scale(img, (64, 64))
            self.hp = hp
            self.initial_hp = initial_hp
            self.friction = friction
            self.acceleration = acceleration
            self.vel_x = 0
            self.vel_y = 0
            self.flip = False #variable for fliping horizontally
            
            self.width = 48
            self.height = 64
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = (x, y)
            self.dash_cooldown = 3000
            self.dash_duration = 100
            self.last_dash_time = 0
            self.dash_start_time = 0
            self.is_dashing = False
        
        def update(self):
            key = pygame.key.get_pressed()
            self.vel_x *= (1 - self.friction)
            self.vel_y *= (1 - self.friction)
            
            
            #controller
            if key[pygame.K_a]:
                self.vel_x -= self.acceleration
                self.flip = False
            if key[pygame.K_d]:
                self.vel_x += self.acceleration
                self.flip = True
            if key[pygame.K_s]:
                self.vel_y += self.acceleration
            if key[pygame.K_w]:
                self.vel_y -= self.acceleration
            
            # Update position based on velocity
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y
                
                
            #ensures that the character won't go off screen
            self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.width))
            self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.height))
        
        def dash(self):
            key = pygame.key.get_pressed()
            current_time = pygame.time.get_ticks()
            if current_time - self.last_dash_time >= self.dash_cooldown:
                # Perform dash action
                key = pygame.key.get_pressed()
                if key[pygame.K_LSHIFT] and not self.is_dashing:
                    self.is_dashing = True
                    self.dash_start_time = current_time
                    self.last_dash_time = current_time
                    
                elif self.is_dashing and current_time - self.dash_start_time >= self.dash_duration:
                    # End dash after duration
                    self.is_dashing = False
                    
                    
            
        def draw(self):
            #load player
            player_sprite = pygame.transform.flip(self.image, self.flip, False)
            
            screen.blit(player_sprite, ((self.rect.x - 10, self.rect.y) if Players == 1 else (self.rect.x - 16, self.rect.y)))
            
    #Player2 Class        
    class PlayerTwo():
        def __init__(self, x, y, hp, initial_hp, friction, acceleration):
            img = pygame.image.load(f"img/Players/Player{player2_choice}.png").convert_alpha()
            self.image = pygame.transform.scale(img, (64, 64))
            self.hp = hp
            self.initial_hp = initial_hp
            self.friction = friction
            self.acceleration = acceleration
            self.vel_x = 0
            self.vel_y = 0
            self.flip = False
            
            self.width = 48
            self.height = 32
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = (x, y)
            self.dash_cooldown = 3000
            self.dash_duration = 100
            self.last_dash_time = 0
            self.dash_start_time = 0
            self.is_dashing = False
        
        def update(self):
            key = pygame.key.get_pressed()
            self.vel_x *= (1 - self.friction)
            self.vel_y *= (1 - self.friction)
            
            
            #controller
            if key[pygame.K_LEFT]:
                self.vel_x -= self.acceleration
                self.flip = False
            if key[pygame.K_RIGHT]:
                self.vel_x += self.acceleration
                self.flip = True
            if key[pygame.K_DOWN]:
                self.vel_y += self.acceleration
            if key[pygame.K_UP]:
                self.vel_y -= self.acceleration
            
            # Update position based on velocity
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y
                
                
            #ensures that the character won't go off screen
            self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.width))
            self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.height))
        
        def dash(self):
            key = pygame.key.get_pressed()
            current_time = pygame.time.get_ticks()
            if current_time - self.last_dash_time >= self.dash_cooldown:
                # Perform dash action
                key = pygame.key.get_pressed()
                if key[pygame.K_LSHIFT] and not self.is_dashing:
                    self.is_dashing = True
                    self.dash_start_time = current_time
                    self.last_dash_time = current_time
                    
                elif self.is_dashing and current_time - self.dash_start_time >= self.dash_duration:
                    # End dash after duration
                    self.is_dashing = False

                    
            
        def draw(self):
            #load player
            player_sprite = pygame.transform.flip(self.image, self.flip, False)
            
            screen.blit(player_sprite, (self.rect.x - 16, self.rect.y))

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y, player_rect):
            pygame.sprite.Sprite.__init__(self)
            self.original_image = pygame.transform.scale(bullet_img, (32, 32))
            self.image = self.original_image.copy()
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.player_rect = player_rect
            self.target_x = player_rect.centerx
            self.target_y = player_rect.centery
            self.rect.center = [x, y]
            self.speed = 5 if Difficulty == "Easy" else 10 if Difficulty == "Medium" else 15 if Difficulty == "Hard" else 5
            
            # Calculate the angle the bullet was fired in and store it
            dx = player_rect.centerx - self.rect.centerx
            dy = player_rect.centery - self.rect.centery
            self.angle = math.atan2(dy, dx)  # Convert to degrees

        def update(self):
            # Adjust speed based on the angle
            bullet_speed_x = self.speed * math.cos(self.angle)
            bullet_speed_y = self.speed * math.sin(self.angle)

            # Move the bullet in the calculated direction
            self.rect.x += bullet_speed_x
            self.rect.y += bullet_speed_y
            
            self.image = pygame.transform.rotate(self.original_image, math.degrees(-self.angle))
            self.rect = self.image.get_rect(center=self.rect.center)
            
        def draw(self):
            screen.blit(self.image, self.rect)
            
        def check_player_hit(self):
            if Players == 1:
                if player.hp > 0 and player.rect.colliderect(bullet.rect):
                    bullet.kill()
                    player.hp -= 1
                    
            if Players == 2:
                if player.hp > 0 and player.rect.colliderect(bullet.rect):
                    bullet.kill()
                    player.hp -= 1
                    
                
                if playertwo.hp > 0 and playertwo.rect.colliderect(bullet.rect):
                    bullet.kill()
                    playertwo.hp -= 1
                    
            
    class HealthPack(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(health_img, (64, 64))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.health = player.initial_hp
        
        def draw(self):
            screen.blit(self.image, self.rect)
    
    class PlayerMarker(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(Player1_marker, (64, 64))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        
        def update(self):
            self.rect.x = player.rect.x - 16
            self.rect.y = player.rect.y - 35
            
        def draw(self):
            screen.blit(self.image, self.rect)
            
    class Player2Marker(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(Player2_marker, (64, 64))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        
        def update(self):
            self.rect.x = playertwo.rect.x - 16
            self.rect.y = playertwo.rect.y - 35
            
        def draw(self):
            screen.blit(self.image, self.rect)
    
    #The use of the player classes, with the values able to be customized (X, Y, hp, initial_hp, friction, acceleration)
    HPs = 5 if Difficulty == "Easy" else 3 if Difficulty == "Medium" else 1 if Difficulty == "Hard" else 5
    
    player = Player((SCREEN_WIDTH // 2) if Players == 1 else ((SCREEN_WIDTH // 2) - 50), (SCREEN_HEIGHT // 2), HPs, HPs, 0.1, 1)
    if Players == 2:
        playertwo = PlayerTwo((SCREEN_WIDTH // 2) + 50, (SCREEN_HEIGHT // 2 - 16), HPs, HPs, 0.1, 1)
        
    #sprite groups for multiple sprites
    bullets = pygame.sprite.Group()
    healthpacks = pygame.sprite.Group()
    
    #marker sprites
    if Players == 2:
        marker1 = PlayerMarker(player.rect.x - 16, player.rect.y - 35)
        marker2 = Player2Marker(playertwo.rect.x - 16, playertwo.rect.y - 35)
    

    #game loop
    run = True
    while run:
        
        #FPS
        clock.tick(FPS)
        
        if Victory and Players == 2:
            screen.blit(winner_img, (0, 0))
        else:
            screen.blit(bg_img, (0, 0))
            
        #updates & draws (independent of amount of players)
        for bullet in bullets.sprites():
            bullet.check_player_hit()
        
        #checking if game_over is false
        if Players == 1:
            if game_over == False:
                player.update()
                player.draw()
                player.dash()
                
                # Spawn bullets outside of the screen
                if random.randint(0, 100) < score:  # Adjust the frequency of bullet spawning
                    side = random.choice(["left", "right", "top", "bottom"])
                    if side == "left":
                        bullet = Bullet(-20, random.randint(0, SCREEN_HEIGHT), player.rect)
                    elif side == "right":
                        bullet = Bullet(SCREEN_WIDTH + 20, random.randint(0, SCREEN_HEIGHT), player.rect)
                    elif side == "top":
                        bullet = Bullet(random.randint(0, SCREEN_WIDTH), -20, player.rect)
                    elif side == "bottom":
                        bullet = Bullet(random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT + 20, player.rect)
                    bullets.add(bullet)
                    
                bullets.update()
                bullets.draw(screen)
                
                #if player hp is below the maximum/initial hp, spawn health packs
                if player.hp < player.initial_hp and health_available == False:
                    #spawns healthpack in a random location
                    health = HealthPack(random.randint(100, SCREEN_WIDTH - 100), random.randint(0, SCREEN_HEIGHT - 100))
                    healthpacks.add(health)
                    
                    health_available = True
                else:
                    healthpacks.draw(screen)
                    
                if pygame.sprite.spritecollide(player, healthpacks, True):
                    player.hp = player.initial_hp
                    health_available = False
                
                #draw text
                draw_text(f"{score}", large_font, WHITE, (SCREEN_WIDTH // 2), 0)
                draw_text(f"HP: {player.hp}", main_font, GREEN, (SCREEN_WIDTH - 75), 0)
                
                
                #if player hp has reached 0
                if player.hp <= 0:
                    game_over = True
                
            else:
                if not Death:
                    play_deaththeme()
                    Death = True
                draw_text("GAME OVER!", main_font, WHITE, (SCREEN_WIDTH // 2) - 75, SCREEN_HEIGHT // 2)
                draw_text(f"SCORE: {score}", main_font, WHITE, (SCREEN_WIDTH // 2) - 75, (SCREEN_HEIGHT // 2) + 30)
                draw_text("PRESS 'SPACE' TO PLAY AGAIN", main_font, WHITE, (SCREEN_WIDTH // 2) - 175, (SCREEN_HEIGHT // 2) + 75)
                
                #start again
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    #reset variables
                    game_over = False
                    health_available = False
                    Death = False
                    score = 0
                    #set player hp back to normal
                    player.hp = player.initial_hp
                    #re-center player
                    player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                    #reset player velocity
                    player.vel_x, player.vel_y = 0, 0
                    #remove all bullets
                    bullets.empty()
                    healthpacks.empty()
                    pygame.mixer.music.load(MainMusic)
                    pygame.mixer.music.play(-1, 0.0)
                    
        if Players == 2:
            if game_over == False:
                
                #better organization (followed an easy tutorial for using less lines of code)
                for p in [player, playertwo]:
                    p.update(), p.draw(), p.dash()
                
                for m in [marker1, marker2]:
                    m.draw(), m.update()
                
                # Spawn bullets outside of the screen
                if random.randint(0, 100) < (score * 0.5) + 0.5:  # Adjust the frequency of bullet spawning
                    side = random.choice(["left", "right", "top", "bottom"])
                    if side == "left":
                        bullet = Bullet(-20, random.randint(0, SCREEN_HEIGHT), player.rect)
                    elif side == "right":
                        bullet = Bullet(SCREEN_WIDTH + 20, random.randint(0, SCREEN_HEIGHT), player.rect)
                    elif side == "top":
                        bullet = Bullet(random.randint(0, SCREEN_WIDTH), -20, player.rect)
                    elif side == "bottom":
                        bullet = Bullet(random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT + 20, player.rect)
                    bullets.add(bullet)
                    
                if random.randint(0, 100) < (score * 0.5) + 0.5:  # Adjust the frequency of bullet spawning
                    side = random.choice(["left", "right", "top", "bottom"])
                    if side == "left":
                        bullet = Bullet(-20, random.randint(0, SCREEN_HEIGHT), playertwo.rect)
                    elif side == "right":
                        bullet = Bullet(SCREEN_WIDTH + 20, random.randint(0, SCREEN_HEIGHT), playertwo.rect)
                    elif side == "top":
                        bullet = Bullet(random.randint(0, SCREEN_WIDTH), -20, playertwo.rect)
                    elif side == "bottom":
                        bullet = Bullet(random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT + 20, playertwo.rect)
                    bullets.add(bullet)
                    
                bullets.update()
                bullets.draw(screen)
                
                #if player hp is below the maximum/initial hp, spawn health packs
                if (player.hp < player.initial_hp or playertwo.hp < playertwo.initial_hp) and health_available == False:
                    #spawns healthpack in a random location
                    health = HealthPack(random.randint(100, SCREEN_WIDTH - 100), random.randint(0, SCREEN_HEIGHT - 100))
                    healthpacks.add(health)
                    
                    health_available = True
                else:
                    healthpacks.draw(screen)
                    
                if pygame.sprite.spritecollide(player, healthpacks, True):
                    player.hp = player.initial_hp
                    health_available = False
                    
                if pygame.sprite.spritecollide(playertwo, healthpacks, True):
                    playertwo.hp = playertwo.initial_hp
                    health_available = False
                
                #draw text
                draw_text(f"P1 HP: {player.hp}", main_font, GREEN, 10, 0)   
                draw_text(f"P2 HP: {playertwo.hp}", main_font, GREEN, (SCREEN_WIDTH - 125), 0)
                
                
                #if player hp has reached 0
                if player.hp <= 0 or playertwo.hp <= 0:
                    if player.hp <= 0:
                        winner = "2"
            
                    if playertwo.hp <= 0:
                        winner = "1"
                        
                    game_over = True
                
            else:
                if not Victory:
                    play_theme()
                    Victory = True
                draw_text("THE WINNER IS...", main_font, WHITE, (SCREEN_WIDTH // 2) - 75, (SCREEN_HEIGHT // 2))
                draw_text("Player " + winner + "!", main_font, WHITE, (SCREEN_WIDTH // 2) - 75, (SCREEN_HEIGHT // 2) + 30)
                draw_text("PRESS 'SPACE' TO FIGHT AGAIN", main_font, WHITE, (SCREEN_WIDTH // 2) - 175, (SCREEN_HEIGHT // 2) + 75)
                
                #start again
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    #reset variables
                    Victory = False
                    game_over = False
                    health_available = False
                    score = 0
                    #set player hp back to normal
                    player.hp = player.initial_hp
                    playertwo.hp = playertwo.initial_hp
                    #re-center player
                    player.rect.center = ((SCREEN_WIDTH // 2) - 50, SCREEN_HEIGHT // 2)
                    playertwo.rect.center = ((SCREEN_WIDTH // 2) + 50, SCREEN_HEIGHT // 2)
                    #reset player velocities
                    player.vel_x, player.vel_y = 0, 0
                    playertwo.vel_x, playertwo.vel_y = 0, 0
                    #remove all bullets
                    bullets.empty()
                    healthpacks.empty()
                    pygame.mixer.music.load(MainMusic)
                    pygame.mixer.music.play(-1, 0.0)
        
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.USEREVENT:
                if event.type == timer:
                    if game_over == False:
                        score_time = 0
                        score += 1
                        
                        
                    
        
        #update display window
        pygame.display.update()
    pygame.quit()
        

mainMenu()









# lets goo