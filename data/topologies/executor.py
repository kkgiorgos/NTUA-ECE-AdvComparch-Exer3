import json
import subprocess
import re
import os

sniper_path = '/root/sniper'
bin_path = '/root/data/bin'
config_script = '/root/data/ask3.cfg'
output_dir = '/root/data/topologies/results'

with open('parameters.json') as f:
    parameters = json.load(f)

iterations = parameters['iterations']
grain_size = parameters['grain_size']
thread_count = parameters['threads']
systems = parameters['systems']
executables = [f'{bin_path}/{executable}' for executable in parameters['executables']]

for system in systems:
    for exec in executables:
        output = f'{output_dir}/sniper_{system["name"]}_{re.findall("sniper_(.+)$", exec)[0]}'
        if not os.path.exists(output):
            os.makedirs(output)
        with open(f'{output}/stdout.log', "w") as out:
            print("Working on: ", output)
            subprocess.run([f'{sniper_path}/run-sniper', 
                        '-c', config_script, 
                        '-n', str(thread_count), 
                        '-d', output,
                        '--roi',
                        f'-c --perf_model/l1_icache/shared_cores={system["l1i_share"]}',
                        f'-c --perf_model/l1_dcache/shared_cores={system["l1d_share"]}',
                        f'-c --perf_model/l2_cache/shared_cores={system["l2_share"]}',
                        f'-c --perf_model/l3_cache/shared_cores={system["l3_share"]}',
                        '--', exec, str(thread_count), str(iterations), str(grain_size)],
                        stdout=out)