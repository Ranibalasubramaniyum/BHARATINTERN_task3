import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Quiz App")
        self.score = 0
        
        # Questions and answers
        self.questions = [
            "What is the capital of France?",
            "What is the largest planet in our solar system?",
            "Who painted the Mona Lisa?"
        ]
        self.choices = [
            ["Paris", "London", "Berlin", "Rome"],
            ["Jupiter", "Saturn", "Mars", "Earth"],
            ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"]
        ]
        self.answers = [0, 0, 0]  # Index of correct answer for each question
        
        self.current_question = 0
        
        # Create question label
        self.question_label = tk.Label(window, text="")
        self.question_label.pack()
        
        # Create answer buttons
        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(window, text="", width=20, command=lambda choice=i: self.check_answer(choice))
            button.pack(pady=5)
            self.answer_buttons.append(button)
        
        # Create score label
        self.score_label = tk.Label(window, text="")
        self.score_label.pack(pady=10)
        
        # Start the quiz
        self.show_question()
    
    def show_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            choices = self.choices[self.current_question]
            
            self.question_label.config(text=question)
            
            for i in range(4):
                self.answer_buttons[i].config(text=choices[i])
            
            self.score_label.config(text="Score: " + str(self.score))
        else:
            messagebox.showinfo("Quiz App", "Quiz completed!\nYour score: " + str(self.score))
            self.window.destroy()
    
    def check_answer(self, choice):
        if choice == self.answers[self.current_question]:
            self.score += 1
        self.current_question += 1
        self.show_question()

# Create the main window
window = tk.Tk()
quiz_app = QuizApp(window)

# Run the main event loop
window.mainloop()
