# File Transfer App Using Tkinter

A simple GUI-based File Transfer application developed using **Python, Tkinter, Socket Programming, and Pillow**.

The application allows users to send and receive files between two computers connected to the **same network**.

## Features

* Simple and user-friendly GUI
* Send files from one computer to another
* Receive files from another computer
* Uses Socket Programming for communication
* Displays Sender ID
* Custom GUI design and images
* Separate Send and Receive interfaces

## Technologies Used

* Python
* Tkinter
* Socket Programming
* Pillow (PIL)

## Required Library

Install Pillow using:

```bash
pip install pillow
```

Tkinter and Socket are part of the standard Python library, so they normally do not need to be installed separately.

## Images / Assets

The `Images` folder contains the image assets used in the graphical user interface:

* `shareit.png` – Main application icon
* `send.png` – Send option and send window icon
* `receive.png` – Receive option and receive window icon
* `sender.png` – Sender window background
* `ID.png` – Sender ID section image
* `receiver.png` – Receiver window background
* `profile.png` – Receiver window profile image
* `arrow.png` – Receive button icon
* `background.png` – Main application background

These images are required for the GUI to work correctly.

## Project Structure

```text
File-Transfer-App-Tkinter/
│
├── File Transfer App.py
├── README.md
│
└── Images/
    ├── shareit.png
    ├── send.png
    ├── receive.png
    ├── sender.png
    ├── ID.png
    ├── receiver.png
    ├── profile.png
    ├── arrow.png
    └── background.png
```

## How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

### Step 2: Install Pillow

Open Command Prompt or Terminal and run:

```bash
pip install pillow
```

### Step 3: Download the Project

Download or clone this repository to your computer.

### Step 4: Keep the Images Folder

Make sure the `Images` folder is in the same directory as the Python file.

### Step 5: Run the Application

Run:

```bash
python "File Transfer App.py"
```

## How to Send a File

1. Open the application.
2. Click on **Send**.
3. Click **+ Select file** and select the file.
4. Note the Sender ID displayed on the screen.
5. Click **SEND**.
6. Wait for the receiver to connect.

## How to Receive a File

1. Open the application.
2. Click on **Receive**.
3. Enter the **Sender ID**.
4. Enter the filename for the incoming file.
5. Click **Receive**.
6. The file will be received from the sender.

## Important Note

Both computers must be connected to the **same network** for the application to communicate with each other.

The application currently selects `.txt` files by default in the file selection dialog, although the code also provides an option for all file types.

## Project Purpose

This project was created to understand:

* GUI development using Tkinter
* Socket programming
* File handling in Python
* Client-server communication
* Sending and receiving data over a network
* Using images in a Tkinter application

## Author

Developed as a Python GUI project using Tkinter.
