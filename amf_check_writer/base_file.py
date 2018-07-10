class AmfFile(object):
    """
    Base class for files generated by this codebase. This class does nothing
    much on its own, but is used as a base for other classes to give files a
    consistent naming scheme
    """
    # Character to separate facets in namespace and filenames
    facet_separator = "_"

    def __init__(self, facets):
        """
        :param facets: list of filename facets
        """
        self.facets = facets
        self.namespace = self.facet_separator.join(facets)

    def get_filename(self, ext):
        return "AMF{sep}{ns}.{ext}".format(sep=self.facet_separator,
                                           ns=self.namespace,
                                           ext=ext)