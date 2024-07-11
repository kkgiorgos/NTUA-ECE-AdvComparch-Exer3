import json

import matplotlib.pyplot as plt

output_dir = 'figures'

with open('results.json', 'r') as file:
    data = json.load(file)

systems = set()
executables = set()

for result in data:
    systems.add(result['system'])
    executables.add(result['executable'])

x = sorted(systems)
executables = sorted(executables)

for executable in executables:
    points = sorted(list(filter(lambda x: x['executable'] == executable, data)), key=lambda x: x['system'])
    cycles = [i['cycles'] for i in points]
    energy = [i['energy'] for i in points]
    time = [i['time'] * 1E-9 for i in points]
    edp = [t*e for t, e in zip(energy, time)]

    plt.figure(f'cycles')
    plt.plot(x, cycles, 'x')
    if executable != 'mutex':
        plt.figure(f'cycles_red')
        plt.plot(x, cycles, 'x')
    plt.figure(f'energy')
    plt.plot(x, energy, 'x')
    plt.figure(f'edp')
    plt.plot(x, edp, 'x')

plt.figure(f'cycles')
plt.legend(executables)
# plt.title(f'Grain Size: {grain_size}')
plt.xlabel('Systems')
plt.ylabel('Clock Cycles')
plt.tight_layout()
plt.savefig(f'{output_dir}/cycles.pdf')

plt.figure(f'energy')
plt.legend(executables)
# plt.title(f'Grain Size: {grain_size}')
plt.xlabel('Systems')
plt.ylabel('Energy (J)')
plt.tight_layout()
plt.savefig(f'{output_dir}/energy.pdf')

plt.figure(f'edp')
plt.legend(executables)
# plt.title(f'Grain Size: {grain_size}')
plt.xlabel('Systems')
plt.ylabel('EDP (J*sec)')
plt.tight_layout()
plt.savefig(f'{output_dir}/edp.pdf')

executables.remove('mutex')
plt.figure(f'cycles_red')
plt.legend(executables)
# plt.title(f'Grain Size: {grain_size}')
plt.xlabel('Systems')
plt.ylabel('Clock Cycles')
plt.tight_layout()
plt.savefig(f'{output_dir}/cycles_red.pdf')