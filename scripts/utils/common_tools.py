import datetime
import loguru as logger
class StopWatch:
    def __init__(self):
        self.start = datetime.datetime.now()
    def reset(self):
        self.start =  datetime.datetime.now()

    def stop(self, msg='Time it took: '):
        end_time= datetime.datetime.now()
        time_range =  end_time - self.start
        seconds = time_range.seconds
        start_time = self.start.strftime('%Y-%m-%d %H:%M')
        end_time=end_time.strftime('%Y-%m-%d %H:%M')
        minutes = seconds // 60
        second = seconds % 60
        timeStr = str(minutes) + '分钟' + str(second) + "秒"
        logger.info('---%s start from %s end at %s, total cost time:%s ---' %(msg,start_time,end_time,timeStr))
        self.reset()
        return seconds