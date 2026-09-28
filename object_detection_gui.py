import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
from ultralytics import YOLO
import sqlite3
import os


# ==========================================================
# YOLO MODEL
# ==========================================================

MODEL_PATH = "yolov8n.pt"

if not os.path.exists(MODEL_PATH):
    print("YOLOv8 model not found.")
    print("The Ultralytics library will download it automatically.")

model = YOLO(MODEL_PATH)


# ==========================================================
# DATABASE
# ==========================================================


import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "users.db")


def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ==========================================================
# MAIN WINDOW
# ==========================================================

root = tk.Tk()

root.title("YOLOv8 Object Detection System")

root.state("zoomed")

root.configure(bg="#171625")


# ==========================================================
# GLOBAL VARIABLES
# ==========================================================

current_image = None
detected_image = None

webcam_running = False
cap = None

confidence_value = 0.25


# ==========================================================
# COLORS
# ==========================================================

BG_COLOR = "#171625"
PANEL_COLOR = "#211F32"
BUTTON_COLOR = "#FFFFFF"
TEXT_COLOR = "#FFFFFF"
ACCENT_COLOR = "#00BFFF"
GREEN_COLOR = "#20C45A"
RED_COLOR = "#FF4B5C"


# ==========================================================
# CLEAR WINDOW
# ==========================================================

def clear_window():

    for widget in root.winfo_children():
        widget.destroy()


# ==========================================================
# SPLASH SCREEN
# ==========================================================

def splash_screen():

    clear_window()

    frame = tk.Frame(
        root,
        bg="#062A43"
    )

    frame.pack(
        fill="both",
        expand=True
    )

    title = tk.Label(
        frame,
        text="✦ Object Detection Model ✦",
        font=("Arial", 28, "bold"),
        fg="#00BFFF",
        bg="#062A43"
    )

    title.place(
        relx=0.5,
        rely=0.45,
        anchor="center"
    )

    start_button = tk.Button(
        frame,
        text="Click to Continue",
        font=("Arial", 12, "bold"),
        bg="#00BFFF",
        fg="white",
        activebackground="#008CCC",
        relief="flat",
        padx=25,
        pady=10,
        command=login_screen
    )

    start_button.place(
        relx=0.5,
        rely=0.55,
        anchor="center"
    )


# ==========================================================
# LOGIN SCREEN
# ==========================================================

def login_screen():

    clear_window()

    main_frame = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main_frame.pack(
        fill="both",
        expand=True
    )

    login_box = tk.Frame(
        main_frame,
        bg="#11111D",
        padx=50,
        pady=40
    )

    login_box.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    title = tk.Label(
        login_box,
        text="✦ Login to Continue ✦",
        font=("Arial", 20, "bold"),
        fg="#00BFFF",
        bg="#11111D"
    )

    title.pack(
        pady=(0, 30)
    )

    username_label = tk.Label(
        login_box,
        text="Username",
        font=("Arial", 11),
        fg="white",
        bg="#11111D"
    )

    username_label.pack(
        anchor="w"
    )

    username_entry = tk.Entry(
        login_box,
        font=("Arial", 12),
        width=30,
        bg="#262638",
        fg="white",
        insertbackground="white",
        relief="flat"
    )

    username_entry.pack(
        pady=(5, 15),
        ipady=8
    )

    password_label = tk.Label(
        login_box,
        text="Password",
        font=("Arial", 11),
        fg="white",
        bg="#11111D"
    )

    password_label.pack(
        anchor="w"
    )

    password_entry = tk.Entry(
        login_box,
        font=("Arial", 12),
        width=30,
        bg="#262638",
        fg="white",
        show="*",
        insertbackground="white",
        relief="flat"
    )

    password_entry.pack(
        pady=(5, 20),
        ipady=8
    )

    def login():

        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if username == "" or password == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter username and password."
            )
            return

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        result = cursor.fetchone()

        conn.close()

        if result:
            dashboard(username)

        else:
            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

    login_button = tk.Button(
        login_box,
        text="Login",
        font=("Arial", 11, "bold"),
        bg="#00BFFF",
        fg="white",
        relief="flat",
        width=15,
        command=login
    )

    login_button.pack(
        pady=10
    )

    register_button = tk.Button(
        login_box,
        text="Register",
        font=("Arial", 10),
        bg="#20C45A",
        fg="white",
        relief="flat",
        width=15,
        command=register_screen
    )

    register_button.pack(
        pady=5
    )


# ==========================================================
# REGISTER SCREEN
# ==========================================================

