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
            btn = tk.Button(
                btn_frame,
                text='',
                width=36,   # 적당한 가로
                height=12,  # 적당한 세로 (6:4 비율)
                font=('Arial', 14),
                wraplength=430,  # 가로 픽셀에 맞춰 줄바꿈
                justify='center',
                relief='solid',
                bd=2,
                command=lambda idx=i: self.select_feature(idx)
            )
            btn.grid(row=0, column=i, padx=10, pady=5, sticky='nsew')
            self.feature_buttons.append(btn)
        self.next_btn = tk.Button(self.master, text='다음', command=self.next_person)
        self.next_btn.pack(pady=20)

    def show_person(self):
        if self.index >= len(self.data):
            self.finish()
            return
        person = self.data[self.index]
        # 이름: '이름' 컬럼 우선, 없으면 첫 번째 컬럼값
        name = person.get('이름')
        if name is None:
            for k in person.keys():
                if k.strip() == '이름':
                    name = person[k]
                    break
        if name is None:
            name = list(person.values())[0]
        self.name_label.config(text=name)
        # 특징: '특징1','특징2','특징3' 컬럼 우선, 없으면 이름 컬럼을 제외한 값이 있는 컬럼 최대 3개
        features = []
        for key in ['특징1', '특징2', '특징3']:
            v = person.get(key)
            if v and v.strip():
                features.append(v.strip())
        if not features:
            for k in person.keys():
                if k.strip() == '이름':
                    continue
                v = person[k]
                if v and v.strip():
                    features.append(v.strip())
                if len(features) == 3:
                    break
        # 버튼에 특징 채우기, 부족하면 '데이터 없음'
        for i in range(3):
            if i < len(features):
                self.feature_buttons[i].config(
                    text=features[i],
                    state='normal',
                    bg='SystemButtonFace',
                    fg='black',
                    highlightbackground='black',
                    highlightcolor='black',
                    highlightthickness=2,
                    bd=2,
                    relief='solid'
                )
            else:
                self.feature_buttons[i].config(
                    text='(데이터 없음)',
                    state='disabled',
                    bg='SystemButtonFace',
                    fg='gray',
                    highlightbackground='black',
                    highlightcolor='black',
                    highlightthickness=2,
                    bd=2,
                    relief='solid'
                )
        self.selected = None

    def select_feature(self, idx):
        self.selected = idx
        for i, btn in enumerate(self.feature_buttons):
            if i == idx:
                btn.config(
                    bg='#ffe5e5',  # 옅은 붉은색 배경
                    fg='red',      # 글자색도 붉게
                    highlightbackground='red',
                    highlightcolor='red',
                    highlightthickness=3,
                    bd=3,
                    relief='ridge'  # 좀 더 강조
                )
            else:
                btn.config(
                    bg='SystemButtonFace',
                    fg='black',
                    highlightbackground='black',
                    highlightcolor='black',
                    highlightthickness=2,
                    bd=2,
                    relief='solid'
                )

    def next_person(self):
        if self.selected is None:
            messagebox.showwarning('경고', '특징을 선택하세요!')
            return
        person = self.data[self.index]
        # 이름: '이름' 컬럼 우선, 없으면 첫 번째 컬럼값
        name = person.get('이름')
        if name is None:
            for k in person.keys():
                if k.strip() == '이름':
                    name = person[k]
                    break
        if name is None:
            name = list(person.values())[0]
        self.selections.append({'이름': name, '선택': self.selected + 1})
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
        data = list(reader)
        return data

def main():
    data = load_data('14기 대전 4반 자기소개 - 시트1.csv')
    root = tk.Tk()
    app = PersonQuizApp(root, data)
    root.mainloop()

if __name__ == '__main__':
    main()
