import threading
import time

import schedule as schedule


# https://github.com/mrhwick/schedule/blob/master/schedule/__init__.py
def run_continuously(self, interval=1):
    """
    不阻塞主线程的异步调用调度任务
    Continuously run, while executing pending jobs at each elapsed
    time interval.
    @return cease_continuous_run: threading.Event which can be set to
    cease continuous run.
    Please note that it is *intended behavior that run_continuously()
    does not run missed jobs*. For example, if you've registered a job
    that should run every minute and you set a continuous run interval
    of one hour then your job won't be run 60 times at each interval but
    only once.
    """
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                self.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()
    return cease_continuous_run


def run_job_while(schedule):
    """
    周期执行调度任务
    :param schedule: 调度任务
    """
    while True:
        schedule.run_pending()
        time.sleep(1)


def run_threaded(job_func):
    """
    使用异步线程运行job
    :param job_func: job
    """
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


# public api ↓

def run_job_second(job, second):
    """
    每隔x秒执行一次
    :param job: 方法签名
    :param second: 秒间隔
    """
    schedule.every(second).seconds.do(run_threaded, job)
    run_continuously(schedule)


def run_job_minute(job, min):
    """
    每隔x分钟执行一次
    :param job: 方法签名
    :param min: 分钟间隔
    """
    schedule.every(min).minutes.do(run_threaded, job)
    run_continuously(schedule)


def run_job_hour(job, hour):
    """
    每隔x小时执行一次
    :param job: 方法签名
    :param hour: 小时间隔
    """
    schedule.every(hour).hour.do(run_threaded, job)
    run_continuously(schedule)


def run_job_daily(job, hhMM):
    """
    每天hh:mm执行一次
    :param job: 方法签名
    :param min: 小时:分钟
    """
    schedule.every().day.at(hhMM).do(run_threaded, job)
    run_continuously(schedule)


def run_job_schedule(schedule):
    """
    按给定调度执行
    :param schedule: 自定义调度
    """
    run_continuously(schedule)


if __name__ == '__main__':
    def hello():
        print("hello")
        time.sleep(10)


    run_job_minute(hello, 1)
    run_job_daily(hello, "23:00")
    print("end")
