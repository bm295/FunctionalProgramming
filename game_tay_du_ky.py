import json
import os
from dataclasses import dataclass
from typing import List

TOTAL_LEVELS = 81


@dataclass
class GameState:
    player_name: str
    current_level: int

    def clamp(self) -> None:
        if self.current_level < 1:
            self.current_level = 1
        if self.current_level > TOTAL_LEVELS:
            self.current_level = TOTAL_LEVELS


def build_trials() -> List[str]:
    return [f"Nạn kiếp {i}: Thử thách số {i} trên hành trình thỉnh kinh." for i in range(1, TOTAL_LEVELS + 1)]


TRIALS = build_trials()


def prompt(msg: str) -> str:
    return input(msg).strip()


def save_game(state: GameState, path: str) -> None:
    state.clamp()
    payload = {
        "player_name": state.player_name,
        "current_level": state.current_level,
    }
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def load_game(path: str) -> GameState:
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    state = GameState(
        player_name=payload.get("player_name", "Hành giả"),
        current_level=int(payload.get("current_level", 1)),
    )
    state.clamp()
    return state


def ask_save_path() -> str:
    while True:
        path = prompt("Nhập đường dẫn lưu game (ví dụ: saves/ten_file.json): ")
        if not path:
            print("Đường dẫn không được để trống.")
            continue
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        return path


def play_level(state: GameState) -> None:
    if state.current_level > TOTAL_LEVELS:
        print("Bạn đã hoàn thành đủ 81 nạn kiếp! Chúc mừng!")
        return

    trial = TRIALS[state.current_level - 1]
    print("\n" + "=" * 60)
    print(f"Người chơi: {state.player_name}")
    print(f"Màn {state.current_level}/{TOTAL_LEVELS}")
    print(trial)
    print("\nChọn hành động:")
    print("1. Chiến thắng thử thách")
    print("2. Thoát về menu chính")

    choice = prompt("Lựa chọn: ")
    if choice == "1":
        print("Bạn đã vượt qua thử thách!")
        state.current_level += 1
        state.clamp()
        if state.current_level > TOTAL_LEVELS:
            print("Bạn đã hoàn thành đủ 81 nạn kiếp! Chúc mừng!")
    elif choice == "2":
        return
    else:
        print("Lựa chọn không hợp lệ.")


def game_loop(state: GameState) -> None:
    while True:
        if state.current_level > TOTAL_LEVELS:
            print("Hành trình đã hoàn thành. Bạn có thể lưu lại thành tích.")
        print("\n" + "-" * 60)
        print("1. Vào màn tiếp theo")
        print("2. Lưu game")
        print("3. Quay lại menu chính")
        action = prompt("Lựa chọn: ")
        if action == "1":
            play_level(state)
        elif action == "2":
            path = ask_save_path()
            save_game(state, path)
            print(f"Đã lưu tiến trình tại: {path}")
        elif action == "3":
            break
        else:
            print("Lựa chọn không hợp lệ.")


def new_game() -> None:
    name = prompt("Nhập tên người chơi: ") or "Hành giả"
    state = GameState(player_name=name, current_level=1)
    game_loop(state)


def load_game_flow() -> None:
    path = prompt("Nhập đường dẫn file save: ")
    if not path:
        print("Đường dẫn không được để trống.")
        return
    if not os.path.exists(path):
        print("Không tìm thấy file save.")
        return
    try:
        state = load_game(path)
    except (json.JSONDecodeError, OSError, ValueError) as exc:
        print(f"Không thể đọc file save: {exc}")
        return
    print(f"Đã tải game cho {state.player_name} tại màn {state.current_level}.")
    game_loop(state)


def main() -> None:
    print("TÂY DU KÝ - 81 NẠN KIẾP")
    while True:
        print("\n=== MENU CHÍNH ===")
        print("1. New Game")
        print("2. Load Game")
        print("3. Thoát")
        choice = prompt("Lựa chọn: ")
        if choice == "1":
            new_game()
        elif choice == "2":
            load_game_flow()
        elif choice == "3":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
