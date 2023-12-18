from models.chapter import Chapter
from models.character import Character
from models.event import Event
from models.dynamics.action import Action


def extract_chapters(data) -> list[Chapter]:
    chapters_data = data["chapters"]
    chapters = []

    for chapter_data in chapters_data:
        events = []
        for event in chapter_data["events"]:
            subjects = []
            for subject in event["subjects"]:
                if subject["type"] == "character":
                    subjects.append(
                        Character(name=subject["name"], image=subject["image"])
                    )
                elif subject["type"] == "event":
                    subjects.append(Event(subject["subjects"], subject["objects"], subject["dynamic"]))
            objects = []
            for object in event["objects"]:
                if object["type"] == "character":
                    objects.append(
                        Character(name=object["name"], image=object["image"])
                    )
                elif object["type"] == "event":
                    objects.append(Event(object["subjects"], object["objects"], object["dynamic"]))

            if event["dynamic"]["type"] == "action":
                dynamic = Action(description=event["dynamic"]["name"])
            else:
                dynamic = None
            events.append(
                Event(subjects=subjects, objects=objects, dynamic=dynamic)
            )

        chapters.append(
            Chapter(id=int(chapter_data["id"]), events=events, image=chapter_data["image"])
        )
    return chapters
