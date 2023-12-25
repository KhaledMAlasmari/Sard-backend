from models.chapter import Chapter
from models.character import Character
from models.event import Event
from models.dynamics.action import Action
from models.ChapterGraph import Graph
from models.dynamics.relationship import Relationship

def extract_chapters(data) -> list[Chapter]:
    chapters_data = data["chapters"]
    chapters = []
    for chapter_data in chapters_data:
        # we got one chapter 
        events = []

        for event in chapter_data["events"]:
            # loop through the events in the chapter
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
            elif event["dynamic"]["type"] == "relationship":
                dynamic = Relationship(description=event["dynamic"]["name"])
            else:
                dynamic = None
            events.append(
                Event(subjects=subjects, objects=objects, dynamic=dynamic)
            )
        # we spliited one event to the infos we need
        #  We have subjects(edge start), objects (edge end), and dynamic (weight)
        chapters.append(
            Chapter(id=int(chapter_data["id"]), events=events, image=chapter_data["image"])
        )
    return chapters
#---------------------------------------------------------------------

def extract_graphs(data) -> list[Graph]:
    chapters_data = data["chapters"]
    graphs = []

    for chapter_data in chapters_data:
        # we got one chapter 
        events = []
        chGraph = Graph(id=int(chapter_data["id"]))
        
        for event in chapter_data["events"]:
            # loop through the events in the chapter
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
            #  we spliited one event to the infos we need
            #  We have subjects(edge start), objects (edge end), and dynamic (weight)


            for sub in subjects:
                for obj in objects:
                    chGraph.add_edge(sub,obj,dynamic)

    graphs.append(
        chGraph
    )
    return graphs
