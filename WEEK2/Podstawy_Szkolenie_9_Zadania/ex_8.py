import datetime


class Case:
    def __init__(self, name, created_task, end_task):
        self.name = name
        self.created_task = created_task
        self.end_task = end_task


    def retrieve_seconds(self):
        created_task_time = datetime.datetime.fromisoformat(self.created_task)

        if self.end_task is None:
            current_time = datetime.datetime.now()
            time_difference = current_time - created_task_time
        else:
            end_task_time = datetime.datetime.fromisoformat(self.end_task)
            time_difference = end_task_time - created_task_time

        return time_difference.total_seconds()


def main():
    first_case = {
        'name': 'first_case',
        'created_task': '2021 - 10 - 26T19: 48:12 + 00: 00',
        'end_task': None
    }

    second_case = {
        'name': 'second_case',
        'created_task': '2021-09-26T19:48:12+00:00',
        'end_task': '2021-10-26T19:48:12+00:00'
    }
    case = Case(**first_case) # -> name='first_case', created_task='xyz', end_task=None
    case_1 = Case(**second_case)

    print(case.retrieve_seconds(case.second_case))


if __name__ == "__main__":
    main()
