from fabric.api import *
from fabric.contrib.files import exists

env.user = 'beertje'
env.home = "/home/%s" % env.user
env.project = 'ledebergdjango'
env.app_name = 'ledeberg'
env.project_dir = env.home + '/webapps/' + env.project
env.app_dir = env.project_dir + '/%s' % env.app_name
env.git_repo = 'git@github.com:bjornkri/ledeberg.git'
env.activate = 'source %s/.virtualenvs/%s/bin/activate' % (env.home, env.app_name)


def virtualenv(command):
    with cd(env.app_dir):
        run(env.activate + ' && ' + command)


def bootstrap():
    run('mkdir -p %s/lib/python2.7/site-packages' % env.home)
    run('easy_install-2.7 pip')
    run('pip-2.7 install virtualenv')


def install():
    run('virtualenv --python=python2.7 ~/.virtualenvs/%s' % env.app_name)
    virtualenv('pip-2.7 install psycopg2')
    with cd(env.project_dir):
        if not exists(env.app_dir + 'manage.py'):
            run('git clone %s %s' % (env.git_repo, env.app_dir))


def deploy():
    with cd(env.app_dir):
        run('git pull')
        virtualenv('pip-2.7 install -r requirements.txt')
        virtualenv('python2.7 manage.py collectstatic --noinput')
        run('../apache2/bin/restart')
