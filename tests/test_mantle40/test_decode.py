import mantle


def test_decode():
    # Make sure it's using the specialized implementation, not common
    assert mantle.Decode is mantle.mantle40.Decode
    assert mantle.DefineDecode is mantle.mantle40.DefineDecode
    assert mantle.decode is mantle.mantle40.decode

    assert mantle.Decode is not mantle.common.decode.Decode
    assert mantle.DefineDecode is not mantle.common.decode.DefineDecode
    assert mantle.decode is not mantle.common.decode.decode
