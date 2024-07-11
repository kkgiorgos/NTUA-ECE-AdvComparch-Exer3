import json
import subprocess
import re
import os

sniper_path = '/root/sniper'
bin_path = '/root/data/bin'
config_script = '/root/data/ask3.cfg'
output_dir = '/root/data/native/results'

with open('parameters.json') as f:
    parameters = json.load(f)

iterations = parameters['iterations']
grain_sizes = parameters['grain_size']
thread_counts = parameters['threads']
executables = [f'{bin_path}/{executable}' for executable in parameters['executables']]

for grain_size in grain_sizes:
    for threads in thread_counts:
        for exec in executables:
            output = f'{output_dir}/real_{threads}_{grain_size}_{re.findall("real_(.+)$", exec)[0]}'
            if not os.path.exists(output):
                os.makedirs(output)
            with open(f'{output}/stdout.log', "w") as out:
                print("Working on: ", output)
                subprocess.run([exec, str(threads), str(iterations), str(grain_size)], stdout=out)