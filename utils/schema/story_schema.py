generate_story_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Story schema",
    "type": "object",
    "properties": {
        "genere": {"type": "string"},
        "chapters": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "events": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "subjects": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "name": {"type": "string"},
                                            "image": {"type": "string"},
                                        },
                                        "required": ["name", "image"],
                                    },
                                },
                                "objects": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "name": {"type": "string"},
                                            "image": {"type": "string"},
                                        },
                                        "required": ["name", "image"],
                                    },
                                },
                                "dynamic": {
                                    "type": "object",
                                    "properties": {
                                        "type": {"type": "string"},
                                        "name": {"type": "string"},
                                    },
                                    "required": ["type", "name"],
                                },
                            },
                            "required": ["subjects", "objects", "dynamic"],
                        },
                    },
                    "image": {"type": "string"},
                },
                "required": ["id", "events", "image"],
            },
        },
    },
    "required": ["genere", "chapters"],
}
