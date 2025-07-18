import csv
import tkinter as tk
from tkinter import messagebox

class PersonQuizApp:
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.index = 0
        self.selected = None
        self.selections = []
        self.setup_ui()
        self.show_person()

    def setup_ui(self):
        self.master.title('특징 선택 퀴즈')
        self.master.geometry('400x300')
        self.name_label = tk.Label(self.master, text='', font=('Arial', 18))
        self.name_label.pack(pady=20)
        self.feature_buttons = []
        btn_frame = tk.Frame(self.master)
        btn_frame.pack(pady=10)
        for i in range(3):
            btn = tk.Button(btn_frame, text='', width=20, height=2, relief='solid', bd=2,
                            command=lambda idx=i: self.select_feature(idx))
            btn.grid(row=0, column=i, padx=5)
            self.feature_buttons.append(btn)
        self.next_btn = tk.Button(self.master, text='다음', command=self.next_person)
        self.next_btn.pack(pady=20)

    def show_person(self):
        if self.index >= len(self.data):
            self.finish()
            return
        person = self.data[self.index]
        self.name_label.config(text=person['이름'])
        for i, key in enumerate(['특징1', '특징2', '특징3']):
            self.feature_buttons[i].config(text=person[key], bg='SystemButtonFace', highlightbackground='black', highlightcolor='black', highlightthickness=2, bd=2, relief='solid')
        self.selected = None

    def select_feature(self, idx):
        self.selected = idx
        for i, btn in enumerate(self.feature_buttons):
            if i == idx:
                btn.config(
                    bg='#ffe5e5',  # 옅은 붉은색 배경
                    highlightbackground='red',
                    highlightcolor='red',
                    highlightthickness=3,
                    bd=3
                )
            else:
                btn.config(
                    bg='SystemButtonFace',
                    highlightbackground='black',
                    highlightcolor='black',
                    highlightthickness=2,
                    bd=2
                )

    def next_person(self):
        if self.selected is None:
            messagebox.showwarning('경고', '특징을 선택하세요!')
            return
        self.selections.append({'이름': self.data[self.index]['이름'], '선택': self.selected + 1})
        self.index += 1
        self.show_person()

    def finish(self):
        messagebox.showinfo('완료', '모든 인물에 대한 선택이 끝났습니다.')
        # 결과 저장 예시 (선택 사항)
        # with open('result.csv', 'w', newline='', encoding='utf-8') as f:
        #     writer = csv.DictWriter(f, fieldnames=['이름', '선택'])
        #     writer.writeheader()
        #     writer.writerows(self.selections)
        self.master.quit()

def load_data(filename):
    with open(filename, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def main():
    data = load_data('data.csv')
    root = tk.Tk()
    app = PersonQuizApp(root, data)
    root.mainloop()

if __name__ == '__main__':
    main()
