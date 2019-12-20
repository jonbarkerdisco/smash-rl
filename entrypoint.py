import sys
import logging
from smashrl.train import _main as run_training
from tools.scraper.scrape import _main as download_training_data
sys.path.append('.')
sys.path.append('./smashrl/')
sys.path.append('./tools/')
sys.path.append('./tools/scraper/')

root = logging.getLogger()
root.setLevel(logging.DEBUG)

def _main():
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)
    download_training_data('./data')
    run_training('./data')



if __name__ == "__main__":

    _main()
