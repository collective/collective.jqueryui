import Products.Five.browser.resource

def do():
    _old_get = Products.Five.browser.resource.DirectoryResource.get
    def DirectoryResource_get(*args, **kwargs):
        resource = _old_get(*args, **kwargs)
        if getattr(resource, '__roles__', None) is None:
            resource.__roles__ = resource.aq_parent.__roles__
        return resource
    Products.Five.browser.resource.DirectoryResource.get = DirectoryResource_get
