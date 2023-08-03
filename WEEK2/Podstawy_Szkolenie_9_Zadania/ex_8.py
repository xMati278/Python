import datetime


class Case:
    def __init__(self):
        self.first_case = {
        'name': 'first_case',
        'created_task': '2021 - 10 - 26T19: 48:12 + 00: 00',
        'end_task': None
        }

        self.second_case = {
        'name': 'second_case',
        'created_task': '2021-09-26T19:48:12+00:00',
        'end_task': '2021-10-26T19:48:12+00:00'
        }

    def retrieve_seconds(self, task):
        created_task_time = datetime.datetime.fromisoformat(task['created_task'])

        if task['end_task'] is None:
            current_time = datetime.datetime.now()
            time_difference = current_time - created_task_time
        else:
            end_task_time = datetime.datetime.fromisoformat(task['end_task'])
            time_difference = end_task_time - created_task_time

        return time_difference.total_seconds()


def main():
    case = Case()
    print(case.retrieve_seconds(case.second_case))


if __name__ == "__main__":
    main()
