"""四則演算のみのGUI電卓。"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


def calculate(left: float, operator: str, right: float) -> float:
    """指定された演算子で計算する。"""
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ValueError("0では割れません。")
        return left / right
    raise ValueError("対応していない演算子です。")


class CalculatorApp:
    """GUI電卓アプリ。"""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("四則演算電卓")

        self.left_var = tk.StringVar()
        self.right_var = tk.StringVar()
        self.operator_var = tk.StringVar(value="+")
        self.result_var = tk.StringVar(value="結果: ")
        self.error_var = tk.StringVar()

        self._build_ui()

    def _build_ui(self) -> None:
        main_frame = ttk.Frame(self.root, padding=16)
        main_frame.grid(row=0, column=0, sticky="nsew")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        ttk.Label(main_frame, text="1つ目の数値").grid(row=0, column=0, sticky="w")
        ttk.Entry(main_frame, textvariable=self.left_var, width=20).grid(
            row=1, column=0, sticky="ew", pady=(4, 12)
        )

        ttk.Label(main_frame, text="演算子").grid(row=0, column=1, sticky="w")
        operator_box = ttk.Combobox(
            main_frame,
            textvariable=self.operator_var,
            values=["+", "-", "*", "/"],
            width=5,
            state="readonly",
        )
        operator_box.grid(row=1, column=1, sticky="w", padx=(8, 0), pady=(4, 12))

        ttk.Label(main_frame, text="2つ目の数値").grid(row=0, column=2, sticky="w")
        ttk.Entry(main_frame, textvariable=self.right_var, width=20).grid(
            row=1, column=2, sticky="ew", padx=(8, 0), pady=(4, 12)
        )

        ttk.Button(main_frame, text="計算", command=self.on_calculate).grid(
            row=2, column=0, columnspan=3, sticky="ew"
        )

        ttk.Label(main_frame, textvariable=self.result_var, font=("", 12, "bold")).grid(
            row=3, column=0, columnspan=3, sticky="w", pady=(12, 0)
        )
        ttk.Label(main_frame, textvariable=self.error_var, foreground="red").grid(
            row=4, column=0, columnspan=3, sticky="w", pady=(4, 0)
        )

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(2, weight=1)

    def on_calculate(self) -> None:
        self.error_var.set("")
        try:
            left = float(self.left_var.get())
            right = float(self.right_var.get())
            operator = self.operator_var.get()
            result = calculate(left, operator, right)
        except ValueError as exc:
            self.result_var.set("結果: ")
            self.error_var.set(str(exc))
            return
        except Exception:
            self.result_var.set("結果: ")
            self.error_var.set("数値を正しく入力してください。")
            return

        self.result_var.set(f"結果: {result}")


def main() -> None:
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
