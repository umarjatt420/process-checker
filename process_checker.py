import psutil
from tabulate import tabulate

processes = psutil.process_iter()
table = []
for process in processes:
    try:
        process_name = process.name()
        process_id = process.pid
        process_status = process.status()
        table.append([process_name, process_id, process_status])
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

headers = ["Process Name", "Process ID", "Process Status"]
print(tabulate(table, headers, tablefmt="grid"))