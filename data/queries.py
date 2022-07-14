from data import data_manager


def connect(kereso):
    if kereso == 0:
        return data_manager.execute_select("select * from piktorfiai ORDER BY type_id DESC;")
    else:
        return data_manager.execute_select("""
            select * from piktorfiai WHERE type_id = %(kereso)s;
        """, {'kereso': kereso})


def index_limit():
    return data_manager.execute_select("SELECT * FROM piktorfiai LIMIT 3")

