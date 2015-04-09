import pytest

from tests.utils import async

import io

import aiohttpretty
import xmltodict

from waterbutler.core import streams
from waterbutler.core import exceptions

from waterbutler.providers.dataverse import DataverseProvider
from waterbutler.providers.dataverse.metadata import DataverseSwordFileMetadata
from waterbutler.providers.dataverse.utils import unpack_filename


@pytest.fixture
def auth():
    return {
        'name': 'cat',
        'email': 'cat@cat.com',
    }


@pytest.fixture
def credentials():
    return {'token': 'wrote harry potter'}


@pytest.fixture
def settings():
    return {
        'doi': 'doi:10.5072/FK2/ABCDEF',
        'id': '18',
        'name': 'A look at wizards'
    }


@pytest.fixture
def provider(auth, credentials, settings):
    return DataverseProvider(auth, credentials, settings)


@pytest.fixture
def file_content():
    return b'SLEEP IS FOR THE WEAK GO SERVE STREAMS'


@pytest.fixture
def file_like(file_content):
    return io.BytesIO(file_content)


@pytest.fixture
def file_stream(file_like):
    return streams.FileStreamReader(file_like)


@pytest.fixture
def file_metadata():
    return b'''<entry>
            <content type="text/plain; charset=US-ASCII" src="https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/162/thefile-3.txt"/>
            <id>https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/162/thefile-3.txt</id>
            <title type="text">Resource https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/162/thefile-3.txt</title>
            <summary type="text">Resource Part</summary>
            <updated>2015-03-26T20:00:12.361Z</updated>
        </entry>'''


@pytest.fixture
def dataset_metadata():
    return b'''<feed xmlns="http://www.w3.org/2005/Atom">
        <id>https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit/study/doi:10.5072/FK2/ABCDEF</id>
        <link href="https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit/study/doi:10.5072/FK2/ABCDEF" rel="self"/>
        <title type="text">A look at wizards</title>
        <author>
            <name>Potter, Harry</name>
        </author>
        <updated>2015-03-26T18:53:50.917Z</updated>
        <entry>
            <content type="text/plain; charset=US-ASCII" src="https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/161/thefile-2.txt"/>
            <id>https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/161/thefile-2.txt</id>
            <title type="text">Resource https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/161/thefile-2.txt</title>
            <summary type="text">Resource Part</summary>
            <updated>2015-03-26T20:00:12.361Z</updated>
        </entry>
        <entry>
            <content type="text/plain; charset=US-ASCII" src="https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/162/thefile-3.txt"/>
            <id>https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/162/thefile-3.txt</id>
            <title type="text">Resource https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/162/thefile-3.txt</title>
            <summary type="text">Resource Part</summary>
            <updated>2015-03-26T20:00:12.361Z</updated>
        </entry>
        <entry>
            <content type="text/plain; charset=US-ASCII" src="https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/150/thefile.txt"/>
            <id>https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/150/thefile.txt</id>
            <title type="text">Resource https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/150/thefile.txt</title>
            <summary type="text">Resource Part</summary>
            <updated>2015-03-26T20:00:12.361Z</updated>
        </entry>
        <entry>
            <content type="text/plain; charset=US-ASCII" src="https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/163/thefile-1.txt"/>
            <id>https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/163/thefile-1.txt</id>
            <title type="text">Resource https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/163/thefile-1.txt</title>
            <summary type="text">Resource Part</summary>
            <updated>2015-03-26T20:00:12.361Z</updated>
        </entry>
        <category term="isMinorUpdate" scheme="http://purl.org/net/sword/terms/state" label="State">true</category>
        <category term="locked" scheme="http://purl.org/net/sword/terms/state" label="State">false</category>
        <category term="latestVersionState" scheme="http://purl.org/net/sword/terms/state" label="State">DRAFT</category>
    </feed>'''


