task = input(Enter your task: )
priority = input(Priority (high,/medium/low): )
time_bound = input(Is it time bound? (yes/no): )

def process comand(priority, time_bound): 
  match priority:
    case "high":
      print("Reminder: '{task}' is a high priority task that requires immediate attention today")
    case "medium":
      print("Reminder: '{task}" is a medium priority task that requires medium attention")
    case "low":
      print("Reminder: '{task}' is a low priority task that requires low attention") 
  match case
    if time_bound = yes:
      print("Reminder: '{task}' is a high priority task that requires immediate attention today")
    else:
      print("Reminder: '{task}' is a low priority task. Consider completing it when you have free time")
  
