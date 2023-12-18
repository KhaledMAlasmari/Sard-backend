generate_story_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Story schema",
    "type": "object",
    "properties": {
        "genre": {
            "type": "string"
        },
        "chapters": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "number"
                    },
                    "events": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "subjects": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "anyOf": [
                                            {
                                                "properties": {
                                                    "name": {
                                                        "type": "string"
                                                    },
                                                    "image": {
                                                        "type": "string"
                                                    },
                                                    "type": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "name",
                                                    "image",
                                                    "type"
                                                ]
                                            },
                                            {
                                                "properties": {
                                                    "subjects": {
                                                        "type": "array"
                                                    },
                                                    "objects": {
                                                        "type": "array"
                                                    },
                                                    "dynamic": {
                                                        "type": "object",
                                                        "properties": {
                                                            "type": {
                                                                "type": "string"
                                                            },
                                                            "name": {
                                                                "type": "string"
                                                            }
                                                        },
                                                        "required": [
                                                            "type",
                                                            "name"
                                                        ]
                                                    },
                                                    "type": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "subjects",
                                                    "objects",
                                                    "dynamic",
                                                    "type"
                                                ]
                                            }
                                        ]
                                    }
                                },
                                "objects": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "anyOf": [
                                            {
                                                "properties": {
                                                    "name": {
                                                        "type": "string"
                                                    },
                                                    "image": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "name",
                                                    "image"
                                                ]
                                            },
                                            {
                                                "properties": {
                                                    "subjects": {
                                                        "type": "array"
                                                    },
                                                    "objects": {
                                                        "type": "array"
                                                    },
                                                    "dynamic": {
                                                        "type": "object",
                                                        "properties": {
                                                            "type": {
                                                                "type": "string"
                                                            },
                                                            "name": {
                                                                "type": "string"
                                                            }
                                                        },
                                                        "required": [
                                                            "type",
                                                            "name"
                                                        ]
                                                    }
                                                },
                                                "required": [
                                                    "subjects",
                                                    "objects",
                                                    "dynamic"
                                                ]
                                            }
                                        ]
                                    }
                                },
                                "dynamic": {
                                    "type": "object",
                                    "properties": {
                                        "type": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "type",
                                        "name"
                                    ]
                                }
                            },
                            "required": [
                                "subjects",
                                "objects",
                                "dynamic"
                            ]
                        }
                    },
                    "image": {
                        "type": "string"
                    }
                },
                "required": [
                    "id",
                    "events",
                    "image"
                ]
            }
        }
    },
    "required": [
        "genre",
        "chapters"
    ]
}
