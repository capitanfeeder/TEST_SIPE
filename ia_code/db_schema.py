# Diccionario SIPE
defaultdb = {
    'chatia': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'title': {'type': 'VARCHAR(255)'},
            'content_id': {'type': 'BIGINT'},
            'user_id': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the chatia',
            'title': 'Title of the chatia',
            'content_id': 'Identifier of the content associated with the chatia',
            'user_id': 'Identifier of the user who created the chatia',
        },
        'relationships': {
            'content': {'type': 'belongsTo', 'foreign_key': 'content_id'},
            'user': {'type': 'belongsTo', 'foreign_key': 'user_id'},
        }
    },
    'content': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'answer': {'type': 'VARCHAR(255)'},
            'question': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the content',
            'answer': 'Answer to the question',
            'question': 'Question',
        },
        'relationships': {},
    },
    'evaluation': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'evaluator_id': {'type': 'BIGINT'},
            'hard_objective_result': {'type': 'INTEGER', 'constraints': 'NOT NULL'},
            'observation': {'type': 'VARCHAR(255)'},
            'soft_objective_result': {'type': 'INTEGER', 'constraints': 'NOT NULL'},
            'technology_result': {'type': 'INTEGER', 'constraints': 'NOT NULL'},
        },
        'metadata': {
            'id': 'Unique identifier of the evaluation',
            'evaluator_id': 'Identifier of the evaluator',
            'hard_objective_result': 'Result of the hard objective evaluation',
            'observation': 'Observations about the evaluation',
            'soft_objective_result': 'Result of the soft objective evaluation',
            'technology_result': 'Result of the technology evaluation',
        },
        'relationships': {},
    },
    'evaluation_control': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'evaluation_date': {'type': 'DATETIME(6)'},
            'response_date': {'type': 'DATETIME(6)'},
            'scheduled_date': {'type': 'DATETIME(6)'},
            'evaluation_id': {'type': 'BIGINT'},
            'evaluation_state_id': {'type': 'BIGINT'},
            'person': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the evaluation control',
            'evaluation_date': 'Date of the evaluation',
            'response_date': 'Date of the response',
            'scheduled_date': 'Scheduled date of the evaluation',
            'evaluation_id': 'Identifier of the evaluation associated with the control',
            'evaluation_state_id': 'Identifier of the state of the evaluation',
            'person': 'Identifier of the person associated with the control',
        },
        'relationships': {
            'evaluation': {'type': 'belongsTo', 'foreign_key': 'evaluation_id'},
            'evaluation_state': {'type': 'belongsTo', 'foreign_key': 'evaluation_state_id'},
            'person': {'type': 'belongsTo', 'foreign_key': 'person'},
        }
    },
    'evaluation_control_notification': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'evaluation_control_id': {'type': 'BIGINT'},
            'notification_id': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the evaluation control notification',
            'evaluation_control_id': 'Identifier of the evaluation control associated with the notification',
            'notification_id': 'Identifier of the notification associated with the evaluation control',
        },
        'relationships': {
            'evaluation_control': {'type': 'belongsTo', 'foreign_key': 'evaluation_control_id'},
            'notification': {'type': 'belongsTo', 'foreign_key': 'notification_id'},
        }
    },
    'evaluation_control_user': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'evaluation_control_id': {'type': 'BIGINT'},
            'user_id': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the evaluation control user',
            'evaluation_control_id': 'Identifier of the evaluation control associated with the user',
            'user_id': 'Identifier of the user associated with the evaluation control',
        },
        'relationships': {
            'evaluation_control': {'type': 'belongsTo', 'foreign_key': 'evaluation_control_id'},
            'user': {'type': 'belongsTo', 'foreign_key': 'user_id'},
        }
    },
    'evaluation_evaluation_technology': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'percentage': {'type': 'INTEGER', 'constraints': 'NOT NULL'},
            'evaluation_id': {'type': 'BIGINT'},
            'evaluation_technology_id': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the evaluation evaluation technology',
            'percentage': 'Percentage of the evaluation technology',
            'evaluation_id': 'Identifier of the evaluation associated with the evaluation technology',
            'evaluation_technology_id': 'Identifier of the evaluation technology associated with the evaluation',
        },
        'relationships': {
            'evaluation': {'type': 'belongsTo', 'foreign_key': 'evaluation_id'},
            'evaluation_technology': {'type': 'belongsTo', 'foreign_key': 'evaluation_technology_id'},
        }
    },
    'evaluation_hard_objetive': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'percentage': {'type': 'INTEGER', 'constraints': 'NOT NULL'},
            'evaluation_id': {'type': 'BIGINT'},
            'hard_objective_id': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the evaluation hard objetive',
            'percentage': 'Percentage of the hard objetive',
            'evaluation_id': 'Identifier of the evaluation associated with the hard objetive',
            'hard_objective_id': 'Identifier of the hard objetive associated with the evaluation',
        },
        'relationships': {
            'evaluation': {'type': 'belongsTo', 'foreign_key': 'evaluation_id'},
            'hard_objective': {'type': 'belongsTo', 'foreign_key': 'hard_objective_id'},
        }
    },
    'evaluation_period': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'anticipation_period': {'type': 'INTEGER'},
            'period_days': {'type': 'INTEGER'},
        },
        'metadata': {
            'id': 'Unique identifier of the evaluation period',
            'anticipation_period': 'Number of days before the evaluation period starts',
            'period_days': 'Number of days in the evaluation period',
        },
        'relationships': {},
    },
    'evaluation_soft_objetive': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'percentage': {'type': 'INTEGER', 'constraints': 'NOT NULL'},
            'evaluation_id': {'type': 'BIGINT'},
            'soft_objective_id': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the evaluation soft objetive',
            'percentage': 'Percentage of the soft objetive',
            'evaluation_id': 'Identifier of the evaluation associated with the soft objetive',
            'soft_objective_id': 'Identifier of the soft objetive associated with the evaluation',
        },
        'relationships': {
            'evaluation': {'type': 'belongsTo', 'foreign_key': 'evaluation_id'},
            'soft_objective': {'type': 'belongsTo', 'foreign_key': 'soft_objective_id'},
        }
    },
    'evaluation_state': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'description': {'type': 'VARCHAR(255)'},
            'name': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the evaluation state',
            'description': 'Description of the evaluation state',
            'name': 'Name of the evaluation state',
        },
        'relationships': {},
    },
    'evaluation_technology': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'description': {'type': 'VARCHAR(255)'},
            'name': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the evaluation technology',
            'description': 'Description of the evaluation technology',
            'name': 'Name of the evaluation technology',
        },
        'relationships': {},
    },
    'hard_objective': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'description': {'type': 'VARCHAR(255)'},
            'enabled': {'type': 'BIT'},
            'name': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the hard objective',
            'description': 'Description of the hard objective',
            'enabled': 'Flag indicating if the hard objective is enabled',
            'name': 'Name of the hard objective',
        },
        'relationships': {},
    },
    'identification_type': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'name': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the identification type',
            'name': 'Name of the identification type',
        },
        'relationships': {},
    },
    'methodology': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'description': {'type': 'VARCHAR(255)'},
            'name': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the methodology',
            'description': 'Description of the methodology',
            'name': 'Name of the methodology',
        },
        'relationships': {},
    },
    'news': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'person_hrss_id': {'type': 'VARCHAR(255)'},
            'evaluation_id': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the news',
            'person_hrss_id': 'Identifier of the HRSS person associated with the news',
            'evaluation_id': 'Identifier of the evaluation associated with the news',
        },
        'relationships': {
            'evaluation': {'type': 'belongsTo', 'foreign_key': 'evaluation_id'},
        }
    },
    'news_news_technology': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'percentage': {'type': 'INTEGER', 'constraints': 'NOT NULL'},
            'news_id': {'type': 'BIGINT'},
            'news_technology_id': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the news news technology',
            'percentage': 'Percentage of the news technology',
            'news_id': 'Identifier of the news associated with the news technology',
            'news_technology_id': 'Identifier of the news technology associated with the news',
        },
        'relationships': {
            'news': {'type': 'belongsTo', 'foreign_key': 'news_id'},
            'news_technology': {'type': 'belongsTo', 'foreign_key': 'news_technology_id'},
        }
    },
    'news_technology': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'description': {'type': 'VARCHAR(255)'},
            'name': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the news technology',
            'description': 'Description of the news technology',
            'name': 'Name of the news technology',
        },
        'relationships': {},
    },
    'notification': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'date': {'type': 'DATETIME(6)'},
            'person_profile_team_ids': {'type': 'VARCHAR(255)'},
            'read_notification': {'type': 'BIT'},
            'subject': {'type': 'VARCHAR(255)'},
            'text': {'type': 'VARCHAR(1000)'},
            'type': {'type': 'VARCHAR(255)'},
            'user_id': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the notification',
            'date': 'Date of the notification',
            'person_profile_team_ids': 'Identifiers of the person profile teams associated with the notification',
            'read_notification': 'Flag indicating if the notification has been read',
            'subject': 'Subject of the notification',
            'text': 'Text of the notification',
            'type': 'Type of the notification',
            'user_id': 'Identifier of the user associated with the notification',
        },
        'relationships': {
            'user': {'type': 'belongsTo', 'foreign_key': 'user_id'},
        }
    },
    'permission': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'permission': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the permission',
            'permission': 'Name of the permission',
        },
        'relationships': {},
    },
    'person': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'admission_date': {'type': 'DATETIME(6)'},
            'email': {'type': 'VARCHAR(255)'},
            'file_number': {'type': 'VARCHAR(255)'},
            'first_superior_id': {'type': 'BIGINT'},
            'gender': {'type': 'VARCHAR(255)'},
            'gyl_id': {'type': 'VARCHAR(255)'},
            'hrss_id': {'type': 'VARCHAR(255)'},
            'identification': {'type': 'VARCHAR(255)'},
            'last_evaluation_days': {'type': 'INTEGER', 'constraints': 'NOT NULL'},
            'last_name': {'type': 'VARCHAR(255)'},
            'name': {'type': 'VARCHAR(255)'},
            'person_active_days': {'type': 'INTEGER', 'constraints': 'NOT NULL'},
            'second_superior_id': {'type': 'BIGINT'},
            'status': {'type': 'BIT'},
            'identification_type_id': {'type': 'BIGINT'},
            'seniority_id': {'type': 'BIGINT'},
            'user_id': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the person',
            'admission_date': 'Date of admission of the person',
            'email': 'Email of the person',
            'file_number': 'File number of the person',
            'first_superior_id': 'Identifier of the first superior of the person',
            'gender': 'Gender of the person',
            'gyl_id': 'Identifier of the GYL associated with the person',
            'hrss_id': 'Identifier of the HRSS associated with the person',
            'identification': 'Identification of the person',
            'last_evaluation_days': 'Number of days since the last evaluation',
            'last_name': 'Last name of the person',
            'name': 'Name of the person',
            'person_active_days': 'Number of active days of the person',
            'second_superior_id': 'Identifier of the second superior of the person',
            'status': 'Status of the person',
            'identification_type_id': 'Identifier of the identification type associated with the person',
            'seniority_id': 'Identifier of the seniority associated with the person',
            'user_id': 'Identifier of the user associated with the person',
        },
        'relationships': {
            'identification_type': {'type': 'belongsTo', 'foreign_key': 'identification_type_id'},
            'seniority': {'type': 'belongsTo', 'foreign_key': 'seniority_id'},
            'user': {'type': 'belongsTo', 'foreign_key': 'user_id'},
        }
    },
    'person_person_technology': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'percentage': {'type': 'INTEGER', 'constraints': 'NOT NULL'},
            'person_id': {'type': 'BIGINT'},
            'person_technology_id': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the person person technology',
            'percentage': 'Percentage of the person technology',
            'person_id': 'Identifier of the person associated with the person technology',
            'person_technology_id': 'Identifier of the person technology associated with the person',
        },
        'relationships': {
            'person': {'type': 'belongsTo', 'foreign_key': 'person_id'},
            'person_technology': {'type': 'belongsTo', 'foreign_key': 'person_technology_id'},
        }
    },
    'person_project_profile': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'person_id': {'type': 'BIGINT'},
            'profile_id': {'type': 'BIGINT'},
            'project_id': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the person project profile',
            'person_id': 'Identifier of the person associated with the profile',
            'profile_id': 'Identifier of the profile associated with the person',
            'project_id': 'Identifier of the project associated with the profile',
        },
        'relationships': {
            'person': {'type': 'belongsTo', 'foreign_key': 'person_id'},
            'profile': {'type': 'belongsTo', 'foreign_key': 'profile_id'},
            'project': {'type': 'belongsTo', 'foreign_key': 'project_id'},
        }
    },
    'person_technology': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'description': {'type': 'VARCHAR(255)'},
            'name': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the person technology',
            'description': 'Description of the person technology',
            'name': 'Name of the person technology',
        },
        'relationships': {},
    },
    'profile': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'name': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the profile',
            'name': 'Name of the profile',
        },
        'relationships': {},
    },
    'project': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'client_name': {'type': 'VARCHAR(255)'},
            'end_date': {'type': 'DATETIME(6)'},
            'name': {'type': 'VARCHAR(255)'},
            'project_code': {'type': 'VARCHAR(255)'},
            'start_date': {'type': 'DATETIME(6)'},
            'project_difficulty_id': {'type': 'BIGINT'},
            'project_status_id': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the project',
            'client_name': 'Name of the client associated with the project',
            'end_date': 'End date of the project',
            'name': 'Name of the project',
            'project_code': 'Code of the project',
            'start_date': 'Start date of the project',
            'project_difficulty_id': 'Identifier of the project difficulty associated with the project',
            'project_status_id': 'Identifier of the project status associated with the project',
        },
        'relationships': {
            'project_difficulty': {'type': 'belongsTo', 'foreign_key': 'project_difficulty_id'},
            'project_status': {'type': 'belongsTo', 'foreign_key': 'project_status_id'},
        }
    },
    'project_project_technology': {
        'columns': {
            'project_id': {'type': 'BIGINT', 'constraints': 'PK NOT NULL'},
            'project_technology_id': {'type': 'BIGINT', 'constraints': 'PK NOT NULL'},
        },
        'metadata': {
            'project_id': 'Identifier of the project associated with the project technology',
            'project_technology_id': 'Identifier of the project technology associated with the project',
        },
        'relationships': {
            'project': {'type': 'belongsTo', 'foreign_key': 'project_id'},
            'project_technology': {'type': 'belongsTo', 'foreign_key': 'project_technology_id'},
        }
    },
    'project_difficulty': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'name': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the project difficulty',
            'name': 'Name of the project difficulty',
        },
        'relationships': {},
    },
    'project_status': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'name': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the project status',
            'name': 'Name of the project status',
        },
        'relationships': {},
    },
    'project_technology': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'description': {'type': 'VARCHAR(255)'},
            'name': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the project technology',
            'description': 'Description of the project technology',
            'name': 'Name of the project technology',
        },
        'relationships': {},
    },
    'role': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'name': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the role',
            'name': 'Name of the role',
        },
        'relationships': {},
    },
    'role_permissions': {
        'columns': {
            'role_id': {'type': 'BIGINT', 'constraints': 'PK NOT NULL'},
            'permissions_id': {'type': 'BIGINT', 'constraints': 'PK NOT NULL'},
        },
        'metadata': {
            'role_id': 'Identifier of the role associated with the permissions',
            'permissions_id': 'Identifier of the permissions associated with the role',
        },
        'relationships': {
            'role': {'type': 'belongsTo', 'foreign_key': 'role_id'},
            'permission': {'type': 'belongsTo', 'foreign_key': 'permissions_id'},
        }
    },
    'seniority': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'description': {'type': 'VARCHAR(255)'},
            'name': {'type': 'VARCHAR(255)'},
            'evaluation_period_id': {'type': 'BIGINT'},
        },
        'metadata': {
            'id': 'Unique identifier of the seniority',
            'description': 'Description of the seniority',
            'name': 'Name of the seniority',
            'evaluation_period_id': 'Identifier of the evaluation period associated with the seniority',
        },
        'relationships': {
            'evaluation_period': {'type': 'belongsTo', 'foreign_key': 'evaluation_period_id'},
        }
    },
    'soft_objective': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'description': {'type': 'VARCHAR(255)'},
            'enabled': {'type': 'BIT'},
            'name': {'type': 'VARCHAR(255)'},
            'type_id': {'type': 'BIGINT'},
            'seniority_id': {'type': 'BIGINT'}
        },
        'metadata': {
            'id': 'Unique identifier of the soft objective',
            'description': 'Description of the soft objective',
            'enabled': 'Flag indicating if the soft objective is enabled',
            'name': 'Name of the soft objective',
            'type_id': 'Identifier of the type of the soft objective',
            'seniority_id': 'Identifier of the seniority associated with the soft objective',
        },
        'relationships': {
            'soft_objective_type': {'type': 'belongsTo', 'foreign_key': 'type_id'},
            'seniority': {'type': 'belongsTo', 'foreign_key': 'seniority_id'},
        }
    },
    'soft_objective_type': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'name': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the soft objective type',
            'name': 'Name of the soft objective type',
        },
        'relationships': {},
    },
    'user': {
        'columns': {
            'id': {'type': 'BIGINT', 'constraints': 'PK AI NOT NULL'},
            'password': {'type': 'VARCHAR(255)'},
            'username': {'type': 'VARCHAR(255)'},
        },
        'metadata': {
            'id': 'Unique identifier of the user',
            'password': 'Password of the user',
            'username': 'Username of the user',
        },
        'relationships': {},
    },
    'user_role': {
        'columns': {
            'user_id': {'type': 'BIGINT', 'constraints': 'PK NOT NULL'},
            'role_id': {'type': 'BIGINT', 'constraints': 'PK NOT NULL'},
        },
        'metadata': {
            'user_id': 'Identifier of the user associated with the role',
            'role_id': 'Identifier of the role associated with the user',
        },
        'relationships': {
            'user': {'type': 'belongsTo', 'foreign_key': 'user_id'},
            'role': {'type': 'belongsTo', 'foreign_key': 'role_id'},
        }
    },
}
