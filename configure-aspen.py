import os
from os.path import basename, dirname, join, realpath

from nav import NavItem


website.renderer_default = "jinja2"
website.renderer_factories['jinja2'].Renderer.global_context = {
    'range': range,
    'unicode': unicode,
    'enumerate': enumerate,
    'len': len,
    'float': float,
    'type': type,
    'str': str,
}


def add_nav_to_website(website):
    website.nav = NavItem(website, None, website.www_root, '')

def add_nav_current_to_context(request, website):
    fs = request.fs
    if basename(request.fs) in website.indices:
        fs = dirname(fs)
    request.context['nav_current'] = website.nav.by_fs.get(fs, website.nav)

add_nav_to_website(website)

website.algorithm.insert_after('dispatch_request_to_filesystem', add_nav_to_website)
website.algorithm.insert_after('dispatch_request_to_filesystem', add_nav_current_to_context)


website.www_gittip_com = realpath(join(website.project_root, os.environ['WWW_GITTIP_COM']))
