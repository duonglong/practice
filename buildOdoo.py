#!/usr/bin/python

import subprocess
import argparse

PROJECT_ROOT = "/opt/Projects"
ODOO_PATH = "/opt/Projects/baskin/odoo9_baskin/odoo.py"
CONFIG_PATH = "/opt/Projects/baskin/config/baskin_staging.conf"
DATABASE = "GS_ERP_P1_GOLIVE_STAGING_29_05"

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
    assert not not args.project, 'Project name was not supplied'
    assert not not args.branch, 'Branch name was not supplied'
    project_path = PROJECT_ROOT + '/' + args.project + '/' + args.branch
    modules = get_to_upgrade_modules(project_path, args.branch)
    # delete_old_build(project_path)

    # Kill old tmux session
    try:
        subprocess.call([
            'tmux',
            'kill-session',
            '-t',
            args.branch
        ])
    except Exception as e:
        pass

    # Restart service
    restart_command = [args.executable, '-c', args.config, '-u', ','.join(modules)]

    subprocess.call([
        'tmux',
        'new',
        '-d',
        '-s',
        args.branch
    ])

    subprocess.call([
        'tmux',
        'send',
        '-t',
        args.branch,
        " ".join(restart_command),
        'ENTER'
    ])


def get_to_upgrade_modules(project_path, branch):
    """

    :return: (list) modules that will be upgrade in this build
    """
    to_upgrades = set([])
    recent_changes = subprocess.check_output([
        'git',
        'diff',
        'HEAD^1',
        branch,
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
    parser.add_argument('--project', help='Project name', required=True)
    parser.add_argument('--branch', help='Branch name', required=True)
    parser.add_argument('--tool', help='Odoo Service management tool', default='tmux', choices=('tmux', 'supervisor', 'systemd'))
    parser.add_argument('--executable', help='Path to odoo executable file', default=ODOO_PATH)
    parser.add_argument('--config', help='Path to project config file', default=CONFIG_PATH)


if __name__ == '__main__':
    init_arguments()
    args = parser.parse_args()
    restart_service(args)
