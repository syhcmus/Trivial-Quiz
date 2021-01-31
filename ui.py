from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, question_bank):
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.score_lable = Label(text=f'Score: {self.score}')
        self.score_lable.grid(row=0, column=1)

        self.quiz = QuizBrain(question_bank)
        self.canvas = Canvas(width=300, height=250, bg='white')
        text = self.quiz.next_question()
        self.quiz_text = self.canvas.create_text(150, 125, width=280, text=text, fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.choose_false_button)
        self.false_button.grid(row=2, column=0)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.choose_true_button)
        self.true_button.grid(row=2, column=1)

        self.window.mainloop()




    def check_answer(self, answer):
        if self.quiz.check_answer(answer):
            self.score += 1
            self.score_lable.config(text=f'Score: {self.score}')

        if self.quiz.still_has_questions():
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=text)
        else:
            messagebox.showinfo(title="Game's Over", message=f"Your's core is: {self.score}")
            self.window.destroy()


    def choose_true_button(self):
        self.check_answer('true')

    def choose_false_button(self):
        self.check_answer('false')

    



       
        
        

    


        

        