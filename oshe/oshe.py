import os
import sys

import click
import shutil

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
SOURCE_DIR = CURRENT_DIR
DEPLOY_DIR = os.path.join(CURRENT_DIR, "deploy")
TEMPLATE_DIR = os.path.join(CURRENT_DIR, "template")
TEST_DIR = os.path.join(CURRENT_DIR, "test")
SUB_TESTS_DIRS = [item for item in os.listdir(TEST_DIR)
                  if os.path.isdir(os.path.join(TEST_DIR, item))]

PROJECT_DIR = os.path.join(os.getcwd(), "project")
if os.path.exists(PROJECT_DIR):
    APP_DIRS = [item for item in os.listdir(PROJECT_DIR)
                if os.path.isdir(os.path.join(PROJECT_DIR, item))
                and not item.startswith("_")]


@click.group()
def oshe():
    pass


@oshe.command()
def init():
    project_dir = os.path.join(os.getcwd(), "project")
    if os.path.exists(project_dir):
        click.echo("Project is already initialized, exiting...")
    else:
        click.echo("No project folder is found, initializing project template")
        os.makedirs(project_dir)
        shutil.copy(os.path.join(TEMPLATE_DIR, "config.py"), project_dir)
        shutil.copy(os.path.join(TEMPLATE_DIR, "celery_app.py"), project_dir)

        click.echo("creating demo app")
        app_dir = os.path.join(project_dir, "demo")
        shutil.copytree(os.path.join(TEMPLATE_DIR, "demo"), app_dir)


@oshe.command()
@click.argument("name")
def create(name):
    if os.path.exists(PROJECT_DIR):
        app_dir = os.path.join(PROJECT_DIR, name)
        if not os.path.exists(app_dir):
            click.echo("creating app: %s" % name)
            shutil.copytree(os.path.join(TEMPLATE_DIR, "demo"), os.path.join(project_dir, name))
        else:
            click.echo("app [%s] already exists, exiting... " % name)
    else:
        click.echo("No project folder is found, you have to initialize project first")


@oshe.command()
@click.argument("environment", type=click.Choice(["internal", "staging", "production"]))
def deploy(environment):
    click.echo("deploying to: %s" % environment)


@oshe.command()
@click.option("queue", "-Q", help="queue to run", default="all")
@click.option("loglevel", "-L", help="log level to run with", default="info")
def worker(queue, loglevel):
    click.echo("starting celery...")
    python_bin_dir = os.path.dirname(sys.executable)
    celery_path = os.path.join(python_bin_dir, "celery")
    if queue != "all":
        os.system("%s -A project.celery_app:celery_app worker -Q %s -l %s" % (celery_path, queue, loglevel))
    else:
        os.system("%s -A project.celery_app:celery_app worker -l %s" % (celery_path, loglevel))


@oshe.command()
def beat():
    python_bin_dir = os.path.dirname(sys.executable)
    celery_path = os.path.join(python_bin_dir, "celery")
    os.system("%s -A project.celery_app:celery_app beat" % celery_path)


@oshe.command()
@click.argument("type", type=click.Choice(SUB_TESTS_DIRS))
@click.option("suit", "--suit", default="all")
def test(type, suit):
    click.echo("testing %s.%s" % (type, suit))


if __name__ == "__main__":
    oshe()
