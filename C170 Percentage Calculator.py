from tkinter import *
root = Tk()

root.title("Percentages on my report card")
root.geometry("500x500")

label = Label(root)
label1 = Label(root)
label2 = Label(root)

class grade3:
    def __init__(self, language_arts, math):
        self.language_arts = language_arts
        self.math = math
    def percentage(self):
        total_marks = self.language_arts + self.math
        total_marks_with_100 = total_marks * 100
        grade_3_percentage = total_marks_with_100/200
        label["text"] = str(grade_3_percentage)+"%"
        
class grade5:
    def __init__(self, language_arts, math, ss):
        self.language_arts = language_arts
        self.math = math
        self.social_studies = ss
    def percentage(self):
        total_marks = self.language_arts + self.math + self.social_studies
        total_marks_with_100 = total_marks * 100
        grade_5_percentage = total_marks_with_100/300
        label1["text"] = str(grade_5_percentage)+"%"

class grade7:
    def __init__(self, language_arts, math, ss, f):
        self.language_arts = language_arts
        self.math = math
        self.social_studies = ss
        self.french = f
    def percentage(self):
        total_marks = self.language_arts + self.math + self.social_studies + self.french
        total_marks_with_100 = total_marks * 100
        grade_7_percentage = total_marks_with_100/400
        label2["text"] = str(grade_7_percentage)+"%"
        

obj3 = grade3(51,94.7)


obj5 = grade5(87,94,68.1)


obj7 = grade7(100,19.6,87.1,99.9)


btn = Button(root, text = "Grade 3", command = obj3.percentage)
btn1 = Button(root, text = "Grade 5", command = obj5.percentage)
btn2 = Button(root, text = "Grade 7", command = obj7.percentage)



btn.pack(padx=10,pady=10)
label.pack(padx=10,pady=10)
btn1.pack(padx=10,pady=10)
label1.pack(padx=10,pady=10)
btn2.pack(padx=10,pady=10)
label2.pack(padx=10,pady=10)


    

root.mainloop()