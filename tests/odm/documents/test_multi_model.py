from tests.odm.models import DocumentMultiModelOne, DocumentMultiModelTwo


async def test_multi_model():

    doc_1 = await DocumentMultiModelOne().insert()
    doc_2 = await DocumentMultiModelTwo().insert()

    new_doc_1 = await DocumentMultiModelOne.get(doc_1.id)
    new_doc_2 = await DocumentMultiModelTwo.get(doc_2.id)

    assert new_doc_1 is not None
    assert new_doc_2 is not None

    new_doc_1 = await DocumentMultiModelTwo.get(doc_1.id)
    new_doc_2 = await DocumentMultiModelOne.get(doc_2.id)

    assert new_doc_1 is None
    assert new_doc_2 is None

    new_docs_1 = await DocumentMultiModelOne.find({}).to_list()
    new_docs_2 = await DocumentMultiModelTwo.find({}).to_list()

    assert len(new_docs_1) == 1
    assert len(new_docs_2) == 1

    await DocumentMultiModelOne.update_all({"$set": {"shared": 100}})

    new_doc_1 = await DocumentMultiModelOne.get(doc_1.id)
    new_doc_2 = await DocumentMultiModelTwo.get(doc_2.id)

    assert new_doc_1.shared == 100
    assert new_doc_2.shared == 0