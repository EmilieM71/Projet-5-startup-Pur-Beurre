from tkinter import *
from tkinter import font


class ViewModel:

    def __init__(self, frame):
        self.frame = frame

    def create_title(self, text, font_size, bg, fg, row, sticky):
        label_title = Label(self.frame, text=text,
                            font=font_size, bg=bg, fg=fg)
        label_title.grid(row=row, sticky=sticky)

    def create_subtitle(self, text, font_size, bg, fg, row, sticky):
        label_subtitle = Label(self.frame, text=text, justify=LEFT,
                               font=font_size, bg=bg, fg=fg)
        label_subtitle.grid(row=row, sticky=sticky)

    def create_line(self, bd, highlightthickness, bg, height,
                    x0, y0, x1, y1, fill, width, row, sticky):
        canvas = Canvas(self.frame, bd=bd,
                        highlightthickness=highlightthickness,
                        background=bg, height=height)
        canvas.create_line((x0, y0), (x1, y1), fill=fill, width=width)
        canvas.grid(row=row, sticky=sticky)

    def create_label_entry(self, label_text, font_size_label, bg_label,
                           fg_label, label_row, column_lable, sticky_label,
                           font_size_entry, bg_entry, fg_entry, column_entry,
                           sticky_entry):
        label = Label(self.frame, text=label_text, font=font_size_label,
                      bg=bg_label, fg=fg_label)
        label.grid(row=label_row, column=column_lable, sticky=sticky_label)
        entry = Entry(self.frame, font=font_size_entry,
                      bg=bg_entry, fg=fg_entry)
        entry.grid(row=(label_row + 1), column=column_entry,
                   sticky=sticky_entry)

    def create_text(self, text, font_size, bg, fg, row, sticky):
        label = Label(self.frame, text=text, justify='left', font=font_size,
                      bg=bg, fg=fg)
        label.grid(row=row, sticky=sticky, pady=5)

    def create_textvariable(self, var, font_size, bg, fg, row, sticky):
        label = Label(self.frame, textvariable=var, font=font_size,
                      bg=bg, fg=fg, justify='left')
        label.grid(row=row, sticky=sticky, pady=5)

    def create_button(self, bd, text, font_size, bg, fg, command, row,
                      sticky, pady, underline):
        button = Button(self.frame, bd=bd, text=text, font=font_size,
                        bg=bg, fg=fg, command=command)
        button.grid(row=row, sticky=sticky, pady=pady)
        f = font.Font(button, button.cget("font"))
        f.configure(underline=underline)
        button.configure(font=f)

    def create_text2(self, bg, bd, font_size, fg, text, row, sticky, pady):
        message = Text(self.frame, bg=bg, bd=bd, font=font_size, fg=fg,
                                 text=text, relief=GROOVE)
        message.grid(row=row, sticky=sticky, pady=pady)
