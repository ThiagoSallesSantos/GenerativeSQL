from sqlalchemy import inspect, Engine

def get_database_struct(engine: Engine):
    database_info = inspect(engine)
    fix_schema = engine.dialect.default_schema_name

    database_struct = dict({})
    for table in database_info.get_table_names(fix_schema):
        database_struct[table] = {
            "columns": database_info.get_columns(table),
            "primary_keys": database_info.get_pk_constraint(table),
            "foreign_keys": database_info.get_foreign_keys(table),
            "unique_constraints": database_info.get_unique_constraints(table),
            "indexes": database_info.get_indexes(table),
            "check_constraints": database_info.get_check_constraints(table),
            "comments": database_info.get_table_comment(table) if engine.dialect.supports_comments else None,
        }

    return database_struct