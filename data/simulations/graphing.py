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
        cycles = [i['cycles'] for i in points]
        energy = [i['energy'] for i in points]
        time = [i['time'] * 1E-9 for i in points]
        edp = [t*e for t, e in zip(energy, time)]

        plt.figure(f'cycles_{grain_size}')
        plt.plot(x, cycles)
        plt.figure(f'energy_{grain_size}')
        plt.plot(x, energy)
        plt.figure(f'edp_{grain_size}')
        plt.plot(x, edp)

    plt.figure(f'cycles_{grain_size}')
    plt.legend(executables)
    plt.title(f'Grain Size: {grain_size}')
    plt.xlabel('System Cores')
    plt.ylabel('Clock Cycles')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/cycles_{grain_size}.pdf')

    plt.figure(f'energy_{grain_size}')
    plt.legend(executables)
    plt.title(f'Grain Size: {grain_size}')
    plt.xlabel('System Cores')
    plt.ylabel('Energy (J)')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/energy_{grain_size}.pdf')

    plt.figure(f'edp_{grain_size}')
    plt.legend(executables)
    plt.title(f'Grain Size: {grain_size}')
    plt.xlabel('System Cores')
    plt.ylabel('EDP (J*sec)')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/edp_{grain_size}.pdf')
