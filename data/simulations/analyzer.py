import os
import re
import json
import subprocess

results_dir = "./results"

mcpat = "/root/sniper/tools/advcomparch_mcpat.py"

results = []

folders = [folder for folder in os.listdir(results_dir) if os.path.isdir(os.path.join(results_dir, folder))]

for folder in folders:
    folder_path = os.path.join(results_dir, folder)

    metadata = re.findall(r"sniper_([0-9]+)_([0-9]+)_(.*)$", folder_path)

    if "stdout.log" in os.listdir(folder_path):
        log_file_path = os.path.join(folder_path, "sim.out")
        if os.path.exists(log_file_path):
            # Execute mcpat analysis
            print('Working on:', folder_path)
            with open(f'{folder_path}/mcpat.out.log', "w") as out:
                subprocess.run([mcpat, '-d', folder_path, '-t', 'total', '-o', f'{folder_path}/mcpat'], stdout=out)

            cycles = None
            time = None     #In Nanoseconds
            energy = None   #In Joules

            with open(log_file_path, 'r') as data:
                for output_line in data.readlines():
                    temp = re.findall(r"Cycles(?: *)\|(?: *)([0-9]+)", output_line)
                    if temp:
                        cycles = temp
                    temp = re.findall(r"Time \(ns\)(?: *)\|(?: *)([0-9]+)", output_line)
                    if temp:
                        time = temp

            with open(os.path.join(folder_path, "mcpat.out.log"), 'r') as data:
                for output_line in data.readlines():
                    temp = re.findall(r"total(?:.*)W(?: *)([0-9]*\.?[0-9]*)(?: *)(kJ|J|mJ)", output_line)
                    if temp:
                        if temp[0][1] == 'J':
                            energy = float(temp[0][0])
                        elif temp[0][1] == 'mJ':
                            energy = float(temp[0][0]) * 1E-3
                        elif temp[0][1] == 'kJ':
                            energy = float(temp[0][0]) * 1E3
            
            result = {
                "cores": metadata[0][0],
                "executable": metadata[0][2],
                "grain_size": metadata[0][1],
                "cycles": int(cycles[0]),
                "time": int(time[0]),
                "energy": energy
            }
            results.append(result)

with open("results.json", "w") as json_file:
    json.dump(results, json_file)