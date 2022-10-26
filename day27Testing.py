class TestDataEmptyArray:
    def get_array():
        arr = []
        return arr

class TestDataUniqueValues:
    def get_array():
        array = [1,2]
        return array
    def get_expected_result():
        index = 0
        return index

class TestDataExactlyTwoDifferentMinimums:
    def get_array():
        array = [3,1,1]
        return array
    def get_expected_result():
        min = 1
        return min


def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False

def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

#seq = TestDataEmptyArray.get_array()
#print(seq)
#seq = TestDataUniqueValues.get_array()
#print(seq)
#seq = TestDataExactlyTwoDifferentMinimums.get_array()
#print(seq)
#print(len(seq) >= 2)
#tmp = sorted(seq)
#print(tmp)
#print(tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2]))
#expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
#print(expected_result)
#result = minimum_index(seq)
#print(result)
#expected_result = TestDataUniqueValues.get_expected_result()
#print(expected_result)
TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")