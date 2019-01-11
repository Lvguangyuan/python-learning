from tkinter import *
import tkinter.messagebox as message_box


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.helloLabel = Label(self, text='Hello, World!')
        self.helloLabel.pack()

        self.nameInput = Entry(self)
        self.nameInput.pack()

        self.quitButton = Button(self, text='Greet', command=self.hello)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        message_box.showinfo('Message', 'Hello, %s' % name)


if __name__ == '__main__':
    app = Application()
    # 设置窗口标题:
    app.master.title('Hello World')
    # 主消息循环:
    app.mainloop()


