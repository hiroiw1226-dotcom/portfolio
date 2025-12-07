todos = []  # タスクを入れておくリスト

def show_menu():
    print("\n===== Python Todo =====")
    print("1) タスク追加")
    print("2) タスク一覧表示")
    print("3) タスクを完了にする")
    print("4) タスクを削除する")
    print("0) 終了")

def add_todo():
    text = input("タスク内容を入力してください: ").strip()
    if not text:
        print("空のタスクは追加できません。")
        return
    todos.append({"text": text, "done": False})
    print("タスクを追加しました。")

def list_todos():
    if not todos:
        print("タスクはまだありません。")
        return
    print("\n--- タスク一覧 ---")
    for i, t in enumerate(todos):
        mark = "✔" if t["done"] else " "
        print(f"{i}: [{mark}] {t['text']}")

def complete_todo():
    if not todos:
        print("タスクがありません。")
        return
    list_todos()
    try:
        idx = int(input("完了にするタスク番号: "))
        todos[idx]["done"] = True
        print("タスクを完了にしました。")
    except (ValueError, IndexError):
        print("番号が正しくありません。")

def delete_todo():
    if not todos:
        print("タスクがありません。")
        return
    list_todos()
    try:
        idx = int(input("削除するタスク番号: "))
        deleted = todos.pop(idx)
        print(f"「{deleted['text']}」を削除しました。")
    except (ValueError, IndexError):
        print("番号が正しくありません。")

def main():
    while True:
        show_menu()
        choice = input("番号を入力してください: ").strip()
        if choice == "1":
            add_todo()
        elif choice == "2":
            list_todos()
        elif choice == "3":
            complete_todo()
        elif choice == "4":
            delete_todo()
        elif choice == "0":
            print("終了します。")
            break
        else:
            print("メニューの番号を入力してください。")

if __name__ == "__main__":
    main()
