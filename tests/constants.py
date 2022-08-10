"""
Constants for `learner-pathway-progress` tests.
"""
LEARNER_PATHWAY_PROGRESS_DATA = [
    {
        "learner_pathway_progress": {
            "id": 118,
            "uuid": "0a017cbe-0f1c-4e5f-9095-2101823fac93",
            "title": "test 3",
            "status": "active",
            "banner_image": "example.com/banner_image",
            "card_image": 'example.com',
            "overview": "",
            "steps": [
                {
                    "uuid": "a230a2f4-d84b-41d0-9756-6bf56d9b51c3",
                    "min_requirement": 1,
                    "courses": [
                        {
                            "key": "",
                            "course_runs": [],
                            "title": "test course 2",
                            "short_description": "",
                            "card_image_url": 'example.com',
                            "content_type": "course",
                            "status": "NOT_STARTED"
                        }
                    ],
                    "programs": [
                        {
                            "uuid": "919e68dd-8147-482f-8666-72240380c251",
                            "title": "edX Demonstration Program",
                            "short_description": "",
                            "card_image_url": "example.com/course_image.jpg",
                            "content_type": "program",
                            "courses": [
                                {
                                    "key": "edX+DemoX",
                                    "course_runs": [
                                        {
                                            "key": "course-v1:edX+DemoX+Demo_Course"
                                        }
                                    ]
                                }
                            ],
                            "status": "NOT_STARTED"
                        }
                    ],
                    "status": 0.0
                },
                {
                    "uuid": "ea54f31a-be7c-4cfc-8d1f-23a4704c9eaf",
                    "min_requirement": 1,
                    "courses": [
                        {
                            "key": "",
                            "course_runs": [],
                            "title": "test course 2",
                            "short_description": "",
                            "card_image_url": 'example.com',
                            "content_type": "course",
                            "status": "NOT_STARTED"
                        }
                    ],
                    "programs": [],
                    "status": 0.0
                }
            ]
        }
    },
    {
        "learner_pathway_progress": {
            "id": 117,
            "uuid": "29efa34c-60c6-4791-88c0-ab3b5fbd7503",
            "title": "test 1",
            "status": "active",
            "banner_image": 'example.com',
            "card_image": 'example.com',
            "overview": "",
            "steps": [
                {
                    "uuid": "7d95ae15-821e-447a-be2e-9fbfa4d777b4",
                    "min_requirement": 2,
                    "courses": [],
                    "programs": [
                        {
                            "uuid": "919e68dd-8147-482f-8666-72240380c251",
                            "title": "edX Demonstration Program",
                            "short_description": "",
                            "card_image_url": "example.com/course_image.jpg",
                            "content_type": "program",
                            "courses": [
                                {
                                    "key": "edX+DemoX",
                                    "course_runs": [
                                        {
                                            "key": "course-v1:edX+DemoX+Demo_Course"
                                        }
                                    ]
                                }
                            ],
                            "status": "NOT_STARTED"
                        }
                    ],
                    "status": 0.0
                },
                {
                    "uuid": "768e4081-901d-4913-8e7c-434ad25636ac",
                    "min_requirement": 2,
                    "courses": [
                        {
                            "key": "",
                            "course_runs": [],
                            "title": "test course 2",
                            "short_description": "",
                            "card_image_url": 'example.com',
                            "content_type": "course",
                            "status": "NOT_STARTED"
                        }
                    ],
                    "programs": [
                        {
                            "uuid": "919e68dd-8147-482f-8666-72240380c251",
                            "title": "edX Demonstration Program",
                            "short_description": "",
                            "card_image_url": "example.com/course_image.jpg",
                            "content_type": "program",
                            "courses": [
                                {
                                    "key": "edX+DemoX",
                                    "course_runs": [
                                        {
                                            "key": "course-v1:edX+DemoX+Demo_Course"
                                        }
                                    ]
                                }
                            ],
                            "status": "NOT_STARTED"
                        }
                    ],
                    "status": 0.0
                },
                {
                    "uuid": "ced544b3-c1e8-47b5-b7fa-76ef75c3fcc2",
                    "min_requirement": 1,
                    "courses": [
                        {
                            "key": "edX+DemoX",
                            "course_runs": [
                                {
                                    "key": "course-v1:edX+DemoX+Demo_Course"
                                }
                            ],
                            "title": "Demonstration Course",
                            "short_description": "Lorem ipsum",
                            "card_image_url": 'example.com',
                            "content_type": "course",
                            "status": "IN_PROGRESS"
                        }
                    ],
                    "programs": [],
                    "status": 0.0
                }
            ]
        }
    },
    {
        "learner_pathway_progress": {
            "id": 119,
            "uuid": "52970da6-888d-4867-baf3-d970759fb11f",
            "title": "test 2",
            "status": "active",
            "banner_image": "example.com/dude.png",
            "card_image": "example.com/dude.jpeg",
            "overview": "Lorem ipsum",
            "steps": [
                {
                    "uuid": "ae44cc82-1413-434a-9005-14e69fafd840",
                    "min_requirement": 1,
                    "courses": [
                        {
                            "key": "",
                            "course_runs": [],
                            "title": "test course 2",
                            "short_description": "",
                            "card_image_url": 'example.com',
                            "content_type": "course",
                            "status": "NOT_STARTED"
                        }
                    ],
                    "programs": [
                        {
                            "uuid": "919e68dd-8147-482f-8666-72240380c251",
                            "title": "edX Demonstration Program",
                            "short_description": "",
                            "card_image_url": "example.com/course_image.jpg",
                            "content_type": "program",
                            "courses": [
                                {
                                    "key": "edX+DemoX",
                                    "course_runs": [
                                        {
                                            "key": "course-v1:edX+DemoX+Demo_Course"
                                        }
                                    ]
                                }
                            ],
                            "status": "NOT_STARTED"
                        }
                    ],
                    "status": 0.0
                },
                {
                    "uuid": "d792fd72-151c-4a2a-8fef-01ca562c4180",
                    "min_requirement": 1,
                    "courses": [
                        {
                            "key": "edX+DemoX",
                            "course_runs": [
                                {
                                    "key": "course-v1:edX+DemoX+Demo_Course"
                                }
                            ],
                            "title": "Demonstration Course",
                            "short_description": "Lorem ipsum",
                            "card_image_url": 'example.com',
                            "content_type": "course",
                            "status": "IN_PROGRESS"
                        }
                    ],
                    "programs": [],
                    "status": 0.0
                }
            ]
        }
    }
]

LEARNER_PATHWAY_A_UUID = LEARNER_PATHWAY_PROGRESS_DATA[0]['learner_pathway_progress']['uuid']
LEARNER_PATHWAY_B_UUID = LEARNER_PATHWAY_PROGRESS_DATA[1]['learner_pathway_progress']['uuid']
LEARNER_PATHWAY_C_UUID = LEARNER_PATHWAY_PROGRESS_DATA[2]['learner_pathway_progress']['uuid']
