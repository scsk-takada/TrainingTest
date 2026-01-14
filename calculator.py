"""四則演算のみの簡易電卓。"""


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


def main() -> None:
    print("四則演算のみの電卓です。")
    left_value = float(input("1つ目の数値を入力してください: "))
    operator = input("演算子を入力してください (+, -, *, /): ").strip()
    right_value = float(input("2つ目の数値を入力してください: "))

    result = calculate(left_value, operator, right_value)
    print(f"結果: {result}")


if __name__ == "__main__":
    main()
