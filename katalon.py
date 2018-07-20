#!/usr/bin/python

import subprocess
import argparse

KATALON_BIN = "/opt/Katalon/katalon"
DEFAULT_PROJECT_PATH = "/opt/Katalon/Projects"
WORK_SPACE = "/var/lib/jenkins/workspace"

parser = argparse.ArgumentParser()


def execute(args):
    for suite in args.suites.split(','):
        _args = [
            KATALON_BIN,
            '--args',
            '-noSplash',
            '-runMod=console',
            '-projectPath={PROJECT_PATH}/{PROJECT}/{PROJECT}.prj'.format(PROJECT_PATH=args.projectPath, PROJECT=args.project),
            '-retry=0',
            '-testSuitePath="Test Suites/{SUITE}"'.format(SUITE=suite),
            '-executionProfile="default"',
            '-browserType="Chrome (headless)"',
            '-reportFolder="{WORK_SPACE}/{PROJECT}/report"'.format(WORK_SPACE=WORK_SPACE,PROJECT=args.project),
            "-reportFileName={SUITE}".format(SUITE=suite)
        ]
        subprocess.call(_args)


def init_arguments():
    parser.add_argument('--project', help='Project name', required=True)
    parser.add_argument('--suites', help='Test suites (separate by comma)', required=True)
    parser.add_argument('--projectPath', help='Project Path', default=DEFAULT_PROJECT_PATH)
    parser.add_argument('--reportFileName', help='Report FileName')
    parser.add_argument('--testSuiteRoot', help='Path to test suites folder', default='Test Suites')


if __name__ == '__main__':
    init_arguments()
    args = parser.parse_args()
    execute(args)
