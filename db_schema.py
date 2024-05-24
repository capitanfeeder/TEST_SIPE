# Diccionario SIPE
sql10708993 = {
    "address": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la dirección)",
        "department": "VARCHAR(255) (Departamento de la dirección)",
        "floor": "VARCHAR(255) (Piso de la dirección)",
        "number": "VARCHAR(255) (Número de la dirección)",
        "street": "VARCHAR(255) (Calle de la dirección)",
        "locality_id": "BIGINT FK (Identificador de la localidad a la que pertenece la dirección)"
    },
    "country": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del país)",
        "name": "VARCHAR(255) (Nombre del país)"
    },
    "evaluation": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la evaluación)",
        "evaluator_id": "BIGINT (Identificador del evaluador)",
        "hard_objective_result": "INTEGER NOT NULL (Resultado del objetivo duro de la evaluación)",
        "observation": "VARCHAR(255) (Observaciones de la evaluación)",
        "soft_objective_result": "INTEGER NOT NULL (Resultado del objetivo blando de la evaluación)",
        "technology_result": "INTEGER NOT NULL (Resultado de la evaluación de tecnología)"
    },
    "evaluation_control": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del control de evaluación)",
        "evaluation_date": "DATETIME(6) (Fecha de la evaluación)",
        "response_date": "DATETIME(6) (Fecha de respuesta de la evaluación)",
        "scheduled_date": "DATETIME(6) (Fecha programada de la evaluación)",
        "evaluation_id": "BIGINT FK (Identificador de la evaluación asociada al control)",
        "evaluation_state_id": "BIGINT FK (Identificador del estado de la evaluación)",
        "person_profile_team_id": "BIGINT FK (Identificador del perfil de persona del equipo asociado al control)"
    },
    "evaluation_control_notification": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la notificación del control de evaluación)",
        "evaluation_control_id": "BIGINT FK (Identificador del control de evaluación asociado a la notificación)",
        "notification_id": "BIGINT FK (Identificador de la notificación asociada al control)"
    },
    "evaluation_control_user": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del usuario del control de evaluación)",
        "evaluation_control_id": "BIGINT FK (Identificador del control de evaluación asociado al usuario)",
        "user_id": "BIGINT FK (Identificador del usuario asociado al control)"
    },
    "evaluation_evaluation_technology": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la evaluación de tecnología)",
        "percentage": "INTEGER NOT NULL (Porcentaje de la evaluación de tecnología)",
        "evaluation_id": "BIGINT FK (Identificador de la evaluación asociada a la evaluación de tecnología)",
        "evaluation_technology_id": "BIGINT FK (Identificador de la tecnología evaluada)"
    },
    "evaluation_hard_objetive": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del objetivo duro de la evaluación)",
        "percentage": "INTEGER NOT NULL (Porcentaje del objetivo duro de la evaluación)",
        "evaluation_id": "BIGINT FK (Identificador de la evaluación asociada al objetivo duro)",
        "hard_objective_id": "BIGINT FK (Identificador del objetivo duro)"
    },
    "evaluation_period": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del período de evaluación)",
        "anticipation_period": "INTEGER (Período de anticipación de la evaluación)",
        "period_days": "INTEGER (Días del período de evaluación)"
    },
    "evaluation_soft_objetive": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del objetivo blando de la evaluación)",
        "percentage": "INTEGER NOT NULL (Porcentaje del objetivo blando de la evaluación)",
        "evaluation_id": "BIGINT FK (Identificador de la evaluación asociada al objetivo blando)",
        "soft_objective_id": "BIGINT FK (Identificador del objetivo blando)"
    },
    "evaluation_state": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del estado de la evaluación)",
        "description": "VARCHAR(255) (Descripción del estado de la evaluación)",
        "name": "VARCHAR(255) (Nombre del estado de la evaluación)"
    },
    "evaluation_technology": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la tecnología evaluada)",
        "description": "VARCHAR(255) (Descripción de la tecnología evaluada)",
        "name": "VARCHAR(255) (Nombre de la tecnología evaluada)"
    },
    "hard_objective": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del objetivo duro)",
        "description": "VARCHAR(255) (Descripción del objetivo duro)",
        "name": "VARCHAR(255) (Nombre del objetivo duro)"
    },
    "identification_type": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del tipo de identificación)",
        "name": "VARCHAR(255) (Nombre del tipo de identificación)"
    },
    "language": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del idioma)",
        "name": "VARCHAR(255) (Nombre del idioma)"
    },
    "language_level": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del nivel de idioma)",
        "name": "VARCHAR(255) (Nombre del nivel de idioma)"
    },
    "locality": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la localidad)",
        "name": "VARCHAR(255) (Nombre de la localidad)",
        "province_id": "BIGINT FK (Identificador de la provincia a la que pertenece la localidad)"
    },
    "methodology": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la metodología)",
        "description": "VARCHAR(255) (Descripción de la metodología)",
        "name": "VARCHAR(255) (Nombre de la metodología)"
    },
    "notification": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la notificación)",
        "date": "DATETIME(6) (Fecha de la notificación)",
        "subject": "VARCHAR(255) (Asunto de la notificación)",
        "text": "VARCHAR(255) (Texto de la notificación)",
        "type": "VARCHAR(255) (Tipo de notificación)",
        "person_profile_id": "BIGINT FK (Identificador del perfil de persona asociado a la notificación)"
    },
    "permission": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del permiso)",
        "permission": "VARCHAR(255) (Nombre del permiso)"
    },
    "person": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la persona)",
        "admission_date": "DATETIME(6) (Fecha de ingreso de la persona)",
        "allotted_time": "INTEGER NOT NULL (Tiempo asignado a la persona)",
        "cc_code": "VARCHAR(255) (Código de área de la persona)",
        "cuil_cuit": "VARCHAR(255) (CUIL/CUIT de la persona)",
        "egress_date": "DATETIME(6) (Fecha de egreso de la persona)",
        "email": "VARCHAR(255) (Correo electrónico de la persona)",
        "file_number": "VARCHAR(255) (Número de legajo de la persona)",
        "identification": "VARCHAR(255) (Número de identificación de la persona)",
        "last_name": "VARCHAR(255) (Apellido de la persona)",
        "name": "VARCHAR(255) (Nombre de la persona)",
        "status": "BIT (Estado de la persona)",
        "total_active_days": "INTEGER NOT NULL (Días activos de la persona)",
        "address_id": "BIGINT FK (Identificador de la dirección asociada a la persona)",
        "identification_type_id": "BIGINT FK (Identificador del tipo de identificación asociado a la persona)",
        "user_id": "BIGINT FK (Identificador del usuario asociado a la persona)"
    },
    "person_person_technology": {
        "person_id": "BIGINT FK (Identificador de la persona asociada a la tecnología)",
        "person_technology_id": "BIGINT FK (Identificador de la tecnología asociada a la persona)"
    },
    "person_language": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del idioma de la persona)",
        "language_id": "BIGINT FK (Identificador del idioma asociado a la persona)",
        "language_level_id": "BIGINT FK (Identificador del nivel de idioma asociado a la persona)",
        "person_id": "BIGINT FK (Identificador de la persona asociada al idioma)"
    },
    "person_profile": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del perfil de persona)",
        "status": "BIT (Estado del perfil de persona)",
        "person_id": "BIGINT FK (Identificador de la persona asociada al perfil)",
        "profile_id": "BIGINT FK (Identificador del perfil asociado a la persona)"
    },
    "person_profile_team": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del perfil de persona del equipo)",
        "dedication": "INTEGER (Dedicación del perfil de persona del equipo)",
        "team_entry_date": "DATETIME(6) (Fecha de ingreso al equipo del perfil de persona)",
        "team_exit_date": "DATETIME(6) (Fecha de egreso del equipo del perfil de persona)",
        "person_profile_id": "BIGINT FK (Identificador del perfil de persona asociado al equipo)",
        "team_id": "BIGINT FK (Identificador del equipo asociado al perfil de persona)"
    },
    "person_technology": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la tecnología de la persona)",
        "description": "VARCHAR(255) (Descripción de la tecnología de la persona)",
        "name": "VARCHAR(255) (Nombre de la tecnología de la persona)"
    },
    "profession": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la profesión)",
        "description": "VARCHAR(255) (Descripción de la profesión)",
        "name": "VARCHAR(255) (Nombre de la profesión)"
    },
    "profile": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del perfil)",
        "description": "VARCHAR(255) (Descripción del perfil)",
        "name": "VARCHAR(255) (Nombre del perfil)",
        "profession_id": "BIGINT FK (Identificador de la profesión asociada al perfil)",
        "seniority_id": "BIGINT FK (Identificador de la antigüedad asociada al perfil)",
        "speciality_id": "BIGINT FK (Identificador de la especialidad asociada al perfil)"
    },
    "project": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del proyecto)",
        "description": "VARCHAR(255) (Descripción del proyecto)",
        "end_date": "DATETIME(6) (Fecha de finalización del proyecto)",
        "name": "VARCHAR(255) (Nombre del proyecto)",
        "project_leader_id": "BIGINT (Identificador del líder del proyecto)",
        "start_date": "DATETIME(6) (Fecha de inicio del proyecto)",
        "supervisor_code": "VARCHAR(255) (Código del supervisor del proyecto)",
        "methodology_id": "BIGINT FK (Identificador de la metodología asociada al proyecto)",
        "project_difficulty_id": "BIGINT FK (Identificador de la dificultad del proyecto)",
        "project_status_id": "BIGINT FK (Identificador del estado del proyecto)"
    },
    "project_project_technology": {
        "project_id": "BIGINT FK (Identificador del proyecto asociado a la tecnología)",
        "project_technology_id": "BIGINT FK (Identificador de la tecnología asociada al proyecto)"
    },
    "project_difficulty": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la dificultad del proyecto)",
        "name": "VARCHAR(255) (Nombre de la dificultad del proyecto)"
    },
    "project_status": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del estado del proyecto)",
        "name": "VARCHAR(255) (Nombre del estado del proyecto)"
    },
    "project_technology": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la tecnología del proyecto)",
        "description": "VARCHAR(255) (Descripción de la tecnología del proyecto)",
        "name": "VARCHAR(255) (Nombre de la tecnología del proyecto)"
    },
    "province": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la provincia)",
        "name": "VARCHAR(255) (Nombre de la provincia)",
        "country_id": "BIGINT FK (Identificador del país al que pertenece la provincia)"
    },
    "role": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del rol)",
        "name": "VARCHAR(255) (Nombre del rol)"
    },
    "role_permissions": {
        "role_id": "BIGINT FK (Identificador del rol asociado a los permisos)",
        "permissions_id": "BIGINT FK (Identificador de los permisos asociados al rol)"
    },
    "seniority": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la antigüedad)",
        "description": "VARCHAR(255) (Descripción de la antigüedad)",
        "name": "VARCHAR(255) (Nombre de la antigüedad. Contenido de la columna: Trainee, Junior, Semisenior, Senior)",
        "evaluation_period_id": "BIGINT FK (Identificador del período de evaluación asociado a la antigüedad)"
    },
    "soft_objective": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del objetivo blando)",
        "description": "VARCHAR(255) (Descripción del objetivo blando)",
        "name": "VARCHAR(255) (Nombre del objetivo blando)",
        "type_id": "BIGINT FK (Identificador del tipo del objetivo blando)"
    },
    "soft_objective_type": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del tipo del objetivo blando)",
        "name": "VARCHAR(255) (Nombre del tipo del objetivo blando)"
    },
    "speciality": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la especialidad)",
        "description": "VARCHAR(255) (Descripción de la especialidad)",
        "name": "VARCHAR(255) (Nombre de la especialidad)"
    },
    "team": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del equipo)",
        "team_code": "VARCHAR(255) (Código del equipo)",
        "project_id": "BIGINT FK (Identificador del proyecto asociado al equipo)",
        "team_type_id": "BIGINT FK (Identificador del tipo de equipo)"
    },
    "team_team_technology": {
        "team_id": "BIGINT FK (Identificador del equipo asociado a la tecnología)",
        "team_technology_id": "BIGINT FK (Identificador de la tecnología asociada al equipo)"
    },
    "team_technology": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la tecnología del equipo)",
        "description": "VARCHAR(255) (Descripción de la tecnología del equipo)",
        "name": "VARCHAR(255) (Nombre de la tecnología del equipo)"
    },
    "team_type": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del tipo de equipo)",
        "description": "VARCHAR(255) (Descripción del tipo de equipo)",
        "name": "VARCHAR(255) (Nombre del tipo de equipo)"
    },
    "user": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del usuario)",
        "password": "VARCHAR(255) (Contraseña del usuario)",
        "username": "VARCHAR(255) (Nombre de usuario)"
    },
    "user_role": {
        "user_id": "BIGINT FK (Identificador del usuario asociado al rol)",
        "role_id": "BIGINT FK (Identificador del rol asociado al usuario)"
    },
    "work_license": {
        "id": "BIGINT PK AI NOT NULL (Identificador único de la licencia de trabajo)",
        "days": "INTEGER NOT NULL (Días de la licencia de trabajo)",
        "description": "VARCHAR(255) (Descripción de la licencia de trabajo)",
        "end_date": "DATETIME(6) (Fecha de finalización de la licencia de trabajo)",
        "start_date": "DATETIME(6) (Fecha de inicio de la licencia de trabajo)",
        "status": "BIT (Estado de la licencia de trabajo)",
        "person_id": "BIGINT FK (Identificador de la persona asociada a la licencia de trabajo)",
        "work_license_type_id": "BIGINT FK (Identificador del tipo de licencia de trabajo)"
    },
    "work_license_type": {
        "id": "BIGINT PK AI NOT NULL (Identificador único del tipo de licencia de trabajo)",
        "name": "VARCHAR(255) (Nombre del tipo de licencia de trabajo)"
    }
}