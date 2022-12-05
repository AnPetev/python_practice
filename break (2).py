import json
from datetime import datetime, timedelta

class Break:
    def __init__(self, span_id, start_time, end_time):
        with open("data.json") as data:
            info = json.load(data)

        self.template = info[str(span_id)]
        self.break_durations = [breaks["break_duration"] for breaks in self.template]
        print(self.break_durations)
        self.start_time_types = [stt["start_time_type"] for stt in self.template]
        self.start_times = [st["start_times"] for st in self.template]
        print(self.start_times)
        print(self.start_time_types)
        self.start = datetime.strptime(start_time, '%H:%M:%S')
        self.end = datetime.strptime(end_time, '%H:%M:%S')


    def relative_to_class_start(self):
        ans = []
        for t in self.start_time_types:
            if t == "RELATIVE_TO_CLASS_START":
                ans = [self.start + timedelta(hours=int(self.start_times[i][j][:2]),
                                              minutes=int(self.start_times[i][j][3:5]), seconds=int(self.start_times[i][j][6:]))
                                              for i in range(len(self.start_times)) for j in range(len(self.start_times[i]))]
        return ans


    def relative_to_class_end(self):
        ans = []
        for t in self.start_time_types:
            if t == "RELATIVE_TO_SHIFT_END":
                ans = [self.end - timedelta(hours=int(self.start_times[i][j][:2]),
                                            minutes=int(self.start_times[i][j][3:5]), seconds=int(self.start_times[i][j][6:]))
                       for i in range(len(self.start_times)) for j in range(len(self.start_times[i]))]
        return ans


    def generalize_break_for_class_start(self):
          type1 = self.relative_to_class_start()
          res1 = [type1[i][j] + break_durations[k] for i in range(len(type1)) 
                                                for j in range(len(type[i]))
                                                for k in range(self.break_durations)]
          return res1
        
        
    def generalize_break_for_class_end(self):
          type2 = self.relative_to_class_end()
          res2 = [type2[i][j] + break_durations[k] for i in range(len(type2)) 
                                                for j in range(len(type2[i]))
                                                for k in range(len(self.break_durations))]
          return res2
          
          
    def check_conditions_for_start(self):
          check_for_stt = generalize_break_for_class_start()
          for item1 in check_for_stt:
                for item2 in check_for_stt:
                      if check_for_stt[item1][item2] + "02:00:00" > check_for_stt[item1 + 1][item2]:
                            raise Exception("Not valid time for break")
     
     
     def check_conditions_for_end(self):
          check_for_stt = generalize_break_for_class_end()
          for item1 in check_for_stt:
                for item2 in check_for_stt:
                      if check_for_stt[item1][item2] + "02:00:00" > check_for_stt[item1 + 1][item2]:
                            raise Exception("Not valid time for break")
                            
#     def put_interval(self):
#           if check_conditions_for_start() or check_conditions_for_end():
                 
           
    
    
s = Break('2',"09:00:00", "15:00:00")
print(s.relative_to_class_start())
