import unittest

from models.dynamics.action import Action
from models.character import Character
from models.event import Event
from models.chapter import Chapter
from models.prompts.chapter_prompt import ChapterPrompt


class TestChapterPrompt(unittest.TestCase):
    def test_get_prompt_without_summary(self):
        self.assertEqual.__self__.maxDiff=None
        char1 = Character("Vex")
        char1.set_description_for_image(
            "A character with a defiant and intense expression. She has bright red, choppy hair with dark roots, styled asymmetrically with one side short and the other longer. A distinctive trait is a tattoo under her right eye resembling the Roman numeral five, V'. She has a septum piercing, a dark lipstick, and wears a high-collared jacket with a futuristic design."
        )
        char2 = Character("Azure Fury")
        char2.set_description_for_image(
            "A character with a bold and confident look. Her hair is a striking blue, pulled back into a long braid draped over one shoulder. Her eyes are a piercing red, and her expression is serious, with a slight frown. She sports several tattoos and scars that suggest a history of bade or conflict. Her attire seems to be a blend of armor and casual wear, indicating a readiness for combat."
        )
        char3 = Character("Kai the Vigilant")
        char3.set_description_for_image(
            "A character with a focused and determined expression. The character has white hair with black roots, styled in twists that are adorned with gold cuffs. There's a certain intensity in the eyes, which are highlighted with white markings underneath. The character's attire, including a scarf and what appears to be a part of a uniform, adds to a look of practicality and purpose."
        )
        event_1 = Event([char1], [char2], Action("fought"))
        event_1.set_description_for_image(
            "A dystopian vision of a city overcome by nature and neglect. The cyberpunk influences are clear, with neon signs cutting through the overgrowth and a lone boat suggesting the only means of traversal through this flooded urban jungle. There's a feeling of decay but also resilience, as the city continues to pulse with life and light despite its apparent abandonment."
        )
        event_2 = Event([char3], [event_1], Action("watched"))
        event_3 = Event([char3], [char2], Action("ran to and hid from"))
        event_3.set_description_for_image(
            "A narrow alleyway in what appears to be an Asian urban setting, possibly within a Chinatown district. The atmosphere is one of quiet everyday life, with red lanterns hanging above adding a vibrant touch to the otherwise muted and weathered buildings. The signs in Chinese characters suggest a place rich in culture and history, while the deserted nature of the alley gives a sense of stillness and solitude. "
        )
        chapter_events = [event_1, event_2, event_3]
        chapter = Chapter(1, chapter_events)
        chapter_prompt = ChapterPrompt(chapter)
        expected_prompt = """Request: \"\"\"<Write chapter 2 with dialogues and emotions using the following characters details:
[character name: Azure Fury
character details: A character with a bold and confident look. Her hair is a striking blue, pulled back into a long braid draped over one shoulder. Her eyes are a piercing red, and her expression is serious, with a slight frown. She sports several tattoos and scars that suggest a history of bade or conflict. Her attire seems to be a blend of armor and casual wear, indicating a readiness for combat.]
[character name: Kai the Vigilant
character details: A character with a focused and determined expression. The character has white hair with black roots, styled in twists that are adorned with gold cuffs. There's a certain intensity in the eyes, which are highlighted with white markings underneath. The character's attire, including a scarf and what appears to be a part of a uniform, adds to a look of practicality and purpose.]
[character name: Vex
character details: A character with a defiant and intense expression. She has bright red, choppy hair with dark roots, styled asymmetrically with one side short and the other longer. A distinctive trait is a tattoo under her right eye resembling the Roman numeral five, V'. She has a septum piercing, a dark lipstick, and wears a high-collared jacket with a futuristic design.]
now map it to the the information you have in the following events:
[Vex fought Azure Fury in A dystopian vision of a city overcome by nature and neglect. The cyberpunk influences are clear, with neon signs cutting through the overgrowth and a lone boat suggesting the only means of traversal through this flooded urban jungle. There's a feeling of decay but also resilience, as the city continues to pulse with life and light despite its apparent abandonment..]
[Kai the Vigilant watched Vex fought Azure Fury in A dystopian vision of a city overcome by nature and neglect. The cyberpunk influences are clear, with neon signs cutting through the overgrowth and a lone boat suggesting the only means of traversal through this flooded urban jungle. There's a feeling of decay but also resilience, as the city continues to pulse with life and light despite its apparent abandonment...]
[Kai the Vigilant ran to and hid from Azure Fury in A narrow alleyway in what appears to be an Asian urban setting, possibly within a Chinatown district. The atmosphere is one of quiet everyday life, with red lanterns hanging above adding a vibrant touch to the otherwise muted and weathered buildings. The signs in Chinese characters suggest a place rich in culture and history, while the deserted nature of the alley gives a sense of stillness and solitude. .]

>\"\"\"
Output Length: \"\"\"<3000 words>\"\"\"
Structure: \"\"\"<You are writing a introduction chapter, follow the rules to write an amazing introduction> \"\"\"
Take your time with the writing, perfection this chapter."""
        self.assertMultiLineEqual(chapter_prompt.get_prompt(), expected_prompt)

    def test_get_prompt_with_summary(self):
        self.assertEqual.__self__.maxDiff=None
        char1 = Character("Vex")
        char1.set_description_for_image(
            "A character with a defiant and intense expression. She has bright red, choppy hair with dark roots, styled asymmetrically with one side short and the other longer. A distinctive trait is a tattoo under her right eye resembling the Roman numeral five, V'. She has a septum piercing, a dark lipstick, and wears a high-collared jacket with a futuristic design."
        )
        char2 = Character("Azure Fury")
        char2.set_description_for_image(
            "A character with a bold and confident look. Her hair is a striking blue, pulled back into a long braid draped over one shoulder. Her eyes are a piercing red, and her expression is serious, with a slight frown. She sports several tattoos and scars that suggest a history of bade or conflict. Her attire seems to be a blend of armor and casual wear, indicating a readiness for combat."
        )
        char3 = Character("Kai the Vigilant")
        char3.set_description_for_image(
            "A character with a focused and determined expression. The character has white hair with black roots, styled in twists that are adorned with gold cuffs. There's a certain intensity in the eyes, which are highlighted with white markings underneath. The character's attire, including a scarf and what appears to be a part of a uniform, adds to a look of practicality and purpose."
        )
        event_1 = Event([char1], [char2], Action("fought"))
        event_1.set_description_for_image(
            "A dystopian vision of a city overcome by nature and neglect. The cyberpunk influences are clear, with neon signs cutting through the overgrowth and a lone boat suggesting the only means of traversal through this flooded urban jungle. There's a feeling of decay but also resilience, as the city continues to pulse with life and light despite its apparent abandonment."
        )
        event_2 = Event([char3], [event_1], Action("watched"))
        event_3 = Event([char3], [char2], Action("ran to and hid from"))
        event_3.set_description_for_image(
            "A narrow alleyway in what appears to be an Asian urban setting, possibly within a Chinatown district. The atmosphere is one of quiet everyday life, with red lanterns hanging above adding a vibrant touch to the otherwise muted and weathered buildings. The signs in Chinese characters suggest a place rich in culture and history, while the deserted nature of the alley gives a sense of stillness and solitude. "
        )
        chapter_events = [event_1, event_2, event_3]
        chapter = Chapter(1, chapter_events)

        chapter_prompt = ChapterPrompt(
            chapter, "omg very awesome action like so intense hahaha"
        )
        expected_prompt = """Request: \"\"\"<Write chapter 2 with dialogues and emotions using the following characters details:
[character name: Azure Fury
character details: A character with a bold and confident look. Her hair is a striking blue, pulled back into a long braid draped over one shoulder. Her eyes are a piercing red, and her expression is serious, with a slight frown. She sports several tattoos and scars that suggest a history of bade or conflict. Her attire seems to be a blend of armor and casual wear, indicating a readiness for combat.]
[character name: Kai the Vigilant
character details: A character with a focused and determined expression. The character has white hair with black roots, styled in twists that are adorned with gold cuffs. There's a certain intensity in the eyes, which are highlighted with white markings underneath. The character's attire, including a scarf and what appears to be a part of a uniform, adds to a look of practicality and purpose.]
[character name: Vex
character details: A character with a defiant and intense expression. She has bright red, choppy hair with dark roots, styled asymmetrically with one side short and the other longer. A distinctive trait is a tattoo under her right eye resembling the Roman numeral five, V'. She has a septum piercing, a dark lipstick, and wears a high-collared jacket with a futuristic design.]
now map it to the the information you have in the following events:
[Vex fought Azure Fury in A dystopian vision of a city overcome by nature and neglect. The cyberpunk influences are clear, with neon signs cutting through the overgrowth and a lone boat suggesting the only means of traversal through this flooded urban jungle. There's a feeling of decay but also resilience, as the city continues to pulse with life and light despite its apparent abandonment..]
[Kai the Vigilant watched Vex fought Azure Fury in A dystopian vision of a city overcome by nature and neglect. The cyberpunk influences are clear, with neon signs cutting through the overgrowth and a lone boat suggesting the only means of traversal through this flooded urban jungle. There's a feeling of decay but also resilience, as the city continues to pulse with life and light despite its apparent abandonment...]
[Kai the Vigilant ran to and hid from Azure Fury in A narrow alleyway in what appears to be an Asian urban setting, possibly within a Chinatown district. The atmosphere is one of quiet everyday life, with red lanterns hanging above adding a vibrant touch to the otherwise muted and weathered buildings. The signs in Chinese characters suggest a place rich in culture and history, while the deserted nature of the alley gives a sense of stillness and solitude. .]
Use previous chapter information but do not include it explicitly: \"\"\"<Summary:
omg very awesome action like so intense hahaha>\"\"\"
>\"\"\"
Output Length: \"\"\"<3000 words>\"\"\"
Structure: \"\"\"<You are writing a introduction chapter, follow the rules to write an amazing introduction> \"\"\"
Take your time with the writing, perfection this chapter."""
        self.assertMultiLineEqual(chapter_prompt.get_prompt(), expected_prompt)


