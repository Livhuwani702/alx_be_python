Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
Time_Bound = input("Is it time-bound? (yes/no): ")

def process comand(Priority, Time_Bound): 
  match Priority:
    case "high":
      print("Reminder: '{Task}' is a high priority task that requires immediate attention today.")
    case "medium":
      print("Reminder: '{Task}" is a medium priority task that requires medium attention.")
    case "low":
      print("Reminder: '{Task}' is a low priority task that requires low attention.") 
  match case
    if time_bound == yes:
      print("Reminder: '{Task}' is a high priority task that requires immediate attention today.")
    else:
      print("Reminder: '{Task}' is a low priority task. Consider completing it when you have free time.")
  
