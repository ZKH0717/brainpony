"""Hello BrainPony — 示例应用。"""

def greet(name: str) -> str:
    """返回问候语。"""
    return f"你好, {name}! 欢迎使用 BrainPony。"


def main():
    """主入口。"""
    name = input("请输入你的名字: ")
    print(greet(name))


if __name__ == "__main__":
    main()
