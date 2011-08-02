from fabric.api import run, cd, settings
from fabric.contrib.files import exists


def host_type():
    need_commit = []
    nonff = []
    with cd('projects'):
        for x in run('ls').split():
            if exists('%s/.git' % x):
                with cd(x):
                    out = run('git status')
                    if out.find('Changes not staged for commit') > 0:
                        need_commit.append(x)
                    with settings(warn_only=True):
                        out = run('git push')
                    if out.find('non-fast-forward') > 0:
                        nonff.append(x)
    print('Non FF[%s]' % (' '.join(nonff)))
    print('Need Commit[%s]' % (' '.join(need_commit)))
