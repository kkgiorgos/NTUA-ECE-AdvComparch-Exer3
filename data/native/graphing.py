import json

import matplotlib.pyplot as plt

output_dir = 'figures'

with open('results.json', 'r') as file:
    data = json.load(file)

core_counts = set()
executables = set()
grain_sizes = set()

for result in data:
    core_counts.add(result['cores'])
    executables.add(result['executable'])
    grain_sizes.add(result['grain_size'])

x = sorted(core_counts, key=lambda x: int(x))
executables = sorted(executables)

for grain_size in grain_sizes:
    for executable in executables:
        points = list(filter(lambda x: x['executable'] == executable and x['grain_size'] == grain_size, data))
        print(grain_size, executable)
        points = sorted(points, key=lambda x: int(x['cores']))
        time = [i['time'] for i in points]

        plt.figure(f'time_{grain_size}')
        plt.plot(x, time)

    plt.figure(f'time_{grain_size}')
    plt.legend(executables)
    plt.title(f'Grain Size: {grain_size}')
    plt.xlabel('System Cores')
    plt.ylabel('Execution Time (seconds)')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/time_{grain_size}.pdf')