@pytest.fixture
def empty_dataset_metadata():
    return b'''<feed xmlns="http://www.w3.org/2005/Atom">
        <id>https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit/study/doi:10.5072/FK2/ABCDEF</id>
        <link href="https://apitest.dataverse.org/dvn/api/data-deposit/v1.1/swordv2/edit/study/doi:10.5072/FK2/ABCDEF" rel="self"/>
        <title type="text">A look at wizards</title>
        <author>
            <name>Potter, Harry</name>
        </author>
        <updated>2015-03-26T18:53:50.917Z</updated>
        <category term="isMinorUpdate" scheme="http://purl.org/net/sword/terms/state" label="State">true</category>
        <category term="locked" scheme="http://purl.org/net/sword/terms/state" label="State">false</category>
        <category term="latestVersionState" scheme="http://purl.org/net/sword/terms/state" label="State">DRAFT</category>
    </feed>'''


@pytest.fixture
def native_dataset_metadata():
    return {'data': {'createTime': '2015-04-02T13:21:59Z',
 'distributionDate': 'Distribution Date',
 'files': [{'datafile': {'contentType': 'text/plain; charset=US-ASCII',
    'description': '',
    'filename': '%2Fusr%2Flocal%2Fglassfish4%2Fglassfish%2Fdomains%2Fdomain1%2Ffiles%2F10.5072%2FFK2%2F232XYH%2F14c7a73c684-4b22a1757aed',
    'id': 19,
    'md5': '2243b9249ca96f7cca9f58f7584b5ddb',
    'name': 'UnZip.java',
    'originalFormatLabel': 'UNKNOWN'},
   'datasetVersionId': 5,
   'description': '',
   'label': 'UnZip.java',
   'version': 1},
  {'datafile': {'contentType': 'text/plain; charset=US-ASCII',
    'description': '',
    'filename': '%2Fusr%2Flocal%2Fglassfish4%2Fglassfish%2Fdomains%2Fdomain1%2Ffiles%2F10.5072%2FFK2%2F232XYH%2F14c7a73d734-8383551cc713',
    'id': 20,
    'md5': 'acbd18db4cc2f85cedef654fccc4a4d8',
    'name': 'thefile.txt',
    'originalFormatLabel': 'UNKNOWN'},
   'datasetVersionId': 5,
   'description': '',
   'label': 'thefile.txt',
   'version': 1},
  {'datafile': {'contentType': 'application/octet-stream',
    'description': '',
    'filename': '%2Fusr%2Flocal%2Fglassfish4%2Fglassfish%2Fdomains%2Fdomain1%2Ffiles%2F10.5072%2FFK2%2F232XYH%2F14c7a73e419-b578b719b05c',
    'id': 21,
    'md5': 'ee5a34fe861617916acde862d4206280',
    'name': 'UnZip.class',
    'originalFormatLabel': 'UNKNOWN'},
   'datasetVersionId': 5,
   'description': '',
   'label': 'UnZip.class',
   'version': 1}],
 'id': 5,
 'lastUpdateTime': '2015-04-02T15:26:21Z',
 'metadataBlocks': {'citation': {'displayName': 'Citation Metadata',
   'fields': [{'multiple': False,
     'typeClass': 'primitive',
     'typeName': 'title',
     'value': 'A look at wizards'},
    {'multiple': True,
     'typeClass': 'compound',
     'typeName': 'author',
     'value': [{'authorName': {'multiple': False,
        'typeClass': 'primitive',
        'typeName': 'authorName',
        'value': 'Baggins, Bilbo'}}]},
    {'multiple': True,
     'typeClass': 'compound',
     'typeName': 'datasetContact',
     'value': [{'datasetContactEmail': {'multiple': False,
        'typeClass': 'primitive',
        'typeName': 'datasetContactEmail',
        'value': 'email@email.com'},
       'datasetContactName': {'multiple': False,
        'typeClass': 'primitive',
        'typeName': 'datasetContactName',
        'value': 'Baggins, Bilbo'}}]},
    {'multiple': True,
     'typeClass': 'compound',
     'typeName': 'dsDescription',
     'value': [{'dsDescriptionValue': {'multiple': False,
        'typeClass': 'primitive',
        'typeName': 'dsDescriptionValue',
        'value': 'desc'}}]},
    {'multiple': True,
     'typeClass': 'controlledVocabulary',
     'typeName': 'subject',
     'value': ['Other']},
    {'multiple': False,
     'typeClass': 'primitive',
     'typeName': 'depositor',
     'value': 'Baggins, Bilbo'},
    {'multiple': False,
     'typeClass': 'primitive',
     'typeName': 'dateOfDeposit',
     'value': '2015-04-02'}]}},
 'productionDate': 'Production Date',
 'releaseTime': '2015-04-02T15:26:21Z',
 'versionMinorNumber': 0,
 'versionNumber': 1,
 'versionState': 'RELEASED'}}