if __name__ == "__main__":
    unittest.main()


"""
Characters:
A character with a defiant and intense expression. She has bright red, choppy hair with dark roots, styled asymmetrically with one side short and the other longer. A distinctive trait is a tattoo under her right eye resembling the Roman numeral five, V'. She has a septum piercing, a dark lipstick, and wears a high-collared jacket with a futuristic design.
This character could be named "Vex".

A character with a bold and confident look. Her hair is a striking blue, pulled back into a long braid draped over one shoulder. Her eyes are a piercing red, and her expression is serious, with a slight frown. She sports several tattoos and scars that suggest a history of bade or conflict. Her attire seems to be a blend of armor and casual wear, indicating a readiness for combat.
This character could be named "Azure Fury".

A character with a focused and determined expression. The character has white hair with black roots, styled in twists that are adorned with gold cuffs. There's a certain intensity in the eyes, which are highlighted with white markings underneath. The character's attire, including a scarf and what appears to be a part of a uniform, adds to a look of practicality and purpose.
This character could be named "Kai the Vigilant". 

A character with a contemplative and enigmatic expression. This character has slicked-back hair of a dark color with a single thick braid over the shoulder. Them are neon-like light highlights accentuating the face and hands. The eyes are captivating with a luminous red glow, adding to the intense and mysterious aura.
This character might be named "Neon Shadow".


A character with a regal and serene demeanor. She has intricately braided black hair adorned with golden accessories, which complement the gold flecks on her dark skin. Her gaze is direct and confident, with eyes that are subtly lined with white. The jewelry she wears, including earrings and a choker, adds to her noble bearing.
This character could be named "Queen Amine".

A character with a sober and thoughtful expression. His hair is dark and tousled, framing a face with a stern brow and deep-set eyes that carry a weight of wisdom or concem. The attire appears formal yet practical, hinting at a person of intellect and possibly authority.
This character could be known as "Professor Alaric". 

"""

