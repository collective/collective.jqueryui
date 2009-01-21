import glob
import os
import setuptools.archive_util
import shutil
import tempfile
import urllib2
import StringIO

JQUERYUI_URL = "http://jquery-ui.googlecode.com/files/jquery.ui-1.6rc5.zip"

CSS_PROFILE_TEMPLATE = """\
<?xml version="1.0"?>
<object name="portal_css">
%s
</object>
"""

JS_PROFILE_TEMPLATE = """\
<?xml version="1.0"?>
<object name="portal_javascripts">
%s
</object>
"""

join = os.path.join
dirname = os.path.dirname
exists = os.path.exists

def replace(where, fro, to):
    for fn in glob.glob(where):
        f = open(fn)
        contents = f.read()
        f.close()
        contents = contents.replace(fro, to)
        f = open(fn, 'w')
        f.write(contents)
        f.close()

def get_jqueryui(dst):
    print "Downloading jQueryUI from %s" % JQUERYUI_URL
    response = urllib2.urlopen(JQUERYUI_URL)
    d = tempfile.mkdtemp()
    fn = join(d, 'jquery.ui.zip')
    f = open(fn, 'wb')
    f.write(response.read())
    f.close()
    setuptools.archive_util.unpack_archive(fn, d)
    os.unlink(fn)
    extracted_dir = glob.glob(join(d, '*'))[0]
    shutil.move(extracted_dir, dst)

def main():
    # Get the jQueryUI source and make some changes:
    base = join(dirname(__file__), 'collective', 'jqueryui')
    jqueryui_src = join(base, 'jquery.ui-src')
    jqueryui_dst = join(base, 'jquery.ui')

    if not exists(jqueryui_src):
        get_jqueryui(jqueryui_src)
    assert exists(jqueryui_src)

    if exists(jqueryui_dst):
        assert raw_input("Delete %s? " % jqueryui_dst).lower() in ('yes', 'y')
        shutil.rmtree(jqueryui_dst)

    os.mkdir(jqueryui_dst)
    shutil.copytree(join(jqueryui_src, 'ui'), join(jqueryui_dst, 'ui'))
    shutil.copytree(join(jqueryui_src, 'themes'), join(jqueryui_dst, 'themes'))

if __name__ == '__main__':
    main()