@pytest.fixture
def empty_native_dataset_metadata():
    return {'data': {'createTime': '2015-04-02T13:21:59Z',
 'distributionDate': 'Distribution Date',
 'files': [],
 'id': 5,
 'lastUpdateTime': '2015-04-02T15:26:21Z',
 'metadataBlocks': {'citation': {'displayName': 'Citation Metadata',
   'fields': [{'multiple': False,
     'typeClass': 'primitive',
     'typeName': 'title',
     'value': 'A look at wizards'},
    {'multiple': True,
     'typeClass': 'compound',
     'typeName': 'author',
     'value': [{'authorName': {'multiple': False,
        'typeClass': 'primitive',
        'typeName': 'authorName',
        'value': 'Baggins, Bilbo'}}]},
    {'multiple': True,
     'typeClass': 'compound',
     'typeName': 'datasetContact',
     'value': [{'datasetContactEmail': {'multiple': False,
        'typeClass': 'primitive',
        'typeName': 'datasetContactEmail',
        'value': 'email@email.com'},
       'datasetContactName': {'multiple': False,
        'typeClass': 'primitive',
        'typeName': 'datasetContactName',
        'value': 'Baggins, Bilbo'}}]},
    {'multiple': True,
     'typeClass': 'compound',
     'typeName': 'dsDescription',
     'value': [{'dsDescriptionValue': {'multiple': False,
        'typeClass': 'primitive',
        'typeName': 'dsDescriptionValue',
        'value': 'desc'}}]},
    {'multiple': True,
     'typeClass': 'controlledVocabulary',
     'typeName': 'subject',
     'value': ['Other']},
    {'multiple': False,
     'typeClass': 'primitive',
     'typeName': 'depositor',
     'value': 'Baggins, Bilbo'},
    {'multiple': False,
     'typeClass': 'primitive',
     'typeName': 'dateOfDeposit',
     'value': '2015-04-02'}]}},
 'productionDate': 'Production Date',
 'releaseTime': '2015-04-02T15:26:21Z',
 'versionMinorNumber': 0,
 'versionNumber': 1,
 'versionState': 'RELEASED'}}


