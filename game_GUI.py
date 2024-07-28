import tkinter as tk
import random

def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result_text.set(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        user_score += 1
        result = "You win!"
    else:
        computer_score += 1
        result = "Computer wins!"

    result_text.set(f"{result_text.get()}\n{result}")
    user_score_text.set(f"User Score: {user_score}")
    computer_score_text.set(f"Computer Score: {computer_score}")

def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_text.set("")
    user_score_text.set("User Score: 0")
    computer_score_text.set("Computer Score: 0")

# Initialize scores
user_score = 0
computer_score = 0

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create and set the result text variable
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

# Create and set the user score text variable
user_score_text = tk.StringVar(value="User Score: 0")
user_score_label = tk.Label(root, textvariable=user_score_text)
user_score_label.pack()

# Create and set the computer score text variable
computer_score_text = tk.StringVar(value="Computer Score: 0")
computer_score_label = tk.Label(root, textvariable=computer_score_text)
computer_score_label.pack()

# Create buttons for Rock, Paper, Scissors
buttons_frame = tk.Frame(root)
buttons_frame.pack()

rock_button = tk.Button(buttons_frame, text="Rock", command=lambda: play("rock"))
rock_button.pack(side=tk.LEFT)

paper_button = tk.Button(buttons_frame, text="Paper", command=lambda: play("paper"))
paper_button.pack(side=tk.LEFT)

scissors_button = tk.Button(buttons_frame, text="Scissors", command=lambda: play("scissors"))
scissors_button.pack(side=tk.LEFT)

# Create a reset button
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack()

# Run the application
root.mainloop()
