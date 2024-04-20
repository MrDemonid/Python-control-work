from View.menu import *
from View.ansi import *
from View.view import *
from Model.menucmd import *
from Model.note import *
from Model.noteitem import *
from Model.fileio import *


class Controller:
    menu: Menu
    note: Note
    file: FileCSV = None
    view: View = None

    def __init__(self) -> None:
        self.menu = Menu("Записная книжка. v 1.0", [
                        MenuItem(mCmd.CREATE_REC, "Новая запись"),
                        MenuItem(mCmd.VIEW_REC, "Просмотр записей",
                                Menu("Просмотр записей", [
                                    MenuItem(mCmd.VIEW_LAST, "Посмотреть последнюю"),
                                    MenuItem(mCmd.VIEW_FROM_INDEX, "Выбрать запись"),
                                    MenuItem(mCmd.VIEW_FROM_DATE, "Просмотр по дате"),
                                    MenuItem(mCmd.VIEW_ALL, "Просмотр всех записей")
                                ])),
                        MenuItem(mCmd.EDIT_REC, "Редактировать запись"),
                        MenuItem(mCmd.DELETE_REC, "Удаление записей",
                                Menu("Удаление записей", [
                                    MenuItem(mCmd.DELETE_LAST, "Удалить последнюю"),
                                    MenuItem(mCmd.DELETE_FROM_INDEX, "Выбрать запись"),
                                    MenuItem(mCmd.DELETE_FROM_DATE, "Удалить по дате")
                                ]))
                        ])
        
        self.view = View()
        self.file = FileCSV('notes.csv')
        self.note = self.file.load()


    def run(self):
        while True:
            n = self.menu.run()
            if n == 0:
                break
            self.proceed_cmd(n)

    #
    # Обработчик главного меню
    #
    def proceed_cmd(self, cmd: int):
        if cmd == mCmd.CREATE_REC:
            self.create_record()                # добавить новую запись

        elif cmd == mCmd.VIEW_LAST:
            self.view_last()                    # посмотреть последнюю запись

        elif cmd == mCmd.VIEW_FROM_INDEX:
            self.view_one()                     # посмотреть выбранную запись

        elif cmd == mCmd.VIEW_FROM_DATE:
            self.view_date()                    # просмотр по временному промежутку

        elif cmd == mCmd.VIEW_ALL:              # просмотр всех записей
            self.view_all()

        elif cmd == mCmd.EDIT_REC:              # изменения записи
            self.edit_rec()

        elif cmd == mCmd.DELETE_LAST:           # удаление последней записи
            self.delete_last()

        elif cmd == mCmd.DELETE_FROM_INDEX:
            self.delete_one()                   # удаление выбранной записи

        elif cmd == mCmd.DELETE_FROM_DATE:
            self.delete_date()                  # удаление за временной промежуток

    ############################################
    #
    # Методы для работы с записями
    #
    ############################################
    
    def create_record(self):                        # добавление новой записи
        pass
    
    def view_one(self):                             # просмотр одной записи
        pass

    def view_all(self):                             # просмотр всех записей
        pass

    def view_last(self):                            # посмотреть последнюю запись
        pass

    def view_date(self):                            # посмотреть по временному промежутку
        pass

    def edit_rec(self):                             # изменение записи
        pass

    def delete_last(self):                          # удаление последней записи
        pass
        
    def delete_one(self):                           # удаление выбранной записи
        pass

    def delete_date(self):                          # удаление за временной промежуток
        pass

