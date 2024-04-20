from View.view import *;
from View.menu import *;

v = View()

# menu = Menu("Записная книжка. v 1.0", [
#             MenuItem(1, "Новая запись"),
#             MenuItem(2, "Просмотр",
#                 Menu("Просмотр", [
#                     MenuItem(3, "Посмотреть последнюю"),
#                     MenuItem(4, "Посмотреть по дате"),
#                     MenuItem(5, "Посмотреть все")
#                 ])),
#             MenuItem(6, "Изменение"),
#             MenuItem(7, "Удаление",
#                 Menu("Удаление", [
#                     MenuItem(8, "Последнюю"),
#                     MenuItem(9, "Удалить по дате")
#                 ]))
#         ])

# v.cls()
# print(menu.run())


from Model.note import *;
from Model.noteitem import *;
from Model.fileio import *;

note = Note()
note.add(NoteItem(1, "rec 1", "Заметка для теста № 1"))
note.add(NoteItem(2, "rec 2", "Record N2 of 2"))
print(note)

f = FileCSV("test.csv")
f.save(note)

