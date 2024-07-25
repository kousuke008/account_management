import tkinter as tk
import re
from tkinter import scrolledtext

def create_text_window(on_submit_callback):
    # メインウィンドウの設定
    root = tk.Tk()
    root.title("テキスト入力ウィンドウ")

    # スクロール可能なテキストウィンドウの設定
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
    text_area.pack(pady=10, padx=10)

    # 送信ボタンの設定
    submit_button = tk.Button(root, text="送信", command=lambda: on_submit_callback(text_area, root))
    submit_button.pack(pady=10)

    # ウィンドウを表示
    root.wait_window(root)

def on_submit(text_area, root, lines_holder):
    # テキストウィンドウの内容を取得
    text_content = text_area.get("1.0", tk.END).strip()
    # 各行をリストに分割
    lines = text_content.split("\n")
    # リストを保持する
    lines_holder.extend(lines)
    # ウィンドウを閉じる
    root.destroy()
    
def process_lines(lines):
    results = []
    for line in lines:
        numbers = re.findall(r'\d+(?::\d+)?', line)
        result = "".join(numbers)
        results.append(result)
    
    final_result = ', '.join(results)
    final_result = final_result.replace(' ','')
    print(final_result)

def main():
    lines = []

    def on_submit_callback(text_area, root):
        on_submit(text_area, root, lines)

    create_text_window(on_submit_callback)
    process_lines(lines)
    
    input("Enterキーを押して終了")



if __name__ == "__main__":
    main()