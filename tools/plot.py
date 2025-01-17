
import pandas as pd
import matplotlib.pyplot as plt
from watchgod import AllWatcher, run_process


def _main():
    watcher = AllWatcher('/Users/johan/Dev/smash-rl')
    run_process(path='stats.json', target=plot_stuff, watcher_cls=watcher)


def plot_stuff():
    df = pd.read_json('stats.json')
    print(df)
    plt.close()
    plt.plot(df.total_reward)
    plt.show()


if __name__ == "__main__":
    _main()