def register_screen():

    clear_window()

    frame = tk.Frame(
        root,
        bg=BG_COLOR
    )

    frame.pack(
        fill="both",
        expand=True
    )

    box = tk.Frame(
        frame,
        bg="#11111D",
        padx=50,
        pady=40
    )

    box.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    tk.Label(
        box,
        text="Create Account",
        font=("Arial", 22, "bold"),
        fg="#00BFFF",
        bg="#11111D"
    ).pack(pady=(0, 25))

    tk.Label(
        box,
        text="Username",
        fg="white",
        bg="#11111D"
    ).pack(anchor="w")

    username = tk.Entry(
        box,
        width=30,
        bg="#262638",
        fg="white",
        insertbackground="white",
        relief="flat"
    )

    username.pack(
        pady=(5, 15),
        ipady=8
    )

    tk.Label(
        box,
        text="Password",
        fg="white",
        bg="#11111D"
    ).pack(anchor="w")

    password = tk.Entry(
        box,
        width=30,
        show="*",
        bg="#262638",
        fg="white",
        insertbackground="white",
        relief="flat"
    )

    password.pack(
        pady=(5, 20),
        ipady=8
    )

    def register():

        user = username.get().strip()
        pwd = password.get().strip()

        if user == "" or pwd == "":
            messagebox.showwarning(
                "Warning",
                "Please fill all fields."
            )
            return

        try:

            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO users(username, password) VALUES (?, ?)",
                (user, pwd)
            )

            conn.commit()
            conn.close()

            messagebox.showinfo(
                "Success",
                "Registration successful!"
            )

            login_screen()

        except sqlite3.IntegrityError:

            messagebox.showerror(
                "Error",
                "Username already exists."
            )

    tk.Button(
        box,
        text="Register",
        font=("Arial", 11, "bold"),
        bg="#20C45A",
        fg="white",
        relief="flat",
        width=15,
        command=register
    ).pack(pady=10)

    tk.Button(
        box,
        text="Back to Login",
        font=("Arial", 10),
        bg="#00BFFF",
        fg="white",
        relief="flat",
        width=15,
        command=login_screen
    ).pack(pady=5)


# ==========================================================
# DASHBOARD
# ==========================================================

def dashboard(username):

    global webcam_running

    webcam_running = False

    clear_window()

    # ------------------------------------------------------
    # TOP BAR
    # ------------------------------------------------------

    top_bar = tk.Frame(
        root,
        bg="#11111D",
        height=70
    )

    top_bar.pack(
        fill="x"
    )

    title = tk.Label(
        top_bar,
        text="YOLOv8 Object Detection - Logged in as " + username,
        font=("Arial", 16, "bold"),
        fg="#00BFFF",
        bg="#11111D"
    )

    title.pack(
        side="left",
        padx=30,
        pady=20
    )

    logout_button = tk.Button(
        top_bar,
        text="Logout",
        font=("Arial", 10, "bold"),
        bg=RED_COLOR,
        fg="white",
        relief="flat",
        command=logout
    )

    logout_button.pack(
        side="right",
        padx=25,
        pady=15
    )

    # ------------------------------------------------------
    # BUTTON FRAME
    # ------------------------------------------------------

    button_frame = tk.Frame(
        root,
        bg=BG_COLOR
    )

    button_frame.pack(
        pady=20
    )

    tk.Button(
        button_frame,
        text="Select Image",
        font=("Arial", 11, "bold"),
        bg=BUTTON_COLOR,
        fg="black",
        width=15,
        command=select_image
    ).pack(
        side="left",
        padx=8
    )

    tk.Button(
        button_frame,
        text="Detect Objects",
        font=("Arial", 11, "bold"),
        bg=BUTTON_COLOR,
        fg="black",
        width=15,
        command=detect_image
    ).pack(
        side="left",
        padx=8
    )

    tk.Button(
        button_frame,
        text="Webcam",
        font=("Arial", 11, "bold"),
        bg=BUTTON_COLOR,
        fg="black",
        width=15,
        command=start_webcam
    ).pack(
        side="left",
        padx=8
    )

    tk.Button(
        button_frame,
        text="Stop Webcam",
        font=("Arial", 11, "bold"),
        bg=BUTTON_COLOR,
        fg="black",
        width=15,
        command=stop_webcam
    ).pack(
        side="left",
        padx=8
    )

    tk.Button(
        button_frame,
        text="Clear",
        font=("Arial", 11, "bold"),
        bg=BUTTON_COLOR,
        fg="black",
        width=15,
        command=clear_images
    ).pack(
        side="left",
        padx=8
    )

    # ------------------------------------------------------
    # IMAGE AREA
    # ------------------------------------------------------

    image_frame = tk.Frame(
        root,
        bg=BG_COLOR
    )

    image_frame.pack(
        fill="both",
        expand=True,
        padx=40,
        pady=20
    )

    # Original panel

    left_panel = tk.Frame(
        image_frame,
        bg="#211F32",
        bd=2,
        relief="ridge"
    )

    left_panel.pack(
        side="left",
        fill="both",
        expand=True,
        padx=15
    )

    tk.Label(
        left_panel,
        text="ORIGINAL IMAGE",
        font=("Arial", 15, "bold"),
        fg="#00BFFF",
        bg="#211F32"
    ).pack(
        pady=15
    )

    global original_label

    original_label = tk.Label(
        left_panel,
        text="Select an image",
        font=("Arial", 13),
        fg="white",
        bg="#211F32"
    )

    original_label.pack(
        expand=True
    )

    # Result panel

    right_panel = tk.Frame(
        image_frame,
        bg="#211F32",
        bd=2,
        relief="ridge"
    )

    right_panel.pack(
        side="right",
        fill="both",
        expand=True,
        padx=15
    )

    tk.Label(
        right_panel,
        text="YOLOv8 DETECTION RESULT",
        font=("Arial", 15, "bold"),
        fg="#00BFFF",
        bg="#211F32"
    ).pack(
        pady=15
    )

    global result_label

    result_label = tk.Label(
        right_panel,
        text="Detection result will appear here",
        font=("Arial", 13),
        fg="white",
        bg="#211F32"
    )

    result_label.pack(
        expand=True
    )


