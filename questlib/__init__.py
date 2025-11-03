import sys

game_state = {
"current_scene": None,
"inventory": [],
"flags": {}
}

scenes = {}

def add_scene(scene_id, text, choices):
    scenes[scene_id] = {
        "text": text,
        "choices": choices
    }
def start_game(start_scene_id):
    game_state["current_scene"] = start_scene_id
    game_loop()

def game_loop():
 while True:
        scene_id = game_state["current_scene"]
        if scene_id not in scenes:
            print("Oшибка: сцена не найдена!")
            break

        scene = scenes[scene_id]
        print("\n" + scene["text"])

        if not scene["choices"]:
            print("Конец игры.")
            break

        for i, (choice_text, _) in enumerate(scene["choices"], 1):
            print(f"[{i}] {choice_text}")

        try:
            user_input = input("> ").strip()
            choice_index = int(user_input) - 1
            if 0 <= choice_index < len(scene["choices"]):
                next_scene = scene["choices"][choice_index][1]
                game_state["current_scene"] = next_scene
            else:
                print("Нет такого варанта.")
        except (ValueError, KeyboardInterrupt):
            print("\nИгра прервана.")
            break
