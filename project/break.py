import json
from datetime import datetime, timedelta


class Break:
    def __init__(self, span_id, start_time, end_time):
        with open("data.json") as data:
            info = json.load(data)

        self.template = info[str(span_id)]
        self.break_durations = [breaks["break_duration"] for breaks in self.template]
        # print(self.break_durations)
        self.start_time_types = [stt["start_time_type"] for stt in self.template]
        self.start_times = [st["start_times"] for st in self.template]
        print(self.start_times)
        # print(self.start_time_types)
        self.start = datetime.strptime(start_time, '%H:%M:%S')
        # print(self.start)
        self.end = datetime.strptime(end_time, '%H:%M:%S')



    def relative_to_class_start(self):
        ans = []
        r = []
        for t in self.start_time_types:
            if t == 'RELATIVE_TO_CLASS_START':
                for i in range(len(self.start_times)):
                    for j in range(len(self.start_times[i])):
                        ans.append(self.start + timedelta(hours=int(self.start_times[i][j][:2]),
                                                          minutes=int(self.start_times[i][j][3:5]),
                                                          seconds=int(self.start_times[i][j][6:])))
        return ans

    def relative_to_class_end(self):
        ans = []
        for t in self.start_time_types:
            if t == 'RELATIVE_TO_SHIFT_END':
                for i in range(len(self.start_times)):
                    for j in range(len(self.start_times[i])):
                        ans.append(self.end - timedelta(hours=int(self.start_times[i][j][:2]),
                                                        minutes=int(self.start_times[i][j][3:5]),
                                                        seconds=int(self.start_times[i][j][6:])))
        return ans

    def generalize_break_for_class_start(self):
        res1 = []
        type1 = self.relative_to_class_start()
        # times = [to_timedelta[i] for i in self.break_durations]
        for i in range(len(type1)):
            res1.append(type1[i] + timedelta(hours=int("00:15:00"[:2]),
                                             minutes=int("00:60:00"[3:5]),
                                             seconds=int("00:15:00"[6:])))
        return res1



    def generalize_break_for_class_end(self):
        res2 = []
        type2 = self.relative_to_class_end()
        # times = [to_timedelta[i] for i in self.break_durations]
        for i in range(len(type2)):
            res2.append(type2[i] + timedelta(hours=int("00:15:00"[:2]),
                                             minutes=int("00:60:00"[3:5]),
                                             seconds=int("00:15:00"[6:])))
        return res2



    def check_conditions_for_start(self):
        check_for_stt = generalize_break_for_class_start()
        for item in check_for_stt:
            if check_for_stt[item] + "02:00:00" > check_for_stt[item + 1]:
                raise Exception("Not valid time for break")



    def check_conditions_for_end(self):
        check_for_stt = generalize_break_for_class_end()
        for item1 in check_for_stt:
            if check_for_stt[item1] + "02:00:00" > check_for_stt[item1 + 1]:
                    raise Exception("Not valid time for break")


#     def put_interval(self, delta = 15):
#         check_for_stt = generalize_break_for_class_end()
#         if check_conditions_for_start() or check_conditions_for_end():
#             for i in check_for_stt:
#                 check_for_stt[i] += timedelta("02:00:00" - "00:15:00")
            
            
            
            
              
