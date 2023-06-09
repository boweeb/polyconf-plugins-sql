# import sqlite3
# from pathlib import Path
#
# from k8scfg.config import base
#
#
# def create_connection(path):
#     connection = None
#     try:
#         connection = sqlite3.connect(path)
#         print("Connection to SQLite DB successful")
#     except sqlite3.Error as e:
#         print(f"The error '{e}' occurred")
#
#     return connection
#
#
# def hydrate(data: base.Data) -> base.Data:
#     # connection = create_connection(Path.home() / ".k8scfg.db")
#     # cursor = connection.cursor()
#     # cursor.execute(
#     #     "SELECT id, lorem FROM ipsum"
#     # )
#     # result = cursor.fetchall()
#     return data
