import json
import exiftool
from datetime import datetime


class ExifWriter:

    def __init__(self):
        self.template = None
        self.file = None
        self.raw_data = None
        self.delimiter = '; '


    def _get_value(self, keyword):
        for data in self.raw_data:
            if data['prop'].get('slug') == self.template[keyword]:
                if data['prop'].get('datatype') == 'enum':
                    _tags = self.delimiter.join(tag.get('value') for tag in data.get('value') if tag.get('value'))
                    return _tags
                elif data['prop'].get('datatype') == 'bool':
                    return str(data.get('value'))
                elif data['prop'].get('datatype') == 'date':
                    _dt = datetime.strptime(data.get('value'), "%Y-%m-%dT%H:%M:%SZ")\
                        .strftime('%Y:%m:%d %H:%M:%S[%f][%z]')
                    return str(_dt)
                else:
                    return data.get('value')
            if keyword.lower().endswith('-ru'):
                if self.template[keyword]:
                    if data['lang'] == 'ru':
                        return data.get('value')
                else:
                    return ''
        return ''


    def _prepare_write_data(self, raw_data, template, file):
        self.raw_data = json.loads(json.dumps(raw_data))
        self.template = template
        self.file = file
        _writable_data = []

        for keyword in self.template:
            _val = self._get_value(keyword)
            _writable_data.append(f"-{keyword}={_val}")
        return _writable_data


    def write_data(self, raw_data, template, file):
        _writable_data = self._prepare_write_data(raw_data, template, file)

        with exiftool.ExifTool() as et:
            for new_tag in _writable_data:
                et.execute(bytes(new_tag, encoding='utf-8'), bytes(file, encoding='utf-8'))
            return et.get_metadata(file)
