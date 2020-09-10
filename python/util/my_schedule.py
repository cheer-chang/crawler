# coding=UTF-8
import schedule


class MySchedule:

    def __init__(self):
        pass

    @staticmethod
    def seconds(interval, job_func):
        schedule.every(interval).seconds.do(job_func)

    @staticmethod
    def minutes(interval, job_func):
        schedule.every(interval).minutes.do(job_func)

    @staticmethod
    def hours(interval, job_func):
        schedule.every(interval).hours.do(job_func)

    @staticmethod
    def cancel_job(job_func):
        schedule.cancel_job(job_func)


# def run_schedule():
#     return MyThreadPoolExecutor.add(pending)


def run_schedule():
    while True:
        schedule.run_pending()
