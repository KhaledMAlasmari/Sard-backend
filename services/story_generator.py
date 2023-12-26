from ai.image_to_text import ImageToText
from ai.story_generation import StoryGeneration
from ai.text_summarization import TextSummarization
from models.chapter import Chapter
from models.character import Character
from models.prompts.story_prompt import StoryPrompt
from models.prompts.chapter_prompt import ChapterPrompt
from models.story import Story
from models.story_element import StoryElement
from utils.extract_data import extract_chapters, extract_graphs


def generate_story(data: dict):
    genre = data["genre"]
    author_name = data.get("author_name", None)
    chapters = extract_chapters(data)
    graphs = extract_graphs(data)

    story = Story(genre=genre, chapters=chapters, author_name=author_name)
    story_prompt = StoryPrompt(story)
    print(story_prompt.get_prompt())
    get_descriptions_for_images(chapters)
    previous_chapter_summary = None
    summerization_model = TextSummarization()
    story_generation_model = StoryGeneration()
    output = []
    for i in range(len(chapters)):
        chapter = chapters[i]
        chapter_prompt = ChapterPrompt(chapter, previous_chapter_summary)
        chapter_story = story_generation_model.generate_story(chapter_prompt.get_prompt())
        output.append(
            {
                "chapter_id": chapter.id,
                "chapter_story": chapter_story,
                "chapter_prompt": chapter_prompt.get_prompt(),
            }
        )
        if len(chapters) > 1 or i != len(chapters) - 1:
            previous_chapter_summary = summerization_model.summerize_chapter(chapter_story)
    return output

def get_descriptions_for_images(chapters: list[Chapter]):
    model = ImageToText()
    for chapter in chapters:
        if chapter.image != None and chapter.get_description_for_image() == None:
            # get the description for the image
            description = model.get_description_for_chapter_image(chapter.image)
            chapter.set_description_for_image(description)
            apply_descriptions_for_images(description, chapters, chapter)

        for event in chapter.events:
            for subject in event.subjects:
                if (
                    subject.image != None
                    and subject.get_description_for_image() == None
                ):
                    # TODO maybe make subjects and objects characters only
                    description = model.get_description_for_character_image(
                        subject.image, subject.name
                    )
                    subject.set_description_for_image(description)
                    apply_descriptions_for_images(description, chapters, subject)
            for object in event.objects:
                if object.image != None and chapter.get_description_for_image() == None:
                    description = model.get_description_for_character_image(
                        object.image, subject.name
                    )
                    object.set_description_for_image(description)
                    apply_descriptions_for_images(description, chapters, object)


def apply_descriptions_for_images(
    description: str, chapters: list[Chapter], story_element: StoryElement
):
    if isinstance(story_element, Chapter):
        for chapter in chapters:
            if chapter.image == story_element.image:
                chapter.set_description_for_image(description)
    elif isinstance(story_element, Character):
        for chapter in chapters:
            for event in chapter.events:
                for subject in event.subjects:
                    if subject.image == story_element.image:
                        subject.set_description_for_image(description)
                for object in event.objects:
                    if object.image == story_element.image:
                        object.set_description_for_image(description)
