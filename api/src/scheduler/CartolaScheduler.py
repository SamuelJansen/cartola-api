from python_framework import SchedulerType
from python_framework import Scheduler, SchedulerMethod, WeekDay, WeekDayConstant


@Scheduler(muteLogs=False)
class CartolaScheduler:

    # @SchedulerMethod(SchedulerType.INTERVAL, seconds=5, instancesUpTo=2)
    @SchedulerMethod(SchedulerType.INTERVAL, minutes=30, instancesUpTo=2)
    def gatherAll(self) :
        self.service.cartola.gatherModelList()
