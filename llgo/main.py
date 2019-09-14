import sys
import subprocess
sys.path.append('/opt/llgo')

from llgo import config


def _start_crawl_pageinfo():
  for i in config.START_URLS.keys():
    for j in config.START_URLS[i].keys():
      for k in config.START_URLS[i][j].keys():
        command = config.COMMAND_PAGEINFO % (i, j ,k)
        print('\n%s\n' % command)
        subprocess.check_call(command , shell=True)


if __name__ == '__main__':
  _start_crawl_pageinfo()