# ==========================================================
# SELECT IMAGE
# ==========================================================

def select_image():

    global current_image

    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    current_image = file_path

    image = cv2.imread(file_path)

    if image is None:

        messagebox.showerror(
            "Error",
            "Unable to open image."
        )

        return

    display_image(
        image,
        original_label
    )


# ==========================================================
# DISPLAY IMAGE
# ==========================================================

def display_image(image, label):

    image_rgb = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    pil_image = Image.fromarray(
        image_rgb
    )

    # Get screen/window size

    max_width = 600
    max_height = 500

    pil_image.thumbnail(
        (max_width, max_height),
        Image.Resampling.LANCZOS
    )

    photo = ImageTk.PhotoImage(
        pil_image
    )

    label.config(
        image=photo,
        text=""
    )

    label.image = photo


# ==========================================================
# YOLO DETECTION
# ==========================================================

def detect_image():

    global current_image
    global detected_image

    if current_image is None:

        messagebox.showwarning(
            "No Image",
            "Please select an image first."
        )

        return

    try:

        results = model.predict(
            source=current_image,
            conf=confidence_value,
            verbose=False
        )

        result = results[0]

        detected_image = result.plot()

        display_image(
            detected_image,
            result_label
        )

        # Save result

        cv2.imwrite(
            "detected_result.jpg",
            detected_image
        )

    except Exception as e:

        messagebox.showerror(
            "Detection Error",
            str(e)
        )


# ==========================================================
# WEBCAM
# ==========================================================

def start_webcam():

    global cap
    global webcam_running

    if webcam_running:
        return

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():

        messagebox.showerror(
            "Webcam Error",
            "Unable to open webcam."
        )

        return

    webcam_running = True

    webcam_detection()


# ==========================================================
# WEBCAM DETECTION
# ==========================================================

def webcam_detection():

    global cap
    global webcam_running

    if not webcam_running:
        return

    ret, frame = cap.read()

    if not ret:

        stop_webcam()

        return

    try:

        results = model.predict(
            source=frame,
            conf=confidence_value,
            verbose=False
        )

        detected = results[0].plot()

        display_image(
            frame,
            original_label
        )

        display_image(
            detected,
            result_label
        )

    except Exception as e:

        print(
            "Webcam detection error:",
            e
        )

    root.after(
        30,
        webcam_detection
    )


# ==========================================================
# STOP WEBCAM
# ==========================================================

def stop_webcam():

    global cap
    global webcam_running

    webcam_running = False

    if cap is not None:

        cap.release()

        cap = None


# ==========================================================
# CLEAR IMAGES
# ==========================================================

def clear_images():

    global current_image
    global detected_image

    current_image = None
    detected_image = None

    original_label.config(
        image="",
        text="Select an image"
    )

    result_label.config(
        image="",
        text="Detection result will appear here"
    )

    original_label.image = None
    result_label.image = None


# ==========================================================
# LOGOUT
# ==========================================================

def logout():

    stop_webcam()

    login_screen()


# ==========================================================
# CLOSE APPLICATION
# ==========================================================

def close_application():

    stop_webcam()

    root.destroy()


root.protocol(
    "WM_DELETE_WINDOW",
    close_application
)


# ==========================================================
# START APPLICATION
# ==========================================================

splash_screen()

root.mainloop()