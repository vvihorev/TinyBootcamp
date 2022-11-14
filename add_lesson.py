#!/usr/bin/python3
import os


def get_lesson_number(lesson_name: str) -> int:
    return int(lesson_name.split(".")[0].split("_")[1])


lessons = os.listdir("lessons")
last_lesson = max(lessons, key=lambda name: get_lesson_number(name))
new_number = get_lesson_number(last_lesson) + 1
new = f"lesson_{new_number}.md"

new_name = input("Lesson title: ")

with open("lessons/" + new, "w") as new_lesson:
    new_lesson.writelines(
        [f"# Занятие {new_number}.\n", "## {new_name}\n", "\n", f"## Источники\n", "1. \n"]
    )
