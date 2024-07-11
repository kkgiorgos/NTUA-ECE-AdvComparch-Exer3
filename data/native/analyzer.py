import os
import re
import json

results_dir = "./results"

results = []

folders = [folder for folder in os.listdir(results_dir) if os.path.isdir(os.path.join(results_dir, folder))]

for folder in folders:
    folder_path = os.path.join(results_dir, folder)

    metadata = re.findall(r"real_([0-9]+)_([0-9]+)_(.*)$", folder_path)

    if "stdout.log" in os.listdir(folder_path):
        log_file_path = os.path.join(folder_path, "stdout.log")
        if os.path.exists(log_file_path):
            time = None     #In seconds

            with open(log_file_path, 'r') as data:
                for output_line in data.readlines():
                    temp = re.findall(r":([0-9]*\.?[0-9]*)", output_line)
                    if temp:
                        time = temp
            
            result = {
                "cores": metadata[0][0],
                "executable": metadata[0][2],
                "grain_size": metadata[0][1],
                "time": float(time[0]),
            }
            results.append(result)

with open("results.json", "w") as json_file:
    json.dump(results, json_file)