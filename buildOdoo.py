#!/usr/bin/python

import subprocess
import argparse
import time
import logging
import ConfigParser

logging.basicConfig(format='[%(asctime)s]/%(levelname)s/%(name)s: %(message)s')
logger = logging.getLogger("Baskin service")
logger.setLevel(logging.INFO)
parser = argparse.ArgumentParser()


def delete_old_build(project_path):
    assert not not project_path, "Project path is not supplied"
    _args = [
        'rm',
        '-rf',
        project_path + '/*'
    ]
    subprocess.call(_args, cwd=project_path)


def restart_service(args):
    # Just to be sure ....

    assert not not args.branch, 'Branch name was not supplied !'
    assert not not args.path, "Project path was not supplied !"
    modules = get_to_upgrade_modules(args.path, args.remote, args.branch)
    logger.info("Modules to upgrade: %s" % ",".join(modules))

    # Pull new code
    git_pull(args.path, args.branch)

    if args.tool == 'tmux':
        tmux_restart(modules, args)
    elif args.tool == 'supervisor':
        supervisor_restart(modules, args)


def get_restart_command(modules, args):
    restart_command = [args.executable, '-c', args.config, '--load=web,web_kanban,connector']
    if modules:
        # Upgrade modules
        restart_command.extend(['-u', ','.join(modules), '-d', args.database])

    if args.database:
        # Upgrade module for specify database
        restart_command.extend(['-d', args.database])
    return restart_command


def supervisor_restart(modules, args):
    assert not not args.supervisor_config, "Path To Supervisord Configuration wasn't supplied !"
    p = ConfigParser.RawConfigParser()
    # Load supervisorctl configuration file
    p.read(args.supervisor_config)
    restart_command = get_restart_command()
    job_section = "program:%s" % args.branch
    p.set(job_section, "command", restart_command)
    with open(args.supervisor_config, "wb") as configfile:
        p.write(configfile)
    # Reload configuration file
    subprocess.call(["supervisorctl", "reread"])
    subprocess.call(["supervisorctl", "reload"])
    # Restart service
    subprocess.call(["supervisorctl", "restart", args.branch])

def tmux_restart(modules, args):
    restart_command = [args.executable, '-c', args.config, '--load=web,web_kanban,connector']
    logger.info("Stopping current service")
    # Stop current service
    subprocess.call([
        'pkill',
        '-f',
        " ".join(restart_command)
    ])

    logger.info("Killing old tmux session ")
    time.sleep(1)
    # Kill old tmux session
    subprocess.call([
        'tmux',
        'kill-session',
        '-t',
        args.branch
    ])

    # Restart service
    if modules:
        restart_command.extend(['-u', ','.join(modules), '-d', args.database])

    if args.database:
        restart_command.extend(['-d', args.database])

    logger.info("Starting service ...")
    # Create new session
    subprocess.call([
        'tmux',
        'new',
        '-d',
        '-s',
        args.branch
    ])

    # Send command to tmux session
    subprocess.call([
        'tmux',
        'send',
        '-t',
        args.branch,
        " ".join(restart_command),
        'ENTER'
    ])


def git_pull(path, branch):
    logger.info("Pulling new code from %s" % branch)
    subprocess.call([
        'git',
        'reset',
        '--hard'
    ], cwd=path)

    subprocess.call([
        'git',
        'checkout',
        branch
    ], cwd=path)

    subprocess.call([
        'git',
        'pull',
        '--rebase',
    ], cwd=path)


def get_to_upgrade_modules(project_path, remote, branch):
    """

    :return: (list) modules that will be upgrade in this build
    """
    to_upgrades = set([])
    subprocess.call([
        'git',
        'remote',
        'update',
        remote,
        '--prune'
    ])
    recent_changes = subprocess.check_output([
        'git',
        'diff',
        'HEAD',
        remote + '/' + branch,
        '--name-only',
    ], cwd=project_path)

    changes = recent_changes.split("\n")
    for c in changes:
        if '/' in c:
            module = c.split("/")
            if module and module[0]:
                to_upgrades.add(module[0])
    return list(to_upgrades)


def init_arguments():
    parser.add_argument('--path', help='Path to project', required=True)
    parser.add_argument('--branch', help='Branch name', required=True)
    parser.add_argument('--tool', help='Odoo Service management tool', default='tmux', choices=('tmux', 'supervisor', 'systemd'))
    parser.add_argument('--supervisor_config', help='Path To Supervisord Configuration File')
    parser.add_argument('--executable', help='Path to odoo executable file', required=True)
    parser.add_argument('--config', help='Path to project config file', required=True)
    parser.add_argument('--database', help='Database name')
    parser.add_argument('--remote', help='Git remote', default='origin')


if __name__ == '__main__':
    init_arguments()
    args = parser.parse_args()
    restart_service(args)

# /opt/scripts/autotest.py --project=${JOB_NAME} --suites=Discount