class TestCRUD:

    @async
    @pytest.mark.aiohttpretty
    def test_download(self, provider, dataset_metadata, native_dataset_metadata):
        path = '/21'
        url = provider.build_url(provider.DOWN_BASE_URL, path, key=provider.token)
        aiohttpretty.register_uri('GET', url, body=b'better')
        draft_url = provider.build_url(provider.METADATA_BASE_URL, provider.doi)
        aiohttpretty.register_uri('GET', draft_url, status=200, body=dataset_metadata)
        published_url = provider.build_url(provider.JSON_BASE_URL.format(provider.id), key=provider.token)
        aiohttpretty.register_json_uri('GET', published_url, status=200, body=native_dataset_metadata)

        result = yield from provider.download(str(path))
        content = yield from result.response.read()

        assert content == b'better'

    @async
    @pytest.mark.aiohttpretty
    def test_download_not_found(self, provider, dataset_metadata, native_dataset_metadata):
        path = '/21'
        url = provider.build_url(provider.DOWN_BASE_URL, path, key=provider.token)
        aiohttpretty.register_uri('GET', url, status=404)
        draft_url = provider.build_url(provider.METADATA_BASE_URL, provider.doi)
        aiohttpretty.register_uri('GET', draft_url, status=200, body=dataset_metadata)
        published_url = provider.build_url(provider.JSON_BASE_URL.format(provider.id), key=provider.token)
        aiohttpretty.register_json_uri('GET', published_url, status=200, body=native_dataset_metadata)

        with pytest.raises(exceptions.DownloadError):
            yield from provider.download(str(path))

    @async
    @pytest.mark.aiohttpretty
    def test_download_invalid_path(self, provider, dataset_metadata, native_dataset_metadata):
        path = '/50'
        draft_url = provider.build_url(provider.METADATA_BASE_URL, provider.doi)
        aiohttpretty.register_uri('GET', draft_url, status=200, body=dataset_metadata)
        published_url = provider.build_url(provider.JSON_BASE_URL.format(provider.id), key=provider.token)
        aiohttpretty.register_json_uri('GET', published_url, status=200, body=native_dataset_metadata)

        with pytest.raises(exceptions.MetadataError):
            yield from provider.download(str(path))

    @async
    @pytest.mark.aiohttpretty
    def test_upload(self, provider, file_stream, file_metadata, dataset_metadata):
        path = '/thefile.txt'
        url = provider.build_url(provider.EDIT_MEDIA_BASE_URL, 'study', provider.doi)
        metadata_url = provider.build_url(provider.METADATA_BASE_URL, provider.doi)
        aiohttpretty.register_uri('POST', url, status=201)
        aiohttpretty.register_uri('GET', metadata_url, status=200, body=dataset_metadata)

        metadata, created = yield from provider.upload(file_stream, path)

        entry = xmltodict.parse(file_metadata)['entry']
        expected = DataverseSwordFileMetadata(entry).serialized()

        assert metadata == expected
        assert created is True
        assert aiohttpretty.has_call(method='POST', uri=url)
        assert aiohttpretty.has_call(method='GET', uri=metadata_url)

    @async
    @pytest.mark.aiohttpretty
    def test_delete_file(self, provider, dataset_metadata, native_dataset_metadata):
        path = '162'
        url = provider.build_url(provider.EDIT_MEDIA_BASE_URL, 'file', path)
        aiohttpretty.register_json_uri('DELETE', url, status=204)
        draft_url = provider.build_url(provider.METADATA_BASE_URL, provider.doi)
        aiohttpretty.register_uri('GET', draft_url, status=200, body=dataset_metadata)
        published_url = provider.build_url(provider.JSON_BASE_URL.format(provider.id), key=provider.token)
        aiohttpretty.register_json_uri('GET', published_url, status=200, body=native_dataset_metadata)

        yield from provider.delete(str(path))

        assert aiohttpretty.has_call(method='DELETE', uri=url)

    @async
    @pytest.mark.aiohttpretty
    def test_delete_file_invalid_path(self, provider, dataset_metadata, native_dataset_metadata):
        path = '21'  # Path in native metadata doesn't count
        draft_url = provider.build_url(provider.METADATA_BASE_URL, provider.doi)
        aiohttpretty.register_uri('GET', draft_url, status=200, body=dataset_metadata)
        published_url = provider.build_url(provider.JSON_BASE_URL.format(provider.id), key=provider.token)
        aiohttpretty.register_json_uri('GET', published_url, status=200, body=native_dataset_metadata)

        with pytest.raises(exceptions.MetadataError):
            yield from provider.delete(str(path))


