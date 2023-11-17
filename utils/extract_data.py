from models.chapter import Chapter
from models.character import Character
from models.dynamics.action import Action


def extract_chapters(data) -> list[Chapter]:
    chapters_data = data["chapters"]
    chapters = []

    for chapter_data in chapters_data:
        events = []
        for event in chapter_data["events"]:
            subjects = [
                Character(name=subject["name"], image=subject["image"])
                for subject in event["subjects"]
            ]
            objects = [
                Character(name=obj["name"], image=obj["image"])
                for obj in event["objects"]
            ]
            if event["dynamic"]["type"] == "action":
                dynamic = Action(name=event["dynamic"]["name"])
            else:
                dynamic = None
            events.append(
                {"subjects": subjects, "objects": objects, "dynamic": dynamic}
            )

        chapters.append(
            Chapter(id=chapter_data["id"], events=events, image=chapter_data["image"])
        )
    return chapters
