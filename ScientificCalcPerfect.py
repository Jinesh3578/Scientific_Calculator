import tkinter as tk
from math import *

window = tk.Tk()
window.title("Scientific Calculator")


class Calculator:

    def fsin(arg):
        return sin(arg)

    def fcos(arg):
        return cos(arg)

    def ftan(arg):
        return tan(arg)

    def arcsin(arg):
        return (asin(arg))

    def arccos(arg):
        return (acos(arg))

    def arctan(arg):
        return (atan(arg))

    def sinh(arg):
        return sinh(arg)

    def cosh(arg):
        return cosh(arg)

    def tanh(arg):
        return tanh(arg)

    def btn_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)

    def btn_clear1(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)

    def change_signs(self):
        self.expression = self.expression + '-'
        self.text_input.set(self.expression)

    def memory_clear(self):
        self.recall = ""

    def memory_add(self):
        self.recall = self.recall + '+' + self.expression

    def answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.text_input.set(self.expression)

    def memory_recall(self):
        if self.expression == "":
            self.text_input.set('0' + self.expression + self.recall)
        else:
            self.text_input.set(self.expression + self.recall)


    def btn_clear_all(self):
        self.expression = ""
        self.text_input.set("")

    def btn_equal(self):
        self.sum_up = str(eval(self.expression))
        self.text_input.set(self.sum_up)
        self.expression = self.sum_up

    def __init__(self, master):
        self.expression = ""
        self.recall = ""
        self.sum_up = ""
        self.text_input = tk.StringVar()
        self.master = master

        top_frame = tk.Frame(master,
                             bd=10, bg='orange')
        top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        bottom_frame = tk.Frame(
            master, bd=2, bg='white')
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        txt_display = tk.Entry(top_frame, font=('Retro', 26), relief='flat', bg='white', fg='orange',
                               textvariable=self.text_input, width=12, bd=12, justify='right')
        txt_display.pack(fill=tk.BOTH, expand=True)

        self.btn_left_brack = tk.Button(
            bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'), width=2, height=2,
            relief=tk.GROOVE, activebackground='black', activeforeground='orange', text="(",
            command=lambda: self.btn_click('('))
        self.btn_left_brack.grid(row=1, column=3)

        self.btn_right_brack = tk.Button(
            bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'), width=2, height=2,
            relief=tk.GROOVE, activebackground='black', activeforeground='orange', text=")",
            command=lambda: self.btn_click(')'))
        self.btn_right_brack.grid(row=1, column=4)

        self.btn_exp = tk.Button(
            bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'), width=2, height=2,
            relief=tk.GROOVE, activebackground='black', activeforeground='orange', text="e^x",
            command=lambda: self.btn_click('exp('))
        self.btn_exp.grid(row=0, column=0)

        self.btn_pi = tk.Button(
            bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'), width=2, height=2,
            relief=tk.GROOVE, activebackground='black', activeforeground='orange', text="π",
            command=lambda: self.btn_click('pi'))
        self.btn_pi.grid(row=5, column=0)

        self.btn_sqrt = tk.Button(
            bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'), width=2, height=2,
            relief=tk.GROOVE, activebackground='black', activeforeground='orange', text="√X",
            command=lambda: self.btn_click('sqrt('))
        self.btn_sqrt.grid(row=2, column=0)

        self.btn_clear = tk.Button(
            bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='gray', font=('Retro', 16, 'bold'), width=2, height=2,
            relief=tk.GROOVE, activebackground='black', activeforeground='orange', text="AC",
            command=self.btn_clear_all)
        self.btn_clear.grid(row=2, column=1)

        self.btn_del = tk.Button(
            bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='gray', font=('Retro', 16, 'bold'), width=2, height=2,
            relief=tk.GROOVE, activebackground='black', activeforeground='orange', text="⫷", command=self.btn_clear1)
        self.btn_del.grid(row=2, column=2)

        self.btn_div = tk.Button(
            bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'), width=2, height=2,
            relief=tk.GROOVE, activebackground='black', activeforeground='orange', text="÷",
            command=lambda: self.btn_click('/'))
        self.btn_div.grid(row=2, column=4)

        self.cube = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'),
                              width=2, height=2, relief=tk.GROOVE, activebackground='black', activeforeground='orange',
                              text=u"x\u00B3", command=lambda: self.btn_click('**3'))
        self.cube.grid(row=4, column=0)

        self.btn_7 = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'),
                               width=2, height=2, relief=tk.GROOVE, activebackground='black', activeforeground='orange',
                               text="7", command=lambda: self.btn_click(7))
        self.btn_7.grid(row=3, column=1)

        self.btn_8 = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'),
                               width=2, height=2, relief=tk.GROOVE, activebackground='black', activeforeground='orange',
                               text="8", command=lambda: self.btn_click(8))
        self.btn_8.grid(row=3, column=2)

        self.btn_9 = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'),
                               width=2, height=2, relief=tk.GROOVE, activebackground='black', activeforeground='orange',
                               text="9", command=lambda: self.btn_click(9))
        self.btn_9.grid(row=3, column=3)

        self.btn_mult = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white',
                                  font=('Retro', 16, 'bold'), width=2, height=2, relief=tk.GROOVE,
                                  activebackground='black', activeforeground='orange', text="x",
                                  command=lambda: self.btn_click('*'))
        self.btn_mult.grid(row=3, column=4)

        self.btn_sin = tk.Button(
            bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'), width=2, height=2,
            relief=tk.GROOVE, activebackground='black', activeforeground='orange', text="sin",
            command=lambda: self.btn_click('fsin('))
        self.btn_sin.grid(row=0, column=2)

        self.btn_sinh = tk.Button(
            bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'), width=2, height=2,
            relief=tk.GROOVE, activebackground='black', activeforeground='orange', text="sinh",
            command=lambda: self.btn_click('sinh('))
        self.btn_sinh.grid(row=0, column=1)

        self.btn_cos = tk.Button(
            bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'), width=2, height=2,
            relief=tk.GROOVE, activebackground='black', activeforeground='orange', text="cos",
            command=lambda: self.btn_click('fcos('))
        self.btn_cos.grid(row=0, column=3)

        self.btn_cosh = tk.Button(
            bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'), width=2, height=2,
            relief=tk.GROOVE, activebackground='black', activeforeground='orange', text="cosh",
            command=lambda: self.btn_click('cosh('))
        self.btn_cosh.grid(row=2, column=3)

        self.btn_tan = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white',
                                 font=('Retro', 16, 'bold'), width=2, height=2, relief=tk.GROOVE,
                                 activebackground='black', activeforeground='orange', text="tan",
                                 command=lambda: self.btn_click('ftan('))
        self.btn_tan.grid(row=0, column=4)

        self.btn_tanh = tk.Button(
            bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'), width=2, height=2,
            relief=tk.GROOVE, activebackground='black', activeforeground='orange', text="tanh",
            command=lambda: self.btn_click('tanh('))
        self.btn_tanh.grid(row=7, column=2)

        self.btn_log = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white',
                                 font=('Retro', 16, 'bold'), width=2, height=2, relief=tk.GROOVE,
                                 activebackground='black', activeforeground='orange', text="log",
                                 command=lambda: self.btn_click('log('))
        self.btn_log.grid(row=1, column=1)

        self.btn_4 = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'),
                               width=2, height=2, relief=tk.GROOVE, activebackground='black', activeforeground='orange',
                               text="4", command=lambda: self.btn_click(4))
        self.btn_4.grid(row=4, column=1)

        self.btn_5 = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'),
                               width=2, height=2, relief=tk.GROOVE, activebackground='black', activeforeground='orange',
                               text="5", command=lambda: self.btn_click(5))
        self.btn_5.grid(row=4, column=2)

        self.btn_6 = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'),
                               width=2, height=2, relief=tk.GROOVE, activebackground='black', activeforeground='orange',
                               text="6", command=lambda: self.btn_click(6))
        self.btn_6.grid(row=4, column=3)

        self.btnSub = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white',
                                font=('Retro', 16, 'bold'), width=2, height=2, relief=tk.GROOVE,
                                activebackground='black', activeforeground='orange', text="-",
                                command=lambda: self.btn_click('-'))
        self.btnSub.grid(row=4, column=4)

        self.btn_sin_inverse = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white',
                                         font=('Retro', 16, 'bold'), width=2, height=2, relief=tk.GROOVE,
                                         activebackground='black', activeforeground='orange', text=u"sin-\u00B9",
                                         command=lambda: self.btn_click('arcsin('))
        self.btn_sin_inverse.grid(row=7, column=1)

        self.btn_cos_inverse = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white',
                                         font=('Retro', 16, 'bold'), width=2, height=2, relief=tk.GROOVE,
                                         activebackground='black', activeforeground='orange', text=u"cos-\u00B9",
                                         command=lambda: self.btn_click('arccos('))
        self.btn_cos_inverse.grid(row=7, column=0)

        self.btn_tan_inverse = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white',
                                         font=('Retro', 16, 'bold'), width=2, height=2, relief=tk.GROOVE,
                                         activebackground='black', activeforeground='orange', text=u"tan-\u00B9",
                                         command=lambda: self.btn_click('arctan('))
        self.btn_tan_inverse.grid(row=6, column=1)

        self.btn_ln = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white',
                                font=('Retro', 16, 'bold'), width=2, height=2, relief=tk.GROOVE,
                                activebackground='black', activeforeground='orange', text="ln",
                                command=lambda: self.btn_click('log1p('))
        self.btn_ln.grid(row=1, column=2)

        self.btn_1 = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'),
                               width=2, height=2, relief=tk.GROOVE, activebackground='black', activeforeground='orange',
                               text="1", command=lambda: self.btn_click(1))
        self.btn_1.grid(row=5, column=1)

        self.btn_2 = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'),
                               width=2, height=2, relief=tk.GROOVE, activebackground='black', activeforeground='orange',
                               text="2", command=lambda: self.btn_click(2))
        self.btn_2.grid(row=5, column=2)

        self.btn_3 = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'),
                               width=2, height=2, relief=tk.GROOVE, activebackground='black', activeforeground='orange',
                               text="3", command=lambda: self.btn_click(3))
        self.btn_3.grid(row=5, column=3)

        self.btn_add = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white',
                                 font=('Retro', 16, 'bold'), width=2, height=2, relief=tk.GROOVE,
                                 activebackground='black', activeforeground='orange', text="+",
                                 command=lambda: self.btn_click('+'))
        self.btn_add.grid(row=5, column=4)

        self.btn_fact = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white',
                                  font=('Retro', 16, 'bold'), width=2, height=2, relief=tk.GROOVE,
                                  activebackground='black', activeforeground='orange', text="X!",
                                  command=lambda: self.btn_click('factorial('))
        self.btn_fact.grid(row=3, column=0)

        self.btn_sqr = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white',
                                 font=('Retro', 16, 'bold'), width=2, height=2, relief=tk.GROOVE,
                                 activebackground='black', activeforeground='orange', text=u"x\u00B2",
                                 command=lambda: self.btn_click('**2'))
        self.btn_sqr.grid(row=6, column=4)

        self.btn_power = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white',
                                   font=('Retro', 16, 'bold'), width=2, height=2, relief=tk.GROOVE,
                                   activebackground='black', activeforeground='orange', text="x^y",
                                   command=lambda: self.btn_click('**'))
        self.btn_power.grid(row=1, column=0)

        self.btn_ans = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white',
                                 font=('Retro', 16, 'bold'), width=2, height=2, relief=tk.GROOVE,
                                 activebackground='black', activeforeground='orange', text="Ans", command=self.answer)
        self.btn_ans.grid(row=6, column=0)

        self.btn_0 = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white', font=('Retro', 16, 'bold'),
                               width=2, height=2, relief=tk.GROOVE, activebackground='black', activeforeground='orange',
                               text="0", command=lambda: self.btn_click(0))
        self.btn_0.grid(row=6, column=2)

        self.btn_eq = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='gray', font=('Retro', 16, 'bold'),
                                width=2, height=2, relief=tk.GROOVE, activebackground='black',
                                activeforeground='orange', text="=", command=self.btn_equal)
        self.btn_eq.grid(row=6, column=4)

        self.btn_dec = tk.Button(bottom_frame, padx=18, pady=1, bd=5, fg='orange', bg='white',
                                 font=('Retro', 16, 'bold'), width=2, height=2, relief=tk.GROOVE,
                                 activebackground='black', activeforeground='orange', text=".",
                                 command=lambda: self.btn_click('.'))
        self.btn_dec.grid(row=6, column=3)


b = Calculator(window)
window.mainloop()