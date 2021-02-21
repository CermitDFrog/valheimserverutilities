import sys
import config

def main():
    '''Runs commands through server manager.'''
    from vhserverutils.manager import execute_command
    execute_command(sys.argv, config)

if __name__=='__main__':
    main()
