import os

ROOT = os.path.join(os.getcwd(), 'things')
current_path = ROOT


def list_current():
    print(f"\nContents of: {os.path.relpath(current_path, ROOT)}")
    for entry in os.listdir(current_path):
        full_path = os.path.join(current_path, entry)
        if os.path.isdir(full_path):
            print(f"[Container] {entry}")
        elif entry.endswith(".item"):
            print(f"[Item]      {entry[:-5]}")

def add_item(name):
    path = os.path.join(current_path, f"{name}.item")
    open(path, 'w').close()

def add_container(name):
    os.mkdir(os.path.join(current_path, name))

def remove(name):
    item_path = os.path.join(current_path, f"{name}.item")
    container_path = os.path.join(current_path, name)
    if os.path.exists(item_path):
        os.remove(item_path)
    elif os.path.exists(container_path):
        os.rmdir(container_path)  # Only works if empty
    else:
        print("No such item or container.")

def enter(name):
    global current_path
    new_path = os.path.join(current_path, name)
    if os.path.isdir(new_path):
        current_path = new_path
    else:
        print("Not a container.")


def go_back():
    global current_path
    if current_path != ROOT:
        current_path = os.path.dirname(current_path)


def print_tree(path=ROOT, prefix=""):
    entries = sorted(os.listdir(path))
    for index, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "
        if os.path.isdir(full_path):
            print(f"{prefix}{connector}[C] {entry}")
            extension = "    " if is_last else "│   "
            print_tree(full_path, prefix + extension)
        elif entry.endswith(".item"):
            print(f"{prefix}{connector}{entry[:-5]}")


def main():
    global current_path
    os.makedirs(ROOT, exist_ok=True)

    while True:
        cmd = input("\n>> ").strip().split()
        if not cmd: continue
        match cmd:
            case ["list"]:
                list_current()
            case ["adit", name]:
                add_item(name)
            case ["adcon", name]:
                add_container(name)
            case ["remove", name]:
                remove(name)
            case ["enter", name]:
                enter(name)
            case ["back"]:
                go_back()
            case ["tree"]:
                print_tree()
            case ["exit"]:
                break
            case _:
                print("Unknown command.")


if __name__ == "__main__":
    main()

