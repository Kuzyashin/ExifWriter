import json
import os
import unittest

from writer import ExifWriter


class TestExifWriter(unittest.TestCase):
    test_writer = ExifWriter()
    rule_ru = """{
        "XMP:LensProfileFilename": "{{ getVal('original_filename') if getVal('original_filename') else "NoData" }}",
        "XMP:Keywords": "{{ getVal('tags') if getVal('tags') else "NoData" }}",
        "XMP:Description": "{{ getVal('description', lang='en') if getVal('description', lang='en') else "NoData" }}",
        "XMP:Description-ru": "{{ getVal('description', lang='ru') if getVal('description', lang='ru') else "NoRuData" }}",
        "XMP:Description-cz": "{{ getVal('description', lang='cz') if getVal('description', lang='cz') else "NoCzData" }}",
        "PNG:Filter": "{{ getVal('source') if getVal('source') else "NoSourceData" }}",
        "XMP:DateTime": "{{ getVal('create_date') if getVal('create_date') else "NoCreatedData" }}"
    }"""
    rule_en = """{
        "XMP:LensProfileFilename": "{{ getVal('original_filename') if getVal('original_filename') else "NoData" }}",
        "XMP:Keywords": "{{ getVal('tags') if getVal('tags') else "NoData" }}",
        "XMP:Description": "{{ getVal('description', lang='en') if getVal('description', lang='en') else "NoData" }}",
        "XMP:Description-ru": "{{ getVal('description', lang='ru') if getVal('description', lang='ru') else "NoRuData" }}",
        "XMP:Description-cz": "{{ getVal('description', lang='cz') if getVal('description', lang='cz') else "NoCzData" }}",
        "PNG:Filter": "{{ getVal('source') if getVal('source') else "NoSourceData" }}",
        "XMP:DateTime": "{{ getVal('create_date') if getVal('create_date') else "NoCreatedData" }}"
    }"""
    raw_data = [
        {
            u'lang': None,
            u'prop':
                {
                    u'content_type':
                        {
                            u'name': u'Base',
                            u'slug': u'base',
                            u'sort': 500
                        },
                    u'datatype': u'bool',
                    u'group': None,
                    u'name': u'Rate',
                    u'slug': u'Rate',
                    u'sort': 500
                },
            u'value': False
        },
        {
            u'lang': None,
            u'prop':
                {
                    u'content_type':
                        {
                            u'name': u'Base',
                            u'slug': u'base',
                            u'sort': 500
                        },
                    u'datatype': u'bool',
                    u'group': None,
                    u'name': u'\u041f\u0443\u0431\u043b\u0438\u0447\u043d\u044b\u0439',
                    u'slug': u'public',
                    u'sort': 10
                },
            u'value': True
        },
        {
            u'lang': None,
            u'prop':
                {
                    u'content_type':
                        {
                            u'name': u'Image',
                            u'slug': u'image',
                            u'sort': 500
                        },
                    u'datatype': u'text',
                    u'group': None,
                    u'name': u'\u041e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u0438\u043c\u044f \u0444\u0430\u0439\u043b\u0430',
                    u'slug': u'original_filename',
                    u'sort': 500
                },
            u'value': u'240a3e22-6fee-11e9-9bff-0242ac110005.jpg'
        },
        {
            u'lang': None,
            u'prop':
                {
                    u'content_type':
                        {
                            u'name': u'Image',
                            u'slug': u'image',
                            u'sort': 500
                        },
                    u'datatype': u'text',
                    u'group': None,
                    u'name': u'\u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a',
                    u'slug': u'source',
                    u'sort': 400
                },
            u'value': u'Image Collector'
        },
        {
            u'lang': None,
            u'prop':
                {
                    u'content_type':
                        {
                            u'name': u'Image',
                            u'slug': u'image',
                            u'sort': 500
                        },
                    u'datatype': u'date',
                    u'group': None,
                    u'name': u'\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f',
                    u'slug': u'create_date',
                    u'sort': 500
                },
            u'value': u'2019-05-02T06:00:07Z'
        },
        {
            u'lang': None,
            u'prop':
                {
                    u'content_type':
                        {
                            u'name': u'Base',
                            u'slug': u'base',
                            u'sort': 500
                        },
                    u'datatype': u'enum',
                    u'group':
                        {
                            u'name': u'\u041e\u0431\u0449\u0438\u0435',
                            u'slug': u'common',
                            u'sort': 100
                        },
                    u'name': u'\u0422\u0435\u0433\u0438',
                    u'slug': u'tags',
                    u'sort': 300
                },
            u'value': [
                {u'pk': 1659, u'value': u'CClass'},
                {u'pk': 243, u'value': u'MercedesBenz'},
                {u'pk': 241, u'value': u'MercedesAMG'},
                {u'pk': 240, u'value': u'mbfanphoto'},
                {u'pk': 239, u'value': u'automotivedesign'},
                {u'pk': 236, u'value': u'mbcar'},
                {u'pk': 235, u'value': u'germany'},
                {u'pk': 234, u'value': u'the best or nothing'},
                {u'pk': 233, u'value': u'Daimler AG'},
                {u'pk': 232, u'value': u'Mercedes-Benz'},
                {u'pk': 350, u'value': u'AMG'},
                {u'pk': 215, u'value': u'vehicles'},
                {u'pk': 214, u'value': u'auto'},
                {u'pk': 85, u'value': u'zimagecollector'},
                {u'pk': 7224, u'value': u'goodmornings'},
                {u'pk': 2233, u'value': u'C63AMG'},
                {u'pk': 2232, u'value': u'BlackSeries'},
                {u'pk': 7223, u'value': u'starttheday'},
                {u'pk': 165, u'value': u'car'},
                {u'pk': 164, u'value': u'instagram'},
                {u'pk': 163, u'value': u'social networks'},
                {u'pk': 159, u'value': u''},
                {u'pk': 158, u'value': u'luxury'}
            ]
        },
        {
            u'lang': u'en',
            u'prop':
                {
                    u'content_type':
                        {
                            u'name': u'Base',
                            u'slug': u'base',
                            u'sort': 500
                        },
                    u'datatype': u'text',
                    u'group':
                        {
                            u'name': u'\u041e\u0431\u0449\u0438\u0435',
                            u'slug': u'common',
                            u'sort': 100
                        },
                    u'name': u'\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435',
                    u'slug': u'description',
                    u'sort': 200
                },
            u'value': u'Hi! Photo by @rokenr. . #MercedesBenz #MercedesAMG # #AMG#CClass #C63AMG #BlackSeries #mbfanphoto #goodmornings #starttheday #automotivedesign #mbcar\n Mercedes Benz via globallookpress.com'
        },
        {
            u'lang': u'ru',
            u'prop':
                {
                    u'content_type':
                        {
                            u'name': u'Base',
                            u'slug': u'base',
                            u'sort': 500
                        },
                    u'datatype': u'text',
                    u'group':
                        {
                            u'name': u'\u041e\u0431\u0449\u0438\u0435',
                            u'slug': u'common',
                            u'sort': 100
                        },
                    u'name': u'\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435',
                    u'slug': u'description',
                    u'sort': 200
                },
            u'value': u'\u041f\u0440\u0438\u0432\u0435\u0442!\u0424\u043e\u0442\u043e @rokenr. . #MercedesBenz #MercedesAMG # @\u0410\u041c\u0413 @\u043a\u043b\u0430\u0441\u0441\u0430 cclass @C63AMG @BlackSeries @mbfanphoto @goodmornings @starttheday @automotivedesign @mbcar\n Mercedes Benz via globallookpress.com'
        },
        {
            u'lang': None,
            u'prop':
                {
                    u'content_type':
                        {
                            u'name': u'Base',
                            u'slug': u'base',
                            u'sort': 500
                        },
                    u'datatype': u'text',
                    u'group':
                        {
                            u'name': u'\u041e\u0431\u0449\u0438\u0435',
                            u'slug': u'common',
                            u'sort': 100
                        },
                    u'name': u'\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435',
                    u'slug': u'title',
                    u'sort': 100
                },
            u'value': u'Mercedes Benz - 02 May 2019'
        }]
    script_path = os.path.dirname(__file__)
    file = f"{script_path}/2.jpg"

    def test_writing_desc_en(self):
        expected_data = {
            'SourceFile': '/Volumes/FlashDrive/new_projects/exifer/2.jpg', 'ExifTool:ExifToolVersion': 11.52,
            'File:MIMEType': 'image/jpeg', 'File:ImageWidth': 3456, 'File:ImageHeight': 5184, 'File:EncodingProcess': 0,
            'File:BitsPerSample': 8, 'File:ColorComponents': 3, 'File:YCbCrSubSampling': '2 2',
            'JFIF:JFIFVersion': '1 1', 'JFIF:ResolutionUnit': 1, 'JFIF:XResolution': 72, 'JFIF:YResolution': 72,
            'XMP:XMPToolkit': 'Image::ExifTool 11.52',
            'XMP:Description': 'Hi! Photo by @rokenr. . #MercedesBenz #MercedesAMG # #AMG#CClass #C63AMG #BlackSeries #mbfanphoto #goodmornings #starttheday #automotivedesign #mbcar',
            'XMP:Description-ru': 'Привет!Фото @rokenr. . #MercedesBenz #MercedesAMG # @АМГ @класса cclass @C63AMG @BlackSeries @mbfanphoto @goodmornings @starttheday @automotivedesign @mbcar',
            'XMP:Description-cz': 'NoCzData',
            'XMP:Keywords': 'CClass; MercedesBenz; MercedesAMG; mbfanphoto; automotivedesign; mbcar; germany; the best or nothing; Daimler AG; Mercedes-Benz; AMG; vehicles; auto; zimagecollector; goodmornings; C63AMG; BlackSeries; starttheday; car; instagram; social networks; luxury',
            'XMP:LensProfileFilename': '240a3e22-6fee-11e9-9bff-0242ac110005.jpg', 'ICC_Profile:ProfileCMMType': 'Lino',
            'ICC_Profile:ProfileVersion': 528, 'ICC_Profile:ProfileClass': 'mntr', 'ICC_Profile:ColorSpaceData': 'RGB ',
            'ICC_Profile:ProfileConnectionSpace': 'XYZ ', 'ICC_Profile:ProfileDateTime': '1998:02:09 06:49:00',
            'ICC_Profile:ProfileFileSignature': 'acsp', 'ICC_Profile:PrimaryPlatform': 'MSFT',
            'ICC_Profile:CMMFlags': 0, 'ICC_Profile:DeviceManufacturer': 'IEC ', 'ICC_Profile:DeviceModel': 'sRGB',
            'ICC_Profile:DeviceAttributes': '0 0', 'ICC_Profile:RenderingIntent': 0,
            'ICC_Profile:ConnectionSpaceIlluminant': '0.9642 1 0.82491', 'ICC_Profile:ProfileCreator': 'HP  ',
            'ICC_Profile:ProfileID': '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0',
            'ICC_Profile:ProfileCopyright': 'Copyright (c) 1998 Hewlett-Packard Company',
            'ICC_Profile:ProfileDescription': 'sRGB IEC61966-2.1', 'ICC_Profile:MediaWhitePoint': '0.95045 1 1.08905',
            'ICC_Profile:MediaBlackPoint': '0 0 0', 'ICC_Profile:RedMatrixColumn': '0.43607 0.22249 0.01392',
            'ICC_Profile:GreenMatrixColumn': '0.38515 0.71687 0.09708',
            'ICC_Profile:BlueMatrixColumn': '0.14307 0.06061 0.7141',
            'ICC_Profile:DeviceMfgDesc': 'IEC http://www.iec.ch',
            'ICC_Profile:DeviceModelDesc': 'IEC 61966-2.1 Default RGB colour space - sRGB',
            'ICC_Profile:ViewingCondDesc': 'Reference Viewing Condition in IEC61966-2.1',
            'ICC_Profile:ViewingCondIlluminant': '19.6445 20.3718 16.8089',
            'ICC_Profile:ViewingCondSurround': '3.92889 4.07439 3.36179', 'ICC_Profile:ViewingCondIlluminantType': 1,
            'ICC_Profile:Luminance': '76.03647 80 87.12462', 'ICC_Profile:MeasurementObserver': 1,
            'ICC_Profile:MeasurementBacking': '0 0 0', 'ICC_Profile:MeasurementGeometry': 0,
            'ICC_Profile:MeasurementFlare': 0.00999, 'ICC_Profile:MeasurementIlluminant': 2,
            'ICC_Profile:Technology': 'CRT ',
            'ICC_Profile:RedTRC': '(Binary data 2060 bytes, use -b option to extract)',
            'ICC_Profile:GreenTRC': '(Binary data 2060 bytes, use -b option to extract)',
            'ICC_Profile:BlueTRC': '(Binary data 2060 bytes, use -b option to extract)',
            'Composite:ImageSize': '3456 5184', 'Composite:Megapixels': 17.915904
        }
        expected_data = json.loads(json.dumps(expected_data))
        result = json.loads(json.dumps(self.test_writer.write_data(self.raw_data, self.rule_en, self.file)))
        for key in expected_data:
            self.assertEqual(expected_data[key], result[key])
        self.assertEqual(self.file, result['SourceFile'])

    def test_writing_desc_ru(self):
        expected_data = {
            'SourceFile': '/Volumes/FlashDrive/new_projects/exifer/2.jpg', 'ExifTool:ExifToolVersion': 11.52,
            'File:MIMEType': 'image/jpeg', 'File:ImageWidth': 3456, 'File:ImageHeight': 5184, 'File:EncodingProcess': 0,
            'File:BitsPerSample': 8, 'File:ColorComponents': 3, 'File:YCbCrSubSampling': '2 2',
            'JFIF:JFIFVersion': '1 1', 'JFIF:ResolutionUnit': 1, 'JFIF:XResolution': 72, 'JFIF:YResolution': 72,
            'XMP:XMPToolkit': 'Image::ExifTool 11.52',
            'XMP:Description': 'Hi! Photo by @rokenr. . #MercedesBenz #MercedesAMG # #AMG#CClass #C63AMG #BlackSeries #mbfanphoto #goodmornings #starttheday #automotivedesign #mbcar',
            'XMP:Description-ru': 'Привет!Фото @rokenr. . #MercedesBenz #MercedesAMG # @АМГ @класса cclass @C63AMG @BlackSeries @mbfanphoto @goodmornings @starttheday @automotivedesign @mbcar',
            'XMP:Description-cz': 'NoCzData',
            'XMP:Keywords': 'CClass; MercedesBenz; MercedesAMG; mbfanphoto; automotivedesign; mbcar; germany; the best or nothing; Daimler AG; Mercedes-Benz; AMG; vehicles; auto; zimagecollector; goodmornings; C63AMG; BlackSeries; starttheday; car; instagram; social networks; luxury',
            'XMP:LensProfileFilename': '240a3e22-6fee-11e9-9bff-0242ac110005.jpg', 'ICC_Profile:ProfileCMMType': 'Lino',
            'ICC_Profile:ProfileVersion': 528, 'ICC_Profile:ProfileClass': 'mntr', 'ICC_Profile:ColorSpaceData': 'RGB ',
            'ICC_Profile:ProfileConnectionSpace': 'XYZ ', 'ICC_Profile:ProfileDateTime': '1998:02:09 06:49:00',
            'ICC_Profile:ProfileFileSignature': 'acsp', 'ICC_Profile:PrimaryPlatform': 'MSFT',
            'ICC_Profile:CMMFlags': 0, 'ICC_Profile:DeviceManufacturer': 'IEC ', 'ICC_Profile:DeviceModel': 'sRGB',
            'ICC_Profile:DeviceAttributes': '0 0', 'ICC_Profile:RenderingIntent': 0,
            'ICC_Profile:ConnectionSpaceIlluminant': '0.9642 1 0.82491', 'ICC_Profile:ProfileCreator': 'HP  ',
            'ICC_Profile:ProfileID': '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0',
            'ICC_Profile:ProfileCopyright': 'Copyright (c) 1998 Hewlett-Packard Company',
            'ICC_Profile:ProfileDescription': 'sRGB IEC61966-2.1', 'ICC_Profile:MediaWhitePoint': '0.95045 1 1.08905',
            'ICC_Profile:MediaBlackPoint': '0 0 0', 'ICC_Profile:RedMatrixColumn': '0.43607 0.22249 0.01392',
            'ICC_Profile:GreenMatrixColumn': '0.38515 0.71687 0.09708',
            'ICC_Profile:BlueMatrixColumn': '0.14307 0.06061 0.7141',
            'ICC_Profile:DeviceMfgDesc': 'IEC http://www.iec.ch',
            'ICC_Profile:DeviceModelDesc': 'IEC 61966-2.1 Default RGB colour space - sRGB',
            'ICC_Profile:ViewingCondDesc': 'Reference Viewing Condition in IEC61966-2.1',
            'ICC_Profile:ViewingCondIlluminant': '19.6445 20.3718 16.8089',
            'ICC_Profile:ViewingCondSurround': '3.92889 4.07439 3.36179', 'ICC_Profile:ViewingCondIlluminantType': 1,
            'ICC_Profile:Luminance': '76.03647 80 87.12462', 'ICC_Profile:MeasurementObserver': 1,
            'ICC_Profile:MeasurementBacking': '0 0 0', 'ICC_Profile:MeasurementGeometry': 0,
            'ICC_Profile:MeasurementFlare': 0.00999, 'ICC_Profile:MeasurementIlluminant': 2,
            'ICC_Profile:Technology': 'CRT ',
            'ICC_Profile:RedTRC': '(Binary data 2060 bytes, use -b option to extract)',
            'ICC_Profile:GreenTRC': '(Binary data 2060 bytes, use -b option to extract)',
            'ICC_Profile:BlueTRC': '(Binary data 2060 bytes, use -b option to extract)',
            'Composite:ImageSize': '3456 5184', 'Composite:Megapixels': 17.915904
        }
        expected_data = json.loads(json.dumps(expected_data))
        result = json.loads(json.dumps(self.test_writer.write_data(self.raw_data, self.rule_ru, self.file)))
        for key in expected_data:
            self.assertEqual(expected_data[key], result[key])
        self.assertEqual(self.file, result['SourceFile'])


if __name__ == '__main__':
    unittest.main()
