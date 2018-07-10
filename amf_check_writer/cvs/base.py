import json
from csv import DictReader

from amf_check_writer.base_file import AmfFile


class BaseCV(AmfFile):
    """
    Base class for a controlled vocabulary instance
    """
    def __init__(self, tsv_file, facets):
        """
        :param tsv_file: file object for the input TSV file
        :param facets:   list of facets to give this CV a unique name and
                         pyessv namespace
        """
        super(BaseCV, self).__init__(facets)
        self.tsv_file = tsv_file
        reader = StripWhitespaceReader(self.tsv_file, delimiter="\t")
        self.cv_dict = self.parse_tsv(reader)

    def to_json(self):
        """
        Return JSON representation of this CV as a string
        """
        return json.dumps(self.cv_dict, indent=4)

    def parse_tsv(self, reader):
        """
        Convert the TSV file to a dictionary in the controlled vocab format.
        Must be implemented in child classes.

        :param reader: StripWhitespaceReader instance for the TSV file
        :return:       dict containing data in JSON controlled vocab format
        """
        raise NotImplementedError


class StripWhitespaceReader(DictReader):
    """
    Subclasss of DictReader that automatically strips whitespace from cell
    and header values
    """
    def next(self):
        # Note: cannot use super because DictReader is an old-style class
        row = DictReader.next(self)
        return {k.strip(): v.strip() if v is not None else v for k, v in row.items()}
