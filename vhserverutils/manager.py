from . import serverutils


def execute_command(args, config):
    '''command runner'''
    if args[1] == 'backup':
        _backup(config, *args)


def _backup(config, *args):
    '''Runs backup process for server.'''
    bkp = serverutils.backup()
    bkp.archive(config.worldPath, config.backupPath)