"""
Backgrounds:

A narrow alleyway in what appears to be an Asian urban setting, possibly within a Chinatown district. The atmosphere is one of quiet everyday life, with red lanterns hanging above adding a vibrant touch to the otherwise muted and weathered buildings. The signs in Chinese characters suggest a place rich in culture and history, while the deserted nature of the alley gives a sense of stillness and solitude. 

A fantastical and majestic scene, seemingly out of a sci-fi or fantasy narrative. An imposing structure that fuses elements of traditional Islamic architecture with futuristic design dominates the landscape. It's night, and the city is bathed in the light of a giant moon, creating a feeling of awe and otherworldliness. The presence of people and the glow of the lights suggest a bustling city that Is still active and vibrant despite the late hour.

A dystopian vision of a city overcome by nature and neglect. The cyberpunk influences are clear, with neon signs cutting through the overgrowth and a lone boat suggesting the only means of traversal through this flooded urban jungle. There's a feeling of decay but also resilience, as the city continues to pulse with life and light despite its apparent abandonment. 

A bustling steampunk city with an old-world European flair. The cobblestone streets, intricate architecture, and mechanical contraptions suggest a fusion of history and fantasy. There's a sense of industriousness and progress, with people engaged in conversation and commerce, and the city's infrastructure humming with activity. The scene is rich with the excitement of innovation and discovery. 



"""
