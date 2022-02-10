from replace_id import IdReplacer


class MyReplacer(IdReplacer):
    def _set_up(self, connection, *args, **kwargs):
        utils = kwargs['utils']
        rows = kwargs['rows']
        sql = ""
        utils.execute(connection, sql)


MyReplacer().execute(
    params={
        'host': 'localhost',
        'user': 'postgres',
        'password': 'postgres',
        'schema': 'public',
        'db_name': 'test',
        'autocommit': True,
        'ignored_tables': ['table_1', 'table_2'],
    }
)