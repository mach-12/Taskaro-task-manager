from pathlib import Path
import datetime
import csv

# To point to correct file and directory, i.e. tasklist.csv
script_loc = Path(__file__).absolute().parent
tasklist_file = script_loc / 'tasklist.csv'
Subjectlist_file = script_loc / 'Subject.csv'

class Task:
    all = []
    fields = ['name', 'subject', 'day', 'isWeekly', 'isMarked', 'color']
    def __init__(self, name: str, subject: str, day: int, isWeekly: bool, isMarked: bool, color: str):
        # Assign to self object
        self.name = name
        self.subject = subject
        self.day = int(day)
        self.isWeekly = bool(isWeekly)
        self.isMarked = bool(isMarked)
        self.color = color
        Task.all.append(self)

    def show_Tasks(self):
        for task in self.all:
            print("name, subject, day, isWeekly, isMarked, Color")
            print(task)

    # Updates Attribute isMarked
    def update_mark_status(self, value: bool):
        assert type(value) == bool, f'"{value}" is not valid, must be a bool'
        self.isMarked = value

    # Updates Attribute isWeekly
    def update_weekly_status(self, value: bool):
        assert type(value) == bool, f'"{value}" is not valid, must be a bool'
        self.isWeekly = value

    # Connverts String to Boolean i.e. "True" -> True
    @staticmethod
    def toBool(input_string: str):
        if input_string == 'True':
            return True
        elif input_string == 'False':
            return False
        else:
            return "Not Boolean"

    @staticmethod
    def numToWeekday(num : int):
        switch = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
            }
        return switch.get(num)

    @staticmethod
    def addSubject(subject: str, color: str):
        # Creating dictionary of inputs
        Subject_dict = {
            'subject' : subject,
            'color' : color
            }

        # Checks if new Task already exists 
        if Task.taskIsUnique(Subject_dict, Task.csv_read_Dict_sub(Task, Subjectlist_file)):
            Task.csv_write_Dict(Task, Subjectlist_file, Subject_dict)

    @classmethod
    def addTask(cls, name: str, subject: str, isWeekly: bool, isMarked: bool, color: str):
        # Creating dictionary of inputs
        task_dict = {
            'name' : name,
            'subject' : subject,
            'day' : cls.get_today_date(),
            'isWeekly' : isWeekly,
            'isMarked' : isMarked, 
            'color' : color
            }

        # Checks if new Task already exists 
        if Task.taskIsUnique(task_dict, cls.csv_read_Dict(cls, tasklist_file)):
            cls.csv_write_Dict(cls, tasklist_file, task_dict)

    def csv_read_Dict(self, file_name: str):
        skipper = False
        read_output = []
        with open(file_name, 'r') as r:
            reader = csv.DictReader(r, fieldnames = self.fields)
            for line in reader:
                if skipper:
                    line['day'] = int(line.get('day'))
                    line['isWeekly'] = self.toBool(line.get('isWeekly'))
                    line['isMarked'] = self.toBool(line.get('isMarked'))
                    read_output.append(line)
                skipper = True
            return read_output

    def csv_read_Dict_sub(self, file_name: str):
        read_output = []
        with open(file_name, 'r') as r:
            reader = csv.DictReader(r, fieldnames = self.fields)
            for line in reader:
                read_output.append(line)
            return read_output

    def csv_write_Dict(self, file_name: str, input_dict: dict):
        with open(file_name , 'a') as a:
            writer = csv.DictWriter(a, fieldnames = self.fields)
            writer.writerow(input_dict)

    @staticmethod
    def taskIsUnique(input_dict: dict, current_dict_list: list):
        if input_dict in current_dict_list:
            return False
        else:
            return True
    
    @staticmethod
    def get_today_date():
        return datetime.date.today().isoweekday()

    @classmethod
    def instantiate_from_csv(cls):
        Task.all.clear
        Tasks = cls.csv_read_Dict(cls, tasklist_file)
        
        for task in Tasks:
            Task(
                name = task.get('name'),
                subject = task.get('subject'),
                day = task.get('day'),
                isWeekly = bool(task.get('isWeekly')),
                isMarked = bool(task.get('isMarked')),
                color = task.get('color')
                )

    def __repr__(self):
        return f"'{self.name}', {self.subject}, {self.numToWeekday(self.day)}, {self.isWeekly}, {self.isMarked}, {self.color}"
        #return f"{self.__class__.__name__}('{self.name}', {self.subject}, {self.day}, {self.isWeekly}, {self.isMarked}, {self.color})"

        #Alarm, Calender
