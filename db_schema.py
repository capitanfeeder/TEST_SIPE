# Diccionario SIPE
defaultdb = {
    "address": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the address)",
        "department": "VARCHAR(255) (Department of the address)",
        "floor": "VARCHAR(255) (Floor of the address)",
        "number": "VARCHAR(255) (Number of the address)",
        "street": "VARCHAR(255) (Street of the address)",
        "locality_id": "BIGINT FK (Identifier of the locality to which the address belongs)"
    }
    ,
    "country": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the country)",
        "name": "VARCHAR(255) (Name of the country)"
    },
    "evaluation": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the evaluation)",
        "evaluator_id": "BIGINT (Identifier of the evaluator)",
        "hard_objective_result": "INTEGER NOT NULL (Result of the hard objective of the evaluation)",
        "observation": "VARCHAR(255) (Observations of the evaluation)",
        "soft_objective_result": "INTEGER NOT NULL (Result of the soft objective of the evaluation)",
        "technology_result": "INTEGER NOT NULL (Result of the technology evaluation)"
    },

    "evaluation_control": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the evaluation control)",
        "evaluation_date": "DATETIME(6) (Date of the evaluation)",
        "response_date": "DATETIME(6) (Response date of the evaluation)",
        "scheduled_date": "DATETIME(6) (Scheduled date of the evaluation)",
        "evaluation_id": "BIGINT FK (Identifier of the evaluation associated with the control)",
        "evaluation_state_id": "BIGINT FK (Identifier of the evaluation state)",
        "person_profile_team_id": "BIGINT FK (Identifier of the person profile of the team associated with the control)"
    },

    "evaluation_control_notification": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the evaluation control notification)",
        "evaluation_control_id": "BIGINT FK (Identifier of the evaluation control associated with the notification)",
        "notification_id": "BIGINT FK (Identifier of the notification associated with the control)"
    },

    "evaluation_control_user": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the user of the evaluation control)",
        "evaluation_control_id": "BIGINT FK (Identifier of the evaluation control associated with the user)",
        "user_id": "BIGINT FK (Identifier of the user associated with the control)"
    },

    "evaluation_evaluation_technology": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the technology evaluation)",
        "percentage": "INTEGER NOT NULL (Percentage of the technology evaluation)",
        "evaluation_id": "BIGINT FK (Identifier of the evaluation associated with the technology evaluation)",
        "evaluation_technology_id": "BIGINT FK (Identifier of the evaluated technology)"
    },

    "evaluation_hard_objetive": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the hard objective of the evaluation)",
        "percentage": "INTEGER NOT NULL (Percentage of the hard objective of the evaluation)",
        "evaluation_id": "BIGINT FK (Identifier of the evaluation associated with the hard objective)",
        "hard_objective_id": "BIGINT FK (Identifier of the hard objective)"
    },

    "evaluation_period": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the evaluation period)",
        "anticipation_period": "INTEGER (Period of anticipation of the evaluation)",
        "period_days": "INTEGER (Days of the evaluation period)"
    },

    "evaluation_soft_objetive": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the soft objective of the evaluation)",
        "percentage": "INTEGER NOT NULL (Percentage of the soft objective of the evaluation)",
        "evaluation_id": "BIGINT FK (Identifier of the evaluation associated with the soft objective)",
        "soft_objective_id": "BIGINT FK (Identifier of the soft objective)"
    },

    "evaluation_state": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the evaluation state)",
        "description": "VARCHAR(255) (Description of the evaluation state)",
        "name": "VARCHAR(255) (Name of the evaluation state)"
    },

    "evaluation_technology": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the evaluated technology)",
        "description": "VARCHAR(255) (Description of the evaluated technology)",
        "name": "VARCHAR(255) (Name of the evaluated technology)"
    },

    "hard_objective": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the hard objective)",
        "description": "VARCHAR(255) (Description of the hard objective)",
        "name": "VARCHAR(255) (Name of the hard objective)"
    },

    "identification_type": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the identification type)",
        "name": "VARCHAR(255) (Name of the identification type)"
    },

    "language": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the language)",
        "name": "VARCHAR(255) (Name of the language)"
    },
    "language_level": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the language level)",
        "name": "VARCHAR(255) (Name of the language level)"
    },

    "locality": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the locality)",
        "name": "VARCHAR(255) (Name of the locality)",
        "province_id": "BIGINT FK (Identifier of the province to which the locality belongs)"
    },

    "methodology": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the methodology)",
        "description": "VARCHAR(255) (Description of the methodology)",
        "name": "VARCHAR(255) (Name of the methodology)"
    },

    "notification": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the notification)",
        "date": "DATETIME(6) (Date of the notification)",
        "subject": "VARCHAR(255) (Subject of the notification)",
        "text": "VARCHAR(255) (Text of the notification)",
        "type": "VARCHAR(255) (Type of notification)",
        "person_profile_id": "BIGINT FK (Identifier of the person profile associated with the notification)"
    },

    "permission": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the permission)",
        "permission": "VARCHAR(255) (Name of the permission)"
    },

    "person": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the person)",
        "admission_date": "DATETIME(6) (Date of admission of the person)",
        "allotted_time": "INTEGER NOT NULL (Time allotted to the person)",
        "cc_code": "VARCHAR(255) (Area code of the person)",
        "cuil_cuit": "VARCHAR(255) (CUIL/CUIT of the person)",
        "egress_date": "DATETIME(6) (Date of egress of the person)",
        "email": "VARCHAR(255) (Email of the person)",
        "file_number": "VARCHAR(255) (File number of the person)",
        "identification": "VARCHAR(255) (Identification number of the person)",
        "last_name": "VARCHAR(255) (Last name of the person)",
        "name": "VARCHAR(255) (Name of the person)",
        "status": "BIT (Status of the person)",
        "total_active_days": "INTEGER NOT NULL (Total active days of the person)",
        "address_id": "BIGINT FK (Identifier of the address associated with the person)",
        "identification_type_id": "BIGINT FK (Identifier of the identification type associated with the person)",
        "user_id": "BIGINT FK (Identifier of the user associated with the person)"
    },

    "person_person_technology": {
        "person_id": "BIGINT FK (Identifier of the person associated with the technology)",
        "person_technology_id": "BIGINT FK (Identifier of the technology associated with the person)"
    },

    "person_language": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the language of the person)",
        "language_id": "BIGINT FK (Identifier of the language associated with the person)",
        "language_level_id": "BIGINT FK (Identifier of the language level associated with the person)",
        "person_id": "BIGINT FK (Identifier of the person associated with the language)"
    },

    "person_profile": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the person profile)",
        "status": "BIT (Status of the person profile)",
        "person_id": "BIGINT FK (Identifier of the person associated with the profile)",
        "profile_id": "BIGINT FK (Identifier of the profile associated with the person)"
    },

    "person_profile_team": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the person profile of the team)",
        "dedication": "INTEGER (Dedication of the person profile of the team)",
        "team_entry_date": "DATETIME(6) (Date of entry to the team of the person profile)",
        "team_exit_date": "DATETIME(6) (Date of exit from the team of the person profile)",
        "person_profile_id": "BIGINT FK (Identifier of the person profile associated with the team)",
        "team_id": "BIGINT FK (Identifier of the team associated with the person profile)"
    },

    "person_technology": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the technology of the person)",
        "description": "VARCHAR(255) (Description of the technology of the person)",
        "name": "VARCHAR(255) (Name of the technology of the person)"
    },

    "profession": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the profession)",
        "description": "VARCHAR(255) (Description of the profession)",
        "name": "VARCHAR(255) (Name of the profession)"
    },

    "profile": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the profile)",
        "description": "VARCHAR(255) (Description of the profile)",
        "name": "VARCHAR(255) (Name of the profile)",
        "profession_id": "BIGINT FK (Identifier of the profession associated with the profile)",
        "seniority_id": "BIGINT FK (Identifier of the seniority associated with the profile)",
        "speciality_id": "BIGINT FK (Identifier of the specialty associated with the profile)"
    },

    "project": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the project)",
        "description": "VARCHAR(255) (Description of the project)",
        "end_date": "DATETIME(6) (End date of the project)",
        "name": "VARCHAR(255) (Name of the project)",
        "project_leader_id": "BIGINT (Identifier of the leader of the project)",
        "start_date": "DATETIME(6) (Start date of the project)",
        "supervisor_code": "VARCHAR(255) (Code of the supervisor of the project)",
        "methodology_id": "BIGINT FK (Identifier of the methodology associated with the project)",
        "project_difficulty_id": "BIGINT FK (Identifier of the difficulty of the project)",
        "project_status_id": "BIGINT FK (Identifier of the status of the project)"
    },
    "project_project_technology": {
        "project_id": "BIGINT FK (Project identifier associated with the technology)",
        "project_technology_id": "BIGINT FK (Technology identifier associated with the project)"
    },

    "project_difficulty": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the project difficulty)",
        "name": "VARCHAR(255) (Name of the project difficulty)"
    },

    "project_status": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the project status)",
        "name": "VARCHAR(255) (Name of the project status)"
    },

    "project_technology": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the project technology)",
        "description": "VARCHAR(255) (Description of the project technology)",
        "name": "VARCHAR(255) (Name of the project technology)"
    },

    "province": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the province)",
        "name": "VARCHAR(255) (Name of the province)",
        "country_id": "BIGINT FK (Identifier of the country to which the province belongs)"
    },

    "role": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the role)",
        "name": "VARCHAR(255) (Name of the role)"
    },

    "role_permissions": {
        "role_id": "BIGINT FK (Identifier of the role associated with the permissions)",
        "permissions_id": "BIGINT FK (Identifier of the permissions associated with the role)"
    },

    "seniority": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the seniority)",
        "description": "VARCHAR(255) (Description of the seniority)",
        "name": "VARCHAR(255) (Name of the seniority. Column content: Trainee, Junior, Semisenior, Senior)",
        "evaluation_period_id": "BIGINT FK (Identifier of the evaluation period associated with the seniority)"
    },

    "soft_objective": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the soft objective)",
        "description": "VARCHAR(255) (Description of the soft objective)",
        "name": "VARCHAR(255) (Name of the soft objective)",
        "type_id": "BIGINT FK (Identifier of the type of the soft objective)"
    },

    "soft_objective_type": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the type of the soft objective)",
        "name": "VARCHAR(255) (Name of the type of the soft objective)"
    },

    "speciality": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the specialty)",
        "description": "VARCHAR(255) (Description of the specialty)",
        "name": "VARCHAR(255) (Name of the specialty)"
    },

    "team": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the team)",
        "team_code": "VARCHAR(255) (Team code)",
        "project_id": "BIGINT FK (Identifier of the project associated with the team)",
        "team_type_id": "BIGINT FK (Identifier of the type of team)"
    },

    "team_team_technology": {
        "team_id": "BIGINT FK (Identifier of the team associated with the technology)",
        "team_technology_id": "BIGINT FK (Identifier of the technology associated with the team)"
    },

    "team_technology": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the team technology)",
        "description": "VARCHAR(255) (Description of the team technology)",
        "name": "VARCHAR(255) (Name of the team technology)"
    },

    "team_type": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the type of team)",
        "description": "VARCHAR(255) (Description of the type of team)",
        "name": "VARCHAR(255) (Name of the type of team)"
    },

    "user": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the user)",
        "password": "VARCHAR(255) (User password)",
        "username": "VARCHAR(255) (Username)"
    },

    "user_role": {
        "user_id": "BIGINT FK (Identifier of the user associated with the role)",
        "role_id": "BIGINT FK (Identifier of the role associated with the user)"
    },

    "work_license": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the work license)",
        "days": "INTEGER NOT NULL (Days of the work license)",
        "description": "VARCHAR(255) (Description of the work license)",
        "end_date": "DATETIME(6) (Work license end date)",
        "start_date": "DATETIME(6) (Work license start date)",
        "status": "BIT (Work license status)",
        "person_id": "BIGINT FK (Identifier of the person associated with the work license)",
        "work_license_type_id": "BIGINT FK (Identifier of the type of work license)"
    },

    "work_license_type": {
        "id": "BIGINT PK AI NOT NULL (Unique identifier of the type of work license)",
        "name": "VARCHAR(255) (Name of the type of work license)"
    }
}