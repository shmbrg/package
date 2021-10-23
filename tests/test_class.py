from package.utils import Numbers, DataTable


def test_numbers():
    n = Numbers()
    assert n.add(n.zero, n.one) == 1


def test_datatable():
    dt = DataTable()
    DT = dt.DT.copy()
    assert DT[3, "A"] == 3