class TestMetadata:

    @async
    @pytest.mark.aiohttpretty
    def test_metadata(self, provider, dataset_metadata):
        url = provider.build_url(provider.METADATA_BASE_URL, provider.doi)
        aiohttpretty.register_uri('GET', url, status=200, body=dataset_metadata)

        result = yield from provider.metadata(state='draft')

        assert isinstance(result, list)
        assert len(result) == 4
        assert result[0]['provider'] == 'dataverse'
        assert result[0]['kind'] == 'file'
        assert result[0]['name'] == 'thefile-2.txt'
        assert result[0]['path'] == '/161'
        assert result[0]['extra']['original'] == 'thefile.txt'
        assert result[0]['extra']['version'] == 2
        assert result[0]['extra']['fileId'] == '161'

    @async
    @pytest.mark.aiohttpretty
    def test_metadata_no_files(self, provider, empty_dataset_metadata):
        url = provider.build_url(provider.METADATA_BASE_URL, provider.doi)
        aiohttpretty.register_uri('GET', url, status=200, body=empty_dataset_metadata)

        result = yield from provider.metadata(state='draft')

        assert isinstance(result, dict)
        assert result['provider'] == 'dataverse'
        assert result['kind'] == 'folder'
        assert result['name'] == 'A look at wizards'
        assert result['path'] == '/{0}/'.format(provider.doi)

    @async
    @pytest.mark.aiohttpretty
    def test_metadata_published(self, provider, native_dataset_metadata):
        url = provider.build_url(provider.JSON_BASE_URL.format(provider.id), key=provider.token)
        aiohttpretty.register_json_uri('GET', url, status=200, body=native_dataset_metadata)

        result = yield from provider.metadata(state='published')

        assert isinstance(result, list)
        assert len(result) == 3
        assert result[0]['provider'] == 'dataverse'
        assert result[0]['kind'] == 'file'
        assert result[0]['name'] == 'UnZip.java'
        assert result[0]['path'] == '/19'
        assert result[0]['extra']['original'] == 'UnZip.java'
        assert result[0]['extra']['version'] == 0
        assert result[0]['extra']['fileId'] == '19'

    @async
    @pytest.mark.aiohttpretty
    def test_metadata_published_no_files(self, provider, empty_native_dataset_metadata):
        url = provider.build_url(provider.JSON_BASE_URL.format(provider.id), key=provider.token)
        aiohttpretty.register_json_uri('GET', url, status=200, body=empty_native_dataset_metadata)

        result = yield from provider.metadata(state='published')

        assert isinstance(result, dict)
        assert result['provider'] == 'dataverse'
        assert result['kind'] == 'folder'
        assert result['name'] == 'A look at wizards'
        assert result['path'] == '/{0}/'.format(provider.doi)


    @async
    @pytest.mark.aiohttpretty
    def test_draft_metadata_missing(self, provider):
        url = provider.build_url(provider.METADATA_BASE_URL, provider.doi)
        aiohttpretty.register_uri('GET', url, status=404)

        with pytest.raises(exceptions.MetadataError):
            yield from provider.metadata(state='draft')

    @async
    @pytest.mark.aiohttpretty
    def test_draft_metadata_no_state_catches_all(self, provider, dataset_metadata, native_dataset_metadata):
        sword_url = provider.build_url(provider.METADATA_BASE_URL, provider.doi)
        aiohttpretty.register_uri('GET', sword_url, status=200, body=dataset_metadata)
        json_url = provider.build_url(provider.JSON_BASE_URL.format(provider.id), key=provider.token)
        aiohttpretty.register_json_uri('GET', json_url, status=200, body=native_dataset_metadata)

        result = yield from provider.metadata()

        assert isinstance(result, list)
        assert len(result) == 7


class TestUtils:

    def test_unpack_filename(self):
        filename = 'somefile.ext'
        original, version = unpack_filename(filename)
        assert original == 'somefile.ext'
        assert version == 0

    def test_unpack_filename_with_spaces(self):
        filename = 'some file.ext'
        original, version = unpack_filename(filename)
        assert original == 'some_file.ext'
        assert version == 0

    def test_unpack_filename_with_version(self):
        filename = 'some file-3.ext'
        original, version = unpack_filename(filename)
        assert original == 'some_file.ext'
        assert version == 3

    def test_unpack_filename_false_alarms(self):
        filename = 'some-file_3.ext'
        original, version = unpack_filename(filename)
        assert original == 'some-file_3.ext'
        assert version == 0

        filename = '1-some-2-file-3.ext'
        original, version = unpack_filename(filename)
        assert original == '1-some-2-file.ext'
        assert version == 3