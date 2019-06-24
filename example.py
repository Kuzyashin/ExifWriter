import os
from writer import ExifWriter
rule = {
    "XMP:LensProfileFilename": 'original_filename',
    "XMP:Keywords": 'tags',
    "XMP:Description": 'description',
    "XMP:Description-ru": "python'{description if description else NO_DESCRIPTION}",
    "XMP:Description-cz": "python'{tags if description else NO_DESCRIPTION}",
    "PNG:Filter": 'source',
    "XMP:DateTime": 'create_date'
}
raw_data = [
        {u'lang': None,
         u'prop':
             { u'content_type':
                   { u'name': u'Base',
                     u'slug': u'base',
                     u'sort': 500},
               u'datatype': u'bool',
               u'group': None,
               u'name': u'Rate',
               u'slug': u'Rate',
               u'sort': 500},
         u'value': False},
        {u'lang': None,
         u'prop':
             { u'content_type':
                   { u'name': u'Base',
                     u'slug': u'base',
                     u'sort': 500},
               u'datatype': u'bool',
               u'group': None,
               u'name': u'\u041f\u0443\u0431\u043b\u0438\u0447\u043d\u044b\u0439',
               u'slug': u'public',
               u'sort': 10},
         u'value': True},
        { u'lang': None,
          u'prop':
              { u'content_type':
                    { u'name': u'Image',
                      u'slug': u'image',
                      u'sort': 500},
                u'datatype': u'text',
                u'group': None,
                u'name': u'\u041e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u0438\u043c\u044f \u0444\u0430\u0439\u043b\u0430',
                u'slug': u'original_filename',
                u'sort': 500},
          u'value': u'240a3e22-6fee-11e9-9bff-0242ac110005.jpg'},
        { u'lang': None,
          u'prop':
              { u'content_type':
                    { u'name': u'Image',
                      u'slug': u'image',
                      u'sort': 500},
                u'datatype': u'text',
                u'group': None,
                u'name': u'\u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a',
                u'slug': u'source',
                u'sort': 400},
          u'value': u'Image Collector'},
        { u'lang': None,
          u'prop':
              { u'content_type':
                    { u'name': u'Image',
                      u'slug': u'image',
                      u'sort': 500},
                u'datatype': u'date',
                u'group': None,
                u'name': u'\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f',
                u'slug': u'create_date',
                u'sort': 500},
          u'value': u'2019-05-02T06:00:07Z'},
        { u'lang': None,
          u'prop':
              { u'content_type':
                    { u'name': u'Base',
                      u'slug': u'base',
                      u'sort': 500},
                u'datatype': u'enum',
                u'group':
                    { u'name': u'\u041e\u0431\u0449\u0438\u0435',
                      u'slug': u'common',
                      u'sort': 100},
                u'name': u'\u0422\u0435\u0433\u0438',
                u'slug': u'tags',
                u'sort': 300},
          u'value': [
              { u'pk': 1659, u'value': u'CClass'},
              { u'pk': 243, u'value': u'MercedesBenz'},
              { u'pk': 241, u'value': u'MercedesAMG'},
              { u'pk': 240, u'value': u'mbfanphoto'},
              { u'pk': 239, u'value': u'automotivedesign'},
              { u'pk': 236, u'value': u'mbcar'},
              { u'pk': 235, u'value': u'germany'},
              { u'pk': 234, u'value': u'the best or nothing'},
              { u'pk': 233, u'value': u'Daimler AG'},
              { u'pk': 232, u'value': u'Mercedes-Benz'},
              { u'pk': 350, u'value': u'AMG'},
              { u'pk': 215, u'value': u'vehicles'},
              { u'pk': 214, u'value': u'auto'},
              { u'pk': 85, u'value': u'zimagecollector'},
              { u'pk': 7224, u'value': u'goodmornings'},
              { u'pk': 2233, u'value': u'C63AMG'},
              { u'pk': 2232, u'value': u'BlackSeries'},
              { u'pk': 7223, u'value': u'starttheday'},
              { u'pk': 165, u'value': u'car'},
              { u'pk': 164, u'value': u'instagram'},
              { u'pk': 163, u'value': u'social networks'},
              { u'pk': 159, u'value': u''},
              { u'pk': 158, u'value': u'luxury'}
          ]},
        { u'lang': u'en',
          u'prop':
              { u'content_type':
                    { u'name': u'Base',
                      u'slug': u'base',
                      u'sort': 500},
                u'datatype': u'text',
                u'group':
                    { u'name': u'\u041e\u0431\u0449\u0438\u0435',
                      u'slug': u'common',
                      u'sort': 100},
                u'name': u'\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435',
                u'slug': u'description',
                u'sort': 200},
          u'value': u'Hi! Photo by @rokenr. . #MercedesBenz #MercedesAMG # #AMG#CClass #C63AMG #BlackSeries #mbfanphoto #goodmornings #starttheday #automotivedesign #mbcar\n Mercedes Benz via globallookpress.com'},
        { u'lang': u'ru',
          u'prop':
              { u'content_type':
                    { u'name': u'Base',
                      u'slug': u'base',
                      u'sort': 500},
                u'datatype': u'text',
                u'group':
                    { u'name': u'\u041e\u0431\u0449\u0438\u0435',
                      u'slug': u'common',
                      u'sort': 100},
                u'name': u'\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435',
                u'slug': u'description',
                u'sort': 200},
          u'value': u'\u041f\u0440\u0438\u0432\u0435\u0442!\u0424\u043e\u0442\u043e @rokenr. . #MercedesBenz #MercedesAMG # @\u0410\u041c\u0413 @\u043a\u043b\u0430\u0441\u0441\u0430 cclass @C63AMG @BlackSeries @mbfanphoto @goodmornings @starttheday @automotivedesign @mbcar\n Mercedes Benz via globallookpress.com'},
        { u'lang': None,
          u'prop':
              { u'content_type':
                    { u'name': u'Base',
                      u'slug': u'base',
                      u'sort': 500},
                u'datatype': u'text',
                u'group':
                    { u'name': u'\u041e\u0431\u0449\u0438\u0435',
                      u'slug': u'common',
                      u'sort': 100},
                u'name': u'\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435',
                u'slug': u'title',
                u'sort': 100},
          u'value': u'Mercedes Benz - 02 May 2019'}]
script_path = os.path.dirname(__file__)
file = f"{script_path}/2.jpg"


example_writer = ExifWriter()
example_writer.delimiter = ", "


result = example_writer.write_data(raw_data, rule, file)

print(result)
