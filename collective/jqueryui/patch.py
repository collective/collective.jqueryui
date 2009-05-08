from Acquisition import aq_parent
import Products.Five.browser.resource

def do():
    _old_get = Products.Five.browser.resource.DirectoryResource.get
    def DirectoryResource_get(*args, **kwargs):
        resource = _old_get(*args, **kwargs)
        if getattr(resource, '__roles__', None) is None:
            resource.__roles__ = aq_parent(resource).__roles__
        return resource
    Products.Five.browser.resource.DirectoryResource.get = DirectoryResource_get
